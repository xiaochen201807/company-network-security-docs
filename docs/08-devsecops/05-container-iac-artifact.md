# Container、IaC 与制品 Standard

## Container

- 基础镜像来自批准来源。
- 使用明确版本/摘要策略。
- 镜像扫描 OS 与应用依赖。
- Secret 不写入镜像层。
- 非必要不 root/privileged。
- Capability 最小化。
- 不无控制挂载 docker.sock/宿主目录。

## IaC

Terraform、Helm、Kubernetes YAML、Ansible 等采用 Git、Review、Secret Scan、IaC Scan；生产变更有 Plan/Approval，State 受控。

## Artifact Repository

- Release 不可覆盖。
- Developer 默认无正式制品删除权限。
- Artifact 保存 Digest。
- 记录 Commit、Build、Time。
- 权限与管理员审计。

## Kubernetes

关注 privileged、hostNetwork/hostPath、root、ServiceAccount、RBAC、Secret、Resource Limit、SecurityContext。

## Controls

SEC-SUP-001、SEC-SUP-004、SEC-CLD-*。
