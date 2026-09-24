# MASTERDB REGISTRATION / INDEXING PACKET

**Dataset ID:** `online_retail_ii_v1`
**Prepared by:** Hariom Upadhyay | **For review/registration by:** Kavy, MASTERDB Lead
**Status:** PREPARED — pending submission through the actual MASTERDB interface

## 0. Important flags

No real MASTERDB API access was available during preparation. The metadata, computed hashes and validation results were prepared, but the dataset has **not** been represented as successfully registered in MASTERDB.

The Kaggle reference is a placeholder for integration day per the task instruction; UCI remains the authoritative provenance/licensing source.

## 1A. MASTERDB Dataset Model — Summary

| Attribute | Value |
|---|---|
| dataset_id | `online_retail_ii_v1` |
| dataset_name | Online Retail II — UK Online Retailer Transactions |
| domain | Retail / e-commerce transactions |
| owner | Hariom Upadhyay |
| custodian | Kavy, MASTERDB Lead |
| source | UCI Machine Learning Repository — Online Retail II |
| schema_id | `online_retail_ii_v1` |
| schema_version | `1.0.0` |
| provenance_id | `online_retail_ii_v1-prov-001` |
| version | `1.0.0` |
| record_count | 1,055,237 active + 12,133 duplicates removed + 1 quarantined = 1,067,371 original |
| quality_status | `GOOD_WITH_KNOWN_GAPS` |
| validation_status | `PASSED` — 12/12 automated checks |
| classification | `FIXTURE` |
| sensitivity_class | `LOW — pseudonymised` |
| licence | CC BY 4.0 |
| lifecycle_status | `PREPARED_FOR_REGISTRATION` |

## 2. Provenance

The dataset originates from the UCI Machine Learning Repository's Online Retail II dataset (Chen, D., 2012). It was combined from both source sheets, profiled and processed through a deterministic transformation pipeline.

## 3. Schema

Full field definitions and controlled vocabularies are provided in the Task 1 package under `schema/schema_notes.json`.

## 4. Validation

The prepared validation results report **12/12 checks passed**, including row accounting, transaction-type consistency, country-vocabulary coverage, StockCode normalisation, date parseability and whitespace hygiene.

## 5. Classification

The proposed classification is FIXTURE with a conservative access policy. The dataset is intended for the controlled MASTERDB training exercise, not as a production system of record.

## 6. MASTERDB Registration Result — PENDING

- [ ] Submitted to MASTERDB registration API/interface
- [ ] Registration timestamp recorded
- [ ] Assigned MASTERDB internal record ID
- [ ] Raw registration response attached

## 7. Discoverability / Search Proof — PENDING

- [ ] Search query used after registration
- [ ] Screenshot/API response showing discoverability
- [ ] Confirmation that dataset ID, classification, schema and validation status are visible

## 8. Known Limitations

1. Live MASTERDB API/runtime access was not available during preparation.
2. Kaggle is recorded as a placeholder connector source and should be re-verified against the authoritative UCI source before ingestion.
3. One quarantined write-off row requires a governance decision.
4. Statistical outliers were flagged for visibility rather than removed.
5. Task-local vocabularies should be reconciled with MDU authority before reuse beyond this dataset.