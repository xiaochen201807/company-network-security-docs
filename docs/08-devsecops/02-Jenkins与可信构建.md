---
aliases:
  - "Jenkins 与可信构建标准"
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
# Jenkins 与可信构建标准

## 控制器

- 不无保护公网暴露。
- 管理员最小化并使用强认证/MFA。
- Script Console 等高危能力严格限制。
- Plugin 有 Inventory、Update、Test、Rollback。
- 配置和关键 Job 有备份。

## 凭据

- 凭据 使用 Credentials Store/凭据管理平台（Secret Manager）。
- Pipeline 不硬编码。
- 日志 Mask。
- 禁止通过 echo/env/printenv 泄露凭据。
- 凭据按项目和环境最小权限。

## 执行节点（Agent）

- Agent 与 Controller 隔离。
- 不默认给所有 Job Docker Socket。
- 高风险项目使用临时 Agent。
- Build 后清理 Workspace/凭据。

## 可追溯性

正式 Build 记录 Repo、Commit、Job、Build ID、Builder、Time、Artifact Digest。

## 可信构建器

项目代码不应无审计修改 Builder 核心安全策略；公共 Pipeline 独立管理。

## 控制项

SEC-SUP-001、SEC-SUP-003、SEC-SUP-005。
