---
aliases:
  - "密码学、PKI、KMS 与凭据治理"
type: "standard"
domain: "cryptography"
phase:
  - "protect"
priority: "P1"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/cryptography"
  - "security/priority/p1"
  - "security/phase/protect"
parent:
  - "[[docs/公司安全知识图谱]]"
related:
  - "[[docs/04-身份与访问控制]]"
  - "[[docs/07-数据安全]]"
  - "[[docs/06-应用与API安全]]"
  - "[[docs/08-DevSecOps与软件供应链安全]]"
  - "[[docs/16-云与工作负载安全]]"
  - "[[docs/22-安全工程平台]]"
  - "[[docs/15-零信任与设备可信]]"
---
# 21 - 密码学、PKI、KMS 与 凭据治理

> 本文档用于统一公司密码学算法、TLS、证书、PKI、KMS/HSM、应用 凭据、代码签名密钥和密钥生命周期管理。目标是避免不同团队自行选择算法、散落密钥或在无法轮换的情况下形成长期高风险依赖。

## 1. 目标

- 公司有统一密码学标准。
- 证书和密钥全生命周期可管理。
- 凭据 不散落在代码、Wiki、脚本和终端。
- 高价值密钥采用更严格保护。
- 密钥支持轮换、吊销和恢复。
- 可以快速回答“哪些系统使用了某个算法、证书或密钥”。

## 2. 适用范围

- TLS 证书。
- API 密钥。
- JWT Key。
- SSH 密钥。
- 数据加密 Key。
- 数据库密码。
- 云 AccessKey。
- Code Signing Key。
- KMS/HSM。
- CA/PKI。
- Backup Encryption Key。

## 3. 密码学策略

公司 SHOULD 定义统一密码学策略，包含：

- 允许算法。
- 禁止算法。
- Key Length。
- TLS 版本。
- Certificate Lifetime。
- Rotation。
- Storage。
- 例外。

## 4. 禁止自研密码算法

开发人员不得自行设计加密、签名、Hash 或随机算法。优先使用成熟标准库。

## 5. 密码学资产清单

建议维护：

| 字段 | 内容 |
|---|---|
| System | |
| Algorithm | |
| 用途 | |
| Key Type | |
| Key Length | |
| Library/Provider | |
| 负责人 | |
| Rotation | |
| Expiry | |

## 6. 密码学敏捷性

系统设计应避免算法硬编码到无法替换。

成熟目标：

- 可切换算法。
- 可轮换 Key。
- 可升级 TLS。
- 可批量替换证书。
- 可识别受影响系统。

## 7. 哈希

不同用途使用不同技术：

- Password Hash。
- Integrity Hash。
- HMAC。
- File Hash。

普通 Hash 不等于密码存储方案。

## 8. 密码哈希

用户密码使用成熟密码哈希算法和合理成本参数，并支持未来调整。

禁止直接使用快速 Hash 作为密码存储。

## 9. 随机数

用于令牌、Key、Nonce、Reset Link 的随机数必须来自密码学安全随机源。

## 10. TLS

### MUST

- 敏感公网通信使用 TLS。
- 禁用已知不安全协议版本。
- 私钥安全存储。
- 证书到期监控。
- Hostname 验证。

## 11. 内部 TLS

内部链路是否启用 TLS/mTLS 根据数据和威胁模型决定。

以下场景优先：

- 高敏数据。
- 跨不可信网络。
- Service Mesh。
- 管理面。
- Multi-cloud。

## 12. 证书生命周期

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

## 13. 证书清单

至少记录：

- Subject/SAN。
- 负责人。
- System。
- CA。
- Issued Date。
- Expiry。
- Key Location。
- Auto Renew。

## 14. 自动续期

SHOULD 优先自动续期证书，并监控自动化失败。

不能因为“配置了自动续期”就取消到期告警。

## 15. 私钥

私钥：

- 不提交 Git。
- 权限最小化。
- 不通过普通聊天工具传输。
- 不多人共享。
- 泄露立即吊销/轮换。

## 16. 内部 PKI

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

## 20. 信封加密

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

## 21. 密钥职责分离

不同用途不要共用同一密钥：

- JWT Signing。
- Database Encryption。
- Backup。
- API Signing。
- Code Signing。

## 22. 密钥轮换

每类 Key 应明确：

- Rotation Frequency。
- Trigger。
- Backward Compatibility。
- Emergency Rotation。
- 负责人。

## 23. 紧急轮换

凭据泄露时：

1. 识别使用范围。
2. 创建新 Key。
3. 更新依赖系统。
4. 切换。
5. 吊销旧 Key。
6. 监控旧 Key 使用。
7. 复盘。

## 24. 密钥版本管理

支持多版本 Key，避免轮换时全系统瞬间失败。

