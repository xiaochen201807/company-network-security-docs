---
aliases:
  - "应用与 API 安全"
type: "standard"
domain: "application-security"
phase:
  - "protect"
priority: "P0"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/application-security"
  - "security/priority/p0"
  - "security/phase/protect"
parent:
  - "[[docs/公司安全知识图谱]]"
related:
  - "[[docs/04-身份与访问控制]]"
  - "[[docs/17-安全架构评审与威胁建模]]"
  - "[[docs/08-DevSecOps与软件供应链安全]]"
  - "[[docs/09-漏洞管理与授权渗透测试]]"
  - "[[docs/18-产品安全与默认安全]]"
  - "[[docs/22-安全工程平台]]"
  - "[[docs/23-AI大模型与智能体安全]]"
  - "[[docs/24-移动应用安全]]"
  - "[[docs/07-数据安全]]"
  - "[[docs/21-密码学PKI-KMS与凭据治理]]"
---
# 06 - 应用与 API 安全

> 本文档定义 Web、API、Java/Spring/Spring Boot 应用从需求、设计、编码、测试、发布到运行阶段的安全要求。OWASP Top 10:2025 用于风险意识与分类；需要可验证要求时，优先参考 OWASP ASVS 5.0.0 并结合公司实际裁剪。

## 1. 目标

- 安全要求进入 SDLC 全过程。
- 身份认证、授权、输入输出和异常处理形成统一基线。
- Secret、依赖、管理接口和业务逻辑风险进入发布 Gate。
- Java/Spring 常见风险有明确编码和测试要求。
- 运行期具备日志、限流、监控和事件响应能力。

## 2. 安全开发生命周期

~~~text
需求 → 数据/资产识别 → 威胁建模 → 安全设计 → 安全编码
→ Code Review → SAST/SCA/Secret → 安全测试 → Security Gate
→ 发布 → 运行监控 → 漏洞/事件反馈
~~~

## 3. 控制级别

- **MUST**：强制要求。
- **SHOULD**：应尽量满足。
- **MAY**：增强要求。

## 4. 安全需求与威胁建模

需求阶段识别用户类型、认证方式、权限模型、敏感数据、数据导出、文件上传、第三方调用、公网暴露、高风险业务操作和审计日志。

核心、公网、高敏系统 SHOULD 进行威胁建模，识别信任边界、攻击入口、身份、数据流、Secret、第三方依赖、可用性风险和管理接口；重大架构变化时重新评估。

## 5. OWASP Top 10:2025

公司应用安全至少关注 Broken Access Control、Security Misconfiguration、Software Supply Chain Failures、Cryptographic Failures、Injection、Insecure Design、Authentication Failures、Software or Data Integrity Failures、Security Logging and Alerting Failures、Mishandling of Exceptional Conditions。

Top 10 是意识框架，不代表扫描工具能够覆盖全部风险。

## 6. OWASP ASVS 5.0.0

ASVS 可用于安全需求、架构 Review、Code Review、安全测试、外包验收和检查表。公司应按系统风险裁剪验证深度，不机械照搬全部条目。

## 7. 身份认证

- 关键系统优先统一身份或 SSO。
- 管理员和高风险登录 SHOULD MFA。
- 登录失败采取合理保护。
- 登录错误避免泄露账号是否存在。
- 密码不得明文存储。
- 用户密码使用成熟密码哈希方案，不使用 MD5/SHA1 直接保存。
- 密码重置 Token 高熵、短有效期、一次性并在使用后失效。

## 8. Session

- 登录后重新生成 Session。
- 注销后服务端失效。
- 设置合理空闲和绝对超时。
- Cookie 按场景设置 Secure、HttpOnly、SameSite。
- 不在 URL 中传递 Session ID。
- 高风险操作可重新认证。

## 9. JWT

**MUST：**验证签名、允许算法、时间声明，并按业务验证 issuer/audience；禁止未签名 Token；签名密钥安全存储且支持轮换。

