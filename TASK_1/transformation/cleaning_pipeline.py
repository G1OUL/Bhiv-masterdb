"""MASTERDB Task 1 — deterministic cleaning/validation pipeline.

The original pipeline reads dataset_original.csv, removes exact duplicates,
quarantines the write-off sign anomaly, normalises StockCode/Country,
derives transaction_type, writes dataset_cleaned.csv and validation evidence.
The full executable pipeline is retained in the original Task 1 submission
bundle; this repository copy documents the intended entry point.
"""

PIPELINE_ENTRY_POINT = "python3 transformation/cleaning_pipeline.py"

TRANSACTION_TYPES = (
    "SALE",
    "CANCELLATION",
    "WRITE_OFF_ADJUSTMENT",
    "NON_MERCHANDISE",
    "STOCK_ADJUSTMENT",
)

EXPECTED_VALIDATION_CHECKS = 12
