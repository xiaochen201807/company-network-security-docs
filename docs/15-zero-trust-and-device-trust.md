---
aliases:
  - "Zero Trust 与设备可信"
type: "standard"
domain: "zero-trust"
phase:
  - "protect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/zero-trust"
  - "security/priority/p1"
  - "security/phase/protect"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/02-assets-and-network-architecture]]"
  - "[[docs/04-identity-and-access-control]]"
  - "[[docs/05-endpoint-and-server-security]]"
  - "[[docs/03-network-and-perimeter-security]]"
  - "[[docs/16-cloud-and-workload-security]]"
  - "[[docs/21-cryptography-pki-kms-and-secrets]]"
---
# 15 - Zero Trust 与设备可信

> 本文档用于将公司访问控制从“连入公司网络即获得较高信任”逐步演进为基于身份、设备、资源和风险上下文的动态访问控制。参考 NIST SP 800-207 与云原生零信任实践，核心原则是不因用户、设备或服务位于内网而自动授予信任。

## 1. 目标

- 访问决策同时考虑用户身份、设备身份、设备健康、资源敏感度和风险上下文。
- VPN 只作为连接方式之一，不再等同于访问授权。
- 关键资源逐步采用按应用、按资源、按身份的细粒度访问。
- 员工、外包、服务账号和 Workload Identity 统一纳入身份治理。
- 不可信或不合规设备无法直接访问高价值资源。

## 2. 核心原则

### 2.1 Never Trust, Always Verify

每次访问都应基于当前上下文验证，而不是依赖“之前登录过”或“已经在内网”。

### 2.2 Assume Breach

设计访问策略时假设某个账号、终端或服务可能已经被攻破，并限制其横向影响。

### 2.3 Least Privilege

权限按资源、时间和业务需要最小化。

### 2.4 Protect Resources, Not Network Segments

最终保护对象是应用、数据、服务和工作负载，而不是只依赖网段。

## 3. Zero Trust 访问模型

~~~text
User Identity
   +
Device Identity
   +
Device Compliance
   +
MFA
   +
Risk Context
   +
Resource Sensitivity
   ↓
Policy Decision
   ↓
Allow / Deny / Step-up / Read-only / JIT
~~~

## 4. 用户身份

关键访问应使用公司受控身份。

要求：

- 实名账号。
- 离职即时回收。
- 高风险访问 MFA。
- 外包账号明确有效期。
- 高权限与普通账号分离。

## 5. 设备身份

公司应逐步为受管设备建立稳定设备身份，例如：

- MDM/UEM Device ID。
- 设备证书。
- EDR Agent Identity。
- TPM/安全硬件能力。
- 云设备注册身份。

避免只用 IP 地址判断“这是公司电脑”。

## 6. 设备合规

访问高价值资源时可检查：

- OS 是否受支持。
- 安全补丁是否严重超期。
- EDR 是否在线。
- 磁盘是否加密。
- 屏幕锁定是否启用。
- 是否存在高风险恶意软件。
- 是否 Root/Jailbreak（移动设备）。
- 是否被 MDM 纳管。

## 7. 条件访问

根据上下文做动态访问决策：

- 用户角色。
- 设备合规状态。
- 网络来源。
- 登录风险。
- 资源敏感度。
- 时间。
- 异常行为。
- MFA 状态。

## 8. Step-up Authentication

对于高风险操作可要求二次认证，例如：

- 修改管理员权限。
- 下载大量敏感数据。
- 访问生产系统。
- 创建长期 Token。
- 修改支付/财务配置。

## 9. VPN 的重新定位

VPN 提供加密隧道，不应自动授予整个内网访问。

目标模型：

~~~text
VPN / ZTNA
   ↓
Identity
   ↓
Device Posture
   ↓
Resource Policy
   ↓
Specific Application
~~~

## 10. ZTNA

成熟阶段可逐步采用 Zero Trust Network Access：

- 按应用授权。
- 隐藏内网网络结构。
- 不向终端开放整个网段。
- 按身份和设备实时判断。
- 访问日志集中。

## 11. BYOD

个人设备访问公司资源需明确：

- 允许访问哪些资源。
- 是否强制 MDM。
- 是否允许下载敏感数据。
- 是否允许访问生产。
- 数据隔离方式。
- 设备丢失后的远程处置能力。

高敏资源原则上不通过未受管 BYOD 访问。

## 12. 外包设备

外包/第三方设备应比正式员工设备更严格：

- 项目有效期。
- 指定设备。
- 受控访问范围。
- 禁止访问无关系统。
- 项目结束后自动回收。

## 13. 管理终端

生产运维和高权限管理 SHOULD 使用受控管理终端：

- 专用或高安全配置。
- EDR。
- 磁盘加密。
- 禁止无关软件。
- 强 MFA。
- 访问路径受控。

## 14. Device Trust 与 EDR

设备可信不应只依赖 MDM。

可结合：

- EDR 风险状态。
- 最近恶意行为。
- Agent 是否被关闭。
- 设备是否被隔离。
- 主机漏洞状态。

## 15. Workload Identity

服务之间访问不应长期依赖共享密码。

