---
aliases:
  - "SAST、凭据与 SBOM 标准"
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
# SAST、凭据与 SBOM 标准

## SAST

重点覆盖 Injection、SSRF、Path Traversal、XXE、Unsafe Deserialization、Weak Crypto、Auth/AuthZ、Dangerous API。

高风险结果人工验证；Security Hotspot 不自动等同漏洞。

## Secret Scan

覆盖 Commit、History、PR/MR、Jenkins Workspace/Log、Artifact、Container Image。

真实 Secret 泄露后必须吊销/轮换，仅删除文本不够。

## SBOM

正式 Release SHOULD 生成 SBOM，并与 Build/Commit/Artifact 绑定，用于 CVE 反查。

## Evidence

SAST、Secret Finding、Rotation Record、SBOM、Exception。

## Controls

SEC-SUP-003、SEC-SUP-005、SEC-APP-*。
