---
aliases:
  - "公司安全参数登记表"
type: "register"
domain: "governance"
phase:
  - "govern"
priority: "P0"
status: "active"
tags:
  - "security"
  - "security/type/register"
  - "security/domain/governance"
  - "security/priority/p0"
  - "security/phase/govern"
parent:
  - "[[docs/governance/README]]"
related:
  - "[[docs/governance/security-current-target-profile]]"
  - "[[docs/00-security-overview]]"
---
# 公司安全参数登记表

> 用于收敛各章节“当前待确认”项。此表填写公司真实参数后，各 Domain Standard 只引用这里，不再到处复制相同 TODO。

## 1. Governance

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Security Leader/Organization | 待确认 | Management | Org Chart | Open |
| Risk Acceptance Authority | 待确认 | Management | Policy | Open |
| Exception Approval Matrix | 待确认 | Security/Management | Workflow | Open |
| Security Meeting Cadence | 待确认 | Security | Calendar | Open |
| Applicable Laws/Contracts | 待确认 | Legal/Compliance | Register | Open |

## 2. Asset / Network

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| CMDB/Asset Platform | 待确认 | IT | System | Open |
| Core Asset Definition | 待确认 | Business/Security | List | Open |
| Network Zones | 待确认 | Network | Topology | Open |
| Public Asset Owner | 待确认 | IT/Security | ASM | Open |
| Firewall/VPN/WAF Platform | 待确认 | Network | Config | Open |
| Bastion/PAM | 待确认 | IT/Ops | Config | Open |

## 3. IAM / Endpoint

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| IAM/SSO Platform | 待确认 | IT/IAM | Config | Open |
| MFA Scope | 待确认 | IAM | Report | Open |
| Password Policy | 待确认 | IAM | Policy | Open |
| EDR Platform | 待确认 | Endpoint | Inventory | Open |
| Patch Platform | 待确认 | IT/Ops | Report | Open |
| MDM/UEM | 待确认 | IT | Config | Open |
| BYOD Policy | 待确认 | IT/Security | Policy | Open |

## 4. Development / DevSecOps

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Git Platform/Version | 待确认 | DevOps | Config | Open |
| Jenkins Version | 待确认 | DevOps | Config | Open |
| Jenkins Plugin Baseline | 待确认 | DevOps | Inventory | Open |
| SonarQube Version/Gate | 待确认 | Dev/Security | Config | Open |
| SCA Tool | 待确认 | Security/DevOps | Config | Open |
| Secret Scan Tool | 待确认 | Security/DevOps | Config | Open |
| Maven/Nexus/Artifactory | 待确认 | DevOps | Config | Open |
| Container Registry | 待确认 | DevOps | Config | Open |
| Security Gate | 待确认 | Security/DevOps | Pipeline | Open |
| SLSA Target | 待确认 | Security Platform | Roadmap | Open |

## 5. Vulnerability / SOC / IR

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Risk Rating Standard | 待确认 | Security | Standard | Open |
| Critical/High SLA | 待确认 | Management/Security | Policy | Open |
| Vulnerability Platform | 待确认 | Security | System | Open |
| SIEM/Log Platform | 待确认 | SOC | System | Open |
| Log Retention | 待确认 | SOC/Legal | Policy | Open |
| P1/P2 Alert SLA | 待确认 | SOC | Runbook | Open |
| 24x7 On-call | 待确认 | Security/SRE | Roster | Open |
| Incident Commander List | 待确认 | Security | Register | Open |
| Evidence Storage | 待确认 | Security | Repository | Open |

## 6. Data / Privacy / Crypto

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Data Classification | 待确认 | Data/Security | Standard | Open |
| Data Owner Mechanism | 待确认 | Business/Data | Register | Open |
| Retention Standard | 待确认 | Data/Legal | Policy | Open |
| Privacy Owner | 待确认 | Legal/Privacy | Org | Open |
| PIA Workflow | 待确认 | Privacy | Workflow | Open |
| Secret Manager | 待确认 | Security Platform | Config | Open |
| KMS/HSM | 待确认 | Security Platform | Config | Open |
| TLS/Crypto Standard | 待确认 | Security | Standard | Open |
| Certificate Platform | 待确认 | Ops/Security | Inventory | Open |

## 7. Reliability / BCP

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Core System SLO | 待确认 | System Owner/SRE | SLO | Open |
| RTO/RPO | 待确认 | Business/System Owner | BIA | Open |
| Backup Platform | 待确认 | Ops | Config | Open |
| Immutable Backup | 待确认 | Ops | Config | Open |
| BIA Owner | 待确认 | Business Continuity | Register | Open |
| BCP Exercise Cycle | 待确认 | Management/Ops | Calendar | Open |

## 8. Email / Third Party / Physical

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Email Platform | 待确认 | IT | Config | Open |
| SPF/DKIM/DMARC Status | 待确认 | IT | DNS/Report | Open |
| Phishing Simulation | 待确认 | Security/HR | Program | Open |
| Supplier Register | 待确认 | Procurement | Register | Open |
| TPRM Tiering | 待确认 | Procurement/Security | Standard | Open |
| Contract Security Clause | 待确认 | Legal | Template | Open |
| Physical Site Model | 待确认 | Facilities | Site List | Open |
| Media Disposal Process | 待确认 | IT/Facilities | Procedure | Open |

## 9. AI / Mobile

| Parameter | Current Value | Owner | Evidence | Status |
|---|---|---|---|---|
| Approved AI Tools | 待确认 | Security/IT | Policy | Open |
| AI Provider | 待确认 | AI Owner | Register | Open |
| Source Code to AI Policy | 待确认 | Security/Legal | Policy | Open |
| Agent/MCP Use Cases | 待确认 | AI Owner | Inventory | Open |
| Android/iOS Apps | 待确认 | Mobile Owner | Inventory | Open |
| App Signing Key Management | 待确认 | Mobile/DevOps | Procedure | Open |

## 10. 使用规则

1. 优先完成 P0 相关参数。
2. Current Value 必须有 Evidence。
3. 参数确认后同步 Current Profile。
4. 发生平台/组织变化时更新。
5. 至少季度复审一次 Open 项。
