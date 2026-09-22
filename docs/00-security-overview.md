---
aliases:
  - "公司安全体系总览"
type: "overview"
domain: "governance"
phase:
  - "govern"
priority: "P0"
status: "active"
tags:
  - "security"
  - "security/type/overview"
  - "security/domain/governance"
  - "security/priority/p0"
  - "security/phase/govern"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/01-governance-and-policy]]"
  - "[[docs/02-assets-and-network-architecture]]"
  - "[[docs/04-identity-and-access-control]]"
  - "[[docs/06-application-and-api-security]]"
  - "[[docs/09-vulnerability-and-penetration-testing]]"
  - "[[docs/10-monitoring-and-security-operations]]"
  - "[[docs/11-incident-response]]"
  - "[[docs/12-backup-dr-and-reliability]]"
  - "[[docs/13-compliance-and-audit]]"
---
# 00 - 公司安全体系总览

> 本文档定义公司信息与网络安全体系的总体框架、治理原则、控制域、角色分工、风险闭环和建设路线。体系参考 NIST CSF 2.0 的 Govern、Identify、Protect、Detect、Respond、Recover 六类功能，并结合 CIS Controls v8.1 的优先化实践进行公司化落地；参考不代表公司自动满足任何外部认证或监管要求。

> 如果需要快速理解 00～30 各章节之间的关系，优先查看 **[公司安全知识图谱](knowledge-map.md)**。

## 1. 建设目标

公司安全体系需要实现：

- 资产、系统、数据和公网暴露面可见。
- 每个关键资产与风险都有明确 Owner。
- 网络、身份、主机、应用、数据和供应链有基础控制。
- 漏洞、异常和攻击能够被发现并分级处理。
- 安全事件可以遏制、取证、恢复和复盘。
- 关键控制有日志、工单、报告等审计证据。
- 安全、性能、稳定性和业务连续性统一考虑。
- 通过指标持续衡量安全能力。

## 2. 适用范围

覆盖员工与外包、办公终端、Windows/Linux、网络设备、防火墙/WAF/VPN、域名证书、公网 IP、Java/Spring/Web/API、数据库/Redis/MQ/Elasticsearch、Git/Jenkins/SonarQube、Maven/Nexus/Artifactory、Docker/Kubernetes、云资源、数据、备份、第三方及安全运营。

## 3. 控制级别

- **MUST**：强制要求，不满足必须进行例外或风险接受审批。
- **SHOULD**：推荐要求，应尽量实施。
- **MAY**：按风险与成熟度选择实施。

## 4. 总体原则

### 4.1 风险驱动
优先保护核心业务、敏感数据、公网系统、高权限系统、研发供应链和可能造成大范围影响的控制点。

### 4.2 默认拒绝
网络、权限和数据访问遵循“默认拒绝，按需开放”。

### 4.3 最小权限
只授予完成工作所需的最小权限、最短时间和最小访问范围。

### 4.4 纵深防御
不得把安全完全依赖于单一产品。Web 系统应综合使用认证、授权、安全编码、WAF、网络隔离、日志和漏洞管理。

### 4.5 安全左移
安全要求应进入需求、架构、Code Review、CI/CD、测试和发布流程。

### 4.6 可追溯
关键操作应能够回答：谁、何时、对什么资产、做了什么、为什么、结果如何。

### 4.7 环境隔离
生产、测试、开发、办公环境根据风险实施网络和权限隔离。

### 4.8 安全与稳定性协同
补丁、扫描、WAF、日志、加密和网络策略变更必须考虑可用性和回退。

## 5. 六大安全功能

