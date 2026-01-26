import pandas as pd
import numpy as np
import re
from io import StringIO

def load_csv(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines:
        return pd.DataFrame()

    header = lines[0]
    expected_fields = len([c for c in header.split(",")])

    repaired_lines = [header]
    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split(",")


        if len(parts) > expected_fields and expected_fields >= 5:
            name = parts[0]
            age = parts[1] if len(parts) > 1 else ""
            salary = ",".join(parts[2:-2]) if len(parts) > 4 else ""

            salary = salary.replace(",", "")
            joindate = parts[-2] if len(parts) >= 2 else ""
            department = parts[-1] if len(parts) >= 1 else ""
            parts = [name, age, salary, joindate, department]

        # If too few parts, pad so downstream cleaning can handle missing values.
        if len(parts) < expected_fields:
            parts = parts + [""] * (expected_fields - len(parts))

        repaired_lines.append(",".join(parts))

    return pd.read_csv(StringIO("\n".join(repaired_lines)))

def clean_column_names(df):
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(' ', '_')
    )
    
    return df

def trim_whitespace(df):
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype("string").str.strip()
    return df

def normalize_text(df, columns):
    for col in columns:
        df[col] = df[col].astype("string").str.lower().str.title()
    return df

def clean_numeric(df, columns):
    for col in columns:
        series = df[col].astype("string").str.replace(r"[^\d.]", "", regex=True)
        df[col] = pd.to_numeric(series, errors="coerce")
    return df

def normalize_dates(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True, format="mixed")
    return df

def handle_missing(df):
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include=["object", "string"]).columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].mode(dropna=True)[0])

    return df

# -----------------------------
# 8. remove duplicates
# -----------------------------
def remove_duplicates(df):
    return df.drop_duplicates()

def clean_csv(input_file, output_file):
    df = load_csv(input_file)
    df = clean_column_names(df)
    df = trim_whitespace(df)
    df = normalize_text(df, ["name", "department"])
    df = clean_numeric(df, ["age", "salary"])
    df = normalize_dates(df, ["joindate"])
    df = handle_missing(df)
    df = remove_duplicates(df)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = "csv_data_cleaner/data.csv"
    output_file = "csv_data_cleaner/clean_data.csv"
    clean_csv(input_file, output_file)
    print("data cleaning complete. saved to clean_data.csv")