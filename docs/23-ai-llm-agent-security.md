# 23 - AI、LLM 与 Agent 安全

> 本文档适用于公司使用或开发生成式 AI、RAG、LLM 应用、Agent、MCP/Tool Calling、AI Coding 等场景。参考 NIST SP 800-218A 的安全开发思想，并结合当前 LLM/Agent 风险进行公司化治理。

## 1. 目标

- 明确 AI 系统资产、数据、模型和 Tool。
- 防止 Prompt Injection 导致越权操作或数据泄露。
- Agent 权限遵循最小权限。
- RAG 数据源可信且访问受控。
- AI 生成代码仍经过安全 Review。
- 模型、Prompt、Plugin/Tool 具备供应链治理。

## 2. 适用范围

- Chatbot。
- RAG。
- Copilot。
- Agent。
- Tool Calling。
- MCP。
- AI Coding。
- Fine-tuning。
- Foundation Model API。
- 本地模型。

## 3. AI 资产台账

记录：

- Application。
- Model。
- Provider。
- Version。
- Data。
- Prompt。
- RAG Source。
- Tools。
- Owner。
- Environment。

## 4. 数据分类

在向第三方模型发送数据前确认：

- 是否敏感。
- 是否客户数据。
- 是否代码。
- 是否 Secret。
- 是否允许外发。
- Provider 是否保存输入。

## 5. 禁止输入

原则上禁止未经批准向公共 AI 工具输入：

- 生产 Secret。
- 私钥。
- 完整客户敏感数据。
- 未授权公司源代码。
- 生产数据库 Dump。

具体范围按公司数据政策确定。

## 6. Prompt Injection

所有来自用户、网页、文档、邮件、RAG 的文本都可能包含恶意指令。

系统不得假设：

> RAG 文档是数据，所以不可能是指令。

## 7. Indirect Prompt Injection

典型场景：

~~~text
Agent reads Web Page
   ↓
Page contains malicious instruction
   ↓
Agent treats it as trusted instruction
   ↓
Calls Tool / leaks data
~~~

需要明确 System Instruction、Data 与 Tool Policy 的边界。

## 8. Agent 最小权限

Agent Tool 权限只授予必要范围。

例如：

- Read-only 优先。
- 不默认删除文件。
- 不默认发送邮件。
- 不默认操作生产。
- 不持有全局管理员 Token。

## 9. Human-in-the-loop

高风险动作 SHOULD 要求人工确认：

- 删除。
- 转账。
- 发布。
- 生产变更。
- 发送外部消息。
- 权限变更。
- 导出敏感数据。

## 10. Tool Allowlist

每个 Agent 明确：

- 可调用 Tool。
- 可访问资源。
- 参数约束。
- 数据范围。
- 超时。
- 审计。

## 11. MCP / Connector

外部 Connector/MCP：

- 来源可信。
- 权限最小化。
- Token Scope。
- Tool 描述 Review。
- 版本/更新治理。
- 日志。
- 禁止无审查连接高权限生产系统。

## 12. Tool Injection

Agent 不应因外部内容指示就自动改变 Tool Policy。

关键约束由应用代码/Policy Enforcement 控制，而不是仅靠 Prompt 文本。

## 13. RAG

RAG 数据源：

- Owner。
- 权限。
- 数据分类。
- 更新机制。
- 内容来源。
- 删除机制。

## 14. RAG Authorization

用户只能检索其有权限看到的数据。

不能：

~~~text
User has no DB access
but RAG index contains all company documents
and model returns them
~~~

## 15. Vector Database

- 网络受控。
- 认证授权。
- Tenant Isolation。
- Sensitive Embedding 数据保护。
- 备份。
- 删除同步。

## 16. Embedding Privacy

Embedding 也可能泄露信息，不能因为不是原文就自动视为公开数据。

## 17. Output Handling

模型输出视为不可信：

- 不直接执行 Shell。
- 不直接拼 SQL。
- 不直接写 HTML。
- 不直接作为权限决策。

必须进行传统输入/输出校验。

## 18. Hallucination

高风险业务不能把模型回答当作确定事实。

需要：

- Grounding。
- Citation。
- Deterministic Validation。
- Human Review。

## 19. AI Authorization

模型不能决定最终权限。

