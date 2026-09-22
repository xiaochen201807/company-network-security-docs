---
aliases:
  - "Security RACI"
type: "matrix"
domain: "governance"
phase:
  - "govern"
priority: "P0"
status: "active"
tags:
  - "security"
  - "security/type/matrix"
  - "security/domain/governance"
  - "security/priority/p0"
  - "security/phase/govern"
parent:
  - "[[docs/governance/README]]"
related:
  - "[[docs/governance/security-control-catalog]]"
  - "[[docs/01-governance-and-policy]]"
---
# Security RACI

> R = Responsible；A = Accountable；C = Consulted；I = Informed。

## 1. 角色

Management、Security、IT/IAM、Development、DevOps/SRE、System Owner、Data Owner、HR、Procurement/Legal、Audit、Facilities。

## 2. Governance

| 活动 | Management | Security | IT/IAM | Dev | DevOps | System Owner | Data Owner | HR | Procurement/Legal | Audit |
|---|---|---|---|---|---|---|---|---|---|---|
| 安全体系规划 | I | R/A | C | C | C | C | C | I | C | C |
| 重大风险接受 | A | C | C | C | C | R | C | I | C | I |
| Control Catalog | I | R/A | C | C | C | C | C | I | C | C |
| 安全例外审核 | I/A* | R | C | C | C | R | C | I | C | I |
| 独立审计 | I | C | C | C | C | I | I | I | I | R/A |

高风险例外由公司权限矩阵确定最终 A。

## 3. Asset / IAM / Network

| 活动 | Security | IT/IAM | DevOps/SRE | System Owner | HR |
|---|---|---|---|---|---|
| 资产发现/CMDB | C | R | R | A | I |
| 公网暴露审批 | C | C | R | A | I |
| 员工账号生命周期 | C | R | I | I | R/C |
| 生产权限审批 | C | R | R | A | I |
| MFA/Conditional Access | C | R/A | C | I | I |
| 防火墙/VPN | C | R | R | A | I |

## 4. Application / DevSecOps

| 活动 | Security | Development | DevOps/SRE | System Owner |
|---|---|---|---|---|
| 安全编码 | C | R | I | A |
| Threat Model | C/R | R | C | A |
| SAST/SCA/Secret | C | R | R | A |
| Security Gate | R/C | C | R | A |
| 漏洞修复 | C | R | R | A |
| 漏洞复测 | R | C | C | A |
| 可信构建 | C | C | R | A |
| 生产发布 | I | C | R | A |

## 5. Data / Privacy

| 活动 | Security | Data Owner | Development | DBA/Ops | Legal/Privacy | System Owner |
|---|---|---|---|---|---|---|
| 数据分类 | C | R/A | C | C | C | C |
| 数据访问授权 | C | R/A | I | R | C | C |
| 大量数据导出 | C | R/A | C | R | I | C |
| PIA/DPIA | C | R | C | C | R/A | C |
| 数据保留/删除 | C | R | C | R | C/A | C |
| 数据泄露响应 | R | C | C | R | C/A | A |

## 6. Vulnerability / SOC / Incident

| 活动 | Security | Development | DevOps/SRE | System Owner | Management |
|---|---|---|---|---|---|
| 漏洞发现/验证 | R | C | C | I | I |
| 风险定级 | R | C | C | A/C | I |
| 修复执行 | C | R | R | A | I |
| 超期风险升级 | R | C | C | A | I |
| SIEM/EDR 运营 | R/A | I | C | I | I |
| SEV1 Incident Commander | R | C | R | A | I |
| 业务中断决策 | C | C | R | A | I |
| 重大风险决策 | R/C | I | C | R | A |

## 7. Third Party

| 活动 | Security | Procurement | Legal | System Owner | Data Owner | IT |
|---|---|---|---|---|---|---|
| 风险分级 | R | R | C | A/C | C | C |
| 安全评估 | R | C | C | A | C | C |
| 合同安全条款 | C | R | R/A | C | C | I |
| 第三方账号 | C | I | I | A | I | R |
| 年度复审 | R | R | C | A | C | C |
| Offboarding | C | R | C | A | C | R |

## 8. BCP / Physical / Awareness

| 活动 | Security | IT/SRE | System Owner | Management | HR | Facilities |
|---|---|---|---|---|---|---|
| BIA | C | C | R | A | I | I |
| BCP | C | R | R | A | I | C |
| DR | C | R | A | I | I | C |
| 机房物理访问 | C | R/C | I | I | I | R/A |
| 介质销毁 | C | R | I | I | I | R/A |
| 全员安全培训 | R | C | I | I | R/A | I |
| 角色化培训 | R | C | R/C | A | C | I |

## 9. 原则

1. 一个重要活动尽量只有一个最终 A。
2. Security 不应成为所有事项的 A。
3. System Owner 对业务系统剩余风险承担 Accountable。
4. 角色或组织变化时更新 RACI。
5. RACI 至少年度复审。
