---
aliases:
  - "威胁情报、Red Team 与 Purple Team"
type: "standard"
domain: "threat-informed-defense"
phase:
  - "detect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/threat-informed-defense"
  - "security/priority/p1"
  - "security/phase/detect"
parent:
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/09-vulnerability-and-penetration-testing]]"
  - "[[docs/10-monitoring-and-security-operations]]"
  - "[[docs/11-incident-response]]"
  - "[[docs/14-security-baselines-and-checklists]]"
---
# 19 - 威胁情报、Red Team 与 Purple Team

> 本文档用于将安全运营从“有规则、有告警”进一步升级为“知道主要对手如何攻击，并能持续验证公司的检测与防御是否真的有效”。

## 1. 目标

- 识别与公司最相关的威胁。
- 用 ATT&CK/TTP 组织攻击行为。
- 通过 Red Team/Adversary Emulation 验证真实攻击链。
- 通过 Purple Team 补齐检测和响应缺口。
- 建立检测覆盖率，而不是只统计 SIEM 规则数量。

## 2. 术语

### Threat Intelligence
关于攻击者、基础设施、漏洞、TTP 和攻击活动的信息。

### Red Team
模拟攻击者目标，验证组织整体防御。

### Purple Team
攻击与防守协作验证，重点提升检测与响应。

### Adversary Emulation
按特定攻击者/TTP 模拟行为。

## 3. Intelligence Requirements

情报工作首先回答：

- 公司最担心什么攻击者？
- 哪些行业威胁最相关？
- 哪些系统最有价值？
- 哪些漏洞正在被利用？
- 哪些 TTP 需要优先检测？

避免无目的收集大量 IOC。

## 4. 情报来源

可包括：

- CISA KEV。
- 厂商公告。
- CERT。
- OSINT。
- ISAC/行业渠道。
- 商业情报。
- EDR/SIEM 内部数据。
- 漏洞情报。

## 5. IOC 与 TTP

IOC：

- IP。
- Domain。
- Hash。

TTP：

- Credential Dumping。
- PowerShell。
- Lateral Movement。
- Persistence。

TTP 通常比单一 IOC 更具长期检测价值。

## 6. MITRE ATT&CK

公司可使用 ATT&CK 作为统一语言组织：

- Initial Access。
- Execution。
- Persistence。
- Privilege Escalation。
- Defense Evasion。
- Credential Access。
- Discovery。
- Lateral Movement。
- Collection。
- Command and Control。
- Exfiltration。
- Impact。

## 7. Threat Profile

建立公司 Threat Profile：

| 字段 | 内容 |
|---|---|
| Threat Actor/Cluster | |
| Motivation | |
| Target | |
| Initial Access | |
| Key TTP | |
| Relevant Assets | |
| Detection | |
| Priority | |

## 8. Threat-informed Defense

流程：

~~~text
Threat Intelligence
   ↓
ATT&CK Mapping
   ↓
Select TTP
   ↓
Detection Requirement
   ↓
Emulation
   ↓
SOC Result
   ↓
Improve
   ↓
Retest
~~~

## 9. Red Team 范围

Red Team 可以验证：

- 身份。
- Endpoint。
- Network。
- Email。
- Cloud。
- Web。
- CI/CD。
- Social Engineering（明确授权）。
- Detection。
- Incident Response。

## 10. 授权

所有攻击模拟必须书面授权，明确：

- Scope。
- Time。
- Techniques。
- Prohibited Actions。
- Safety Boundaries。
- Emergency Stop。
- Data Handling。

遵循 09 章节授权原则。

## 11. Rules of Engagement

ROE 至少包含：

- 目标。
- 范围。
- 通讯方式。
- White Cell。
- Stop Condition。
- 是否允许钓鱼。
- 是否允许凭据操作。
- 是否允许生产。
- 数据限制。

## 12. Safety

禁止无专门批准的：

- 破坏生产数据。
- DDoS。
- 大规模锁账号。
- 不可逆动作。
- 对第三方未授权攻击。
- 超范围横向。

## 13. Red Team 目标

目标不是“拿多少漏洞”，而是验证：

- 能否进入。
- 能否提权。
- 能否横向。
- 能否访问 Crown Jewel。
- SOC 是否发现。
- IR 是否响应。

## 14. Crown Jewel

在演练前明确公司 Crown Jewel：

- IAM。
- Git/Jenkins。
- 核心数据库。
- Cloud Admin。
- 备份。
- 核心业务。

## 15. Adversary Emulation Plan

按真实 TTP 设计：

1. Initial Access。
2. Execution。
3. Persistence。
4. Privilege。
5. Lateral Movement。
6. Collection。
7. Exfiltration Simulation。

## 16. Atomic Test

在大规模 Red Team 之前可用小型原子测试验证单个 TTP：

- PowerShell。
- New Admin。
- Scheduled Task。
- Suspicious DNS。
- Credential Access。

## 17. Breach & Attack Simulation

成熟阶段 MAY 使用自动化 BAS 验证检测控制，但结果不能替代人工 Red Team。

