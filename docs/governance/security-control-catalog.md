# Security Control Catalog

> 本文档是公司安全控制的统一目录。后续 Policy、Standard、Baseline、Checklist、审计和自动化检查应尽量引用 Control ID，减少重复和冲突。

## 1. Control ID

格式：SEC-<DOMAIN>-<NNN>。

示例：SEC-GOV-001、SEC-IAM-001、SEC-APP-003、SEC-VUL-002。

## 2. 控制字段

| 字段 | 说明 |
|---|---|
| Control ID | 唯一编号 |
| Requirement | 控制要求 |
| Level | MUST / SHOULD / MAY |
| Owner | 执行责任域 |
| Accountable | 最终责任角色 |
| Scope | 适用范围 |
| Evidence | 证明材料 |
| Frequency | 检查频率 |
| Metric | 度量 |
| Exception | 例外方式 |
| Source | 主要章节 |

## 3. 核心控制

| ID | Requirement | Level | Owner | Evidence | Frequency | Metric | Source |
|---|---|---|---|---|---|---|---|
| SEC-GOV-001 | 生产资产必须有明确 Owner | MUST | IT/System | CMDB | 持续 | Owner 覆盖率 | 00/02 |
| SEC-GOV-002 | 无法满足 MUST 必须走正式例外 | MUST | Security | 例外记录 | 持续 | 过期例外数 | 00/01 |
| SEC-GOV-003 | 重大剩余风险由有权限的业务/管理负责人接受 | MUST | Management/System Owner | 风险接受记录 | 持续 | 未授权接受数 | 01 |
| SEC-GOV-004 | 关键控制必须有可复核证据 | MUST | Control Owner | 日志/工单/报告 | 持续 | Evidence Coverage | 13 |
| SEC-AST-001 | 生产与公网资产进入统一台账 | MUST | IT/Cloud | CMDB/ASM | 持续 | 纳管率 | 02 |
| SEC-AST-002 | 公网暴露必须有业务原因与 Owner | MUST | System Owner | 暴露面清单 | 每周 | 无 Owner 暴露数 | 02/03 |
| SEC-AST-003 | EOL 软件必须升级或正式接受风险 | MUST | System Owner | EOL 报告/例外 | 每月 | EOL 数量 | 02/05 |
| SEC-NET-001 | 跨安全区默认拒绝、按需放行 | MUST | Network | Firewall Rules | 持续 | 过宽规则数 | 03 |
| SEC-NET-002 | 临时网络规则必须有到期时间 | MUST | Network | Rule Metadata | 每周 | 过期临时规则 | 03 |
| SEC-NET-003 | 数据库、Redis、Jenkins、K8s API 等管理面不得无保护公网暴露 | MUST | Ops/Network | ASM/Firewall | 持续 | 高危公网端口 | 03 |
| SEC-IAM-001 | 人员账号一人一号 | MUST | IAM | Account Export | 每月 | 共享账号数 | 04 |
| SEC-IAM-002 | 离职高权限与远程访问及时失效 | MUST | IAM/HR | Offboarding Log | 每次 | 回收及时率 | 04 |
| SEC-IAM-003 | 关键管理面启用 MFA | SHOULD | IAM | MFA Report | 每月 | MFA 覆盖率 | 04/15 |
| SEC-IAM-004 | 服务账号必须有 Owner、最小权限且可轮换 | MUST | System Owner | Service Account Register | 每季度 | 无 Owner 服务账号 | 04 |
| SEC-IAM-005 | 生产高权限逐步采用 JIT/PAM | SHOULD | IAM/Ops | PAM/JIT Log | 持续 | 长期管理员数 | 15 |
| SEC-END-001 | 关键终端/服务器纳入 EDR | MUST | Endpoint/Ops | EDR Inventory | 每日 | EDR 覆盖率 | 05 |
| SEC-END-002 | Critical/High 安全补丁按 SLA 处理 | MUST | Ops | Patch Report | 每周 | 超期率 | 05/09 |
| SEC-END-003 | SSH/RDP 不得无保护公网暴露 | MUST | Ops/Network | ASM | 持续 | 暴露数 | 05 |
| SEC-APP-001 | 敏感接口必须服务端执行认证和授权 | MUST | Development | Review/Test | 每发布 | AuthZ 缺陷数 | 06 |
| SEC-APP-002 | SQL 使用参数化查询，动态标识符白名单 | MUST | Development | SAST/Review | 每提交 | Injection Finding | 06 |
| SEC-APP-003 | 管理/Debug/Actuator 敏感能力不得无保护公网暴露 | MUST | Development/Ops | Config/ASM | 每发布 | 暴露数量 | 06 |
| SEC-APP-004 | 核心/公网/高敏系统进行 Threat Model | SHOULD | Architecture/Dev | Threat Model | 重大变更 | 覆盖率 | 17 |
| SEC-DAT-001 | 核心/敏感数据集有 Owner 与分类 | MUST | Data Owner | Data Catalog | 每季度 | 分类覆盖率 | 07 |
| SEC-DAT-002 | 应用数据库账号不得默认使用 root/superuser | MUST | DBA/Dev | DB Grants | 每月 | 高权应用账号数 | 07 |
| SEC-DAT-003 | 日志不得记录不必要的密码、完整 Token、私钥 | MUST | Dev/SOC | Log Scan | 持续 | 泄露 Finding | 07/10 |
| SEC-DAT-004 | 高风险数据导出必须授权并留审计 | MUST | Data Owner | Export Audit | 持续 | 未授权导出数 | 07 |
| SEC-SUP-001 | 生产仅部署受控 CI/CD 生成的正式制品 | MUST | DevOps | Build/Deploy Record | 每发布 | 非受控制品数 | 08 |
| SEC-SUP-002 | 主分支保护并通过 Review 合并 | MUST | Development | Git Policy | 持续 | 保护覆盖率 | 08 |
| SEC-SUP-003 | Secret 不得硬编码进源码和 Pipeline | MUST | Dev/DevOps | Secret Scan | 每提交 | Secret Finding | 08 |
| SEC-SUP-004 | Release 制品不可被无审计覆盖 | MUST | DevOps | Repository Config | 持续 | 覆盖事件数 | 08 |
| SEC-SUP-005 | 重要制品逐步生成 SBOM 与 Provenance | SHOULD | DevOps | SBOM/Attestation | 每发布 | 覆盖率 | 08/22 |
| SEC-SUP-006 | 高风险供应链逐步实施 Artifact Signing 与部署前验证 | SHOULD | DevOps/Security Platform | Signature/Deploy Verification | 每发布 | 签名验证覆盖率 | 08/22 |
| SEC-VUL-001 | 漏洞必须有 Owner、风险等级、截止时间和状态 | MUST | Security/System Owner | Vulnerability Platform | 持续 | 字段完整率 | 09 |
| SEC-VUL-002 | Critical/High 按公司 SLA 处理 | MUST | System Owner | Ticket/SLA | 每日/周 | 超期率 | 09 |
| SEC-VUL-003 | 高风险误报/不适用必须有技术证据 | MUST | Security | Disposition Record | 持续 | 无证据关闭数 | 09 |
| SEC-VUL-004 | 漏洞关闭前必须复测 | MUST | Security/Verifier | Retest | 每 Finding | 复测覆盖率 | 09 |
| SEC-VUL-005 | 渗透测试必须有明确授权、范围与停止条件 | MUST | Security/System Owner | Authorization | 每次 | 未授权测试数 | 09 |
| SEC-MON-001 | 关键系统安全日志集中留存 | MUST | SOC/Ops | Log Source Register | 每日 | 接入率 | 10 |
| SEC-MON-002 | P1/P2 告警有 Owner、SLA 和 Runbook | SHOULD | SOC | Alert/Runbook | 持续 | SLA 达标率 | 10 |
| SEC-MON-003 | 关键检测通过 Purple Team/模拟攻击验证 | SHOULD | SOC/Red Team | Validation Report | 每季度 | Validated Coverage | 19 |
| SEC-IR-001 | 重大安全事件指定 Incident Commander | MUST | Security | Incident Record | 每事件 | 覆盖率 | 11 |
| SEC-IR-002 | 重大事件保留时间线和关键证据 | MUST | Security/Ops | Timeline/Evidence | 每事件 | Evidence 完整率 | 11 |
| SEC-BCM-001 | 核心系统明确 RTO/RPO | MUST | Business/System Owner | Service Catalog | 年度 | 覆盖率 | 12/28 |
| SEC-BCM-002 | 关键备份必须定期恢复验证 | MUST | Ops | Restore Report | 季度/半年 | 恢复成功率 | 12 |
| SEC-BCM-003 | 核心业务完成 BIA 并识别关键依赖 | SHOULD | Business Continuity | BIA | 年度 | BIA 覆盖率 | 28 |
| SEC-CLD-001 | Cloud Root/Owner 不用于日常操作并启用 MFA | MUST | Cloud | IAM Report | 每月 | 风险账号数 | 16 |
| SEC-CLD-002 | 云公网资源与 Security Group 持续发现 | MUST | Cloud/Security | CSPM | 持续 | Public Risk 数 | 16 |
| SEC-CRY-001 | 高价值证书/密钥进入台账并具备 Owner | MUST | Security Platform/Ops | Crypto Inventory | 每月 | 无 Owner Key 数 | 21 |
| SEC-PRD-001 | 产品不得使用公共固定默认弱口令 | MUST | Product/Dev | Release Test | 每发布 | 违规数 | 18 |
| SEC-PSI-001 | 外部漏洞报告有稳定接收渠道和 Case 跟踪 | MUST | PSIRT | PSIRT Case | 持续 | 首次响应时间 | 20 |
| SEC-EML-001 | 公司主域配置并监控 SPF、DKIM、DMARC | SHOULD | IT/Email | DNS/DMARC Report | 每月 | 域覆盖率 | 25 |
| SEC-EML-002 | 管理员和高风险邮箱启用 MFA | MUST | IAM/Email | MFA Report | 每月 | 覆盖率 | 25 |
| SEC-PRI-001 | 新高风险个人信息处理进行隐私影响评估 | SHOULD | Privacy/Data Owner | PIA/DPIA | 项目变更 | 评估覆盖率 | 26 |
| SEC-TPR-001 | 高风险供应商上线前完成安全评估与分级 | MUST | Procurement/Security | TPRM Assessment | 每供应商 | 评估覆盖率 | 27 |
| SEC-TPR-002 | 高权限第三方访问设置 Owner 和到期时间 | MUST | System Owner | Access Register | 每月 | 超期数 | 27 |
| SEC-PHY-001 | 关键机房/受控区域限制未授权物理访问 | MUST | Facilities/IT | Access Log | 持续 | 未授权事件 | 29 |
| SEC-PHY-002 | 存储介质报废前安全清除或销毁 | MUST | IT/Facilities | Disposal Record | 每次 | 合规处置率 | 29 |
| SEC-AWR-001 | 员工完成基础安全培训 | MUST | HR/Security | Training Record | 入职/年度 | 完成率 | 30 |
| SEC-AWR-002 | 开发、运维、管理员接受角色化安全培训 | SHOULD | Security/Managers | Training Record | 年度 | 覆盖率 | 30 |
| SEC-AI-001 | 高风险 Agent Tool 权限必须最小化 | MUST | AI App Owner | Tool Permission Review | 每发布 | 高权 Tool 数 | 23 |
| SEC-MOB-001 | 移动端长期 Secret 不得硬编码在 App 包 | MUST | Mobile Dev | Secret Scan | 每发布 | Finding 数 | 24 |

## 4. Control Lifecycle

~~~text
Draft → Review → Approved → Implemented → Measured
→ Tested → Exception / Improve → Periodic Review
~~~

## 5. 维护要求

现有章节中的 MUST/SHOULD 应逐步映射到本目录。新增安全要求原则上先创建 Control ID，再由 Standard、Procedure、Baseline 和 Checklist 引用。