JWT 仅解码成功不等于认证成功。长期 Refresh Token 应支持撤销、轮换或风险控制。

## 10. 授权

认证解决身份，授权解决权限。每个敏感接口必须明确角色、对象归属、数据范围和租户边界。

### 10.1 对象级授权

访问订单、文件、用户、工单等对象时，除验证登录外，还必须验证当前主体对目标对象的权限。

### 10.2 功能级授权

管理员、审批、导出、删除、配置修改等能力必须在服务端校验。

**MUST：不得依赖前端隐藏按钮作为授权控制。**

### 10.3 数据级权限

按用户、组织、租户、部门、Owner 限制查询范围，避免查询全部数据后只在前端过滤。

## 11. Spring Security

Spring 项目 SHOULD 统一使用成熟安全框架。重点 Review SecurityFilterChain、路径匹配、permitAll、方法级授权、默认拒绝、CSRF、CORS、Session/JWT 和管理接口。

新增 permitAll 必须 Review；关键业务可增加方法级授权，避免只依赖 URL 层。

## 12. 输入验证

Query、Path、Header、Cookie、JSON/XML、文件、MQ 消息、第三方响应和历史数据库内容均视为不可信输入。

验证类型、长度、范围、格式、枚举和业务约束，优先白名单。

## 13. SQL 注入

- MUST 使用参数化查询或 PreparedStatement。
- MyBatis 使用参数绑定处理数据参数。
- 动态表名和列名使用严格白名单。
- Native Query、动态 JPQL、动态排序字段同样需要检查。
- 禁止拼接用户输入形成 SQL。

## 14. 命令注入

避免直接调用 Shell。确需执行系统命令时，不拼接用户输入，参数白名单，使用结构化 Process API，并以最小权限运行。

## 15. XSS

根据 HTML、JavaScript、URL、CSS 等不同输出上下文进行正确编码。富文本使用成熟 Sanitizer，不自行用简单正则过滤。不得无必要关闭框架自动转义。

## 16. CSRF

浏览器 Cookie 认证场景必须评估 CSRF。Spring Security 的 CSRF 保护不得只因调试方便而全局关闭；Token/API 模式也应根据实际浏览器行为建模。

## 17. SSRF

服务端请求外部 URL 时采用协议和目标白名单，限制 localhost、内网、云元数据等敏感地址，设置连接/读取超时和响应大小限制，并评估 DNS 重绑定。

## 18. 文件上传

**MUST：**限制大小和数量、服务端生成文件名、防路径穿越、校验实际类型、上传目录与执行目录隔离、禁止用户控制最终绝对路径。

SHOULD 增加恶意文件扫描；适用时对图片/文档重新编码。

## 19. 路径穿越

文件读写使用固定根目录、规范化路径并校验最终路径仍位于允许范围内。

## 20. 反序列化

避免对不可信数据做任意对象反序列化。重点检查 Java 原生序列化、JSON 多态类型、不可信类名、MQ/RPC 数据；使用安全版本并限制可实例化类型。

## 21. SpEL 与表达式注入

不得直接执行用户可控表达式。确需动态表达式时限制语法、对象、方法和资源消耗。

## 22. XML / XXE

按业务关闭不需要的外部实体和 DTD 能力，避免不可信 XML 读取本地文件或发起网络请求。

## 23. 日志安全

不得记录密码、完整 Token、私钥、Authorization Header 或不必要的完整敏感字段。用户输入控制字符不得破坏日志结构。

## 24. 错误与异常处理

- 不向客户端返回堆栈。
- 不泄露 SQL、目录、Secret、内部 IP 等信息。
- 服务端记录 Trace/Correlation ID。
- 安全失败尽量 fail closed。
- 异常不能绕过授权、金额和状态机校验。
- Java 项目建立统一 Exception Handler。

## 25. CORS

CORS 不是身份认证。敏感接口禁止无差别允许任意 Origin，不动态反射任意 Origin；携带凭据时只允许可信 Origin。