| 功能 | 公司关注点 | 对应章节 |
|---|---|---|
| Govern | 制度、责任、风险、第三方、审计、产品安全 | 01、13、18、20 |
| Identify | 资产、架构、数据、依赖、云资产、Threat Model | 02、07、08、16、17 |
| Protect | 网络、IAM、主机、应用、数据、Zero Trust、密码学、移动与 AI | 03～08、12、15、16、21、23、24 |
| Detect | 漏洞、日志、威胁情报、攻击验证 | 09、10、19 |
| Respond | 事件分级、遏制、取证、PSIRT | 11、20 |
| Recover | 恢复、容灾、复盘、产品与供应链改进 | 11、12、18、22 |

## 6. 控制域

公司至少维护：安全治理、资产、网络、IAM、主机、应用、数据、供应链、漏洞、安全运营、事件响应、业务连续性、审计与基线检查，并建设 Zero Trust、Cloud/Workload、Security Architecture、Product Security、Threat-informed Defense、PSIRT、Crypto/PKI、Security Engineering Platform、AI/Agent、Mobile、Email、Privacy、TPRM、BIA/BCP、Physical/Media 与 Security Awareness。

## 7. 角色职责

| 角色 | 主要责任 |
|---|---|
| 管理层 | 风险偏好、重大风险接受、资源 |
| 安全负责人 | 体系规划、风险升级、重大事件协调 |
| 安全工程师 | 扫描、基线、运营、测试、复测 |
| 系统负责人 | 对业务资产和剩余风险负责 |
| 研发负责人 | 安全开发、漏洞修复、代码质量 |
| 运维/SRE | 主机、网络、发布、监控、容灾 |
| 数据负责人 | 数据分类、授权和保护 |
| 审计/内控 | 独立检查控制执行和整改 |
| 全体员工 | 遵守制度并报告异常 |

## 8. Owner 原则

**MUST：任何生产资产必须有明确 Owner。**

Critical/High 风险至少明确系统负责人、整改负责人和截止日期。安全团队负责规则、检测和推动，但业务系统负责人承担资产风险责任。

## 9. 风险闭环

~~~text
识别资产 → 识别威胁/脆弱性 → 风险评估 → 建立控制
→ 持续检测 → 发现问题 → 整改/补偿 → 复测
→ 关闭/例外 → 度量与复盘
~~~

## 10. 风险等级

统一使用 Critical、High、Medium、Low。定级综合技术严重程度、资产重要性、数据敏感性、公网暴露、可利用性、真实攻击情况和补偿控制，不得机械复制扫描工具 Severity。

## 11. 核心资产

建议重点关注统一认证、核心业务、核心数据库、Git、Jenkins、制品仓库、VPN、堡垒机、云管理平台、备份平台、IAM/域控和安全管理平台。最终名单由公司确认。

## 12. 安全例外

无法满足 MUST 时必须记录控制项、原因、影响、补偿控制、责任人、审批人、生效与到期时间、正式整改计划。

**MUST：禁止无限期永久例外。**

## 13. 核心指标

### 资产
- 资产纳管率
- 公网资产识别率
- 无 Owner 资产数
- EOL 资产数

### 身份
- MFA 覆盖率
- 高权限账号数
- 离职权限及时回收率
- 共享账号数

### 漏洞
- Critical/High 数量
- 超期率
- 漏洞 MTTR
- SAST/SCA 覆盖率

### 运营与事件
- 日志接入率
- 高危告警响应时间
- MTTD
- 事件 MTTR
- 重复事件数

### 连续性
- 备份成功率
- 恢复测试通过率
- RTO/RPO 达标率
- 演练完成率

## 14. 安全会议机制

### 每周
关注新增 Critical、未修复 High、安全事件、公网风险和重大变更。

### 每月
输出安全运营月报、漏洞月报、资产变化、权限风险和重点整改。

### 每季度
管理层风险 Review、权限复审、基线检查、应急/容灾演练和第三方风险复审。

## 15. 建设优先级

### P0
资产台账、系统 Owner、公网暴露面、Git/Jenkins/SCA/Sonar 纳管、Critical/High 流程、管理员治理、主机基线、日志集中、应急联系人、备份恢复验证。

