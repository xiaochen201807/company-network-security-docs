# 08 - DevSecOps 与软件供应链安全

> 本文档用于规范公司从代码提交、依赖获取、持续集成、静态扫描、依赖分析、制品生成到发布部署全过程中的安全要求。
>
> 建设目标不是简单增加扫描工具，而是形成一套 **可执行、可度量、可阻断、可审计、可持续改进** 的研发供应链安全体系。

---

## 1. 文档目标

DevSecOps 与软件供应链安全需要达到以下目标：

1. 保证进入公司研发环境的代码、依赖、工具、镜像和制品来源可信。
2. 尽可能在开发和构建阶段发现安全问题，降低问题进入生产环境后的处理成本。
3. 防止密码、Token、私钥、AccessKey 等敏感凭据进入代码仓库、构建日志和制品。
4. 对第三方依赖中的 CVE、许可证和传递依赖风险进行持续治理。
5. 对 Git、Jenkins、Maven/Nexus、SonarQube、制品仓库等关键研发基础设施实施最小权限和审计。
6. 保证构建过程可追溯，能够回答“某个生产制品由谁、在什么时候、基于哪次代码提交、使用哪些依赖构建”。
7. 对达到公司阻断标准的重大风险建立自动化门禁。
8. 对暂时无法修复的问题建立正式的安全例外审批机制。
9. 对扫描工具误报、漏报和规则质量持续治理。
10. 将安全检查融入研发日常流程，而不是只依赖上线前突击检查。

---

## 2. 适用范围

本规范适用于公司内部所有软件研发、构建和发布活动，包括但不限于：

- Java / Spring / Spring Boot 项目
- Web 前端项目
- Node.js 项目
- Python 项目
- 移动端项目
- 微服务
- API 服务
- 定时任务
- 数据处理程序
- Docker 镜像
- Kubernetes 应用
- Infrastructure as Code
- Jenkins Pipeline
- Maven / Gradle
- NPM / PNPM / Yarn
- Git 仓库
- Nexus / Artifactory 等制品仓库
- SonarQube
- SAST / SCA / Secret Scan
- Docker Registry
- CI/CD Runner
- 自动化发布平台

第三方外包项目、采购软件二次开发项目和供应商交付代码原则上也应纳入同类安全控制。

---

## 3. 控制级别

本文档统一使用以下控制级别：

- **MUST**：强制要求，不满足时必须进入安全例外审批。
- **SHOULD**：推荐要求，应尽量实施；无法实施时应说明原因。
- **MAY**：可选增强控制，可根据业务和风险逐步建设。

---

## 4. 研发供应链整体模型

推荐将公司研发供应链划分为以下阶段：

~~~text
开发人员
   │
   ▼
Git 仓库
   │
   ├── Code Review
   ├── Secret Scan
   └── 分支保护
   │
   ▼
Jenkins / CI
   │
   ├── SAST
   ├── SCA
   ├── 单元测试
   ├── License 检查
   ├── IaC 检查
   └── Build
   │
   ▼
制品
   │
   ├── JAR / WAR
   ├── 前端包
   └── Docker Image
   │
   ▼
制品仓库 / 镜像仓库
   │
   ├── 完整性校验
   ├── 漏洞扫描
   ├── 元数据记录
   └── 版本冻结
   │
   ▼
发布审批
   │
   ▼
测试 / 预发布 / 生产
~~~

**MUST：生产环境只能部署经过公司受控 CI/CD 链路生成的正式制品。**

禁止开发人员绕过正式构建流程，将个人电脑本地生成的 JAR、WAR、前端包或镜像直接上传生产环境。

---

## 5. 角色与职责

| 角色 | 主要职责 |
|---|---|
| 安全负责人 | 制定供应链安全策略、风险等级、阻断规则和安全例外制度 |
| 安全工程师 | 维护 SAST/SCA/Secret 等能力，分析漏洞，推动整改并复测 |
| 研发负责人 | 确保项目接入安全流程，推动研发修复问题 |
| 开发人员 | 安全编码、依赖治理、修复扫描问题 |
| DevOps/运维 | 负责 Jenkins、Git、制品仓库、Runner、发布平台安全 |
| 系统负责人 | 判断业务影响，协调业务窗口，承担经批准的剩余风险 |
| 审计人员 | 检查流程、权限、证据、例外和整改闭环 |

**MUST：高风险安全例外不得由问题开发人员自行批准。**

---

## 6. 基本安全原则

### 6.1 最小权限

所有研发系统账号、Token、服务账号和自动化凭据必须遵循最小权限原则。

