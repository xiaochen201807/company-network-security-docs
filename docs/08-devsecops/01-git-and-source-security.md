# Git 与源代码安全 Standard

## 控制要求

- 代码进入公司受控 Git。
- main/master/release/production 等关键分支保护。
- 普通开发不能 Force Push 受保护分支。
- 合并通过 PR/MR 与独立 Review。
- 高价值仓库考虑 CODEOWNERS/双人 Review。
- 管理员、仓库可见性和 Token 变化可审计。
- 一人一号，高权限 MFA，离职及时回收。
- CI Token 与个人 Token 分离。
- Token 有 Owner、Purpose、Scope、Expiry、Rotation、Revocation。

## Code Review 重点

Authentication/Authorization、SQL/File/Network、Secret、Dependency、Jenkinsfile/Dockerfile、IaC、管理接口。

## Evidence

Git Protection、PR/MR、Review、Admin List、Token Register、Audit Log。

## Controls

SEC-SUP-002、SEC-IAM-*、SEC-APP-*。
