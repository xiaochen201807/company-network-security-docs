# 25 - 邮件与协作平台安全

> 邮件、企业 IM、云文档和协作平台是身份攻击、钓鱼、BEC、恶意附件、OAuth 授权滥用和数据外泄的重要入口。

## 1. 目标

- 降低钓鱼、账号接管与 BEC 风险。
- 防止公司域名被伪造用于欺诈。
- 保护高价值邮箱与协作平台管理员。
- 控制第三方 OAuth/App 集成。
- 对恶意邮件和协作链接具备检测与响应能力。
- 兼顾敏感数据外发治理。

## 2. 范围

- 企业邮箱。
- 邮件域名/DNS。
- 企业 IM。
- 云文档/网盘。
- Calendar。
- OAuth App。
- 邮件网关。
- 邮件客户端。
- 外部共享。

## 3. 身份与 MFA

**MUST：**

- 邮件管理员不得共享账号。
- 管理员和高风险邮箱启用 MFA。
- 离职邮箱及时禁用或按审批进入交接。
- 高权限管理账号与日常账号适当分离。

## 4. SPF

公司发信域 SHOULD 配置 SPF，明确授权邮件服务器。

定期检查：

- 是否超过 DNS Lookup 限制。
- 是否包含不再使用的第三方发信服务。
- 是否存在过宽 include。
- 子域策略是否一致。

## 5. DKIM

公司主要发信服务 SHOULD 启用 DKIM：

- 密钥安全管理。
- 定期轮换。
- 记录 Selector。
- 第三方 SaaS 发信纳入管理。

## 6. DMARC

公司主域和重要发信域 SHOULD 配置 DMARC，并通过监控逐步从观察模式提升到更严格策略。

建议路线：

~~~text
p=none
 ↓
分析合法/非法发信源
 ↓
p=quarantine
 ↓
p=reject
~~~

策略升级前避免误伤真实业务发信。

## 7. Lookalike Domain

SHOULD 监测：

- 拼写相似域名。
- 高价值品牌仿冒域名。
- 新注册钓鱼域。
- 可疑证书。

发现恶意仿冒后启动域名/品牌处置流程。

## 8. Anti-Phishing

邮件平台 SHOULD 支持：

- 恶意链接检测。
- 附件扫描。
- 可疑发件人检测。
- Impersonation Protection。
- URL Rewrite/Sandbox（按平台能力）。
- 外部邮件标记。

## 9. BEC

重点保护：

- 财务。
- 高管。
- HR。
- 采购。
- 管理员。

高风险财务操作不能仅凭邮件指令完成，应有独立审批或第二渠道验证。

## 10. Attachment

高风险附件类型按公司策略限制。

Office/PDF/压缩包等：

- 恶意内容扫描。
- 宏风险控制。
- 密码压缩包建立额外流程。
- 未知可执行文件默认阻断或隔离。

## 11. Links

高风险链接：

- 新注册域。
- URL Shortener。
- 仿冒登录页。
- Credential Harvesting。

浏览器/网关安全能力与邮件检测联动。

## 12. OAuth App

第三方 OAuth App 是常见持久化入口。

要求：

- 用户不能无控制批准高权限 App。
- 高权限 App 由管理员审批。
- 定期审查 App Consent。
- 离职账号相关授权及时处理。
- 异常 App 创建触发告警。

## 13. Mailbox Rule

重点检测：

- 自动转发到外部。
- 隐藏/删除安全邮件。
- 可疑 Inbox Rule。
- 邮件委派变化。

## 14. External Forwarding

默认限制自动转发敏感邮件到个人邮箱。确需使用应有明确业务原因和审批。

## 15. Admin Audit

记录：

- 管理员登录。
- 邮箱委派。
- Transport Rule。
- Anti-spam Policy。
- OAuth App。
- Retention。
- eDiscovery 高风险操作。

## 16. Collaboration Platform

企业 IM/云文档：

- SSO/MFA。
- 外部成员标识。
- 外部共享限制。
- 管理员最小化。
- 安全日志。
- Token/Integration 管理。

## 17. External Sharing

共享文档时：

- 明确收件人。
- 禁止默认公开链接。
- 设置到期时间（能力支持时）。
- 敏感资料按数据等级限制外部共享。

## 18. DLP

成熟阶段可配置：

- 敏感字段识别。
- 邮件外发告警。
- 高风险附件阻断。
- 云文档外部共享告警。

DLP 规则需持续调优，避免大量误报。

## 19. Phishing Report

员工应有简单的“报告钓鱼”入口。

报告后：

- 自动收集原始邮件。
- 安全分析。
- 查询相同邮件是否发送给其他员工。
- 必要时批量清理。

## 20. Phishing Simulation

可定期开展钓鱼演练，但：

- 以培训和改进为目标。
- 不羞辱员工。
- 高风险岗位进行针对性培训。
- 统计 Report Rate，而不仅是 Click Rate。

## 21. Email Incident

账号被入侵：

1. 禁用/重置身份。
2. 撤销 Session/Token。
3. 检查 MFA。
4. 查询 Inbox Rule。
5. 查询 OAuth App。
6. 查询异常邮件。
7. 通知可能受影响对象。
8. 必要时搜索同类活动。

## 22. 指标

- MFA 覆盖率。
- DMARC 覆盖率。
- Phishing Report Rate。
- 邮箱账号接管事件数。
- 高风险 OAuth App 数。
- 外部自动转发数。
- BEC 事件数。

## 23. P0

1. 管理员/高风险邮箱 MFA。
2. SPF/DKIM/DMARC。
3. 外部自动转发治理。
4. OAuth App Review。
5. Phishing Report。
6. BEC 二次验证流程。

## 24. P1

1. DMARC reject。
2. Lookalike Domain Monitoring。
3. Advanced Phishing Protection。
4. DLP。
5. Phishing Simulation。

## 25. 审计证据

- DNS Record。
- DMARC Report。
- MFA Report。
- OAuth App。
- Mailbox Rule Alert。
- Phishing Incident。
- DLP Report。

## 26. 当前待确认

- [ ] 企业邮箱平台
- [ ] 主域/发信域
- [ ] SPF/DKIM/DMARC 当前状态
- [ ] OAuth App 管理方式
- [ ] 邮件安全网关
- [ ] DLP 能力
- [ ] 钓鱼演练机制

## 27. 关联控制

SEC-EML-001、SEC-EML-002、SEC-IAM-*、SEC-DAT-*、SEC-AWR-*。
