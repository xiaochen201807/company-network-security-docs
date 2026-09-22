# Dependency 与 SCA Standard

## Dependency Source

依赖优先通过公司批准仓库或代理获取。新增第三方仓库评估来源、Owner 和范围。

## SCA

输出至少包含 Component、Version、CVE、CVSS、Direct/Transitive、Fixed Version、License、Project、Owner。

## Risk

CVSS 结合公网暴露、代码可达性、Exploit、KEV/真实攻击、资产重要性、数据和补偿控制。

## Scan Timing

PR/MR、Main、Release、Periodic Full Scan、Major CVE Trigger。

## Gate

新增 Critical/High、已知被利用、高可信可达严重漏洞可进入发布阻断；禁止简单“任何 CVE 都阻断”。

## Evidence

SCA Report、Dependency Lock、Exception、Remediation、Retest。

## Controls

SEC-SUP-*、SEC-VUL-*。
