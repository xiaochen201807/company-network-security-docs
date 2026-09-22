---
aliases:
  - "Account Compromise Playbook"
type: "playbook"
domain: "operations"
phase:
  - "respond"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/playbook"
  - "security/domain/operations"
  - "security/priority/p1"
  - "security/phase/respond"
parent:
  - "[[docs/knowledge-map]]"
---
# Account Compromise Playbook

| Metadata | Value |
|---|---|
| Document ID | SEC-PLB-IR-001 |
| Type | Playbook |
| Owner | Security/SOC |

## Trigger

异常登录、Token 泄露、钓鱼凭据提交、MFA 异常或其他账号被控迹象。

## Immediate Actions

1. 确认账号类型与权限。
2. 禁用账号或强制密码重置。
3. 撤销 Session/Token。
4. 检查 MFA 变化。
5. 搜索异常登录和管理操作。
6. 检查新增 Token/OAuth App/API Key。
7. 检查横向使用。
8. 高权限账号立即升级 Incident。

## Email Account Extra

检查 Inbox Rule、External Forwarding、Sent Mail、OAuth Consent。

## Cloud/Admin Extra

检查 IAM、Role、Security Group、New Credential、Resource Creation。

## Recovery

重新启用前确认设备可信、凭据已轮换、恶意持久化已清理。

## Evidence

Identity Log、MFA、Session、Token、Endpoint、Email/Cloud Audit。
