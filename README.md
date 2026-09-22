# 公司网络安全体系文档

> 本项目用于沉淀公司网络安全、应用安全、数据安全、安全运营、漏洞管理、应急响应以及稳定性协同等方面的统一文档。
>
> 当前阶段统一采用 **Markdown（.md）** 编写，后续可按需要生成 PDF、Word、Wiki 或内部知识库版本。

## 1. 建设目标

本项目希望形成一套可长期维护、可落地检查、可审计、可用于培训和应急处置的企业安全知识体系，覆盖：

- 安全治理与制度
- 资产管理与网络架构
- 网络边界与访问控制
- 身份认证与权限管理
- 终端、服务器与操作系统安全
- Web、API、Java 与应用安全
- 数据安全与敏感信息保护
- DevSecOps 与软件供应链安全
- 漏洞管理、扫描与授权渗透测试
- 日志、监控、告警与安全运营
- 安全事件与应急响应
- 备份、容灾、性能与稳定性协同
- 合规、审计与安全检查
- 安全基线与检查清单
- Zero Trust 与设备可信
- 云与 Workload 安全
- 安全架构评审与 Threat Modeling
- Product Security 与 Secure by Default
- 威胁情报、Red Team 与 Purple Team
- PSIRT 与漏洞披露
- 密码学、PKI、KMS 与 Secret 治理
- Security Engineering Platform / Golden Path
- AI、LLM 与 Agent 安全
- 移动应用安全
- 邮件与协作平台安全
- 隐私与个人信息保护
- 第三方风险管理（TPRM）
- BIA 与业务连续性
- 物理、环境与介质安全
- 安全意识与人才体系

## 2. 文档导航

| 编号 | 文档 | 说明 |
|---|---|---|
| 00 | [安全体系总览](docs/00-security-overview.md) | 总体框架、原则、角色和闭环 |
| 01 | [安全治理与制度](docs/01-governance-and-policy.md) | 制度、职责、风险管理与例外流程 |
| 02 | [资产与网络架构](docs/02-assets-and-network-architecture.md) | 资产台账、网络分区、数据流与暴露面 |
| 03 | [网络与边界安全](docs/03-network-and-perimeter-security.md) | 防火墙、VPN、DNS、出口、东西向访问控制 |
| 04 | [身份与访问控制](docs/04-identity-and-access-control.md) | IAM、账号、权限、MFA、最小权限 |
| 05 | [终端与服务器安全](docs/05-endpoint-and-server-security.md) | Windows/Linux、中间件、补丁、基线、EDR |
| 06 | [应用与 API 安全](docs/06-application-and-api-security.md) | SDL、OWASP、Java、接口、认证授权、输入输出 |
| 07 | [数据安全](docs/07-data-security.md) | 数据分类分级、加密、脱敏、备份、泄露防护 |
| 08 | [DevSecOps 与供应链安全](docs/08-devsecops-and-supply-chain.md) | SAST/SCA/Secret/IaC/CI-CD/制品安全 |
| 09 | [漏洞与授权渗透测试](docs/09-vulnerability-and-penetration-testing.md) | 漏洞发现、验证、修复、复测与授权测试规范 |
| 10 | [日志监控与安全运营](docs/10-monitoring-and-security-operations.md) | 日志、SIEM、告警、SOC、威胁发现 |
| 11 | [安全事件与应急响应](docs/11-incident-response.md) | 分级、响应、取证、恢复、复盘 |
| 12 | [备份容灾与稳定性协同](docs/12-backup-dr-and-reliability.md) | 备份、RTO/RPO、容灾、容量、性能、稳定性 |
| 13 | [合规与审计](docs/13-compliance-and-audit.md) | 审计证据、整改闭环、监管与内控要求 |
| 14 | [安全基线与检查清单](docs/14-security-baselines-and-checklists.md) | 周/月/季度安全检查与基线清单 |
| 15 | [Zero Trust 与设备可信](docs/15-zero-trust-and-device-trust.md) | 条件访问、设备可信、ZTNA、Workload Identity |
| 16 | [云与 Workload 安全](docs/16-cloud-and-workload-security.md) | Cloud IAM、CSPM、Kubernetes、Runtime Security |
| 17 | [安全架构评审与 Threat Modeling](docs/17-security-architecture-and-threat-modeling.md) | DFD、STRIDE、Abuse Case、安全 Sign-off |
| 18 | [Product Security 与 Secure by Default](docs/18-product-security-and-secure-by-default.md) | 产品默认安全、Patch、EOL、Security Advisory |
| 19 | [威胁情报、Red Team 与 Purple Team](docs/19-threat-intelligence-redteam-purpleteam.md) | ATT&CK、攻防演练、Detection Validation |
| 20 | [PSIRT 与漏洞披露](docs/20-psirt-and-vulnerability-disclosure.md) | 外部漏洞接收、VDP、CVE、协调披露 |
| 21 | [密码学、PKI、KMS 与 Secret 治理](docs/21-cryptography-pki-kms-and-secrets.md) | TLS、证书、密钥、KMS/HSM、轮换 |
| 22 | [Security Engineering Platform](docs/22-security-engineering-platform.md) | Golden Path、安全 SDK、Security Gate、SLSA |
| 23 | [AI、LLM 与 Agent 安全](docs/23-ai-llm-agent-security.md) | RAG、Prompt Injection、Tool/MCP、Agent 权限 |
| 24 | [移动应用安全](docs/24-mobile-application-security.md) | Android/iOS、MASVS、存储、网络、逆向与发布 |
| 25 | [邮件与协作平台安全](docs/25-email-and-collaboration-security.md) | SPF/DKIM/DMARC、BEC、OAuth、钓鱼与外发 |
| 26 | [隐私与个人信息保护](docs/26-privacy-and-personal-data-protection.md) | Processing Inventory、PIA/DPIA、Retention |
| 27 | [第三方风险管理](docs/27-third-party-risk-management.md) | Supplier Tier、采购评估、合同、持续监控、退出 |
| 28 | [BIA 与业务连续性](docs/28-business-impact-and-continuity.md) | MTPD、BIA、BCP、关键依赖与演练 |
| 29 | [物理、环境与介质安全](docs/29-physical-and-media-security.md) | 门禁、机房、设备、USB、介质销毁 |
| 30 | [安全意识与人才体系](docs/30-security-awareness-and-workforce.md) | 全员培训、角色培训、Champion、Skills Matrix |