### 6.2 构建输入默认不可信

源码、第三方依赖、插件、镜像、构建脚本、外部仓库均应视为潜在风险输入。

### 6.3 构建可重复

同一个代码版本和依赖版本应尽可能产生一致的构建结果。

### 6.4 正式制品不可随意覆盖

Release 版本正式发布后原则上禁止使用相同版本号覆盖。

### 6.5 全链路可追溯

正式制品至少需要关联：

- Git 仓库
- Commit ID
- 分支
- 构建编号
- Jenkins Job
- 构建时间
- 构建触发人或服务账号
- 主要依赖版本
- 制品 SHA-256
- 发布环境

### 6.6 安全检查自动化

可以自动执行的安全检查应逐步进入 CI/CD。

### 6.7 新问题优先治理

存量问题较多时，优先做到“不再新增重大风险”，再逐步消化存量。

---

## 7. Git 与源代码安全

### 7.1 仓库管理

**MUST：正式业务代码进入公司统一管理的 Git 平台。**

禁止：

- 将正式代码长期只存储在个人电脑。
- 使用个人网盘作为公司代码主存储。
- 未经授权将公司私有代码上传公共代码平台。
- 未经审批将私有仓库修改为公开仓库。

---

### 7.2 分支保护

生产项目主分支，例如 main、master、release、production，应开启保护。

**MUST：**

- 禁止普通开发人员直接 push 生产主分支。
- 禁止 force push 主分支。
- 禁止随意删除主分支。
- 合并必须通过 Merge Request / Pull Request。
- 关键项目必须至少经过一名非提交者 Review。

**SHOULD：**

- 核心系统采用两人 Review。
- 安全敏感代码指定 CODEOWNER 或专门审核人员。

---

### 7.3 Code Review 安全检查

Code Review 除业务逻辑外应特别关注：

- 是否新增敏感接口。
- 是否缺少权限校验。
- 是否新增外部网络访问。
- 是否新增文件上传。
- 是否引入新的第三方依赖。
- 是否硬编码密码、Token 或 Key。
- 是否关闭现有安全验证。
- 是否新增调试接口或管理接口。
- 是否修改认证和授权逻辑。
- 是否新增动态 SQL。
- 是否修改 Jenkinsfile。
- 是否修改 Dockerfile。
- 是否修改发布和启动脚本。
- 是否降低 TLS、安全 Header、CORS 等安全要求。

---

### 7.4 Git 权限

建议按照平台能力划分 Guest、Reporter、Developer、Maintainer、Owner/Administrator 等角色。

**MUST：**

- 普通研发人员不得默认拥有平台管理员权限。
- Git 管理员数量受控。
- 离职员工账号及时禁用。
- 外包账号具有明确有效期。
- 高权限 Token 明确用途和 owner。

**SHOULD：**

- 管理员启用 MFA。
- 每季度复审高权限成员。

---

### 7.5 Git Token

禁止使用长期有效且拥有所有 Scope 的万能 Token。

Token 至少应具备：

- 明确 owner
- 明确用途
- 最小 Scope
- 有效期
- 可轮换
- 可吊销
- 使用记录可审计

**MUST：CI 服务 Token 与个人 Token 分离。**

---

## 8. Secret 与凭据安全

### 8.1 禁止进入 Git 的内容

以下内容禁止直接提交 Git：

- 数据库密码
- Redis 密码
- SSH 私钥
- TLS 私钥
- API Key
- AccessKey / SecretKey
- JWT 签名密钥
- OAuth Client Secret
- Jenkins Token
- Git Token
- 云平台 Secret
- VPN 密码
- 第三方平台凭据

---

### 8.2 Secret Scan

CI/CD 应逐步接入 Secret Scan。

扫描范围至少包括：

- 新增 Commit
- Merge Request
- 当前代码
- 配置文件
- Shell 脚本
- Jenkinsfile
- Dockerfile
- YAML
- properties
- XML
- JSON

**SHOULD：高可信的新提交 Secret 直接阻断。**

---

### 8.3 Secret 泄露处置

发现 Secret 已经提交到 Git 后，单纯删除文件并不代表风险消失。

正确流程：

1. 判断 Secret 是否真实有效。
2. 立即吊销或禁用旧 Secret。
3. 生成新 Secret。
4. 更新相关应用配置。
5. 清理 Git 历史中的敏感信息。
6. 检查 Secret 是否已经被使用。
7. 检查 Jenkins 构建日志。
8. 检查制品。
9. 检查 Wiki、聊天、工单等其他传播渠道。
10. 影响较大时进入安全事件响应流程。

