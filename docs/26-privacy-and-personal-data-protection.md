---
aliases:
  - "隐私与个人信息保护"
type: "standard"
domain: "privacy"
phase:
  - "govern"
  - "protect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/privacy"
  - "security/priority/p1"
  - "security/phase/govern"
  - "security/phase/protect"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/07-data-security]]"
  - "[[docs/25-email-and-collaboration-security]]"
  - "[[docs/18-product-security-and-secure-by-default]]"
  - "[[docs/23-ai-llm-agent-security]]"
  - "[[docs/27-third-party-risk-management]]"
---
# 26 - 隐私与个人信息保护

> 本文档提供 Privacy Engineering 与个人信息治理的安全框架。实际法律义务必须由法务/隐私专业人员根据公司所在地区、客户、员工和业务场景确认。

## 1. 目标

- 知道公司处理哪些个人信息。
- 明确处理目的、Owner、存储、共享与保留。
- 在设计阶段识别隐私风险。
- 对高风险处理进行 Privacy Impact Assessment。
- 数据主体请求具备可执行流程。
- 隐私要求进入产品与系统生命周期。

## 2. Privacy by Design

在需求阶段考虑：

- 是否必须收集。
- 能否少收。
- 保存多久。
- 谁能访问。
- 是否第三方共享。
- 是否跨区域。
- 是否能删除。
- 是否用于新的目的。

## 3. Processing Inventory

建立数据处理活动清单：

| 字段 | 内容 |
|---|---|
| Processing ID | |
| Business Purpose | |
| System | |
| Data Subject | |
| Personal Data | |
| Sensitive Data | |
| Owner | |
| Source | |
| Recipient | |
| Retention | |
| Third Party | |
| Region | |

## 4. Data Minimization

只收集完成明确业务目的所需要的数据。

新字段上线前应回答：

- 为什么需要？
- 是否可以不用？
- 是否可以降精度？
- 是否可以短期保存？

## 5. Purpose Limitation

数据不应因为“技术上可以访问”就用于与原始目的明显无关的新用途。

用途变化应重新评估隐私风险。

## 6. PIA / DPIA

高风险场景 SHOULD 进行隐私影响评估：

- 大规模敏感数据。
- 新型跟踪/画像。
- AI 自动决策。
- 高风险第三方共享。
- 大规模员工监控。
- 新跨境/跨区域处理。
- 精确位置、生物识别等高敏信息。

## 7. PIA 内容

至少记录：

- Processing Purpose。
- Data Flow。
- Data Categories。
- Legal/Contract Context。
- Necessity。
- Risk。
- Security Control。
- Retention。
- Third Party。
- Residual Risk。
- Approver。

## 8. Consent / Notice

如果业务需要基于同意或隐私声明，应确保：

- 表述清晰。
- 与真实处理一致。
- 版本可追溯。
- 撤回机制可执行。

具体法律适用由法务确认。

## 9. Data Subject Request

根据适用要求建立：

- 查询。
- 更正。
- 删除。
- 导出。
- 撤回。

请求必须验证身份，避免把隐私请求本身变成数据泄露渠道。

## 10. Deletion

删除流程要覆盖：

- 主库。
- 历史库。
- 搜索索引。
- 缓存。
- 对象存储。
- 导出文件。
- 可合理处理的备份生命周期。

## 11. Retention

每类个人信息定义保留期限和理由。

禁止默认无限保存。

## 12. Access Control

敏感个人信息：

- 最小权限。
- 角色化。
- 大量访问审计。
- 管理员使用受控。

## 13. Logging

日志应避免记录完整不必要个人信息。

需要排障时优先使用：

- User ID。
- Masked Value。
- Hash。
- Trace ID。

## 14. Test Data

测试环境原则上不直接使用完整生产个人信息。

如确需：

- 审批。
- 最小数据集。
- 脱敏。
- 权限控制。
- 到期清理。

## 15. Analytics

埋点/Analytics：

- 字段清单。
- 目的。
- 第三方 SDK。
- Retention。
- 用户标识。

避免把敏感字段无意识发送到分析平台。

## 16. Third Party

第三方处理个人信息前确认：

- 目的。
- 字段。
- 安全能力。
- 子处理方。
- Incident Notification。
- Retention/Deletion。
- Contract。

## 17. Privacy in AI

AI/RAG：

- Prompt Data。
- Provider Training Use。
- Conversation Retention。
- Embedding。
- Model Output。
- Automated Decision。

需要纳入 PIA。

## 18. Employee Privacy

员工监控、EDR、日志、邮件调查等安全能力也应遵循必要性、最小化和访问控制。

## 19. Privacy Incident

疑似个人信息泄露时：

- 进入事件响应。
- 确认数据类型。
- 数量。
- 数据主体。
- 时间。
- 下载/访问情况。
- 第三方。
- 法务判断通知义务。

## 20. Metrics

- Processing Inventory 覆盖率。
- PIA 完成率。
- 超期数据集数。
- 高风险第三方数量。
- 数据主体请求响应时间。
- Privacy Incident 数量。

## 21. P0

1. Processing Inventory。
2. 数据 Owner。
3. Retention。
4. 高风险数据访问。
5. PIA 模板。
6. 第三方个人数据清单。

## 22. P1

1. Privacy Review Gate。
2. 自动 Retention。
3. Data Subject Request Workflow。
4. Privacy Dashboard。

## 23. 审计证据

- Processing Inventory。
- PIA/DPIA。
- Retention。
- Consent/Notice Version。
- Access Review。
- Data Subject Request。
- Third-party Agreement。
- Incident。

## 24. 当前待确认

- [ ] 适用地区/法律
- [ ] Privacy Owner/DPO 类职责
- [ ] 个人信息清单
- [ ] 敏感个人信息定义
- [ ] Retention
- [ ] Data Subject Request
- [ ] PIA 审批流程

## 25. 关联控制

SEC-PRI-001、SEC-DAT-*、SEC-TPR-*、SEC-AI-*。

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/07-data-security|07 数据安全]] · [[docs/25-email-and-collaboration-security|25 邮件与协作平台安全]]
- **下游知识**：无
- **横向关联**：[[docs/18-product-security-and-secure-by-default|18 Product Security 与 Secure by Default]] · [[docs/23-ai-llm-agent-security|23 AI、LLM 与 Agent 安全]] · [[docs/27-third-party-risk-management|27 第三方风险管理]]

<!-- obsidian-relations:end -->
