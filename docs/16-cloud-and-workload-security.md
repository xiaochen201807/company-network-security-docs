---
aliases:
  - "云与 Workload 安全"
type: "standard"
domain: "cloud-security"
phase:
  - "protect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/cloud-security"
  - "security/priority/p1"
  - "security/phase/protect"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/02-assets-and-network-architecture]]"
  - "[[docs/03-network-and-perimeter-security]]"
  - "[[docs/04-identity-and-access-control]]"
  - "[[docs/05-endpoint-and-server-security]]"
  - "[[docs/08-devsecops-and-supply-chain]]"
  - "[[docs/12-backup-dr-and-reliability]]"
  - "[[docs/14-security-baselines-and-checklists]]"
  - "[[docs/15-zero-trust-and-device-trust]]"
  - "[[docs/21-cryptography-pki-kms-and-secrets]]"
  - "[[docs/22-security-engineering-platform]]"
---
# 16 - 云与 Workload 安全

> 本文档用于统一云账号、云身份、网络、Workload Identity、容器、Kubernetes、云日志、CSPM 和运行时安全要求，使云环境不成为传统安全体系之外的独立“例外区域”。

## 1. 目标

- 云账号和资源有清晰组织边界。
- 生产与开发环境隔离。
- 云管理员、服务身份、AccessKey 最小化。
- 公网暴露可持续发现。
- 云配置错误能够自动检测。
- Kubernetes、容器和工作负载具备运行期保护。
- 云审计日志可用于事件调查。

## 2. 适用范围

- IaaS。
- PaaS。
- Kubernetes。
- Serverless。
- Object Storage。
- Cloud Database。
- Load Balancer。
- Security Group。
- IAM。
- KMS。
- Cloud CI/CD。
- Multi-cloud / Hybrid Cloud。

## 3. Cloud Organization

云资源 SHOULD 纳入统一企业 Organization/Account 体系。

避免：

- 员工个人云账号承载生产。
- 一个账号混合所有环境。
- 无法统一回收的历史账号。

## 4. 账号/订阅分层

推荐：

~~~text
Organization
 ├── Security
 ├── Shared Services
 ├── Production
 ├── Staging
 ├── Development
 └── Sandbox
~~~

核心目标是降低跨环境影响。

## 5. Root / Owner 账号

云 Root/Owner：

- 不用于日常操作。
- 开启 MFA。
- 凭据安全封存。
- 使用触发告警。
- 定期验证恢复能力。

## 6. Cloud IAM

### MUST

- 管理员最小化。
- 禁止长期共享账号。
- 高权限 MFA。
- 离职及时回收。
- Service Account 有 Owner。
- 权限变化有日志。

## 7. AccessKey

长期 AccessKey 应逐步减少。

优先：

- Managed Identity。
- Instance Role。
- Workload Identity。
- Temporary Credential。

必须保留的 AccessKey：

- Owner。
- Scope。
- 有效期。
- 轮换。
- 泄露检测。

## 8. Workload Identity

云工作负载访问数据库、对象存储、消息服务时优先使用云原生身份而不是硬编码 AccessKey。

## 9. Cloud Network

- 生产 VPC/VNet 与开发隔离。
- Security Group 最小权限。
- 管理端口不公网暴露。
- 数据库不公网暴露。
- 跨 VPC/VNet 连接有 Owner。
- Egress 按需控制。

## 10. Public Exposure

持续发现：

- Public IP。
- Public Load Balancer。
- Public Bucket。
- Public Database。
- Public Kubernetes API。
- Public Admin Console。

任何新增公网暴露必须有 Owner。

## 11. Security Group

重点检测：

- 0.0.0.0/0 到 SSH/RDP。
- 0.0.0.0/0 到 DB。
- 过宽网段。
- 无 Owner 规则。
- 长期临时规则。

## 12. Object Storage

- 默认私有。
- Public Access 必须业务审批。
- 临时 URL 限时。
- Access Log。
- 版本控制/不可变策略按风险启用。
- 敏感 Bucket 加密。

## 13. Cloud Database

- 不公网暴露。
- 网络白名单。
- IAM/数据库身份最小权限。
- 加密。
- 备份。
- 审计。
- 高可用。

## 14. KMS

云 KMS 要求：

- Key Owner。
- Key Policy 最小化。
- Rotation。
- Audit Log。
- 禁止普通开发拥有全局 Key Admin。
- 关键 Key 删除有保护期/审批。

## 15. Cloud Logging

优先接入：

- Control Plane Audit。
- IAM。
- Security Group。
- Object Storage。
- KMS。
- Kubernetes Audit。
- Cloud WAF。
- LB。
- Database Audit。

## 16. CSPM

SHOULD 建立 Cloud Security Posture Management：

- 公网暴露。
- IAM 过权。
- 未加密资源。
- 日志未开启。
- Security Group。
- Root 风险。
- Bucket Public。
- 过期 Key。

## 17. IaC

Terraform、CloudFormation、Bicep 等：

- Git 管理。
- Code Review。
- IaC Scan。
- 禁止硬编码 Secret。
- 生产变更有 Plan/Review。
- 状态文件保护。

## 18. Terraform State

State 可能包含敏感信息。

必须：

- 远程受控存储。
- 权限最小化。
- 加密。
- 不提交公共 Git。
- 访问审计。

## 19. Kubernetes Control Plane

- API Server 不无保护公网开放。
- RBAC。
- Audit Log。
- Cluster Admin 最小化。
- 控制面版本受支持。

## 20. Namespace

按业务、环境、团队合理隔离，避免所有工作负载放在默认 Namespace。

## 21. Kubernetes RBAC

重点检查：

