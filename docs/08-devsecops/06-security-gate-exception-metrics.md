# Security Gate、例外与度量

## Gate Pipeline

~~~text
Commit → Review → Secret → SAST → SCA → Test
→ Build → Artifact/Image Scan → Gate → Release → Production
~~~

## Block Conditions

高可信 Secret、新增 Critical、已确认严重 SAST、已被利用高风险依赖、制品不可追溯、关键测试失败。

## Exception

记录 Finding/Control、Business Reason、Risk、Compensating Control、Owner、Reviewer、Approver、Expiry、Fix Plan。禁止永久例外。

## False Positive / Retest

误报必须有技术证据；修复后通过相应扫描或人工验证复测再关闭。

## Metrics

Coverage、Critical/High、Overdue、MTTR、Gate Block、Bypass、Exception、False Positive、SBOM/Provenance Coverage。

## Controls

SEC-SUP-*、SEC-VUL-*、SEC-GOV-002。
