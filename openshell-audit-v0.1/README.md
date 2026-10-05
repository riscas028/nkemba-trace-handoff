# N’KEMBA — NVIDIA OpenShell Independent Audit

## V0.1

N’KEMBA is publishing an independent, evidence-oriented audit catalogue of NVIDIA OpenShell. The purpose is not to assume that vendor claims fail; it is to separate what is **documented**, what still requires **controlled testing**, and what has actually produced an **experimental result**.

### Core audit rule

> **Policy Proof ≠ Enforcement Proof ≠ Evidence Proof.**

A documented mechanism is not automatically proof that a concrete execution behaved that way. Likewise, an internal log is not automatically proof of an external effect.

## Scope

This V0.1 freezes the classification of audit cards **#001–#284**. The detailed cards were developed sequentially and are being converted into reproducible publication artefacts.

### Current classification

| Status | Count |
|---|---:|
| DOCUMENTADO | 166 |
| TESTE_REQUERIDO | 118 |
| RESULTADO_EXPERIMENTAL | 0 |

The zero experimental-result count is intentional: no live OpenShell laboratory run has been executed and preserved as evidence in this publication yet.

## Evidence standard

Each future experimental card should preserve:

1. exact OpenShell version/commit;
2. base and effective policy;
3. provider/profile and credential context where relevant;
4. configuration/revision/load state;
5. execution identifier and nonce;
6. raw local/gateway evidence;
7. independent destination receipt where external effect is claimed;
8. hashes and timestamps;
9. reproduction instructions;
10. limitations and unresolved gaps.

## Official source basis

The current NVIDIA documentation states that provider profiles contribute provider-owned network policy to the sandbox effective policy, while the base policy remains separate; it also documents provider/profile updates and configuration synchronization. NVIDIA's current provider documentation describes unknown, malformed, expired, or unresolved credential placeholders as fail-closed rather than forwarded. citeturn0search0turn0search3

GitHub's repository-content API supports creating and modifying repository files, which is the mechanism used to stage these publication artefacts. citeturn0search1

## Publication principle

N’KEMBA will publish passes as well as failures. A finding is only escalated from **DOCUMENTADO** to **RESULTADO_EXPERIMENTAL** after the experiment and its evidence are preserved.
