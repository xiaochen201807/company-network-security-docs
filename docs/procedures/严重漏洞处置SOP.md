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
| 负责人 | Security |
| Related Control | SEC-VUL-002 |

## 1. 触发条件

出现 Critical、Active Exploitation、KEV 或其他经评估需要紧急处置的漏洞。

## 2. 处置动作

1. Security 确认技术信息与影响版本。
2. Asset/CMDB/SBOM 搜索受影响资产。
3. 确认公网暴露和核心业务。
4. 建立统一发现项/Incident Channel。
5. 分配 System 负责人和 Remediation 负责人。
6. 不能立即 Patch 时先执行隔离、ACL、WAF、Disable Feature 等临时控制。
7. 在测试/灰度验证 Patch。
8. 执行生产变更。
9. 复测。
10. 对历史日志进行必要 Threat Hunt。
11. 更新看板并关闭或进入例外。

## 3. 停止 / 升级条件

如果修复造成明显生产异常，按变更回退，同时保持补偿控制并升级 System 负责人/Security。

## 4. 证据

Asset Search、发现项、Change、Patch、补偿控制、Retest、Hunt Result。
