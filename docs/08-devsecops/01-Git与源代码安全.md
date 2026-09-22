---
aliases:
  - "Git 与源代码安全标准"
type: "standard"
domain: "devsecops"
phase:
  - "protect"
priority: "P0"
status: "active"
tags:
  - "security"
  - "security/type/standard"
  - "security/domain/devsecops"
  - "security/priority/p0"
  - "security/phase/protect"
parent:
  - "[[docs/08-DevSecOps与软件供应链安全]]"
---
# Git 与源代码安全标准

## 控制要求

- 代码进入公司受控 Git。
- main/master/release/production 等关键分支保护。
- 普通开发不能 Force Push 受保护分支。
- 合并通过 PR/MR 与独立评审。
- 高价值仓库考虑 CODEOWNERS/双人评审。
- 管理员、仓库可见性和令牌变化可审计。
- 一人一号，高权限 MFA，离职及时回收。
- CI 令牌与个人令牌分离。
- 令牌有负责人、用途、范围、到期时间、轮换、吊销。

## 代码评审重点

Authentication/Authorization、SQL/File/Network、凭据、Dependency、Jenkinsfile/Dockerfile、IaC、管理接口。

## 证据

Git Protection、PR/MR、评审、管理员 List、令牌 Register、审计日志。

## 控制项

SEC-SUP-002、SEC-IAM-*、SEC-APP-*。
