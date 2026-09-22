# 文档层级与维护规则

> 解决当前文档全部平铺、Standard/SOP/模板混在一起的问题。

## 1. 文档层级

~~~text
Policy
  ↓
Standard
  ↓
Procedure / SOP
  ↓
Playbook
  ↓
Baseline
  ↓
Checklist
  ↓
Template / Evidence
~~~

## 2. Policy

回答公司为什么要求、管理原则、适用范围和责任。应稳定，不写过多产品参数。

## 3. Standard

回答必须满足什么技术/流程要求、Control ID、如何验证。当前 00～30 主文档多数属于 Standard / Domain Guide。

## 4. Procedure / SOP

回答谁在什么时候按什么步骤做。例如 Critical Vulnerability SOP、离职权限回收 SOP、Certificate Rotation SOP。

## 5. Playbook

面向特定事件，例如 Ransomware、Secret Leak、Account Compromise。重点是快速动作，不重复完整政策。

## 6. Baseline

面向具体技术对象的最低配置，例如 Linux、Windows、Nginx、Jenkins、Kubernetes。14 章节作为 Baseline 总入口。

## 7. Checklist / Template

Checklist 用于发布、月度检查和评审；Template 用于统一证据格式，不定义新的控制要求。

## 8. 目录规划

~~~text
docs/
  00-30 domain standards
  governance/
  procedures/
  playbooks/
  baselines/
  templates/
  references/
~~~

## 9. 文档元数据

正式文档 SHOULD 逐步增加 Document ID、Type、Owner、Approver、Version、Effective Date、Review Cycle、Related Controls。

## 10. 去重原则

1. Control Catalog 保留唯一正式 Requirement。
2. Domain Standard 解释实现方式。
3. Procedure 只描述执行步骤。
4. Checklist 引用 Control ID。
5. Template 不重复解释政策。

## 11. 08 / 09 拆分目标

### 08 DevSecOps
拆为 Git & Source、Jenkins & Builder、Dependency/SCA、SAST/Secret/SBOM、Container/IaC/Artifact、Security Gate & Exception、Trusted Build/SLSA。

### 09 Vulnerability
拆为 Vulnerability Management、Risk Rating & SLA、Remediation & Exception、Penetration Testing、Reporting & Metrics、Operations Checklist。

主 08 / 09 文件保留索引入口，避免链接失效。

## 12. Review Cycle

- Policy：年度。
- Standard：年度或重大技术变化。
- SOP/Playbook：半年或演练后。
- Baseline：季度或版本变化。
- Checklist/Template：按使用反馈。

## 13. Archive

废弃文档标记 Retired、记录替代文档并保留审计历史，避免搜索结果误用过期规范。

## 14. 文档质量检查

- [ ] 有 Owner
- [ ] 有适用范围
- [ ] Control ID 可追踪
- [ ] 无明显重复冲突
- [ ] Evidence 可获得
- [ ] 例外方式明确
- [ ] 链接有效
- [ ] 版本/日期更新
