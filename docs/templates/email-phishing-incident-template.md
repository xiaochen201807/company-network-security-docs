# 邮件 / Phishing Incident 模板

## 基本信息

| 字段 | 内容 |
|---|---|
| Case ID | |
| Reporter | |
| Time | |
| Mailbox | |
| Severity | |
| Analyst | |

## 可疑邮件

- From：
- Reply-To：
- Subject：
- URL：
- Attachment：
- Sender Domain：
- Authentication Result（SPF/DKIM/DMARC）：

## 用户行为

- [ ] 仅收到
- [ ] 点击链接
- [ ] 输入凭据
- [ ] 打开附件
- [ ] 执行程序
- [ ] 回复/转账/发送数据

## 账号调查

- [ ] 异常登录
- [ ] MFA 变化
- [ ] Inbox Rule
- [ ] External Forwarding
- [ ] OAuth App
- [ ] Session/Token
- [ ] Sent Mail

## 处置

- [ ] 删除相同邮件
- [ ] 禁用/重置账号
- [ ] 撤销 Session
- [ ] 吊销 OAuth App
- [ ] 封禁 URL/Domain
- [ ] EDR 检查
- [ ] 通知受影响方

## 结论与整改
