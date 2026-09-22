# Security Current / Target Profile

> 本文档用于区分“文档已经定义”与“公司真实已经实施”。Current 必须基于真实证据评估，不能因为规范中写了某项要求就判断为已实施。

## 1. 成熟度等级

| Level | 定义 |
|---|---|
| L0 | 未建立或主要依赖个人经验 |
| L1 | 有基础控制、人工执行，可重复性有限 |
| L2 | 已标准化、覆盖主要范围、可度量，部分自动化 |
| L3 | Secure by Default、平台化、持续验证、自动证据与风险闭环 |

## 2. Current 评估证据

至少引用一种真实证据：配置导出、CMDB、IAM/MFA 报告、扫描、CI/CD、SIEM/EDR、工单、演练、备份恢复或审计抽样。

## 3. 初始 Profile

> Current 一律先标记“待评估”，直到拿到公司真实证据。Recommended Target 是建议目标，不等于管理层已批准目标。

| Domain | Current | Recommended Target | Priority | 关键 Gap |
|---|---|---|---|---|
| Governance | 待评估 | L2 | P0 | Owner、风险接受、控制证据 |
| Asset | 待评估 | L2 | P0 | 资产与公网暴露完整性 |
| Network | 待评估 | L2 | P0 | 过宽规则、管理面 |
| IAM | 待评估 | L2 | P0 | MFA、离职、服务账号 |
| Endpoint | 待评估 | L2 | P0 | EDR、EOL、补丁 |
| AppSec | 待评估 | L2 | P0 | AuthZ、统一安全基线 |
| Data | 待评估 | L2 | P0 | 分类、导出、Retention |
| DevSecOps | 待评估 | L3 | P0 | Gate、SBOM、Provenance |
| Vulnerability | 待评估 | L2 | P0 | SLA、复测、例外 |
| SOC | 待评估 | L2 | P1 | 日志覆盖、Runbook |
| Incident Response | 待评估 | L2 | P1 | 分级、取证、演练 |
| Reliability/DR | 待评估 | L2 | P0 | RTO/RPO、恢复验证 |
| Audit/GRC | 待评估 | L2 | P1 | 控制映射、自动证据 |
| Baseline | 待评估 | L2 | P0 | 自动化、例外 |
| Zero Trust | 待评估 | L2 | P1 | Device Trust、JIT |
| Cloud | 待评估 | L2 | P1 | Root、IAM、Public Asset |
| Threat Modeling | 待评估 | L2 | P1 | 触发条件、Sign-off |
| Product Security | 待评估 | L2 | P1 | Secure by Default、EOL |
| Threat-informed Defense | 待评估 | L2 | P1 | Validated Coverage |
| PSIRT | 待评估 | L1-L2 | P2 | 接收、SLA、披露 |
| Crypto/PKI | 待评估 | L2 | P1 | Key Owner、Rotation |
| Security Platform | 待评估 | L3 | P1 | SDK、Gate、Self-service |
| AI Security | 待评估 | L1-L2 | 按需 | Provider、Agent Tool |
| Mobile Security | 待评估 | L1-L2 | 按需 | Signing、Storage、API |
| Email Security | 待评估 | L2 | P0 | DMARC、MFA、BEC |
| Privacy | 待评估 | L2 | P1 | Processing Inventory、PIA |
| TPRM | 待评估 | L2 | P1 | Risk Tier、Contract、Offboarding |
| BIA/BCP | 待评估 | L2 | P1 | MTPD、业务连续性 |
| Physical/Media | 待评估 | L1-L2 | P2 | 门禁、介质销毁 |
| Awareness/Workforce | 待评估 | L2 | P1 | 角色培训、Champion |

## 4. Gap Roadmap

每个 Gap 至少记录：Gap ID、Domain、Current、Target、Risk、Priority、Owner、Accountable、Target Date、Evidence 和 Status。

## 5. 升级路径

### L0 → L1
Owner、制度、基础工具、人工流程、关键资产覆盖。

### L1 → L2
统一 Standard、自动扫描、Coverage、SLA、Dashboard、Evidence、定期复审。

### L2 → L3
Golden Path、Policy as Code、Continuous Validation、JIT/Zero Trust、Trusted Build、Risk Graph、自动闭环。

## 6. 第一轮评估顺序

P0：资产、IAM、终端、网络、AppSec、DevSecOps、漏洞、备份恢复、邮件安全。

第二批：SOC、Threat Modeling、Cloud、Crypto、Data/Privacy、TPRM、BCP。

第三批：Zero Trust 深化、Purple Team、Product Security、PSIRT、Security Platform、AI/Mobile。

## 7. 季度输出

1. Current Profile。
2. Target Profile。
3. Top 10 Gaps。
4. 过期 P0/P1。
5. 资源与预算阻塞。
6. 成熟度变化。
7. 管理层风险接受。
