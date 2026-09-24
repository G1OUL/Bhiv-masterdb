# MASTERDB Task 1

This folder contains the review-ready Task 1 metadata and validation artifacts for the Online Retail II curation exercise.

## Dataset
- Dataset ID: `online_retail_ii_v1`
- Source: UCI Machine Learning Repository — Online Retail II
- Original records: 1,067,371
- Cleaned active records: 1,055,237
- Exact duplicates removed: 12,133
- Rows quarantined: 1
- Validation: 12/12 checks passed

## Pipeline
The intended reproducible pipeline is:
`transformation/cleaning_pipeline.py`

## Registration
MASTERDB runtime registration and discoverability proof remain pending because live MASTERDB API/runtime access was not available during preparation.

## Large data files
The raw and cleaned CSVs are intentionally not committed to this repository because they are above GitHub's normal 100 MB per-file limit.