**MUST：泄露凭据首先进行吊销/轮换，而不是仅删除代码中的文本。**

---

## 9. Jenkins / CI 安全

### 9.1 Jenkins 风险定位

Jenkins 属于公司高价值研发基础设施。

Jenkins 一旦被控制，攻击者可能进一步获得：

- 源代码
- Git Token
- Jenkins Credentials
- Maven 私服凭据
- 制品仓库权限
- 部署权限
- 生产环境访问能力

因此 Jenkins 应按照关键基础设施进行保护。

---

### 9.2 Jenkins 权限

建议区分：

- Jenkins 管理员
- Job 管理人员
- 开发人员
- 只读人员
- 自动化服务账号

**MUST：普通开发人员不得默认拥有 Jenkins 系统管理员权限。**

---

### 9.3 Jenkins 管理员账号

要求：

- 一人一号。
- 禁止共享管理员账号。
- 离职立即禁用。
- 管理员名单定期复审。
- 身份系统支持时启用 MFA。

---

### 9.4 Jenkins Credentials

密码、Token、SSH Key 等应使用 Jenkins Credentials 或公司 Secret 管理平台。

禁止在 Jenkinsfile 中写入：

~~~groovy
environment {
    DB_PASSWORD = "真实密码"
}
~~~

禁止在脚本中硬编码：

~~~text
Authorization: Bearer 真实Token
~~~

---

### 9.5 Pipeline 日志

构建日志不得主动打印 Secret。

重点检查：

- echo 密码变量
- env
- printenv
- set
- 调试模式输出 Header
- curl verbose 模式
- Maven/NPM 调试日志

**MUST：涉及凭据的 Pipeline 必须验证日志脱敏机制。**

---

### 9.6 Jenkins 插件

插件属于供应链风险的重要来源。

**MUST：**

- 控制插件安装权限。
- 禁止普通开发随意安装插件。
- 建立插件清单。
- 删除长期不用插件。

**SHOULD：**

- 定期检查插件安全更新。
- 插件升级先在测试 Jenkins 验证。
- 尽量减少插件数量。

---

### 9.7 Jenkins Controller

Jenkins Controller 应：

- 禁止直接暴露公网。
- 限制管理端访问来源。
- 及时升级安全补丁。
- 备份关键配置。
- 记录管理员操作。
- 限制 Script Console 等高危能力。

---

### 9.8 Jenkins Agent / Node

构建节点应根据项目安全等级进行隔离。

特别关注：

- Shell 执行权限
- Docker Socket
- SSH Key
- Kubernetes ServiceAccount
- Maven settings.xml
- NPM Token
- Git Token
- 云平台凭据

不建议多个安全等级完全不同的项目长期共享同一个高权限构建节点。

---

### 9.9 Docker Socket

如果 Jenkins Agent 能直接访问 /var/run/docker.sock，通常意味着该构建任务具备非常高的宿主机控制能力。

**MUST：Docker Socket 不得无差别暴露给所有构建任务。**

---

### 9.10 临时构建节点

**SHOULD：**逐步采用临时 Agent、Docker Agent、Kubernetes Pod Agent。

构建结束后销毁环境，可以减少：

- 工作区残留
- Secret 残留
- 不同项目相互影响
- 恶意构建持久化

---

## 10. Maven / Nexus / Artifactory 安全

### 10.1 Maven 仓库来源

公司 Java 项目原则上通过公司 Maven 私服获取依赖。

推荐：

~~~text
Developer
   │
   ▼
Company Nexus / Artifactory
   │
   ├── Maven Central Proxy
   ├── Internal Release
   └── Internal Snapshot
~~~

**SHOULD：**尽量避免每个项目直接连接多个互联网 Maven 仓库。

---

### 10.2 外部仓库治理

开发人员不应为了下载某个依赖，随意在 pom.xml 中增加未知仓库。

新增第三方仓库前至少评估：

- 仓库运营方是否可信
- 是否使用 HTTPS
- 是否长期维护
- 依赖来源是否明确
- 是否容易发生依赖替换或抢注
- 是否可以统一代理到公司私服

---

### 10.3 Release 与 Snapshot

内部组件建议采用：

~~~text
SNAPSHOT
    ↓
开发/测试
    ↓
Release
    ↓
正式版本
~~~

**MUST：正式 Release 版本原则上不可覆盖。**

生产构建原则上不依赖不可控 SNAPSHOT。

若必须使用，应记录：

- 使用原因
- owner
- 生命周期
- 转正式版本计划

