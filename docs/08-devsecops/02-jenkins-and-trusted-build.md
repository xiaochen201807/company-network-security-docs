# Jenkins 与可信构建 Standard

## Controller

- 不无保护公网暴露。
- 管理员最小化并使用强认证/MFA。
- Script Console 等高危能力严格限制。
- Plugin 有 Inventory、Update、Test、Rollback。
- 配置和关键 Job 有备份。

## Credentials

- Secret 使用 Credentials Store/Secret Manager。
- Pipeline 不硬编码。
- 日志 Mask。
- 禁止通过 echo/env/printenv 泄露凭据。
- 凭据按项目和环境最小权限。

## Agent

- Agent 与 Controller 隔离。
- 不默认给所有 Job Docker Socket。
- 高风险项目使用临时 Agent。
- Build 后清理 Workspace/Secret。

## Traceability

正式 Build 记录 Repo、Commit、Job、Build ID、Builder、Time、Artifact Digest。

## Trusted Builder

项目代码不应无审计修改 Builder 核心安全策略；公共 Pipeline 独立管理。

## Controls

SEC-SUP-001、SEC-SUP-003、SEC-SUP-005。
