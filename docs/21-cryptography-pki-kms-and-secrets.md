# 21 - 密码学、PKI、KMS 与 Secret 治理

> 本文档用于统一公司密码学算法、TLS、证书、PKI、KMS/HSM、应用 Secret、代码签名密钥和密钥生命周期管理。目标是避免不同团队自行选择算法、散落密钥或在无法轮换的情况下形成长期高风险依赖。

## 1. 目标

- 公司有统一密码学标准。
- 证书和密钥全生命周期可管理。
- Secret 不散落在代码、Wiki、脚本和终端。
- 高价值密钥采用更严格保护。
- 密钥支持轮换、吊销和恢复。
- 可以快速回答“哪些系统使用了某个算法、证书或密钥”。

## 2. 适用范围

- TLS 证书。
- API Key。
- JWT Key。
- SSH Key。
- 数据加密 Key。
- 数据库密码。
- 云 AccessKey。
- Code Signing Key。
- KMS/HSM。
- CA/PKI。
- Backup Encryption Key。

## 3. Crypto Policy

公司 SHOULD 定义统一密码学策略，包含：

- 允许算法。
- 禁止算法。
- Key Length。
- TLS Version。
- Certificate Lifetime。
- Rotation。
- Storage。
- Exception。

## 4. 禁止自研密码算法

开发人员不得自行设计加密、签名、Hash 或随机算法。优先使用成熟标准库。

## 5. Crypto Inventory

建议维护：

| 字段 | 内容 |
|---|---|
| System | |
| Algorithm | |
| Purpose | |
| Key Type | |
| Key Length | |
| Library/Provider | |
| Owner | |
| Rotation | |
| Expiry | |

## 6. Crypto Agility

系统设计应避免算法硬编码到无法替换。

成熟目标：

- 可切换算法。
- 可轮换 Key。
- 可升级 TLS。
- 可批量替换证书。
- 可识别受影响系统。

## 7. Hash

不同用途使用不同技术：

- Password Hash。
- Integrity Hash。
- HMAC。
- File Hash。

普通 Hash 不等于密码存储方案。

## 8. Password Hash

用户密码使用成熟密码哈希算法和合理成本参数，并支持未来调整。

禁止直接使用快速 Hash 作为密码存储。

## 9. Random Number

用于 Token、Key、Nonce、Reset Link 的随机数必须来自密码学安全随机源。

## 10. TLS

### MUST

- 敏感公网通信使用 TLS。
- 禁用已知不安全协议版本。
- 私钥安全存储。
- 证书到期监控。
- Hostname 验证。

## 11. Internal TLS

内部链路是否启用 TLS/mTLS 根据数据和威胁模型决定。

以下场景优先：

- 高敏数据。
- 跨不可信网络。
- Service Mesh。
- 管理面。
- Multi-cloud。

## 12. Certificate Lifecycle

~~~text
Request
 ↓
Approve
 ↓
Issue
 ↓
Deploy
 ↓
Monitor
 ↓
Renew / Rotate
 ↓
Revoke
 ↓
Retire
~~~

## 13. Certificate Inventory

至少记录：

- Subject/SAN。
- Owner。
- System。
- CA。
- Issued Date。
- Expiry。
- Key Location。
- Auto Renew。

## 14. 自动续期

SHOULD 优先自动续期证书，并监控自动化失败。

不能因为“配置了自动续期”就取消到期告警。

## 15. Private Key

私钥：

- 不提交 Git。
- 权限最小化。
- 不通过普通聊天工具传输。
- 不多人共享。
- 泄露立即吊销/轮换。

## 16. Internal PKI

如果公司有大量内部服务，可建设内部 PKI 管理：

- Server Certificate。
- Device Certificate。
- User Certificate。
- Workload Certificate。
- SSH Certificate。

## 17. CA

CA 私钥属于高价值密钥。

应：

- 严格访问。
- 分离 Root/Intermediate。
- 离线 Root（成熟阶段）。
- HSM 保护（高风险场景）。
- 操作审计。

## 18. KMS

应用数据加密 SHOULD 优先使用 KMS 类平台：

- Key Policy。
- Audit。
- Rotation。
- Access Control。
- Disable/Delete Protection。

## 19. HSM

以下场景根据风险考虑 HSM：

- Root CA。
- Code Signing。
- 关键支付/金融密钥。
- 高价值主密钥。
- 法规/合同明确要求。

## 20. Envelope Encryption

大规模数据加密可使用：

~~~text
Master Key / KEK
   ↓
KMS/HSM
   ↓
Data Encryption Key
   ↓
Encrypted Data
~~~

减少主密钥直接处理大量数据。

## 21. Key Separation

