import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_DIR  = os.path.join(BASE_DIR, "data")
CHART_DIR = os.path.join(BASE_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(DATA_DIR, "cleaned_ads.csv"))
print("✅ Cleaned data loaded | Shape:", df.shape)
sns.set_theme(style="darkgrid")

# ── 1. AVG ROI BY CHANNEL ────────────────────────────
channel_roi = df.groupby('Channel_Used')['ROI'].mean().sort_values(ascending=False)
channel_roi.plot(kind='bar', color='steelblue', figsize=(8, 5))
plt.title("Average ROI by Channel")
plt.ylabel("ROI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "1_roi_by_channel.png"))
plt.close()
print("✅ Chart 1: ROI by Channel")

# ── 2. CONVERSION RATE BY CAMPAIGN GOAL ─────────────
goal_conv = df.groupby('Campaign_Goal')['Conversion_Rate'].mean().sort_values(ascending=False)
goal_conv.plot(kind='bar', color='coral', figsize=(8, 5))
plt.title("Avg Conversion Rate by Campaign Goal")
plt.ylabel("Conversion Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "2_conversion_by_goal.png"))
plt.close()
print("✅ Chart 2: Conversion Rate by Goal")

# ── 3. CTR BY CHANNEL ───────────────────────────────
ctr_channel = df.groupby('Channel_Used')['CTR'].mean().sort_values(ascending=False)
ctr_channel.plot(kind='bar', color='mediumseagreen', figsize=(8, 5))
plt.title("Avg CTR by Channel")
plt.ylabel("CTR (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "3_ctr_by_channel.png"))
plt.close()
print("✅ Chart 3: CTR by Channel")

# ── 4. ENGAGEMENT SCORE BY TARGET AUDIENCE ───────────
audience_eng = df.groupby('Target_Audience')['Engagement_Score'].mean().sort_values(ascending=False)
audience_eng.plot(kind='bar', color='mediumpurple', figsize=(10, 5))
plt.title("Avg Engagement Score by Target Audience")
plt.ylabel("Engagement Score (1-10)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "4_engagement_by_audience.png"))
plt.close()
print("✅ Chart 4: Engagement by Audience")

# ── 5. CTR BY DAY OF WEEK ───────────────────────────
dow_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ctr_dow = df.groupby('DayOfWeek')['CTR'].mean().reindex(dow_order)
ctr_dow.plot(kind='line', marker='o', color='tomato', figsize=(10, 5))
plt.title("Avg CTR by Day of Week")
plt.ylabel("CTR (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "5_ctr_by_day.png"))
plt.close()
print("✅ Chart 5: CTR by Day of Week")

# ── 6. ROI BY CUSTOMER SEGMENT ──────────────────────
seg_roi = df.groupby('Customer_Segment')['ROI'].mean().sort_values(ascending=False)
seg_roi.plot(kind='bar', color='goldenrod', figsize=(8, 5))
plt.title("Avg ROI by Customer Segment")
plt.ylabel("ROI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "6_roi_by_segment.png"))
plt.close()
print("✅ Chart 6: ROI by Customer Segment")

# ── 7. CLICKS VS IMPRESSIONS (sampled) ──────────────
sample = df.sample(n=500, random_state=42)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=sample, x='Impressions', y='Clicks', hue='Channel_Used')
plt.title("Clicks vs Impressions (500 sample)")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "7_clicks_vs_impressions.png"))
plt.close()
print("✅ Chart 7: Clicks vs Impressions")

# ── 8. CAMPAIGN COUNT BY CHANNEL ────────────────────
df['Channel_Used'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7))
plt.title("Campaign Share by Channel")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "8_campaign_share_by_channel.png"))
plt.close()
print("✅ Chart 8: Campaign Share by Channel")

print("\n🎉 All 8 charts saved to charts/ folder!")