### P1
网络分区、SIEM 规则、Security Gate、数据分类、自动资产发现、安全 Dashboard、定期渗透测试、不可变备份、容灾演练、供应商治理。

### P2
控制自动验证、PAM/JIT、威胁情报联动、SOAR、SBOM 与资产联动、统一风险平台、安全与 SRE 联合 Dashboard。

## 15.1 安全成熟度模型

建议结合 OWASP SAMM 与公司实际，将各安全域按成熟度管理，而不是仅统计“是否有制度”。

### L0 - 未建立
主要依赖个人经验，控制不可重复。

### L1 - 基础可执行
有制度、Owner、人工流程和基础检查。

### L2 - 标准化与自动化
流程统一，CI/CD、IAM、日志、基线和安全平台自动执行主要控制。

### L3 - 持续验证与工程化
具备 Secure by Default、Golden Path、Zero Trust、可信供应链、持续攻击验证和自动风险闭环。

成熟度用于规划投资和能力改进，不应简单作为团队绩效排名。

## 15.2 Security Program V2.0

安全体系的核心管理工件统一放在 [governance](governance/README.md)：

- [Control Catalog](governance/security-control-catalog.md)：统一 Requirement 与 Control ID。
- [Current / Target Profile](governance/security-current-target-profile.md)：只依据真实证据评估当前能力。
- [Security RACI](governance/security-raci.md)：明确 R/A/C/I。
- [Company Security Parameters Register](governance/company-security-parameters-register.md)：统一维护平台、版本、SLA、Owner、RTO/RPO 等公司参数。
- [Document Hierarchy](governance/document-hierarchy-and-maintenance.md)：统一 Policy、Standard、SOP、Playbook、Baseline 和 Template。

原则：**文档已经写明 ≠ 控制已经实施；Current Profile 必须以配置、日志、报告、工单或演练证据为准。**

## 16. 审计证据

至少能够提供资产台账、网络拓扑、权限清单、制度版本、漏洞报告、整改记录、构建发布记录、日志告警、事件记录、备份恢复记录、安全例外和审计整改记录。

## 17. 参考框架

- NIST Cybersecurity Framework 2.0
- CIS Critical Security Controls v8.1
- OWASP Top 10:2025
- OWASP ASVS 5.0.0
- NIST SP 800-61 Rev.3

- NIST SP 800-207 / 800-207A
- NIST SSDF / SP 800-218A
- SLSA v1.2
- OWASP SAMM
- OWASP MASVS
- Microsoft SDL
- CISA Secure by Design

## 18. 公司参数与待确认项

各章节中的待确认项由 [公司安全参数登记表](governance/company-security-parameters-register.md) 统一管理。Domain 文档可保留必要上下文，但参数登记表是 V2.0 的统一 Source of Truth。

## 19. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立总体框架 |
| V0.2 | 2026-09 | 按六大安全功能完善整体体系 |
| V0.3 | 2026-09 | 增加 15～24 进阶安全能力与安全成熟度模型 |
| V0.4 | 2026-09 | 升级为 Security Program V2.0，增加治理工件与 25～30 企业级安全域 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：无
- **下游知识**：[[docs/01-governance-and-policy|01 安全治理与制度]] · [[docs/02-assets-and-network-architecture|02 资产与网络架构]] · [[docs/04-identity-and-access-control|04 身份与访问控制]] · [[docs/06-application-and-api-security|06 应用与 API 安全]] · [[docs/09-vulnerability-and-penetration-testing|09 漏洞管理与授权渗透测试]] · [[docs/10-monitoring-and-security-operations|10 日志监控与安全运营]] · [[docs/11-incident-response|11 安全事件与应急响应]] · [[docs/12-backup-dr-and-reliability|12 备份容灾与稳定性协同]] · [[docs/13-compliance-and-audit|13 合规与审计]]
- **横向关联**：无

<!-- obsidian-relations:end -->
