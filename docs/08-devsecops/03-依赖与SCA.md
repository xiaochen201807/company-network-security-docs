---
aliases:
  - "依赖与 SCA 标准"
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
# 依赖与 SCA 标准

## 依赖来源

依赖优先通过公司批准仓库或代理获取。新增第三方仓库评估来源、负责人和范围。

## SCA

输出至少包含 Component、版本、CVE、CVSS、Direct/Transitive、Fixed 版本、License、Project、负责人。

## 风险

CVSS 结合公网暴露、代码可达性、Exploit、KEV/真实攻击、资产重要性、数据和补偿控制。

## 扫描时机

PR/MR、Main、Release、Periodic Full Scan、Major CVE Trigger。

## 门禁

新增 Critical/High、已知被利用、高可信可达严重漏洞可进入发布阻断；禁止简单“任何 CVE 都阻断”。

## 证据

SCA 报告、Dependency Lock、例外、Remediation、Retest。

## 控制项

SEC-SUP-*、SEC-VUL-*。