## 18. Purple Team

Purple Team 不是独立颜色团队，而是攻防协作：

~~~text
Red executes TTP
   ↓
Blue checks telemetry
   ↓
Rule fires?
   ↓
Runbook works?
   ↓
Improve
   ↓
Retest
~~~

## 19. Detection Gap

每个测试结果记录：

- TTP。
- 是否有日志。
- 是否检测。
- 告警等级。
- SOC 是否看到。
- 响应时间。
- Gap Owner。
- Retest。

## 20. ATT&CK Coverage

不要简单用“覆盖百分比”代表安全水平。

应区分：

- Data Source Coverage。
- Detection Coverage。
- Validated Coverage。
- Response Coverage。

## 21. Detection-as-Code

检测规则 SHOULD：

- Git 管理。
- Code Review。
- 测试。
- 版本。
- Owner。
- Deployment Pipeline。
- Rollback。

## 22. Rule Test

规则发布前用历史日志或模拟事件测试：

- True Positive。
- False Positive。
- Performance。
- Missing Field。

## 23. Threat Hunting

基于假设进行 Hunt：

- 是否存在未发现 WebShell？
- 是否有未知管理员？
- 是否有异常 OAuth/App？
- 是否有 C2 Beacon？
- 是否有服务账号交互登录？

## 24. Hunt 记录

记录：

- Hypothesis。
- Data Source。
- Query。
- Result。
- Finding。
- New Detection。

## 25. Vulnerability Intelligence

新严重漏洞出现时：

- 是否影响资产。
- 是否进入 KEV。
- 是否有 Exploit。
- 是否有真实扫描。
- 历史日志是否存在利用迹象。

## 26. IOC 生命周期

IOC：

- 来源。
- Confidence。
- Expiry。
- Context。
- Scope。

避免永久保存低质量黑名单。

## 27. Threat Intel 与漏洞联动

如果组件 CVE 进入真实利用阶段，提高漏洞优先级，并触发：

- Asset Search。
- Patch。
- Compensating Control。
- Historical Hunt。

## 28. Threat Intel 与 SOC

情报转化为：

- SIEM Rule。
- EDR Query。
- WAF Rule。
- DNS Block。
- Hunt Query。
- IR Runbook。

不能停留在“转发情报邮件”。

## 29. Red Team 报告

包含：

- Objective。
- Attack Path。
- Timeline。
- TTP。
- Detection Result。
- Business Impact。
- Root Cause。
- Remediation。

## 30. Purple Team 报告

重点是：

- TTP。
- Expected Telemetry。
- Actual Telemetry。
- Rule。
- Alert。
- Analyst Response。
- Gap。
- Retest。

## 31. 复测

所有重大 Detection Gap 修复后必须重新执行相同或等价 TTP。

## 32. 频率

### 每月
- Threat Intel Review。
- 新 KEV/重大漏洞。
- Targeted Hunt。

### 每季度
- Purple Team 专项。
- ATT&CK Coverage Review。

### 每年/重大变化
- Red Team 或综合攻防演练。

具体周期按公司风险和资源确定。

## 33. 指标

- Validated TTP 数量。
- Detection Gap 数量。
- Gap 修复时间。
- Purple Team 复测通过率。
- Threat Hunt 发现数。
- ATT&CK Data Source Coverage。
- Red Team 被发现时间。

## 34. P0

1. Threat Profile。
2. KEV/重大漏洞情报流程。
3. ATT&CK Mapping。
4. 每季度 Purple Team 小型验证。
5. Detection Gap 台账。

## 35. P1

1. Threat Hunting。
2. Detection-as-Code。
3. Atomic Tests。
4. 年度 Red Team。
5. ATT&CK Coverage Dashboard。

## 36. P2

1. BAS。
2. 持续控制验证。
3. Automated Retest。
4. Threat Intel Platform。
5. Exposure + Threat + Detection 联动。

## 37. 审计证据

- Threat Profile。
- 情报记录。
- ATT&CK Mapping。
- ROE。
- Red/Purple 报告。
- Detection Gap。
- Retest。
- Hunt Report。

## 38. 当前待确认

- [ ] Threat Intel 来源
- [ ] ATT&CK 使用方式
- [ ] Red Team 负责人
- [ ] Purple Team 周期
- [ ] 是否允许社会工程
- [ ] BAS 工具
- [ ] Detection-as-Code 仓库

## 39. 参考

- MITRE ATT&CK
- CISA KEV
- 公司 09 漏洞与渗透测试
- 公司 10 日志监控与安全运营

## 40. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立威胁情报、Red Team、Purple Team 与持续检测验证框架 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/09-vulnerability-and-penetration-testing|09 漏洞管理与授权渗透测试]] · [[docs/10-monitoring-and-security-operations|10 日志监控与安全运营]]
- **下游知识**：[[docs/11-incident-response|11 安全事件与应急响应]]
- **横向关联**：[[docs/14-security-baselines-and-checklists|14 安全基线与检查清单]]

<!-- obsidian-relations:end -->
