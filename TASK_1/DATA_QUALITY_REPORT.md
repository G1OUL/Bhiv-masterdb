# DATA QUALITY & TRANSFORMATION REPORT

Dataset: `online_retail_ii_v1`

| Metric | Value |
|---|---:|
| Records before | 1,067,371 |
| Exact duplicates removed | 12,133 |
| Records quarantined | 1 |
| Records after | 1,055,237 |
| Validation checks | 12 |
| Validation passed | 12/12 |
| Quantity outliers flagged | 73 |
| Price outliers flagged | 249 |

## Key transformations

1. Exact full-row duplicates were removed mechanically and retained as evidence.
2. Missing Description and Customer ID values were preserved rather than imputed.
3. One inconsistent write-off row was quarantined rather than guessed or silently corrected.
4. A governed `transaction_type` field was derived with five values: SALE, CANCELLATION, WRITE_OFF_ADJUSTMENT, NON_MERCHANDISE, STOCK_ADJUSTMENT.
5. StockCode values were normalised to uppercase while retaining the source value.
6. Country values were normalised to ISO alpha-2 codes or explicit governed non-country tags.
7. Row-level quality status and deterministic validation were applied.

Row accounting reconciles exactly:
`1,067,371 = 1,055,237 + 12,133 + 1`.

See the full submission bundle for the complete pipeline outputs and evidence.