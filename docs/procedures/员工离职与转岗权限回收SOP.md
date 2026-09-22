---
aliases:
  - "员工离职与转岗权限回收 SOP"
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
# 员工离职与转岗权限回收 SOP

| Metadata | Value |
|---|---|
| Document ID | SEC-SOP-IAM-001 |
| Type | Procedure |
| 负责人 | IAM/IT |
| Related Control | SEC-IAM-002 |

## 1. 触发条件

HR 提交离职/转岗生效信息。

## 2. 离职处理

在生效时间执行：

- 禁用统一身份账号。
- 撤销 VPN/ZTNA。
- Git/Jenkins/Cloud 管理权限回收。
- 数据库/生产权限回收。
- 撤销令牌/SSH 密钥/证书。
- 注销高风险 Session。
- 回收公司设备。
- 转移 System/Data 负责人。
- 处理个人创建的自动化和服务账号。

## 3. 转岗处理

转岗：

1. 回收旧岗位无关权限。
2. 新岗位权限重新审批。
3. 检查生产、数据、管理员、VPN 和第三方系统。

## 4. 验证

IAM/IT 输出回收清单并由系统负责人抽查高权限系统。

## 5. 证据

HR Trigger、Account Disable、Access 评审、Device Return、负责人 Transfer。