优先考虑：

- Service Account。
- Cloud Managed Identity。
- Kubernetes ServiceAccount。
- SPIFFE/SPIRE 类身份。
- 短生命周期证书/Token。

## 16. Service-to-Service Zero Trust

微服务访问应逐步实现：

- 服务身份认证。
- 服务级授权。
- mTLS（适用时）。
- 最小 API 权限。
- Workload Identity。
- 服务访问日志。

## 17. 短生命周期凭据

长期静态凭据风险较高。

成熟目标：

- 短期 Token。
- 临时证书。
- JIT 权限。
- 自动轮换。
- 自动吊销。

## 18. PAM / JIT

高权限生产访问：

- 先申请。
- 限时开通。
- 最小范围。
- 操作审计。
- 到期自动回收。

## 19. Policy Engine

成熟阶段可建立统一策略决策：

- Identity Provider。
- Device Context。
- Resource Metadata。
- Risk Signal。
- Policy Decision Point。
- Policy Enforcement Point。

## 20. 资源标签

资源应带风险标签：

- Public。
- Internal。
- Sensitive。
- Critical。
- Production。
- Admin。

条件访问根据资源标签执行不同策略。

## 21. 网络微隔离

Zero Trust 不等于取消网络隔离。

仍应使用：

- 防火墙。
- NetworkPolicy。
- Security Group。
- Host Firewall。
- Service Mesh。

网络隔离作为纵深防御。

## 22. 应用代理/IAP

内部 Web 管理系统可逐步通过身份感知代理访问：

~~~text
User
 ↓
Identity-Aware Proxy
 ↓
MFA + Device Trust
 ↓
Internal Application
~~~

减少传统“整个内网 VPN”暴露面。

## 23. Break-glass

紧急账号应独立于常规访问策略，但：

- 严格保存。
- 使用即告警。
- 使用后 Review。
- 凭据轮换。
- 定期验证可用。

## 24. 登录风险

可纳入：

- 新设备。
- 异常 IP。
- 异常时间。
- 高风险国家/地区（结合实际业务）。
- Impossible Travel 信号。
- EDR 风险。
- 密码泄露信号。

风险信号只能作为决策输入，不能单一因素决定全部访问。

## 25. 会话风险

访问授权后仍需持续评估：

- 设备突然不合规。
- Token 被吊销。
- 用户被禁用。
- 权限变化。
- 高风险行为。

必要时终止现有 Session。

## 26. 日志

至少记录：

- 用户。
- 设备。
- 资源。
- 访问策略。
- Allow/Deny。
- MFA。
- Risk Signal。
- JIT 授权。
- Session 终止。

## 27. 检测场景

- 未受管设备访问关键系统。
- 设备 EDR 离线仍访问生产。
- 离职用户 Token 继续使用。
- 新设备直接申请高权限。
- 同账号多个异常设备。
- JIT 权限超期未回收。

## 28. 指标

- MFA 覆盖率。
- 设备纳管率。
- 设备合规率。
- 高风险资源 ZTNA 覆盖率。
- 生产 JIT 权限占比。
- 长期管理员权限数量。
- Workload Identity 覆盖率。

## 29. P0

1. VPN 一人一号。
2. 管理员 MFA。
3. MDM/EDR 资产打通。
4. 生产访问设备要求。
5. 外包账号/设备有效期。
6. 管理终端策略。

## 30. P1

1. Conditional Access。
2. ZTNA/IAP。
3. PAM/JIT。
4. 设备证书。
5. Workload Identity。
6. 微服务 mTLS/身份授权。

## 31. P2

1. 统一 Policy Engine。
2. Continuous Access Evaluation。
3. Risk-based Access。
4. 全面短生命周期凭据。
5. 大规模微隔离。

## 32. 审计证据

- 设备清单。
- MDM/EDR 合规。
- MFA 配置。
- ZTNA 策略。
- JIT 工单。
- 访问日志。
- 外包设备清单。
- Workload Identity 配置。

## 33. 当前待确认

- [ ] MDM/UEM 平台
- [ ] EDR 平台
- [ ] VPN/ZTNA 平台
- [ ] IAM/SSO
- [ ] 生产管理终端范围
- [ ] BYOD 政策
- [ ] 外包设备要求
- [ ] Workload Identity 路线

## 34. 参考

- NIST SP 800-207 Zero Trust Architecture
- NIST SP 800-207A Cloud-Native Zero Trust
- Microsoft Zero Trust / SDL 实践

## 35. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立 Zero Trust 与设备可信框架 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/02-assets-and-network-architecture|02 资产与网络架构]] · [[docs/04-identity-and-access-control|04 身份与访问控制]] · [[docs/05-endpoint-and-server-security|05 终端与服务器安全]]
- **下游知识**：无
- **横向关联**：[[docs/03-network-and-perimeter-security|03 网络与边界安全]] · [[docs/16-cloud-and-workload-security|16 云与 Workload 安全]] · [[docs/21-cryptography-pki-kms-and-secrets|21 密码学、PKI、KMS 与 Secret 治理]]

<!-- obsidian-relations:end -->