---

### 10.4 依赖版本固定

生产项目不建议长期使用动态版本。

依赖应尽量固定到明确版本，避免相同源码在不同时间构建出不同依赖组合。

---

### 10.5 私服权限

至少区分：

- Read
- Deploy Snapshot
- Deploy Release
- Delete
- Admin

**MUST：普通开发人员不得默认拥有正式 Release 仓库删除权限。**

---

## 11. SCA 软件成分分析

### 11.1 SCA 目标

SCA 至少需要回答：

- 当前项目使用了哪些第三方组件？
- 当前实际使用哪个版本？
- 是否存在已知 CVE？
- 漏洞来自直接依赖还是传递依赖？
- 推荐修复版本是什么？
- 是否存在许可证风险？
- 哪些生产系统正在使用该组件？

---

### 11.2 SCA 输出字段

建议至少包含：

| 字段 | 说明 |
|---|---|
| 项目 | 项目名称 |
| 组件 | 第三方依赖 |
| 当前版本 | 实际版本 |
| CVE | 漏洞编号 |
| CVSS | 漏洞评分 |
| 风险等级 | 严重/高/中/低 |
| 依赖类型 | 直接/传递 |
| 修复版本 | 推荐升级版本 |
| 可利用性 | 已确认/疑似/未知/不适用 |
| 责任人 | 整改 owner |
| 状态 | 新增/处理中/已修复/例外 |

---

### 11.3 传递依赖

例如：

~~~text
Project
  └── A
      └── B
          └── C
~~~

如果漏洞存在于 C，即使 pom.xml 没有直接声明 C，仍然属于项目供应链风险。

因此 SCA 不应只分析直接依赖。

---

### 11.4 扫描时机

建议至少：

1. Merge Request / Pull Request。
2. 主分支构建。
3. Release 构建。
4. 定期全量重新扫描。
5. 出现新严重 CVE 后重新评估。

原因是：即使代码和依赖版本没有变化，新的 CVE 仍可能在未来被披露。

---

## 12. CVE、CVSS 与业务风险

### 12.1 CVSS 定位

CVSS 是技术严重程度的重要参考，但不能机械等同于公司实际风险。

还需要考虑：

- 是否公网暴露
- 是否需要认证
- 是否存在成熟利用代码
- 是否出现真实攻击
- 是否影响生产
- 是否属于核心业务
- 是否涉及敏感数据
- 是否存在可靠补偿控制
- 组件漏洞代码路径是否真正被调用

---

### 12.2 初始风险分级建议

| 等级 | CVSS 参考 | 处理原则 |
|---|---:|---|
| 严重 Critical | 9.0 - 10.0 | 优先处置，可触发发布阻断 |
| 高危 High | 7.0 - 8.9 | 高优先级整改 |
| 中危 Medium | 4.0 - 6.9 | 纳入计划整改 |
| 低危 Low | 0.1 - 3.9 | 根据业务情况整改 |

以上为初始建议，公司最终等级应结合业务风险确认。

---

### 12.3 风险升级因素

以下情况可人工提高优先级：

- 公网可直接利用
- 无需认证
- 已存在成熟利用代码
- 已存在真实攻击
- 影响核心系统
- 可直接取得服务器权限
- 可直接泄露大量敏感数据
- 可绕过核心鉴权

---

### 12.4 风险降级因素

在充分证据支持下可以降低处理优先级，例如：

- 漏洞代码路径实际未使用
- 组件只存在于测试环境
- 受严格网络隔离
- 存在可靠 WAF / ACL 补偿控制
- 漏洞只影响未启用功能

**MUST：所有人工降级必须保留分析证据和审核人。**

---

## 13. 漏洞整改 SLA

建议建立统一漏洞整改 SLA。

初始建议值：

| 风险等级 | 建议整改时间 |
|---|---|
| 严重 | 24～72 小时内完成临时控制，并尽快完成正式修复 |
| 高危 | 7 天内 |
| 中危 | 30 天内 |
| 低危 | 90 天内或随版本整改 |

以上属于公司制度制定前的建议值，最终需要结合业务重要性、发布周期和管理要求确认。

**MUST：无法在 SLA 内完成修复的问题进入安全例外流程。**

---

## 14. 新增漏洞与存量漏洞治理

存量安全问题较多时，不建议第一天就阻断所有历史问题。

推荐路线：

~~~text
阶段 1：全量扫描，不阻断
阶段 2：禁止新增 Critical
阶段 3：禁止新增 Critical + High
阶段 4：逐步清理存量 Critical / High
阶段 5：加入超期漏洞阻断
~~~

