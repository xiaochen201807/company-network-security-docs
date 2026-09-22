---
aliases:
  - "BIA 与业务连续性"
type: "standard"
domain: "business-continuity"
phase:
  - "recover"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/business-continuity"
  - "security/priority/p1"
  - "security/phase/recover"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/11-incident-response]]"
  - "[[docs/27-third-party-risk-management]]"
  - "[[docs/12-backup-dr-and-reliability]]"
  - "[[docs/29-physical-and-media-security]]"
---
# 28 - BIA 与业务连续性管理

> 本文档补充 12 章节的技术容灾视角，从业务流程出发确定最大可接受中断、关键依赖、替代方式和连续性策略。

## 1. 目标

- 知道哪些业务不能停。
- 明确停多久会产生什么影响。
- RTO/RPO 由业务影响而不是技术团队单方面决定。
- 识别人员、系统、场地、供应商等关键依赖。
- 在 IT 不完全可用时仍有业务连续性方案。
- 通过演练验证计划可执行。

## 2. BIA

Business Impact Analysis 用于评估业务中断影响。

每个关键业务流程至少记录：

- Process Owner。
- 关键产品/服务。
- 用户/客户影响。
- 财务影响。
- 合规/合同影响。
- 声誉影响。
- 数据影响。
- 关键依赖。
- MTPD。
- RTO。
- RPO。

## 3. MTPD

Maximum Tolerable Period of Disruption 表示业务可以承受的最大中断时间。

RTO 应小于 MTPD，并留出恢复和业务处理缓冲。

## 4. RTO / RPO

业务 Owner 与 IT/SRE 联合确认：

- RTO：多久恢复服务。
- RPO：最多允许丢多少数据。

避免所有系统都写成“0 数据丢失、5 分钟恢复”但没有对应成本与架构。

## 5. Dependency Mapping

关键业务依赖：

- 人员。
- 应用。
- 数据库。
- IAM。
- 网络。
- DNS。
- 云。
- 机房。
- 供应商。
- 办公场地。
- 支付/短信/邮件等外部服务。

## 6. Single Point

业务连续性不仅看技术单点，还包括：

- 唯一管理员。
- 唯一供应商。
- 唯一场地。
- 唯一证书/密钥。
- 唯一审批人。
- 唯一外部接口。

## 7. Continuity Strategy

策略可包括：

- 高可用。
- 灾备。
- 手工业务流程。
- Alternate Supplier。
- Remote Work。
- Alternate Site。
- 关键岗位备份人员。
- 数据离线导出/恢复流程。

## 8. Manual Workaround

对于可接受短时间降级的流程，提前定义：

- 手工登记。
- 延迟处理。
- 离线审批。
- 后续补录。
- 对账。

避免故障时临时设计。

## 9. Crisis Organization

重大业务中断时明确：

- Crisis Lead。
- Business Owner。
- IT/SRE。
- Security。
- Communications。
- Legal。
- Vendor Contact。

## 10. Invocation

BCP 启动条件应清晰，例如：

- 核心系统预计超过 RTO。
- 主办公场地不可用。
- 关键供应商长时间不可用。
- 大规模网络故障。
- 勒索事件影响生产。

## 11. Communications

预先准备：

- 内部通知。
- 客户沟通。
- 供应商沟通。
- 管理层更新。
- Status Page（如适用）。

未经授权人员不得对外发布未确认事件信息。

## 12. Remote Work

如果办公场地不可用，关键岗位确认：

- VPN/ZTNA。
- MFA。
- 管理终端。
- 电话/IM。
- 审批。
- 备用网络。

## 13. Supplier Continuity

Tier 1 供应商明确：

- SLA。
- DR。
- 联系人。
- 替代方案。
- 数据导出/迁移能力。

## 14. Backup 与 BCP

备份只是连续性的一部分。

必须确认：

- 恢复数据后应用能否运行。
- 人员能否登录。
- DNS/证书是否可恢复。
- 业务是否能重新开始处理。

## 15. Scenario

演练场景建议：

- 核心数据库不可用。
- 云区域故障。
- IAM 故障。
- 勒索。
- 关键供应商不可用。
- 办公场地不可用。
- DNS/证书问题。

## 16. Exercise

### Tabletop
讨论决策和流程。

### Technical Recovery
实际恢复系统。

### Integrated Exercise
业务、IT、安全、供应商共同演练。

## 17. Exercise Result

至少记录：

- 目标。
- 场景。
- 实际恢复时间。
- 数据损失。
- 决策问题。
- 联系人问题。
- 技术问题。
- 改进项。

## 18. BCP Maintenance

以下变化触发更新：

- 新核心业务。
- 架构重大变化。
- 供应商变化。
- 组织变化。
- 场地变化。
- 演练失败。
- 重大 Incident。

## 19. 指标

- 核心业务 BIA 覆盖率。
- RTO/RPO 确认率。
- BCP 演练覆盖率。
- 演练达标率。
- 过期 BCP 数。
- 关键单点数量。

## 20. P0

1. 核心业务清单。
2. BIA。
3. MTPD/RTO/RPO。
4. Dependency Map。
5. 关键联系人。
6. 恢复演练。

## 21. P1

1. 手工连续性方案。
2. Tier 1 Supplier Continuity。
3. 综合演练。
4. Crisis Communication。

## 22. 审计证据

- BIA。
- RTO/RPO。
- BCP。
- Dependency Map。
- Exercise Report。
- Improvement Action。

## 23. 当前待确认

- [ ] 核心业务流程
- [ ] BIA Owner
- [ ] MTPD
- [ ] RTO/RPO 审批人
- [ ] Crisis Lead
- [ ] 手工业务方案
- [ ] 演练周期

## 24. 关联控制

SEC-BCM-001～004、SEC-IR-*、SEC-TPR-*。

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/11-incident-response|11 安全事件与应急响应]] · [[docs/27-third-party-risk-management|27 第三方风险管理]]
- **下游知识**：[[docs/12-backup-dr-and-reliability|12 备份容灾与稳定性协同]]
- **横向关联**：[[docs/29-physical-and-media-security|29 物理、环境与介质安全]]

<!-- obsidian-relations:end -->
