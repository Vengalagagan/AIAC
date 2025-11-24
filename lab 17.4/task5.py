import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv("financial_data.csv")

# missing values
df["stock_price"] = df["stock_price"].fillna(df["stock_price"].mean())
df["volume"] = df["volume"].fillna(df["volume"].mean())

# date conversion
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# feature engineering
df["ma_7"] = df["stock_price"].rolling(7).mean()
df["ma_30"] = df["stock_price"].rolling(30).mean()

# encoding
enc_sector = LabelEncoder()
df["sector_enc"] = enc_sector.fit_transform(df["sector"])

enc_company = LabelEncoder()
df["company_enc"] = enc_company.fit_transform(df["company_name"])

# normalization
scaler = StandardScaler()
df[["stock_price_norm","volume_norm"]] = scaler.fit_transform(df[["stock_price","volume"]])

print(df.head())
