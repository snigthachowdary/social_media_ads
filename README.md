# 📊 Social Media Campaign Performance Analyzer

## Project Structure
```
social_media_project/
├── data/
│   ├── Social_Media_Advertising.csv   ← raw dataset
│   └── cleaned_ads.csv                ← generated after cleaning
├── charts/                            ← generated after EDA
├── cleaning_data.py                   ← Step 1: Run this first
├── eda.py                             ← Step 2: Run this second
└── README.md
```

## How to Run

### Step 1 — Install dependencies
```bash
pip install pandas matplotlib seaborn
```

### Step 2 — Clean the data
```bash
python cleaning_data.py
```
This generates `data/cleaned_ads.csv`

### Step 3 — Generate charts
```bash
python eda.py
```
This generates 8 charts in the `charts/` folder

## Dataset
- 300,000 social media ad campaigns
- Channels: Instagram, Facebook, Pinterest, Twitter
- Goals: Product Launch, Brand Awareness, Increase Sales, Market Expansion
- Segments: Health, Home, Technology, Food, Fashion

## Key Metrics Derived
| Metric | Formula |
|---|---|
| CTR | Clicks / Impressions * 100 |
| Clicks_per_Engagement | Clicks / Engagement_Score |

## Charts Generated
1. Average ROI by Channel
2. Conversion Rate by Campaign Goal
3. CTR by Channel
4. Engagement Score by Target Audience
5. CTR by Day of Week
6. ROI by Customer Segment
7. Clicks vs Impressions
8. Campaign Share by Channel
