# EvidenceFlow Research

EvidenceFlow is an evidence-grounded research skill for competitive analysis, market research, product discovery, and voice-of-customer synthesis. It turns research questions and source material into an auditable evidence ledger, structured comparison, and decision-ready memo.

## Why it exists

Many AI research workflows produce fluent reports while hiding weak citations, mixed scopes, unsupported inference, and contradictory evidence. EvidenceFlow separates facts, user signals, inferences, and unknowns; preserves claim-level source links; and applies an explicit quality gate.

## Core capabilities

- Research planning and scope confirmation
- Source register and claim-level evidence ledger
- Competitor matrices with `UNKNOWN` rather than assumed absence
- Voice-of-customer coding with sample and denominator discipline
- Contradiction and evidence-gap handling
- Evidence-linked decision memos
- LLM output evaluation and human-review gates
- Reusable CSV and Markdown templates

## Validation

```bash
python scripts/validate_evidence.py examples/ai-meeting-tools/evidence-ledger.csv
```

## Design provenance

The session-oriented planning and artifact workflow was informed by a prior-art review of [atypica-research-skill](https://github.com/atypica-ai/atypica-research-skill). EvidenceFlow is an independent implementation and does not use Atypica's API, private research engine, persona database, prompts, branding, or generated reports. Its original focus is claim-level traceability, source assessment, contradiction handling, qualitative research integrity, and LLM quality evaluation.

## Limitations

EvidenceFlow improves research structure; it does not guarantee that accessible sources are true, current, representative, or independent. High-impact claims and decisions require qualified human verification.

## License

MIT. See `LICENSE`.