权限由可信应用层执行。

## 20. AI Generated Code

AI 生成代码必须：

- Code Review。
- SAST。
- SCA。
- Secret Scan。
- Test。

不能因为“AI 写的”降低审核标准。

## 21. License / Provenance

AI 生成代码和模型资产根据公司法务/开源政策评估许可和来源风险。

## 22. Model Supply Chain

记录：

- Model Source。
- Hash/Version。
- License。
- Fine-tune。
- Adapter。
- Runtime。
- Dependency。

## 23. Model Download

本地模型从可信源获取，验证 Hash/Signature（能力支持时），避免未知模型文件。

## 24. Model Serialization

加载模型可能涉及不安全反序列化格式。优先使用安全格式和可信来源。

## 25. Fine-tuning Data

训练数据：

- 来源合法/授权。
- Sensitive Data Review。
- Poisoning 风险。
- Version。
- Owner。

## 26. Data Poisoning

防止不可信数据进入训练/RAG 导致行为操纵。

建立：

- Source Validation。
- Review。
- Version。
- Rollback。

## 27. Model Endpoint

- Authentication。
- Rate Limit。
- Quota。
- Cost Limit。
- Abuse Detection。
- Logging。

## 28. Resource Exhaustion

LLM 请求成本高，应限制：

- Prompt Size。
- Output Token。
- Concurrency。
- Tool Loop。
- Agent Step。

避免资源/费用 DoS。

## 29. Agent Loop

Agent 必须有：

- Max Step。
- Timeout。
- Budget。
- Cancellation。
- Loop Detection。

## 30. Secret in Prompt

System Prompt 不应保存长期 Secret，因为 Prompt 可能被泄露或调试输出。

## 31. Prompt Logging

Prompt/Response 日志可能包含敏感数据。

需要：

- 脱敏。
- 访问控制。
- 保留周期。
- Opt-out/Privacy 评估（按业务）。

## 32. Model Provider

第三方 Provider 评估：

- 数据保留。
- Training Use。
- Region。
- Security。
- Incident。
- Access Control。
- Contract。

## 33. AI Red Team

核心 AI 产品 SHOULD 测试：

- Prompt Injection。
- Jailbreak。
- Data Leakage。
- Tool Abuse。
- Authorization。
- RAG Poisoning。
- Excessive Agency。

## 34. AI Incident

事件可能包括：

- 敏感数据泄露。
- Agent 越权操作。
- Prompt Injection。
- Model Provider Incident。
- Poisoned Knowledge Base。

纳入 11 事件响应。

## 35. AI Kill Switch

高风险 Agent SHOULD 有快速：

- Disable Tool。
- Disable Model。
- Revoke Token。
- Read-only Mode。

## 36. Metrics

- AI 应用纳管率。
- 高权限 Agent 数。
- 未审批外部 AI Provider 数。
- AI Red Team 覆盖率。
- Prompt/Data 安全事件。
- Tool 权限例外数。

## 37. P0

1. AI 应用台账。
2. AI 数据使用政策。
3. Tool 最小权限。
4. 高风险动作人工确认。
5. AI 代码同等 Security Gate。
6. 第三方 Provider 评估。

## 38. P1

1. AI Threat Model。
2. Prompt Injection Test。
3. RAG Authorization。
4. AI Red Team。
5. Agent Kill Switch。
6. MCP/Connector Governance。

## 39. P2

1. AI Security Gateway。
2. Prompt/Tool Policy Engine。
3. Continuous AI Red Team。
4. Model Supply Chain Attestation。

## 40. 审计证据

- AI Inventory。
- Provider Review。
- Data Review。
- Threat Model。
- Tool Permission。
- Red Team。
- Incident。
- Exception。

## 41. 当前待确认

- [ ] 公司允许使用的 AI 工具
- [ ] 是否允许上传源代码
- [ ] AI Provider
- [ ] Agent/MCP 使用场景
- [ ] AI 数据分类
- [ ] AI Security Owner
- [ ] AI Red Team 范围

## 42. 参考

- NIST SP 800-218A
- NIST SSDF
- OWASP LLM/GenAI 安全实践
- 公司数据、IAM、应用安全规范

## 43. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立 AI、LLM、Agent 与 Tool Security 框架 |
