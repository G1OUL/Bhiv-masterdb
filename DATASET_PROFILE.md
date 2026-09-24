# DATASET PROFILE

**Task:** MASTERDB Task 1 — Dataset Curation, Normalisation & Canonical Registration
**Candidate:** Hariom Upadhyay
**Working with:** Kavy, MASTERDB Lead
**Profile date:** 2026-09-23
**Supersedes:** an earlier dry-run of this task on a synthetic dataset (PulseFit Users). This submission uses a real, user-supplied dataset instead.

## 1. Identity

| Field | Value |
|---|---|
| Dataset ID (proposed) | `online_retail_ii_v1` |
| Dataset name | Online Retail II — UK Online Retailer Transactions |
| Description | Line-item transaction data for a UK-based, non-store online retailer selling all-occasion gift-ware, covering every invoice from 1 Dec 2009 to 9 Dec 2011. |
| Source | UCI Machine Learning Repository — "Online Retail II", donated by Dr Daqing Chen |
| Source citation | Chen, D. (2012). *Online Retail II* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D |
| Format (source) | XLSX, 2 sheets (`Year 2009-2010`, `Year 2010-2011`) |
| Format (cleaned) | CSV |

## 2. Structure

Original record count: **1,067,371** across the two source sheets.

Original fields: `Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country`, plus `source_sheet` added at combine step.

## 3. Known Quality Issues

- Exact full-row duplicates: **12,133**
- Missing Description: **4,382**
- Missing Customer ID: **243,007 (22.8%)**
- Cancellation invoices: **19,494** before duplicate removal
- Write-off/adjustment invoices: **6** before quarantine
- Ordinary numeric invoices with Quantity <= 0: **3,457**
- Price <= 0: **6,207**

## 4. Curation Summary

The cleaned/registered output contains **1,055,237 active rows**, with exact duplicates removed and one anomalous write-off row quarantined. Missing customer IDs/descriptions were not imputed.

## 5. Classification and governance

Proposed classification: **FIXTURE** with a conservative access policy because the source contains pseudonymised customer-level purchase history.

Sensitivity class: **LOW — pseudonymised**.

Licence: **CC BY 4.0**, with attribution to Chen, Daqing (2012), UCI Machine Learning Repository.

## 6. Registration Status

The data curation and validation work is prepared. Actual MASTERDB API registration and discoverability proof remain **PENDING** because live MASTERDB runtime access was not available during preparation.