## 26. Actuator

Spring Boot Actuator 管理端口限制来源，按需开放 Endpoint，不无保护公网暴露 heapdump、env、configprops 等敏感能力。

## 27. Swagger / OpenAPI

生产环境评估是否需要公开 API 文档；管理/内部 API 不公开；若开放，配合认证和来源控制；示例不得包含真实 Secret。

## 28. Debug 与管理接口

禁止生产无保护暴露 Debug、Test、Mock、Admin、H2 Console、JMX、Profiling 和临时运维接口。临时接口必须按计划删除。

## 29. 加密与密钥

敏感传输使用 TLS，存储按数据等级加密或哈希；使用成熟算法和库，不自研密码算法；密钥与数据分离并支持轮换。

## 30. 安全随机数

安全 Token、重置链接、验证码种子等使用密码学安全随机数。

## 31. Secret

禁止在代码、配置仓库、日志和前端包中硬编码长期 Secret。使用 Secret Manager、Jenkins Credentials 或受控注入。

## 32. API 请求与响应

限制请求体、数组、分页、嵌套深度等；响应只返回必要字段，不返回密码哈希、内部权限字段、Secret、不必要个人信息和调试字段。

## 33. Mass Assignment

DTO 显式声明可修改字段，禁止普通用户通过提交 role、status 等受保护字段改变权限或业务状态。

## 34. Rate Limit

登录、验证码、密码重置、短信/邮件、搜索、导出、高成本计算和第三方调用 SHOULD 限流，按用户、IP、设备和业务主体组合设计。

## 35. 幂等与重放

支付、审批、创建资源等使用 Idempotency Key、唯一业务号、数据库唯一约束或状态机；敏感接口按需使用 nonce、timestamp、短 Token 或一次性令牌。

## 36. 业务逻辑安全

越权优惠、重复领取、金额篡改、审批绕过、非法状态跳转、批量接口滥用等通常无法靠 SAST 自动发现，核心业务必须人工威胁建模和安全测试。

## 37. 状态机

订单、审批、退款、账户状态等必须由服务端校验合法状态转换，不能信任客户端直接指定最终状态。

## 38. 第三方 API

明确数据范围，验证 TLS，安全存储 Secret，设置连接/读取超时，限制重试，验证响应，避免第三方故障拖垮业务线程池。

## 39. 超时、重试、熔断

所有外部调用设置超时。重试有上限、有退避，不对不可幂等操作盲目重试，避免重试风暴；必要时熔断、隔离和降级。

## 40. 资源消耗

限制请求体、上传、批量数量、分页上限、查询时间、报表范围、正则复杂度和并发任务数，降低应用层 DoS 风险。

## 41. 正则 ReDoS

复杂正则处理不可信输入时评估灾难性回溯，限制输入长度并使用安全模式或引擎。

## 42. 缓存与多租户

缓存设置合理 TTL，多租户 Key 必须隔离，权限变化考虑缓存失效，不缓存不应跨用户共享的数据。

租户 ID 不得只相信客户端传值，应从可信身份上下文确定，并贯穿查询、缓存和消息。

## 43. MQ

消费者把消息视为不可信输入：校验格式与业务状态、防重复、防超大消息、设计 DLQ/重试、不反序列化任意类型。

## 44. 前端安全

前端不存长期 Secret；避免 XSS；Token 存储按威胁模型选择；CSP 等 Header 按项目实施；生产 Source Map 是否公开需评估；npm 依赖进入 SCA。

## 45. 安全 Header

公网 Web 按场景评估 CSP、HSTS、X-Content-Type-Options、Referrer-Policy 和 Frame 控制，配置上线前测试。

## 46. Code Review 重点

认证授权、SQL、文件、网络请求、反序列化、表达式、加密、Secret、管理接口、第三方依赖、Jenkinsfile/Dockerfile 变化必须重点 Review。

