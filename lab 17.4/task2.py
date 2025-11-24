import sys
import pandas as pd
"""
Preprocess sales transaction dataset.
- Reads 'sales_transaction_dataset_proper.csv' from the current directory.
- Converts transaction date to datetime.
- Creates 'Month-Year' column.
- Removes rows with non-positive or missing transaction amounts.
- Adds Min-Max normalized column 'transaction_amount_normalized'.
- Writes cleaned output to 'sales_transaction_dataset_proper_preprocessed.csv'.
"""
INPUT_FILE = "sales_transactions.csv"
OUTPUT_FILE = "sales_transaction_dataset_proper_preprocessed.csv"
# Helper to find a candidate column name (case-insensitive)
def find_column(df, candidates):
    lower_map = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    return None
def main():
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"Input file not found: {INPUT_FILE}", file=sys.stderr)
        sys.exit(1)
    # Detect columns (common names)
    date_col = find_column(df, ["transaction_date", "date", "transaction date", "Transaction_Date"])
    amount_col = find_column(df, ["transaction_amount", "amount", "transaction amount", "amount_usd"])
    if date_col is None:
        print("Could not find a date column. Expected names like 'transaction_date' or 'date'.", file=sys.stderr)
        sys.exit(1)
    if amount_col is None:
        print("Could not find an amount column. Expected names like 'transaction_amount' or 'amount'.", file=sys.stderr)
        sys.exit(1)
    # Convert date column to datetime, drop invalid dates
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", infer_datetime_format=True)
    before = len(df)
    df = df.dropna(subset=[date_col])
    dropped_dates = before - len(df)
    # Create Month-Year column (e.g., "Jan-2020")
    df["Month-Year"] = df[date_col].dt.strftime("%b-%Y")
    # Ensure amount is numeric, drop rows with NaN
    df[amount_col] = pd.to_numeric(df[amount_col], errors="coerce")
    before = len(df)
    df = df.dropna(subset=[amount_col])
    dropped_non_numeric = before - len(df)
    # Remove rows with non-positive amounts
    before = len(df)
    df = df[df[amount_col] > 0]
    dropped_non_positive = before - len(df)
    # Min-Max normalize the transaction amount into a new column
    min_val = df[amount_col].min()
    max_val = df[amount_col].max()
    if pd.isna(min_val) or pd.isna(max_val):
        print("No valid transaction amounts to normalize.", file=sys.stderr)
        sys.exit(1)
    if max_val == min_val:
        # All values identical -> normalized to 0.0
        df["transaction_amount_normalized"] = 0.0
    else:
        df["transaction_amount_normalized"] = (df[amount_col] - min_val) / (max_val - min_val)

    # Save result
    df.to_csv(OUTPUT_FILE, index=False)

    # Summary
    print(f"Input rows: {len(pd.read_csv(INPUT_FILE))}")
    print(f"Dropped invalid dates: {dropped_dates}")
    print(f"Dropped non-numeric amounts: {dropped_non_numeric}")
    print(f"Dropped non-positive amounts: {dropped_non_positive}")
    print(f"Output rows: {len(df)}")
    print(f"Preprocessed data written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()