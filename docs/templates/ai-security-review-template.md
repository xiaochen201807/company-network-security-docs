---
aliases:
  - "AI / LLM / Agent 安全评审模板"
type: "template"
domain: "template"
phase:
  - "govern"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/template"
  - "security/domain/template"
  - "security/priority/p1"
  - "security/phase/govern"
parent:
  - "[[docs/knowledge-map]]"
---
# AI / LLM / Agent 安全评审模板

## 1. 基本信息

| 字段 | 内容 |
|---|---|
| AI 应用 | |
| Owner | |
| Model/Provider | |
| 环境 | |
| 是否 Agent | 是 / 否 |
| 是否 RAG | 是 / 否 |
| 是否 Tool/MCP | 是 / 否 |

## 2. 数据

- 输入数据分类：
- 是否包含客户数据：
- 是否包含代码：
- 是否发送第三方：
- Provider 是否保存/训练：

## 3. RAG

- [ ] 数据源有 Owner
- [ ] 用户权限贯穿检索
- [ ] 租户隔离
- [ ] 数据删除同步
- [ ] Poisoning 风险评估

## 4. Agent / Tool

| Tool | Permission | Data | High Risk | Human Approval |
|---|---|---|---|---|
| | | | | |

- [ ] Max Step
- [ ] Timeout
- [ ] Budget
- [ ] Kill Switch
- [ ] Audit Log

## 5. Prompt Injection

- [ ] Direct Injection Test
- [ ] Indirect Injection Test
- [ ] Tool Abuse Test
- [ ] Data Leakage Test
- [ ] Authorization Test

## 6. Output

- [ ] 输出不直接执行 Shell/SQL
- [ ] 传统输入校验仍存在
- [ ] 高风险事实有人/规则验证

## 7. 结论

- [ ] 通过
- [ ] 有条件通过
- [ ] 阻断

风险与整改：
