# Sources and evidence

## Source register

Record:

`source_id, title, publisher, url_or_file, published_date, accessed_date, source_type, primary_status, geography, time_scope, method, limitations`

Useful types include official product page, pricing page, documentation, regulatory filing, dataset, research paper, reputable reporting, user review, interview, survey response, and analyst synthesis.

## Source assessment

Assess sources dimension by dimension rather than assigning a mysterious numeric score:

- proximity to the underlying event or data;
- identifiable publisher and author;
- explicit date and version;
- transparent method and sample;
- direct support for the exact claim;
- relevant geography, segment, tier, and period;
- independence from commercial incentives;
- corroboration by independent evidence.

Use `HIGH` confidence only when evidence directly supports the claim, fits scope, is sufficiently current, and has no unresolved material contradiction. `MEDIUM` indicates useful but limited evidence. `LOW` indicates directional or weakly verified evidence.

## Evidence types

- `FACT`: directly stated or observed information that can be checked.
- `USER_SIGNAL`: an expressed experience, preference, complaint, or behavior from an identified research unit.
- `INFERENCE`: an analyst conclusion derived from one or more facts or user signals.
- `UNKNOWN`: an important question the available evidence cannot answer.

Do not convert a company statement about itself into an independently verified fact. Describe it as an official claim when relevant.

## Atomic claims

One ledger row should express one checkable proposition. Split claims joined by “and” when different evidence could support each half. Store the shortest sufficient quotation or exact data point; keep full context accessible through the source ID.

## Conflicts

Capture the precise disagreement, dates, definitions, markets, product tiers and samples; whether it is reconcilable; which source is more applicable and why; and the remaining uncertainty. Never average incompatible figures merely to create one number.

## Citation coverage

A material claim could change the recommendation, risk assessment, or user understanding. Every material `FACT`, and every recommendation's factual premise, needs traceable support. An `INFERENCE` should cite its input claim IDs rather than pretending to have an external source of its own.