## 2.0 Security Governance V2.0

- [Governance 总览](docs/governance/README.md)
- [Security Control Catalog](docs/governance/security-control-catalog.md)
- [Current / Target Profile](docs/governance/security-current-target-profile.md)
- [Security RACI](docs/governance/security-raci.md)
- [公司安全参数登记表](docs/governance/company-security-parameters-register.md)
- [文档层级与维护规则](docs/governance/document-hierarchy-and-maintenance.md)
- [Information Security Policy](docs/policies/information-security-policy.md)
- [Critical Vulnerability SOP](docs/procedures/critical-vulnerability-sop.md)
- [员工离职/转岗 SOP](docs/procedures/employee-offboarding-sop.md)
- [Account Compromise Playbook](docs/playbooks/account-compromise-playbook.md)
- [Secret Leak Playbook](docs/playbooks/secret-leak-playbook.md)

## 2.1 配套模板

当前已经提供可直接复制使用的 Markdown 执行模板：

### 资产与权限

- [资产台账模板](docs/templates/asset-inventory-template.md)
- [权限申请与复核模板](docs/templates/access-request-and-review-template.md)

### 漏洞与渗透测试

- [漏洞记录模板](docs/templates/vulnerability-record-template.md)
- [安全例外申请模板](docs/templates/vulnerability-exception-template.md)
- [授权渗透测试申请模板](docs/templates/penetration-test-authorization-template.md)
- [漏洞月报模板](docs/templates/monthly-vulnerability-report-template.md)

### 安全运营、连续性与审计

- [安全事件报告模板](docs/templates/security-incident-report-template.md)
- [备份恢复与容灾演练模板](docs/templates/backup-recovery-exercise-template.md)
- [审计发现与整改模板](docs/templates/audit-finding-remediation-template.md)
- [安全基线检查记录模板](docs/templates/security-baseline-check-template.md)

### 架构、产品与新技术

- [Threat Model 模板](docs/templates/threat-model-template.md)
- [Product Security 发布检查模板](docs/templates/product-security-release-checklist.md)
- [PSIRT Case 模板](docs/templates/psirt-case-template.md)
- [Crypto / Key Inventory 模板](docs/templates/crypto-inventory-template.md)
- [AI / LLM / Agent 安全评审模板](docs/templates/ai-security-review-template.md)
- [Mobile Security 检查模板](docs/templates/mobile-security-checklist.md)
- [Privacy Impact Assessment 模板](docs/templates/privacy-impact-assessment-template.md)
- [第三方安全评估模板](docs/templates/third-party-security-assessment-template.md)
- [Business Impact Analysis 模板](docs/templates/business-impact-analysis-template.md)
- [邮件 / Phishing Incident 模板](docs/templates/email-phishing-incident-template.md)