不同用途不要共用同一密钥：

- JWT Signing。
- Database Encryption。
- Backup。
- API Signing。
- Code Signing。

## 22. Key Rotation

每类 Key 应明确：

- Rotation Frequency。
- Trigger。
- Backward Compatibility。
- Emergency Rotation。
- Owner。

## 23. Emergency Rotation

Secret 泄露时：

1. 识别使用范围。
2. 创建新 Key。
3. 更新依赖系统。
4. 切换。
5. 吊销旧 Key。
6. 监控旧 Key 使用。
7. 复盘。

## 24. Key Versioning

支持多版本 Key，避免轮换时全系统瞬间失败。

## 25. Key Revocation

系统必须能够撤销不可信 Key，而不是只能“等它过期”。

## 26. Key Deletion

高价值 Key 删除：

- 审批。
- 延迟删除。
- 恢复窗口。
- Audit。

避免误删导致数据永久不可恢复。

## 27. Backup Key

加密备份的恢复密钥必须与备份同时考虑灾难恢复。

如果备份存在但 Key 丢失，等同于不可恢复。

## 28. Secret Manager

优先集中管理：

- Database Password。
- API Token。
- Cloud Key。
- Certificate。
- Service Credential。

## 29. Secret Delivery

应用获取 Secret：

- Runtime Pull。
- Short-lived Credential。
- Managed Identity。
- Sidecar/Agent。
- Secure Injection。

避免长期写在配置文件。

## 30. Secret in CI/CD

Jenkins/Git CI：

- Credentials Store。
- Masking。
- 最小 Scope。
- 不打印。
- Build 后清理。

## 31. Kubernetes Secret

Kubernetes Secret 并不天然等于强加密存储。

应结合：

- RBAC。
- etcd Encryption。
- External Secret Manager。
- Namespace Isolation。

## 32. Code Signing

正式软件包、脚本或制品成熟阶段可进行 Code/Artifact Signing。

签名私钥：

- 高等级保护。
- 使用审计。
- 构建系统最小权限访问。
- 支持吊销/轮换。

## 33. SSH Key

个人 SSH Key：

- 不共享。
- 私钥加密。
- 离职吊销。
- 丢设备吊销。

大量 SSH 管理成熟阶段可采用 SSH CA 短期证书。

## 34. JWT Key

JWT Signing Key：

- 与应用配置分离。
- Key ID/版本。
- Rotation。
- 多 Key 验证窗口。
- 禁止弱 Secret。

## 35. API Signing

对高价值 API 使用签名时，明确：

- Algorithm。
- Timestamp。
- Nonce。
- Key ID。
- Replay Prevention。
- Rotation。

## 36. Secret Scan

Secret Scan 覆盖：

- Git。
- History。
- CI Log。
- Artifact。
- Container Image。
- Wiki（能力允许时）。

## 37. Certificate Monitoring

告警窗口可分：

- 60 天。
- 30 天。
- 14 天。
- 7 天。

具体按续期机制设置。

## 38. Quantum Readiness

公司短期不必盲目迁移所有算法，但 SHOULD 建立 Crypto Inventory，为未来算法迁移和 Post-Quantum 变化做好可见性。

## 39. 指标

- Secret Manager 覆盖率。
- 代码明文 Secret 数量。
- 证书过期事故。
- 30 天内到期未续期数。
- 长期 AccessKey 数。
- 未轮换高风险 Key 数。
- Crypto Inventory 覆盖率。

## 40. P0

1. Secret 禁止明文入库。
2. 证书台账与到期告警。
3. JWT/TLS/密码 Hash 标准。
4. 高价值 Key Owner。
5. Jenkins Credentials。
6. 泄露轮换流程。

## 41. P1

1. Secret Manager。
2. KMS。
3. 自动证书续期。
4. Key Rotation。
5. Crypto Inventory。
6. Code Signing。

## 42. P2

1. HSM。
2. SSH CA。
3. Workload Certificate。
4. Crypto Agility。
5. PQC Readiness。

## 43. 审计证据

- Crypto Policy。
- Certificate Inventory。
- Key Inventory。
- Rotation。
- KMS Audit。
- Secret Scan。
- Code Signing。
- Exception。

## 44. 当前待确认

- [ ] TLS 标准
- [ ] 证书平台
- [ ] Secret Manager
- [ ] KMS/HSM
- [ ] Code Signing
- [ ] Key Rotation 周期
- [ ] Crypto Inventory Owner

## 45. 参考

- NIST 密码学相关指南
- Microsoft SDL Cryptography Practice
- 公司数据安全与 IAM 规范

## 46. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立密码学、PKI、KMS 和 Secret 治理体系 |
