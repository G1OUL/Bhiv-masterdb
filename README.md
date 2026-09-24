# TASK 1 — MASTERDB Dataset Curation, Normalisation & Canonical Registration

**Candidate:** Hariom Upadhyay | **Working with:** Kavy, MASTERDB Lead

This submission uses a real, user-supplied dataset (`online_retail_II.xlsx`) and supersedes an earlier dry-run of this task performed on a synthetic dataset (PulseFit Users) before this file was provided.

## What this is

```
Source → Structure → Validate → Classify → Govern → Register (prepared) → Index (pending)
```

## Dataset chosen

**Online Retail II** — real (not synthetic) invoice line-item transactions from a UK-based online gift-ware retailer, 1 Dec 2009 – 9 Dec 2011. 1,067,371 source rows across two sheets, combined into one logical dataset; **1,055,237 rows in the registered/cleaned output** after removing 12,133 exact duplicates and quarantining 1 anomalous row.

## How to reproduce everything

```bash
cd TASK_1/
python3 transformation/cleaning_pipeline.py
```

## Where to look

| What | Where |
|---|---|
| Dataset identity, source, classification, known issues | `DATASET_PROFILE.md` |
| Every quality issue found, rule applied, and validated | `DATA_QUALITY_REPORT.md` |
| MASTERDB Dataset Model mapping and registration status | `MASTERDB_REGISTRATION_PACKET.md` |
| Raw combined source file | `dataset_original.csv` |
| Cleaned, governed output | `dataset_cleaned.csv` |
| Deterministic cleaning/validation code | `transformation/cleaning_pipeline.py` |
| Schema + controlled vocabularies | `schema/schema_notes.json` |
| Automated validation results | `validation/validation_results.json` |
| Before/after statistics and evidence | `evidence/before_after_statistics/` |

## Proof Gates

| Gate | Status |
|---|---|
| **Proof 1 — Data Quality** | Met — 12/12 automated validation checks |
| **Proof 2 — Governance** | Met — owner, custodian, provenance, licence and classification documented |
| **Proof 3 — MASTERDB Runtime** | Pending — requires access to the real MASTERDB API/interface |

The final MASTERDB registration and discoverability steps are explicitly marked pending rather than fabricated.

## Submission bundle

The complete Task 1 package is included as `TASK_1.zip`.