## 2.2 Python 自动质检

项目提供纯 Python 标准库质检脚本：

~~~bash
python3 scripts/security_docs_quality_check.py
~~~

严格模式适合 Jenkins / CI：

~~~bash
python3 scripts/security_docs_quality_check.py --strict
~~~

只分析、不生成报告：

~~~bash
python3 scripts/security_docs_quality_check.py --no-write
~~~

脚本默认生成：

- `reports/security-doc-quality-report.md`
- `reports/security-doc-quality-report.json`

检查范围包括：

- Markdown H1、标题层级、代码围栏与内部链接。
- 00～30 核心章节完整性和 README 导航。
- Governance、Policy、SOP、Playbook、Template 必备工件。
- 08/09 拆分结构与历史归档。
- Control Catalog 的 ID 重复、字段、Level 和引用一致性。
- Current / Target Profile 评估进度。
- 公司安全参数 Open/Resolved 进度。
- 超长活跃文档、孤儿文档、过期版本标记。
- 未完成 Checklist 统计。

退出码：

| Code | 含义 |
|---|---|
| 0 | 通过 |
| 1 | 存在 ERROR |
| 2 | `--strict` 下存在 WARNING |
| 3 | 脚本执行/配置失败 |

Jenkins 示例：

~~~groovy
stage('Security Docs Quality') {
    steps {
        sh 'python3 scripts/security_docs_quality_check.py --strict'
        archiveArtifacts artifacts: 'reports/security-doc-quality-report.*', fingerprint: true
    }
}
~~~

Current Profile 的“待评估”、公司参数“Open”和未勾选检查项属于建设进度信息，默认作为 INFO 输出，不阻断 CI。

## 3. 文档编写约定

每个主题原则上按以下结构维护：

1. **目的**：为什么要做。
2. **适用范围**：适用于哪些系统、人员和环境。
3. **风险说明**：不实施控制会产生什么风险。
4. **安全要求**：必须满足的控制项。
5. **实施方案**：推荐技术与流程。
6. **检查方法**：如何验证控制有效。
7. **审计证据**：需要保留哪些记录。
8. **例外处理**：无法满足时如何审批和补偿。
9. **常见问题**：经验与故障案例。
10. **变更记录**：何时、为什么修改。

## 4. 控制项级别

建议后续统一使用以下级别：

- **MUST**：强制要求，不满足需要正式例外审批。
- **SHOULD**：推荐要求，应尽量实施。
- **MAY**：可选增强措施。

## 5. 安全工作闭环

统一采用以下闭环：

**识别资产 → 识别风险 → 建立控制 → 持续检测 → 发现问题 → 分级处置 → 修复验证 → 复盘改进 → 留存证据**

## 6. 当前状态

当前版本为 **V2.0 Security Program 重构版**：00～30 覆盖核心安全域，同时新增 Control Catalog、Current/Target Profile、RACI、公司参数登记表和正式 Policy/SOP/Playbook 层级；08 DevSecOps 与 09 漏洞管理已由超长单文件拆分为索引 + 专项 Standard/SOP，并保留 V1 历史全文作为迁移参考。

下一阶段正式进入 **公司真实环境取证评估 + 自动化控制落地**：

1. 导入公司真实资产、网络区域、核心系统和数据 Owner。
2. 固化 Git / Jenkins / Maven / SonarQube / SCA 的实际版本、权限和 Gate。
3. 根据当前 Java/Spring 技术栈确定公司安全编码细则和统一组件。
4. 确认漏洞风险等级、SLA、超期升级和安全例外审批链。
5. 将 Windows/Linux/Nginx/Tomcat/JDK/数据库/Redis 等基线转换为自动化检查。
6. 确认日志平台、P1/P2 告警 SLA、值班与 Incident Commander。
7. 为核心系统填写 SLO、RTO、RPO，并执行恢复/容灾演练。
8. 根据实际适用法律法规、客户合同和公司制度建立合规映射。
9. 以 Current/Target Profile 为季度主计划，不再以新增文档数量衡量进度。
10. 新增控制优先进入 Control Catalog，并逐步通过 CI/CD、IAM、SIEM、扫描器和配置平台自动取证。

---
维护原则：**文档必须可执行、可检查、可审计，避免只写概念。**