## 25. 密钥吊销

系统必须能够撤销不可信 Key，而不是只能“等它过期”。

## 26. 密钥删除

高价值 Key 删除：

- 审批。
- 延迟删除。
- 恢复窗口。
- Audit。

避免误删导致数据永久不可恢复。

## 27. 备份密钥

加密备份的恢复密钥必须与备份同时考虑灾难恢复。

如果备份存在但 Key 丢失，等同于不可恢复。

## 28. 凭据管理平台（Secret Manager）

优先集中管理：

- Database Password。
- API 令牌。
- Cloud Key。
- Certificate。
- Service Credential。

## 29. 凭据交付

应用获取 凭据：

- Runtime Pull。
- Short-lived Credential。
- Managed Identity。
- Sidecar/Agent。
- Secure Injection。

避免长期写在配置文件。

## 30. CI/CD 中的凭据

Jenkins/Git CI：

- Credentials Store。
- Masking。
- 最小范围。
- 不打印。
- Build 后清理。

## 31. Kubernetes Secret

Kubernetes Secret 并不天然等于强加密存储。

应结合：

- RBAC。
- etcd Encryption。
- 外部凭据管理平台（Secret Manager）。
- Namespace Isolation。

## 32. 代码签名

正式软件包、脚本或制品成熟阶段可进行 Code/Artifact Signing。

签名私钥：

- 高等级保护。
- 使用审计。
- 构建系统最小权限访问。
- 支持吊销/轮换。

## 33. SSH 密钥

个人 SSH 密钥：

- 不共享。
- 私钥加密。
- 离职吊销。
- 丢设备吊销。

大量 SSH 管理成熟阶段可采用 SSH CA 短期证书。

## 34. JWT 密钥

JWT Signing Key：

- 与应用配置分离。
- Key ID/版本。
- Rotation。
- 多 Key 验证窗口。
- 禁止弱 凭据。

## 35. API 签名

对高价值 API 使用签名时，明确：

- Algorithm。
- Timestamp。
- Nonce。
- Key ID。
- Replay Prevention。
- Rotation。

## 36. 凭据扫描（Secret Scan）

凭据扫描（Secret Scan）覆盖：

- Git。
- History。
- CI Log。
- Artifact。
- Container Image。
- Wiki（能力允许时）。

## 37. 证书监控

告警窗口可分：

- 60 天。
- 30 天。
- 14 天。
- 7 天。

具体按续期机制设置。

## 38. 抗量子准备度

公司短期不必盲目迁移所有算法，但 SHOULD 建立 Crypto Inventory，为未来算法迁移和 Post-Quantum 变化做好可见性。

## 39. 指标

- 凭据管理平台（Secret Manager）覆盖率。
- 代码明文 凭据 数量。
- 证书过期事故。
- 30 天内到期未续期数。
- 长期 AccessKey 数。
- 未轮换高风险 Key 数。
- Crypto Inventory 覆盖率。

## 40. P0

1. 凭据 禁止明文入库。
2. 证书台账与到期告警。
3. JWT/TLS/密码 Hash 标准。
4. 高价值 Key 负责人。
5. Jenkins Credentials。
6. 泄露轮换流程。

## 41. P1

1. 凭据管理平台（Secret Manager）。
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
- 凭据扫描（Secret Scan）。
- Code Signing。
- 例外。

## 44. 当前待确认

- [ ] TLS 标准
- [ ] 证书平台
- [ ] 凭据管理平台（Secret Manager）
- [ ] KMS/HSM
- [ ] Code Signing
- [ ] Key Rotation 周期
- [ ] Crypto Inventory 负责人

## 45. 参考

- NIST 密码学相关指南
- Microsoft SDL Cryptography Practice
- 公司数据安全与 IAM 规范

## 46. 变更记录

| 版本 | 日期 | 说明 |
|---|---|---|
| V0.1 | 2026-09 | 建立密码学、PKI、KMS 和 凭据治理体系 |

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian 全局图谱 / 局部图谱。业务正文请维护在上方章节。

- **上级导航**：[[docs/公司安全知识图谱|公司安全知识图谱]]
- **前置知识**：[[docs/04-身份与访问控制|04 身份与访问控制]] · [[docs/07-数据安全|07 数据安全]]
- **下游知识**：[[docs/06-应用与API安全|06 应用与 API 安全]] · [[docs/08-DevSecOps与软件供应链安全|08 DevSecOps 与供应链安全]] · [[docs/16-云与工作负载安全|16 云与工作负载安全]] · [[docs/22-安全工程平台|22 安全工程平台]]
- **横向关联**：[[docs/15-零信任与设备可信|15 零信任与设备可信]]

<!-- obsidian-relations:end -->
