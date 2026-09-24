# TASK 1 — MASTERDB Dataset Curation, Normalisation & Canonical Registration

**Candidate:** Hariom Upadhyay | **Working with:** Kavy, MASTERDB Lead

This submission uses the real Online Retail II dataset supplied for Task 1.

## Current phase

```
Source → Structure → Validate → Classify → Govern → Register (prepared) → MASTERDB integration (Integration Day)
```

**Kavy's integration instruction:** Kaggle is used as the placeholder connector/source reference now. On the day of integration, the Kaggle connector will be connected to MASTERDB. UCI remains the authoritative provenance and licence-attribution source.

## Dataset

- Original records: **1,067,371**
- Cleaned active records: **1,055,237**
- Exact duplicates removed: **12,133**
- Quarantined: **1**
- Validation: **12/12 checks passed**

## Proof Gates

| Gate | Status |
|---|---|
| Proof 1 — Data Quality | Met — 12/12 automated validation checks |
| Proof 2 — Governance | Met — provenance, licence, classification and access notes documented |
| Proof 3 — MASTERDB Runtime | **Integration Day** — live connection is intentionally deferred |

No fake MASTERDB registration response or discovery screenshot is included.

## Large data files

The original and cleaned CSVs are kept in the final submission ZIP because they exceed GitHub's normal 100 MB per-file limit and therefore are not committed here.

See `TASK_1/` for the documentation, validation, transformation and integration-day artifacts.