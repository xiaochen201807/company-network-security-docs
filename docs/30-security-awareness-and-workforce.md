# 30 - 安全意识、Security Champion 与安全人才体系

> 安全能力不能只依赖安全团队。本章建立全员安全意识、角色化培训、Security Champion 和关键岗位能力模型。

## 1. 目标

- 全员掌握基础安全行为。
- 高风险岗位接受针对性培训。
- 研发和运维具备必要安全能力。
- Security Champion 将安全融入团队日常。
- 安全事件和演练反向驱动培训。
- 关键安全能力不依赖单个人。

## 2. 培训分层

### Level 1 - 全员
- Phishing。
- Password/MFA。
- Data Handling。
- Device。
- Incident Reporting。
- AI 使用边界。

### Level 2 - Role Based
研发、运维、管理员、财务、HR、采购等专项培训。

### Level 3 - Specialist
Security、SRE、Architect、Champion 深度能力。

## 3. New Hire

入职安全培训：

- 账号安全。
- MFA。
- 设备。
- 数据。
- 邮件。
- 公司安全报告渠道。
- 可接受使用政策。

应在合理期限内完成并留证据。

## 4. Annual Training

年度复训根据真实事件调整内容，而不是每年播放完全相同视频。

## 5. Developer Training

重点：

- Authentication/Authorization。
- SQLi。
- SSRF。
- Upload。
- Secret。
- Dependency。
- Threat Modeling。
- Secure Logging。
- Spring Security。

培训最好结合公司真实代码案例。

## 6. DevOps/SRE Training

重点：

- IAM。
- Secret。
- Jenkins。
- Kubernetes。
- Cloud。
- Logging。
- IR。
- Backup/DR。
- Production Change。

## 7. Admin Training

管理员：

- PAM/JIT。
- MFA。
- Privileged Session。
- Break-glass。
- Incident。
- Evidence。

## 8. Finance / HR / Procurement

重点：

- BEC。
- Impersonation。
- Invoice Fraud。
- Sensitive Data。
- Third-party Risk。
- Verification Channel。

## 9. Executive

管理层培训：

- 风险接受责任。
- Incident 决策。
- Business Continuity。
- Regulatory/Contract Risk。
- Security Investment。

## 10. Phishing Simulation

指标：

- Click Rate。
- Credential Submission（仅安全演练设计允许时）。
- Report Rate。
- Repeat Failure。
- Department Trend。

目标是提升识别和报告能力，不以羞辱或惩罚作为主要方式。

## 11. Just-in-Time Training

发生以下情况后提供针对性培训：

- Secret 泄露。
- 重复越权漏洞。
- 钓鱼点击。
- 错误数据外发。
- 不安全生产变更。

## 12. Security Champion

每个主要研发/平台团队可指定 Champion。

职责：

- 协助 Threat Model。
- 推动安全修复。
- 分享安全知识。
- 收集团队反馈。
- 参与 Security Community。

Champion 不替代 Security Team，也不承担所有风险责任。

## 13. Champion Selection

优先选择：

- 对安全感兴趣。
- 熟悉业务。
- 能影响团队工程实践。
- 有时间承担职责。

不建议仅按行政指派而不给时间。

## 14. Champion Enablement

提供：

- 培训路径。
- Office Hour。
- Threat Model 模板。
- Secure Coding Guide。
- Dashboard。
- 专项 Workshop。

## 15. Security Community

定期：

- 分享漏洞案例。
- 新 CVE。
- Secure Coding。
- Cloud。
- AI。
- Incident Lessons Learned。

## 16. Skills Matrix

关键岗位维护能力矩阵：

| Role | Basic | Working | Advanced |
|---|---|---|---|
| AppSec | | | |
| Cloud Security | | | |
| SOC | | | |
| IR | | | |
| Pentest | | | |
| IAM | | | |
| Security Architecture | | | |

## 17. Key Person Risk

识别：

- 只有一个人会处理 Jenkins。
- 只有一个人知道证书续期。
- 只有一个 IR 负责人。
- 只有一个数据库管理员。

建立 Backup Owner 和知识转移。

## 18. Exercise

培训不只靠课程：

- Tabletop。
- Purple Team。
- Restore Exercise。
- Phishing Simulation。
- Secure Coding Workshop。

## 19. Knowledge Base

沉淀：

- FAQ。
- Runbook。
- Secure Example。
- Incident Lesson。
- Tool Guide。
- Common Fix。

## 20. Metrics

- 全员培训完成率。
- Role-based 覆盖率。
- Champion 覆盖率。
- Phishing Report Rate。
- 重复安全问题下降趋势。
- 演练完成率。
- 关键岗位 Backup Coverage。

## 21. P0

1. New Hire Training。
2. Annual Training。
3. Developer/DevOps Role Training。
4. Phishing Report。
5. 关键岗位 Backup Owner。

## 22. P1

1. Security Champion。
2. Phishing Simulation。
3. Skills Matrix。
4. Security Community。
5. Incident-driven Training。

## 23. P2

1. Internal Security Academy。
2. Hands-on Lab。
3. Capture-the-Flag。
4. Specialist Certification Path。

## 24. 审计证据

- Training Plan。
- Completion。
- Role Matrix。
- Simulation。
- Champion Register。
- Workshop。
- Exercise。

## 25. 当前待确认

- [ ] 培训平台
- [ ] 全员培训周期
- [ ] 研发培训周期
- [ ] Champion 机制
- [ ] 钓鱼演练
- [ ] Skills Matrix
- [ ] 安全关键岗位 Backup

## 26. 关联控制

SEC-AWR-001、SEC-AWR-002、SEC-EML-*、SEC-APP-*、SEC-IR-*。