核心思想：

> 老问题需要计划治理，新代码不能持续制造同等级的新问题。

---

## 15. SCA 发布阻断策略

### 15.1 推荐优先阻断

- 新增 Critical 漏洞
- 新增 High 漏洞
- 已确认可利用的严重漏洞
- 已被真实攻击利用的漏洞
- 已超过 SLA 的 Critical
- 未获得例外审批的重大风险

---

### 15.2 不建议的阻断策略

不建议：

~~~text
发现任意 CVE → 构建失败
~~~

这种策略容易造成：

- 大量无效阻断
- 误报压力
- 开发绕过安全工具
- 发布流程瘫痪
- 安全平台失去可信度

---

## 16. SonarQube 与 SAST

### 16.1 SAST 重点风险

静态代码扫描重点关注：

- SQL 注入
- 命令注入
- 路径穿越
- SSRF
- XXE
- 弱加密
- 不安全反序列化
- 敏感信息泄露
- 不安全随机数
- 安全配置错误
- 危险 API
- Java/Spring 常见鉴权和输入校验问题

---

### 16.2 SonarQube 问题类型

需要区分：

- Bug
- Vulnerability
- Security Hotspot
- Code Smell

**注意：Security Hotspot 不等于已确认漏洞。**

Security Hotspot 通常需要人工 Review，根据上下文判断是否安全。

---

### 16.3 Quality Gate

建议逐步将 Quality Gate 接入 Jenkins。

例如：

~~~text
新增严重安全问题 > 0
        ↓
Pipeline Fail
~~~

但是在强制启用之前，应先在公司真实项目中验证规则质量，避免大量误报导致全部项目无法构建。

---

### 16.4 New Code 优先

推荐优先治理 New Code。

原则：

> 不要求一次性清理全部历史代码问题，但新代码不允许持续引入同等级重大问题。

---

## 17. Secret Scan 进一步要求

Secret Scan 建议覆盖：

- Git Commit
- Merge Request
- 主分支
- Jenkins Workspace
- 构建制品

重点识别：

- RSA Private Key
- SSH Private Key
- Git Token
- Jenkins Token
- Database Password
- JWT Secret
- OAuth Secret
- API Key
- 云厂商 AccessKey / SecretKey

误报应建立白名单，但白名单必须有明确原因和审核记录。

---

## 18. SBOM

### 18.1 目标

SBOM 用于记录软件中包含的第三方组件，可以理解为软件“成分表”。

至少包括：

- 组件名称
- 组件版本
- 包类型
- 依赖关系
- License
- Hash

---

### 18.2 价值

出现新的严重 CVE 后，可以快速查询：

~~~text
某组件出现严重漏洞
        │
        ▼
查询 SBOM
        │
        ├── 系统 A
        ├── 系统 B
        └── 系统 C
~~~

从而快速确定公司受影响范围。

---

### 18.3 管理要求

**SHOULD：**

- Release 构建生成 SBOM。
- SBOM 与构建编号、Commit、制品版本绑定。
- SBOM 存入制品仓库或安全平台。
- SBOM 可以按组件版本反查业务系统。

---

## 19. Docker 与镜像安全

### 19.1 基础镜像

应尽量使用：

- 公司批准基础镜像
- 官方可信镜像
- 固定版本

不建议长期使用 latest。

---

### 19.2 镜像扫描

镜像进入生产前应扫描：

- OS 包漏洞
- 应用依赖漏洞
- Secret
- 不安全配置
- 不必要工具和组件

---

### 19.3 容器权限

容器原则上：

- 非必要不使用 root
- 禁止无必要 privileged
- 限制 Linux Capability
- 文件系统尽量只读
- 不挂载敏感宿主目录
- 不暴露 Docker Socket

---

## 20. IaC 与 Kubernetes 安全

如果公司使用 Kubernetes YAML、Helm、Terraform、Ansible 等，应逐步加入 IaC 扫描。

重点检查：

- privileged
- hostNetwork
- hostPath
- root 用户
- ServiceAccount 高权限
- Secret 明文
- 过宽 RBAC
- 不必要公网暴露
- 不安全 SecurityContext
- 未设置资源限制
- 不必要的宿主机能力

---

## 21. 制品仓库安全

### 21.1 制品范围

包括：

- JAR
- WAR
- ZIP
- 前端包
- Docker Image
- RPM
- DEB

---

### 21.2 正式制品要求

**MUST：正式 Release 制品：**

