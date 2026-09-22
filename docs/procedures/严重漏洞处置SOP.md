---
aliases:
  - "严重漏洞处置 SOP"
type: "procedure"
domain: "operations"
phase:
  - "respond"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/procedure"
  - "security/domain/operations"
  - "security/priority/p1"
  - "security/phase/respond"
parent:
  - "[[docs/公司安全知识图谱]]"
---
# 严重漏洞处置 SOP

| Metadata | Value |
|---|---|
| Document ID | SEC-SOP-VUL-001 |
| Type | Procedure |
| Owner | Security |
| Related Control | SEC-VUL-002 |

## 1. Trigger

出现 Critical、Active Exploitation、KEV 或其他经评估需要紧急处置的漏洞。

## 2. Actions

1. Security 确认技术信息与影响版本。
2. Asset/CMDB/SBOM 搜索受影响资产。
3. 确认公网暴露和核心业务。
4. 建立统一 Finding/Incident Channel。
5. 分配 System Owner 和 Remediation Owner。
6. 不能立即 Patch 时先执行隔离、ACL、WAF、Disable Feature 等临时控制。
7. 在测试/灰度验证 Patch。
8. 执行生产变更。
9. 复测。
10. 对历史日志进行必要 Threat Hunt。
11. 更新 Dashboard 并关闭或进入例外。

## 3. Stop / Escalation

如果修复造成明显生产异常，按变更回退，同时保持补偿控制并升级 System Owner/Security。

## 4. Evidence

Asset Search、Finding、Change、Patch、Compensating Control、Retest、Hunt Result。
