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
