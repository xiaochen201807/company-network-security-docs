---
aliases:
  - "Product Security 与 Secure by Default"
type: "standard"
domain: "product-security"
phase:
  - "protect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/product-security"
  - "security/priority/p1"
  - "security/phase/protect"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/06-application-and-api-security]]"
  - "[[docs/08-devsecops-and-supply-chain]]"
  - "[[docs/17-security-architecture-and-threat-modeling]]"
  - "[[docs/20-psirt-and-vulnerability-disclosure]]"
  - "[[docs/22-security-engineering-platform]]"
  - "[[docs/23-ai-llm-agent-security]]"
  - "[[docs/24-mobile-application-security]]"
---
# 18 - Product Security 与 Secure by Default

> 本文档用于把安全责任从“用户自己加固”前移到产品设计、默认配置、发布、维护和生命周期管理。目标是让产品最容易使用的方式同时也是更安全的方式。

## 1. 目标

- 产品默认配置具备合理安全性。
- 用户不需要先阅读复杂加固手册才能避免明显风险。
- 安全功能不是可有可无的附加项。
- 产品漏洞、更新、EOL、客户通知具备统一机制。
- 安全责任进入产品规划和发布决策。

## 2. 适用范围

- 对外交付的软件。
- SaaS。
- 客户私有化部署。
- SDK。
- Agent。
- API 产品。
- 中间件/平台产品。
- 移动应用。
- 内部公共平台。

## 3. Secure by Design

设计阶段考虑：

- 攻击者如何滥用。
- 默认信任边界。
- 管理面。
- 权限模型。
- 数据最小化。
- 更新机制。
- 客户错误配置风险。

安全不是发布前再加。

## 4. Secure by Default

默认状态 SHOULD：

- 认证开启。
- 最小权限。
- 敏感管理接口不公网开放。
- 默认使用 TLS（适用场景）。
- 审计日志开启。
- 默认禁用危险 Debug。
- 安全 Header/配置合理。
- 不使用默认弱口令。

## 5. 默认账号

禁止：

- admin/admin。
- 123456。
- 公共固定默认密码。

首次初始化 SHOULD 强制用户设置管理员身份和强凭据。

## 6. 安全初始配置

首次部署流程应明确：

- 管理员初始化。
- TLS/证书。
- Secret。
- 数据库。
- 外部网络。
- 日志。
- 备份。
- MFA（支持时）。

## 7. 管理接口

产品的管理接口：

- 与业务接口分离。
- 有强认证。
- 支持来源限制。
- 默认不公网。
- 有操作审计。

## 8. 安全 Feature

对高价值产品 SHOULD 提供：

- MFA。
- SSO。
- RBAC。
- Audit Log。
- API Token Scope。
- Session 管理。
- IP Restriction。
- Security Notification。

## 9. 不把安全作为“高级付费选项”

关键基础安全能力不应因为商业套餐导致默认用户完全无法启用合理保护。具体商业策略由公司决定，但应避免产生结构性安全风险。

## 10. 默认最小权限

新建：

- 用户。
- Token。
- Service Account。
- API Key。
- Integration。

默认只给最低必要权限。

## 11. 安全错误处理

默认错误页面：

- 不显示堆栈。
- 不泄露内部路径。
- 不暴露数据库信息。
- 提供 Request ID 便于支持。

## 12. 默认日志

关键审计默认记录：

- 登录。
- 管理员操作。
- 权限变化。
- Token。
- 配置变化。
- 数据导出。

## 13. 安全配置向导

复杂产品可提供安全检查：

- 当前是否使用默认密码。
- 是否公网暴露。
- TLS 是否配置。
- 管理员 MFA。
- 备份。
- 审计。

## 14. 安全配置警告

当客户执行危险操作时：

- 明确风险。
- 要求确认。
- 高风险动作可二次认证。
- 不使用模糊描述。

## 15. 产品 Threat Model

每个主要产品应维护 Threat Model，并随架构变化更新。

## 16. Product Security Owner

产品 SHOULD 有明确 Product Security Owner 或责任团队，负责：

- 安全需求。
- Threat Model。
- 发布风险。
- 漏洞响应。
- 安全公告。
- 客户沟通。

## 17. Security Champion

研发团队建立 Champion 机制，协助落实安全工程实践。

## 18. 产品安全门禁

正式发布前至少检查：

- 未批准 Critical。
- 高风险依赖。
- Secret。
- 安全测试。
- 默认配置。
- 管理接口。
- 升级路径。
- 日志。
- 文档。

## 19. 安全更新

产品必须有可操作的更新机制：

- 明确安全版本。
- 发布说明。
- 升级指南。
- 回退说明。
- 客户可识别当前版本。

## 20. Patch Policy

根据产品类型明确：

- Critical 修复目标。
- 受支持版本范围。
- 哪些旧版本获得安全补丁。
- 客户升级责任。
- 临时缓解措施。

## 21. Support Lifecycle

每个主要版本明确：

- GA。
- Maintenance。
- Security Support。
- EOL。

避免客户长期运行“没有人知道还支不支持”的版本。

## 22. EOL Policy

EOL 前：

- 提前通知。
- 提供升级路径。
- 说明安全影响。
- 文档明确截止日期。