- 不允许随意覆盖。
- 不允许人工修改内容后仍使用原版本号。
- 保存 SHA-256。
- 记录构建来源。
- 记录构建时间。
- 能够追溯 Commit。
- 能够追溯 Jenkins Job 和 Build Number。

---

### 21.3 制品权限

至少区分：

- Upload
- Download
- Delete
- Admin

普通开发人员不应默认拥有正式制品删除权限。

---

## 22. CI/CD 发布门禁

推荐流程：

~~~text
Git Commit
   │
   ▼
Code Review
   │
   ▼
Secret Scan
   │
   ▼
SAST
   │
   ▼
SCA
   │
   ▼
Unit Test
   │
   ▼
Build
   │
   ▼
Artifact / Image Scan
   │
   ▼
Quality Gate
   │
   ▼
Release Artifact
   │
   ▼
Deploy Approval
   │
   ▼
Production
~~~

---

### 22.1 初始强制阻断建议

可优先对以下情况进行阻断：

- 高可信 Secret 泄露
- 新增严重 SAST 漏洞
- 新增 Critical SCA 漏洞
- 已确认可利用重大漏洞
- 构建失败
- 单元测试失败
- 制品扫描发现明确重大风险
- 制品无法追溯源码或构建记录

---

### 22.2 发布绕过

紧急发布如果需要绕过安全门禁，必须：

1. 明确绕过原因。
2. 指定业务负责人。
3. 指定安全风险负责人。
4. 记录审批。
5. 设置补做安全检查时间。
6. 发布后及时复测。

禁止长期关闭 Gate 作为“临时解决办法”。

---

## 23. 安全例外机制

业务无法在规定时间修复时，不允许简单标记“忽略”。

必须创建安全例外记录。

至少包含：

- 项目
- 漏洞/CVE
- 风险等级
- 业务影响
- 无法修复原因
- 当前补偿控制
- 责任人
- 安全审核人
- 审批人
- 到期时间
- 正式修复计划

**MUST：例外具有到期时间，不允许无限期永久例外。**

---

## 24. 漏洞误报管理

扫描工具出现误报属于正常情况，但误报必须有证据。

建议记录：

| 字段 | 内容 |
|---|---|
| 漏洞 ID | 唯一编号 |
| 工具 | Sonar/SCA/Secret |
| 项目 | 项目名 |
| 结论 | False Positive / Not Applicable |
| 原因 | 技术分析 |
| 证据 | 代码/配置/日志 |
| 审核人 | 安全 |
| 日期 | 审核时间 |

禁止开发人员无说明地自行关闭高风险问题。

---

## 25. 漏洞复测

漏洞修复完成后必须复测。

复测方式可以包括：

- SCA 重新扫描
- SAST 重新扫描
- 人工代码 Review
- DAST
- 安全专项测试
- 组件版本核对
- 配置核对

**MUST：复测通过后问题才能正式关闭。**

---

## 26. 安全审计证据

DevSecOps 至少应保留以下证据：

- Jenkins 构建记录
- Git Commit
- Merge Request
- Code Review
- SonarQube 扫描结果
- SCA 报告
- Secret Scan 报告
- SBOM
- 制品 SHA-256
- 发布记录
- 漏洞整改记录
- 安全例外
- 漏洞复测记录
- 高权限账号变更记录

---

## 27. 安全度量指标

### 27.1 漏洞指标

建议统计：

- Critical 数量
- High 数量
- 新增漏洞数量
- 已关闭漏洞数量
- 超期漏洞数量
- 漏洞平均修复时间
- 各项目未修复漏洞趋势

---

### 27.2 安全覆盖率

例如：

~~~text
SAST 覆盖率 = 已接入 SAST 项目数 / 应接入项目总数
SCA 覆盖率 = 已接入 SCA 项目数 / 应接入项目总数
Secret Scan 覆盖率 = 已接入 Secret Scan 项目数 / 应接入项目总数
SBOM 覆盖率 = 可生成 SBOM 项目数 / 应接入项目总数
~~~

---

### 27.3 CI 阻断指标

统计：

- SAST 阻断次数
- SCA 阻断次数
- Secret Scan 阻断次数
- 人工绕过次数
- 误报次数
- 平均处理时长

这些数据用于调整规则，而不是单纯考核开发人员。

---

## 28. 公司级 DevSecOps Dashboard

建议最终建立统一 Dashboard：

~~~text
公司 DevSecOps

项目
│
├── 总项目数
├── SAST 覆盖率
├── SCA 覆盖率
├── Secret Scan 覆盖率
└── SBOM 覆盖率

