# CSV Data Cleaner (Python)

A small, production-style Python utility that **repairs and cleans messy CSV files** into an analysis-ready dataset using **Pandas** (schema normalization, numeric/date parsing, missing-value handling, and de-duplication).

## Why it matters
Real-world CSVs often contain:
- inconsistent casing/whitespace
- malformed rows (extra commas inside numeric fields)
- mixed date formats
- missing values and duplicates

This project demonstrates building a **defensive cleaning pipeline** that converts unreliable inputs into a consistent output.

## What it does
Implemented in `clean_csv` within `csv_data_cleaner/cleaner.py`:

1. **Loads + repairs rows** with unexpected comma splits via `load_csv`.  
2. Normalizes headers via `clean_column_names`.
3. Trims whitespace via `trim_whitespace`
4. Normalizes text fields via `normalize_text`.
5. Cleans numeric columns via `clean_numeric`.
6. Parses mixed date formats via `normalize_dates`.
7. Fills missing values via `handle_missing`.
8. Removes duplicates via `remove_duplicates`.
9. Writes cleaned output to CSV

## Input / Output
- **Input:** `csv_data_cleaner/data.csv`
- **Output:** `csv_data_cleaner/clean_data.csv`

Expected output columns (after cleaning):
- `name` (Title Case)
- `age` (numeric)
- `salary` (numeric; currency/commas removed)
- `joindate` (parsed date)
- `department` (Title Case)

## Quick start
### Requirements
- `pandas`, `numpy`

### Run
```bash
python csv_data_cleaner/cleaner.py
```


## Project structure
```text
csv_data_cleaner/
  cleaner.py        # cleaning pipeline
  data.csv          # sample messy input
  clean_data.csv    # cleaned output 
  README.md
```

## Notable implementation details
- **Row repair for malformed CSV lines:** [`load_csv`](csv_data_cleaner/cleaner.py) attempts to reconstruct rows when the number of comma-separated fields exceeds the header width (common when numeric values contain commas).
- **Type-safe conversions:** numeric parsing uses `to_numeric(..., errors="coerce")` in [`clean_numeric`](csv_data_cleaner/cleaner.py); date parsing uses tolerant conversion in [`normalize_dates`](csv_data_cleaner/cleaner.py).
- **Missing-value strategy:** numeric columns filled with median; text columns filled with mode in [`handle_missing`](csv_data_cleaner/cleaner.py).

## Learning outcomes

- Building a defensive ETL-style pipeline: load/repair → normalize → validate → export
- Cleaning messy real-world data with Pandas (types, missing values, duplicates)
- Writing resilient parsers that handle malformed rows without crashing
- Designing reusable, testable helper functions for each cleaning stage

## Reasonable next improvements
- Add a CLI (`--input`, `--output`) instead of hardcoded paths in [csv_data_cleaner/cleaner.py](csv_data_cleaner/cleaner.py)
- Add unit tests for parsing/repair edge cases (extra commas, missing columns, mixed date formats)
- Add schema validation + configurable cleaning rules (YAML/JSON)
- Emit a cleaning report (rows repaired, values coerced, missing filled, duplicates removed)