EOL 后原则上不继续承诺常规安全修复，除非另有合同约定。

## 23. Version Identification

系统管理员应能可靠查看：

- 产品版本。
- Build。
- Commit/Release。
- 安全更新状态。

同时避免向未认证外部用户暴露不必要精确版本。

## 24. 产品 SBOM

对重要对外交付软件 SHOULD：

- 生成 SBOM。
- 与版本绑定。
- 可用于 CVE 影响分析。
- 根据客户合同决定提供方式。

## 25. Artifact Integrity

正式安装包/镜像：

- Hash。
- Signature（成熟阶段）。
- 来源明确。
- 下载渠道可信。

## 26. 自动更新风险

自动更新机制必须：

- 验证来源。
- 验证签名/完整性。
- 防止降级攻击（按产品风险）。
- 有失败恢复。

## 27. 客户配置兼容

安全升级时评估：

- 是否破坏旧配置。
- 是否导致客户无法登录。
- 是否有 Migration。
- 是否可以灰度。

## 28. 安全文档

客户安全文档至少说明：

- 推荐部署架构。
- 端口。
- TLS。
- 权限。
- Secret。
- 备份。
- 日志。
- 安全更新。
- 已知高风险配置。

## 29. Hardening Guide

复杂私有化产品 SHOULD 提供：

- OS。
- Network。
- Database。
- Middleware。
- Application。
- TLS。
- IAM。
- Audit。

## 30. Deployment Validation

安装完成后可提供自检工具或 Checklist，验证关键安全配置。

## 31. 安全遥测

在合法、透明、符合公司政策与适用要求的前提下，可通过安全遥测发现：

- 版本过旧。
- 默认密码风险。
- 高危配置。
- 攻击趋势。

具体数据收集必须经过隐私/合规评估。

## 32. Security Advisory

安全公告至少包含：

- 影响版本。
- 风险描述。
- 修复版本。
- 缓解措施。
- 致谢（适用时）。
- 发布时间。

## 33. CVE

是否申请 CVE 根据产品、漏洞和披露政策决定。不能为了避免负面影响而隐藏客户真正需要知道的安全风险。

## 34. 客户安全通知

重大漏洞通知：

- 明确受影响版本。
- 明确优先级。
- 提供修复。
- 提供 Workaround。
- 不在修复可用前无必要公开可直接武器化细节。

## 35. 安全兼容性测试

修复安全问题同时测试：

- 功能。
- 性能。
- 升级。
- 回滚。
- 高可用。
- 老版本兼容。

## 36. 产品安全事件

产品安全事件与公司内部 IR 联动，但额外考虑：

- 受影响客户。
- 公共组件。
- 客户通知。
- Advisory。
- 供应链。
- 多版本修复。

## 37. 产品滥用

安全设计还需要考虑：

- API Abuse。
- 批量注册。
- Spam。
- Credential Stuffing。
- Fraud。
- Scraping。
- 资源滥用。

## 38. 安全反馈渠道

产品文档应有明确安全报告入口：

- security@company。
- 安全响应页面。
- 工单渠道。

安全报告不应只进入普通客服后无人处理。

## 39. 指标

- 发布前 Security Review 覆盖率。
- 默认高危配置数量。
- 产品 Critical/High 数量。
- 安全补丁平均发布时间。
- EOL 版本使用比例（可获得时）。
- 客户安全问题重复率。

## 40. P0

1. Secure by Default Checklist。
2. 默认账号治理。
3. Product Security Owner。
4. Support/EOL Policy。
5. Security Advisory 流程。
6. 安全报告入口。

## 41. P1

1. Product Threat Model。
2. Hardening Guide。
3. SBOM。
4. Artifact Signing。
5. Security Champion。
6. 部署安全自检。

## 42. P2

1. Secure-by-default 自动验证。
2. 产品安全遥测。
3. 自动安全更新治理。
4. 客户风险 Dashboard。

## 43. 审计证据

- 产品安全需求。
- Threat Model。
- Release Gate。
- 默认配置测试。
- Advisory。
- Patch Policy。
- EOL 通知。
- SBOM。
- 安全测试。

## 44. 当前待确认

- [ ] 公司是否有对外交付产品
- [ ] 产品安全 Owner
- [ ] 安全补丁 SLA
- [ ] Support/EOL 周期
- [ ] Advisory 发布渠道
- [ ] CVE/披露规则
- [ ] Secure by Default Checklist

## 45. 参考

- CISA Secure by Design / Secure by Default
- Microsoft SDL
- NIST SSDF

## 46. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立 Product Security 与 Secure by Default 规范 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/06-application-and-api-security|06 应用与 API 安全]] · [[docs/08-devsecops-and-supply-chain|08 DevSecOps 与供应链安全]] · [[docs/17-security-architecture-and-threat-modeling|17 安全架构评审与 Threat Modeling]]
- **下游知识**：[[docs/20-psirt-and-vulnerability-disclosure|20 PSIRT 与漏洞披露]]
- **横向关联**：[[docs/22-security-engineering-platform|22 Security Engineering Platform]] · [[docs/23-ai-llm-agent-security|23 AI、LLM 与 Agent 安全]] · [[docs/24-mobile-application-security|24 移动应用安全]]

<!-- obsidian-relations:end -->