漏洞
│
├── Critical
├── High
├── Medium
├── Low
└── 超期漏洞

供应链
│
├── Jenkins
├── Git
├── Maven/Nexus
├── Docker
└── Kubernetes

趋势
│
├── 新增漏洞
├── 已关闭漏洞
├── 平均修复时间
└── CI Gate 阻断次数
~~~

---

## 29. DevSecOps 成熟度路线

## 阶段 1：可见

目标：先知道公司有哪些安全问题。

实施：

- SAST
- SCA
- Secret Scan
- 项目和资产清单

初期以发现问题为主，不急于全量阻断。

---

## 阶段 2：治理

建立：

- 漏洞责任人
- 风险分级
- SLA
- 整改流程
- Dashboard
- 误报与例外流程

---

## 阶段 3：门禁

CI/CD 开始阻断：

- 新增 Critical
- 新增 High
- 高可信 Secret
- 已确认重大漏洞

---

## 阶段 4：供应链深化

加入：

- SBOM
- 镜像安全
- IaC Scan
- 制品完整性
- 基础镜像治理
- Maven/Nexus 来源治理

---

## 阶段 5：持续运营

形成：

~~~text
发现
 ↓
分析
 ↓
修复
 ↓
复测
 ↓
度量
 ↓
规则优化
~~~

---

## 30. 推荐落地优先级

结合公司已有 Java、Jenkins、SonarQube、Maven 等研发体系，建议按以下顺序推进。

## P0：优先完成

1. Git 主分支保护。
2. Jenkins 管理员权限梳理。
3. Jenkins Credentials 治理。
4. SonarQube 项目全量接入。
5. SCA 全量扫描。
6. Secret Scan。
7. Critical / High 漏洞统一统计。
8. 漏洞整改 owner。
9. 漏洞整改和复测流程。
10. 建立安全例外制度。

---

## P1：第二阶段

1. CVSS + 业务风险分级。
2. 正式漏洞整改 SLA。
3. SCA 新增漏洞阻断。
4. SonarQube Quality Gate。
5. Maven/Nexus 仓库治理。
6. SBOM。
7. Docker 镜像扫描。
8. 制品 SHA-256。
9. CI 构建可追溯。

---

## P2：成熟阶段

1. Kubernetes IaC Scan。
2. 镜像签名。
3. 制品签名。
4. 临时 Jenkins Agent。
5. 供应链威胁检测。
6. 安全指标 Dashboard。
7. 全链路安全审计。

---

## 31. 日常检查清单

## 每日

- [ ] Critical 漏洞是否新增
- [ ] 是否发现新的 Secret
- [ ] Jenkins 是否存在高危安全告警
- [ ] CI 安全 Gate 是否异常失败
- [ ] 是否出现未经审批的 Gate 绕过

## 每周

- [ ] High 漏洞整改进度
- [ ] 超期漏洞
- [ ] 新增第三方依赖
- [ ] Jenkins 管理员变化
- [ ] Git 高权限用户变化
- [ ] 新增外部 Maven/NPM 仓库
- [ ] 安全例外即将到期项

## 每月

- [ ] Jenkins 插件安全更新
- [ ] Git 权限 Review
- [ ] Maven/Nexus 权限 Review
- [ ] SCA 全量重新扫描
- [ ] Secret 全量扫描
- [ ] 安全例外 Review
- [ ] SBOM 覆盖率
- [ ] CI Gate 命中和误报分析
- [ ] 制品可追溯性抽查

---

## 32. 单项目安全检查模板

每个项目建议记录：

~~~text
项目名称：
系统负责人：
研发负责人：
Git 地址：
默认分支：
Jenkins Job：
Sonar Project Key：
SCA Project：
制品仓库：
生产环境：

主分支保护：是 / 否
Code Review：是 / 否
SAST：已接入 / 未接入
SCA：已接入 / 未接入
Secret Scan：已接入 / 未接入
SBOM：已接入 / 未接入
制品 Hash：已接入 / 未接入

Critical：
High：
Medium：
Low：
超期漏洞：

当前安全例外：
最近安全扫描时间：
最近人工 Review 时间：
最近发布版本：
对应 Commit：
对应 Jenkins Build：
~~~

---

## 33. 公司级整改流程

推荐统一为：

~~~text
扫描发现
   ↓
自动创建问题 / 汇总报告
   ↓
安全初步分析
   ↓
确认项目与责任人
   ↓
风险定级
   ↓
研发整改
   ↓
重新构建
   ↓
重新扫描
   ↓
安全复测
   ↓
关闭
~~~

