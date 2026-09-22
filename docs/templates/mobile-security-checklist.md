---
aliases:
  - "Mobile Security 检查模板"
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
# Mobile Security 检查模板

## 基本信息

| 字段 | 内容 |
|---|---|
| App | |
| Platform | Android / iOS |
| Version | |
| Owner | |
| Release | |

## STORAGE

- [ ] Token 使用安全存储
- [ ] 无明文密码/私钥
- [ ] Cache/Temp 无敏感残留
- [ ] 日志无敏感信息

## CRYPTO

- [ ] 使用平台标准密码学
- [ ] 无硬编码主密钥
- [ ] 安全随机数

## AUTH

- [ ] 服务端认证授权
- [ ] Token 可失效
- [ ] 对象/功能权限服务端校验

## NETWORK

- [ ] TLS
- [ ] Hostname Verification
- [ ] Release 不信任所有证书
- [ ] Pinning（若使用）有轮换方案

## PLATFORM

- [ ] Deep Link 校验
- [ ] WebView 安全
- [ ] Exported Component/IPC Review
- [ ] 系统权限最小化

## CODE

- [ ] Debug 关闭
- [ ] SAST/SCA/Secret
- [ ] 第三方 SDK Review
- [ ] 无长期高权限 Secret

## RESILIENCE

- [ ] 混淆（适用时）
- [ ] 完整性/防篡改（适用时）
- [ ] Root/Jailbreak 作为风险信号而非唯一控制

## PRIVACY

- [ ] 权限申请合理
- [ ] 数据最小化
- [ ] 第三方 SDK 数据收集 Review

## Security Test

- [ ] MASVS/MASTG 检查
- [ ] API 越权
- [ ] Pentest（适用时）

结论：
