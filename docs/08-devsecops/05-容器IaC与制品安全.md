---
aliases:
  - "容器、IaC 与制品安全标准"
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
# 容器、IaC 与制品安全标准

## 容器

- 基础镜像来自批准来源。
- 使用明确版本/摘要策略。
- 镜像扫描 OS 与应用依赖。
- 凭据 不写入镜像层。
- 非必要不 root/privileged。
- Capability 最小化。
- 不无控制挂载 docker.sock/宿主目录。

## IaC

Terraform、Helm、Kubernetes YAML、Ansible 等采用 Git、评审、凭据扫描（Secret Scan）、IaC Scan；生产变更有 Plan/Approval，State 受控。

## 制品仓库

- Release 不可覆盖。
- Developer 默认无正式制品删除权限。
- Artifact 保存 Digest。
- 记录 Commit、Build、Time。
- 权限与管理员审计。

## Kubernetes

关注 privileged、hostNetwork/hostPath、root、ServiceAccount、RBAC、凭据、Resource Limit、SecurityContext。

## 控制项

SEC-SUP-001、SEC-SUP-004、SEC-CLD-*。
