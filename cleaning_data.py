import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load raw data
df = pd.read_csv(os.path.join(DATA_DIR, "Social_Media_Advertising.csv"))
print("✅ Raw data loaded | Shape:", df.shape)

# ── DROP USELESS COLUMNS ─────────────────────────────
# Duration is always "15 Days" — no variation, useless
# Acquisition_Cost is always $500 — no variation, useless
df.drop(columns=['Duration', 'Acquisition_Cost'], inplace=True)

# ── FIX DATE ─────────────────────────────────────────
df['Date'] = pd.to_datetime(df['Date'])
df['Month']      = df['Date'].dt.month_name()
df['Year']       = df['Date'].dt.year
df['DayOfWeek']  = df['Date'].dt.day_name()

# ── DERIVE MEANINGFUL METRICS ─────────────────────────
# CTR: how compelling is the ad?
df['CTR'] = (df['Clicks'] / df['Impressions']) * 100

# Clicks per Engagement point: efficiency of engagement
df['Clicks_per_Engagement'] = df['Clicks'] / df['Engagement_Score']

# ── SAVE CLEANED DATA ─────────────────────────────────
df.to_csv(os.path.join(DATA_DIR, "cleaned_ads.csv"), index=False)
print("✅ Cleaned data saved!")
print("   Shape:", df.shape)
print("   Columns:", df.columns.tolist())
