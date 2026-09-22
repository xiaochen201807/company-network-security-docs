---
aliases:
  - "DevSecOps 与供应链安全"
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
  - "[[docs/knowledge-map]]"
related:
  - "[[docs/06-application-and-api-security]]"
  - "[[docs/17-security-architecture-and-threat-modeling]]"
  - "[[docs/09-vulnerability-and-penetration-testing]]"
  - "[[docs/18-product-security-and-secure-by-default]]"
  - "[[docs/22-security-engineering-platform]]"
  - "[[docs/21-cryptography-pki-kms-and-secrets]]"
---
# 08 - DevSecOps 与软件供应链安全

> V2.0 起，本章改为索引页。原 V1.1 长文档已保留为 [历史完整参考](08-devsecops/reference-full-v1.md)，日常维护以以下拆分标准为准。

## 1. 子标准

1. [Git 与源代码安全](08-devsecops/01-git-and-source-security.md)
2. [Jenkins 与可信构建](08-devsecops/02-jenkins-and-trusted-build.md)
3. [Dependency 与 SCA](08-devsecops/03-dependency-and-sca.md)
4. [SAST、Secret 与 SBOM](08-devsecops/04-sast-secret-sbom.md)
5. [Container、IaC 与制品](08-devsecops/05-container-iac-artifact.md)
6. [Security Gate、例外与度量](08-devsecops/06-security-gate-exception-metrics.md)
7. [SLSA、Provenance 与 Signing](08-devsecops/07-slsa-provenance-signing.md)

## 2. 核心控制

- SEC-SUP-001：生产仅部署受控 CI/CD 生成的正式制品。
- SEC-SUP-002：主分支保护并通过 Review。
- SEC-SUP-003：Secret 不得硬编码进入源码和 Pipeline。
- SEC-SUP-004：Release 制品不可被无审计覆盖。
- SEC-SUP-005：重要制品逐步生成 SBOM 与 Provenance。

## 3. 维护原则

新要求写入对应子标准，不再继续扩展历史长文档。历史完整参考仅用于迁移期间查阅。

<!-- obsidian-relations:start -->
## Obsidian 关联知识

> [!tip] 图谱导航
> 本区由 scripts/obsidian_optimize.py 维护，用于 Obsidian Global Graph / Local Graph。业务正文请维护在上方章节。

- **上级导航**：[[docs/knowledge-map|公司安全知识图谱]]
- **前置知识**：[[docs/06-application-and-api-security|06 应用与 API 安全]] · [[docs/17-security-architecture-and-threat-modeling|17 安全架构评审与 Threat Modeling]]
- **下游知识**：[[docs/09-vulnerability-and-penetration-testing|09 漏洞管理与授权渗透测试]] · [[docs/18-product-security-and-secure-by-default|18 Product Security 与 Secure by Default]] · [[docs/22-security-engineering-platform|22 Security Engineering Platform]]
- **横向关联**：[[docs/21-cryptography-pki-kms-and-secrets|21 密码学、PKI、KMS 与 Secret 治理]]

<!-- obsidian-relations:end -->
