---
name: evidenceflow-research
description: Plan and conduct evidence-grounded market, competitor, product, and voice-of-customer research. Use when a user needs traceable findings, source comparison, claim verification, a competitor matrix, user-feedback synthesis, or a decision-ready research memo. Do not use for investment, medical, or legal decisions without explicit risk framing and independent verification.
---

# EvidenceFlow Research

Turn an ambiguous business question and a bounded source set into traceable evidence and a decision-ready memo. Optimize for auditability, not report length.

## Core contract

- Preserve the user's decision, audience, market, time horizon, and constraints.
- Separate `FACT`, `USER_SIGNAL`, `INFERENCE`, and `UNKNOWN` throughout the work.
- Every material fact or recommendation must trace to evidence. Never invent a citation, interview, sample size, metric, or source date.
- Prefer primary and current sources for product capabilities, pricing, policies, and company claims. Treat company claims as claims, not independent proof.
- Report contradictory and missing evidence instead of silently resolving it.
- AI personas may generate hypotheses or interview questions only. Never present simulated responses as real user research.
- For high-impact financial, medical, legal, safety, or regulatory claims, require independent verification and keep final judgment with a qualified human.

## Select a mode

Choose the lightest mode that answers the user's decision:

| Mode | Use when | Main output |
|---|---|---|
| `quick-scan` | Directional understanding is enough | One-page evidence brief |
| `competitive-study` | Comparing products, positioning, pricing, or opportunities | Evidence ledger + competitor matrix + decision memo |
| `voice-of-customer` | Analyzing reviews, interviews, survey text, or support logs | Codebook + themes + segment differences + implications |

If the request mixes modes, choose one primary mode and attach only the necessary secondary analysis.

## Workflow

### 1. Frame the decision

Before collecting evidence, establish the decision, decision-maker, audience, market, users, time window, comparison set, available sources, constraints, deliverable, deadline, and non-goals.

Ask only for missing information that would materially change the design. For a substantial study, draft a short plan and obtain confirmation before deep collection. Read [research-planning.md](references/research-planning.md) for scoping, sampling, and stopping rules.

### 2. Build a source register

Create a source register before synthesis. Record URL or file, publisher, title, date, access date, source type, primary/secondary status, scope, and limitations. Use [source-and-evidence.md](references/source-and-evidence.md) for assessment and conflict handling.

Do not collapse all sources into a single undifferentiated context. Preserve enough metadata to reopen and verify each item.

### 3. Extract an evidence ledger

Extract atomic claims rather than prose summaries. Each row must contain:

`claim_id, claim_text, evidence_excerpt_or_data, source_id, evidence_type, scope, confidence, verification_status, analyst_note`

Controlled values:

- `evidence_type`: `FACT`, `USER_SIGNAL`, `INFERENCE`, `UNKNOWN`
- `confidence`: `HIGH`, `MEDIUM`, `LOW`
- `verification_status`: `VERIFIED`, `PARTIAL`, `CONFLICT`, `UNVERIFIED`

Keep quoted text short and distinguish quotations from paraphrases. A claim may require multiple evidence rows.

### 4. Analyze for the selected mode

- For competitor work, compare only dimensions that affect the decision. Do not treat an undocumented feature as absent; mark it `UNKNOWN`.
- For voice-of-customer work, preserve the unit of analysis, create a codebook, retain representative IDs, and distinguish frequency from importance.
- Recommendations must state the evidence used, the inference made, and the condition under which the recommendation could change.

Read [competitive-and-voc.md](references/competitive-and-voc.md) for matrices, positioning analysis, review synthesis, interviews, or open-text coding.

### 5. Run a contradiction and gap pass

Before writing conclusions:

1. group claims about the same subject;
2. flag incompatible values or definitions;
3. check whether dates, geographies, editions, tiers, or samples explain the difference;
4. prefer neither source solely because it appears first or sounds authoritative;
5. list unresolved gaps and the next evidence needed.

### 6. Draft the decision memo

Use this structure unless the user requests another format:

1. Decision and scope
2. Executive summary
3. Findings and supporting evidence
4. Comparison or user themes
5. Opportunities and recommendations
6. Risks, uncertainty, and alternative explanations
7. Open questions and next research
8. Sources and method note

Read [deliverables.md](references/deliverables.md) for field-level templates and claim-to-recommendation rules.

### 7. Quality gate

Check factual support, citation correctness and coverage, fact/inference separation, conflict disclosure, scope consistency, missing critical evidence, recommendation proportionality, and clarity. Read [evaluation.md](references/evaluation.md) for the rubric. When an evidence CSV is available, run `scripts/validate_evidence.py` and resolve structural errors before delivery.

## Human-review gates

Require explicit human review when:

- evidence materially conflicts;
- a recommendation could cause financial, legal, medical, safety, privacy, or reputational harm;
- a source cannot be accessed directly;
- the conclusion depends on a small or biased sample;
- the model is asked to infer intent, causality, or population prevalence from qualitative data;
- an important claim remains `UNVERIFIED` or `UNKNOWN`.

## Output discipline

- Lead with the decision-relevant conclusion, then show evidence and uncertainty.
- Use exact dates, markets, product tiers, sample sizes, and denominators when available.
- Label directional findings as directional.
- Do not turn convenience-sample counts into population estimates.
- Specify what new evidence could change the decision rather than generically requesting more data.
- Keep a compact method note so another researcher can reproduce the result.

## Included resources

- [research-planning.md](references/research-planning.md): scope, questions, sampling, and stopping rules.
- [source-and-evidence.md](references/source-and-evidence.md): source register, evidence, confidence, and conflicts.
- [competitive-and-voc.md](references/competitive-and-voc.md): competitor comparison and qualitative coding.
- [deliverables.md](references/deliverables.md): output schemas and memo construction.
- [evaluation.md](references/evaluation.md): quality rubric and failure tests.
- `assets/`: editable brief, ledger, matrix, codebook, and memo templates.