## 47. SAST / SCA / Secret

遵循 08、09 章节：新增严重问题优先阻断，高危结果人工验证，误报有证据，修复后复测。

## 48. 安全测试

根据风险执行认证、越权、输入验证、API、文件上传、SSRF、业务逻辑、配置和异常测试。核心/公网系统 SHOULD 做授权渗透测试。

## 49. Security Gate

- [ ] 无未批准 Critical
- [ ] High 已处置或例外
- [ ] 无高可信 Secret
- [ ] SAST/SCA 完成
- [ ] 认证授权完成 Review
- [ ] 管理接口无无保护公网暴露
- [ ] 日志与告警就绪
- [ ] 制品和依赖可追溯
- [ ] 高风险变更有回退

## 50. 应用日志与检测

至少记录登录/注销、权限失败、管理员操作、敏感配置变化、高风险数据导出、关键业务状态、安全校验失败和 Trace ID。

重点检测暴力破解、越权探测、SQLi/XSS/SSRF 特征、大量 4xx/5xx、管理接口访问、大量导出、异常 API 调用和高成本接口滥用。

## 51. 指标

- SAST/SCA 覆盖率
- Security Gate 覆盖率
- 新代码高危问题数
- 越权漏洞数
- 应用漏洞 MTTR
- Secret 泄露次数
- 核心系统安全测试覆盖率

## 52. 检查频率

### 每次发布
Security Gate、安全扫描、依赖变化、Secret、管理接口、日志。

### 每月
高风险应用问题、依赖、公开 API、管理员接口和证书。

### 每季度
核心应用威胁模型/安全 Review、权限模型和渗透测试计划。

## 53. 落地路线

### P0
统一 Spring 安全编码、认证授权 Review、SAST/SCA/Secret、异常处理、Actuator/Swagger 治理。

### P1
ASVS 检查表、威胁建模、API 安全测试、Rate Limit、统一安全组件。

### P2
安全需求自动映射、自动 Security Gate、运行时高级检测和成熟度度量。

## 54. 审计证据

安全设计、Code Review、扫描报告、测试报告、发布 Gate、例外、应用日志、渗透报告和复测记录。

## 55. 当前待确认

- [ ] Spring/Spring Boot 主版本范围
- [ ] 统一认证方式
- [ ] JWT/Session 标准
- [ ] API Gateway
- [ ] SAST/SCA 工具
- [ ] Security Gate 标准
- [ ] ASVS 公司裁剪清单
- [ ] 核心应用列表

## 56. 参考

- OWASP Top 10:2025
- OWASP ASVS 5.0.0
- OWASP API Security 项目
- 公司 08 DevSecOps 与供应链安全
- 公司 09 漏洞管理与授权渗透测试

## 57. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立应用安全框架 |
| V0.2 | 2026-09 | 完善 Java/Spring、API、认证授权、输入输出、业务逻辑、异常和 Gate 要求 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/公司安全知识图谱|公司安全知识图谱]]
- **前置知识**：[[docs/04-身份与访问控制|04 身份与访问控制]] · [[docs/17-安全架构评审与威胁建模|17 安全架构评审与 Threat Modeling]]
- **下游知识**：[[docs/08-DevSecOps与软件供应链安全|08 DevSecOps 与供应链安全]] · [[docs/09-漏洞管理与授权渗透测试|09 漏洞管理与授权渗透测试]] · [[docs/18-产品安全与默认安全|18 Product Security 与 Secure by Default]] · [[docs/22-安全工程平台|22 Security Engineering Platform]] · [[docs/23-AI大模型与智能体安全|23 AI、LLM 与 Agent 安全]] · [[docs/24-移动应用安全|24 移动应用安全]]
- **横向关联**：[[docs/07-数据安全|07 数据安全]] · [[docs/21-密码学PKI-KMS与凭据治理|21 密码学、PKI、KMS 与 Secret 治理]]

<!-- obsidian-relations:end -->