无法按期整改：

~~~text
无法修复
   ↓
提交安全例外
   ↓
风险说明
   ↓
补偿控制
   ↓
负责人审批
   ↓
设置到期日期
   ↓
到期重新评估
~~~

---

## 33.1 可信构建、Provenance 与 SLSA v1.2

在现有 SAST、SCA、Secret、SBOM 和制品扫描基础上，供应链安全应进一步回答：

> 这个生产制品是否确实由预期源码、预期 Builder、预期 Pipeline 生成，且构建过程没有被未授权修改？

建议参考 SLSA v1.2 逐步增强：

### Build Provenance

正式制品逐步关联：

- Source Repository。
- Commit。
- Builder Identity。
- Build Invocation。
- Build Time。
- Artifact Digest。
- Provenance Attestation。

### Trusted Builder

高风险项目 SHOULD：

- 使用受控 Builder。
- 普通项目代码不能修改 Builder 安全策略。
- 构建节点最小权限。
- 构建环境尽量临时化。
- Build 后清理 Secret。

### Ephemeral Runner

优先逐步采用临时 Jenkins Agent/Kubernetes Pod Runner，每次构建从干净环境启动并在结束后销毁。

### Artifact Signing

成熟阶段正式 Release 制品自动签名：

~~~text
Source
  ↓
Trusted CI
  ↓
Build
  ├── SBOM
  ├── Provenance
  └── Signature
       ↓
Verify Before Deploy
       ↓
Production
~~~

### Deploy Verification

生产部署平台 SHOULD 在部署前验证：

- Artifact Digest。
- Signature。
- Provenance。
- Approved Repository。
- Security Gate。

### Attestation

除 Provenance 外，可逐步对以下结果产生可验证 Attestation：

- SAST。
- SCA。
- SBOM。
- Image Scan。
- Policy Check。

### Source Track

随着能力成熟，可进一步关注源码仓库保护、变更审核和来源可信，使 Source → Build → Artifact → Deployment 形成连续可信链。

### 指标

- Provenance 覆盖率。
- Artifact Signing 覆盖率。
- Ephemeral Runner 覆盖率。
- 部署签名验证覆盖率。
- 无法追溯制品数量。

详细平台化实施见 22 Security Engineering Platform。

---

## 34. 公司当前需要补充的信息

为了让本规范从通用框架变成公司的正式执行标准，后续需要补充以下真实信息：

- [ ] Git 平台类型及版本
- [ ] Git 管理员名单
- [ ] Git 主分支保护现状
- [ ] Jenkins 版本
- [ ] Jenkins 插件清单
- [ ] Jenkins Agent 架构
- [ ] Jenkins Credentials 使用现状
- [ ] SonarQube 版本
- [ ] SonarQube Quality Gate 当前配置
- [ ] 当前 SCA 工具和漏洞数据来源
- [ ] CVSS 阻断阈值
- [ ] Maven 私服类型、版本和仓库结构
- [ ] Nexus/Artifactory 权限
- [ ] Docker Registry
- [ ] Kubernetes 环境
- [ ] 当前发布审批流程
- [ ] 当前漏洞整改 SLA
- [ ] 安全例外审批人
- [ ] 安全 Dashboard 实现方式

---

## 35. 关键原则总结

DevSecOps 的核心不是“安装更多工具”，而是形成闭环：

~~~text
开发
 ↓
自动安全扫描
 ↓
风险判断
 ↓
修复
 ↓
CI Gate
 ↓
可信制品
 ↓
部署
 ↓
持续监控
~~~

最终目标是：

> **让存在重大安全风险的软件尽可能无法轻易进入生产环境，同时保证安全治理具备可解释、可例外、可追溯和可持续运营能力。**

一个有效的 DevSecOps 体系应该做到：

- 安全问题尽可能早发现。
- 开发人员能够理解问题。
- 修复建议明确。
- 误报能够快速处理。
- 高风险问题可以自动阻断。
- 业务紧急情况存在受控例外机制。
- 所有关键操作可审计。
- 安全流程不会因为规则粗暴而迫使研发绕过系统。

---

## 36. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立 DevSecOps 与软件供应链安全总体框架 |
| V0.2 | 2026-09 | 详细补充 Git、Jenkins、Maven/Nexus、SonarQube、SCA、CVSS、Secret、SBOM、镜像、制品、CI/CD Gate、SLA、例外、审计和运营要求 |
| V0.3 | 2026-09 | 增加 SLSA v1.2、Provenance、Attestation、Artifact Signing 与 Trusted Builder 路线 |