- cluster-admin。
- wildcard。
- Secret 读取。
- Pod Exec。
- Impersonate。
- RoleBinding 到高权限角色。

## 22. ServiceAccount

- 不共用万能 ServiceAccount。
- 权限最小化。
- 不需要 API Token 的 Pod 禁止自动挂载。
- 与 Workload Identity 对接。

## 23. Pod Security

重点：

- privileged。
- root。
- hostNetwork。
- hostPID。
- hostPath。
- Capability。
- writable root filesystem。
- seccomp。

## 24. NetworkPolicy

核心 Namespace SHOULD 限制东西向访问，只允许必要流量。

## 25. Ingress

- TLS。
- 管理接口限制。
- WAF/API Gateway（适用时）。
- Host/Route 变化审计。
- 不暴露内部服务。

## 26. Image Security

- Approved Registry。
- Image Scan。
- 固定版本/摘要。
- 禁止来源不明镜像。
- Secret 不进入镜像层。
- 基础镜像周期升级。

## 27. Admission Policy

成熟阶段可通过 OPA/Gatekeeper/Kyverno 等类型能力进行策略控制：

- 禁 privileged。
- 禁 latest（按公司策略）。
- 强制资源限制。
- 限制 Registry。
- 强制 SecurityContext。

## 28. Runtime Security

重点检测：

- 容器逃逸。
- 异常 Shell。
- 新进程。
- 写入系统路径。
- 异常网络。
- Crypto Miner。
- 反向 Shell。
- Kubernetes API 异常。

## 29. CNAPP

成熟阶段可整合：

- CSPM。
- CWPP。
- CIEM。
- Container Security。
- IaC Security。
- Runtime Detection。

## 30. CIEM

云权限规模较大时 SHOULD 分析：

- 未使用权限。
- 超权角色。
- 长期 Key。
- 跨账号 Trust。
- 服务账号权限。

## 31. Serverless

- Function Identity 最小权限。
- Secret 不写代码。
- Trigger 来源受控。
- 网络出口受控。
- 日志。
- 依赖 SCA。

## 32. Multi-cloud

多云环境重点避免：

- 每个云独立账号体系。
- 不同云日志不可统一调查。
- 同一人员多套永久管理员。
- Secret 重复散落。

统一资产、身份、日志和策略视图。

## 33. Cloud Incident Response

至少准备：

- 账号禁用。
- AccessKey 吊销。
- Snapshot。
- Security Group 隔离。
- Instance 隔离。
- Cloud Audit 查询。
- KMS/Secret 轮换。

## 34. Cloud Forensics

重要云日志应有足够保留时间。调查时关注：

- 控制面 API。
- IAM。
- 新凭据。
- 新实例。
- 网络规则。
- Bucket Access。
- KMS。
- CI/CD。

## 35. Backup

云备份不应只在同一权限域。

核心业务考虑：

- 跨账号。
- 跨区域。
- Immutable。
- 恢复演练。

## 36. Cost Abuse

云安全也需检测：

- Crypto Mining。
- 大量实例创建。
- 异常带宽。
- API 滥用。
- 资源耗尽。

## 37. 指标

- 云资产纳管率。
- Public Resource 数量。
- 云管理员数量。
- MFA 覆盖率。
- 长期 AccessKey 数量。
- CSPM Critical 数量。
- Kubernetes 高权限账号数。
- 镜像扫描覆盖率。

## 38. P0

1. 云账号统一纳管。
2. Root MFA。
3. 生产/开发隔离。
4. 公网资产清单。
5. Cloud Audit Log。
6. Security Group 高危规则治理。
7. AccessKey 台账。

## 39. P1

1. CSPM。
2. Workload Identity。
3. IaC Scan。
4. Kubernetes RBAC/Policy。
5. Image Scan。
6. 跨账号备份。

## 40. P2

1. CNAPP。
2. CIEM。
3. Runtime Protection。
4. Policy-as-Code。
5. Multi-cloud 统一身份与策略。

## 41. 审计证据

- 云账号清单。
- IAM 导出。
- Root/MFA。
- Security Group。
- CSPM 报告。
- Cloud Audit。
- Kubernetes RBAC。
- IaC Pipeline。
- 镜像扫描。
- 备份恢复。

## 42. 当前待确认

- [ ] 云厂商
- [ ] 账号/订阅结构
- [ ] 云 IAM
- [ ] CSPM/CNAPP
- [ ] Kubernetes 规模
- [ ] Registry
- [ ] KMS
- [ ] IaC 技术栈
- [ ] Cloud IR 责任人

## 43. 参考

- NIST CSF 2.0
- NIST SP 800-207A
- 云厂商 Well-Architected Security 实践

## 44. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立云与 Workload 安全框架 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/02-assets-and-network-architecture|02 资产与网络架构]] · [[docs/03-network-and-perimeter-security|03 网络与边界安全]] · [[docs/04-identity-and-access-control|04 身份与访问控制]] · [[docs/05-endpoint-and-server-security|05 终端与服务器安全]]
- **下游知识**：无
- **横向关联**：[[docs/08-devsecops-and-supply-chain|08 DevSecOps 与供应链安全]] · [[docs/12-backup-dr-and-reliability|12 备份容灾与稳定性协同]] · [[docs/14-security-baselines-and-checklists|14 安全基线与检查清单]] · [[docs/15-zero-trust-and-device-trust|15 Zero Trust 与设备可信]] · [[docs/21-cryptography-pki-kms-and-secrets|21 密码学、PKI、KMS 与 Secret 治理]] · [[docs/22-security-engineering-platform|22 Security Engineering Platform]]

<!-- obsidian-relations:end -->
