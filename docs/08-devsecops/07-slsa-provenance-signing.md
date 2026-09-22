# SLSA、Provenance 与 Artifact Signing

## 目标

证明生产制品由预期源码、预期 Builder、预期 Pipeline 生成并可验证。

## Provenance

重要 Release 记录 Source Repo、Commit、Builder Identity、Build Invocation、Build Time、Artifact Digest。

## Attestation

可为 Build Provenance、SBOM、SAST、SCA、Image Scan、Policy Check 产生 Attestation。

## Ephemeral Runner

高风险构建使用临时 Runner，结束后销毁，降低跨项目残留和持久化风险。

## Artifact Signing

~~~text
Source → Trusted Builder
           ├── SBOM
           ├── Provenance
           └── Signature
                  ↓
          Verify Before Deploy
                  ↓
              Production
~~~

## Deploy Verification

验证 Digest、Signature、Provenance、Approved Registry/Repository、Security Gate。

## SLSA

参考 SLSA v1.2 的 Build/Source 思路逐步提升，不以追求标签替代实际控制。

## Metrics

Provenance、Signing、Ephemeral Runner、Verify-before-deploy Coverage 与 Untraceable Artifact Count。

## Controls

SEC-SUP-001、SEC-SUP-005、SEC-SUP-006。
