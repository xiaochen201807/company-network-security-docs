# Security Governance V2.0

> 本目录用于把 00～30 的安全知识与规范转换为公司可执行的 Security Program。

## 1. 四个核心治理工件

1. [Security Control Catalog](security-control-catalog.md)：统一 Control ID、Owner、Evidence、Frequency、Metric 和 Exception。
2. [Current / Target Profile](security-current-target-profile.md)：区分“当前真实做到什么”和“目标做到什么”。
3. [Security RACI](security-raci.md)：明确 Responsible、Accountable、Consulted、Informed。
4. [文档层级与维护规则](document-hierarchy-and-maintenance.md)：统一 Policy、Standard、Procedure、Playbook、Baseline、Checklist、Template。
5. [公司安全参数登记表](company-security-parameters-register.md)：统一维护散落在各章节的公司实际参数与待确认项。

## 2. 使用原则

安全体系不以“文档数量”衡量成熟度，而以控制是否真实执行、是否可验证、是否有 Owner、是否能持续运行衡量。

任何控制应尽量形成：

~~~text
Control ID
  ↓
Requirement
  ↓
Owner / Scope
  ↓
Implementation
  ↓
Evidence
  ↓
Frequency
  ↓
Metric
  ↓
Exception
  ↓
Review
~~~

## 3. V2.0 工作方式

### 第一步：控制归一化
把现有 MUST / SHOULD 映射到 Control Catalog。

### 第二步：现状评估
基于真实配置、日志、扫描、工单和演练填写 Current Profile。

### 第三步：目标设定
由业务风险、公司资源和管理层目标确定 Target Profile。

### 第四步：Gap Roadmap
Gap 必须形成 Priority、Owner、Deadline 和 Budget/Resource。

### 第五步：持续证据
逐步将人工截图升级为 API、日志、扫描器、CI/CD 和平台自动证据。

## 4. 重要原则

- 文档存在 ≠ 控制有效。
- 扫描通过 ≠ 风险为零。
- 安全部门负责体系和专业能力，不自动承担所有业务风险。
- Accountable 必须明确到业务/系统责任角色。
- 任何永久例外都应被视为控制设计失败并进入管理层复审。
