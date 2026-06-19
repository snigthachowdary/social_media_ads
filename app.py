import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Social Media Ads Analytics", layout="wide")

df = pd.read_csv("data/cleaned_ads.csv")

st.title("📊 Social Media Advertising Analytics Dashboard")

# Filters
st.sidebar.header("Filters")

channel = st.sidebar.multiselect(
    "Select Channel",
    options=df["Channel_Used"].unique(),
    default=df["Channel_Used"].unique()
)

goal = st.sidebar.multiselect(
    "Select Campaign Goal",
    options=df["Campaign_Goal"].unique(),
    default=df["Campaign_Goal"].unique()
)

audience = st.sidebar.multiselect(
    "Select Target Audience",
    options=df["Target_Audience"].unique(),
    default=df["Target_Audience"].unique()
)

filtered_df = df[
    (df["Channel_Used"].isin(channel)) &
    (df["Campaign_Goal"].isin(goal)) &
    (df["Target_Audience"].isin(audience))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Campaigns", len(filtered_df))
col2.metric("Avg ROI", round(filtered_df["ROI"].mean(), 2))
col3.metric("Avg CTR", f"{round(filtered_df['CTR'].mean(), 2)}%")
col4.metric("Avg Conversion Rate", round(filtered_df["Conversion_Rate"].mean(), 4))

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    roi_channel = filtered_df.groupby("Channel_Used")["ROI"].mean().reset_index()
    fig = px.bar(
        roi_channel,
        x="Channel_Used",
        y="ROI",
        title="Average ROI by Channel"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    ctr_channel = filtered_df.groupby("Channel_Used")["CTR"].mean().reset_index()
    fig = px.bar(
        ctr_channel,
        x="Channel_Used",
        y="CTR",
        title="Average CTR by Channel"
    )
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    conv_goal = filtered_df.groupby("Campaign_Goal")["Conversion_Rate"].mean().reset_index()
    fig = px.bar(
        conv_goal,
        x="Campaign_Goal",
        y="Conversion_Rate",
        title="Average Conversion Rate by Campaign Goal"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    audience_eng = filtered_df.groupby("Target_Audience")["Engagement_Score"].mean().reset_index()
    fig = px.bar(
        audience_eng,
        x="Target_Audience",
        y="Engagement_Score",
        title="Average Engagement Score by Audience"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Day of week chart
dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ctr_day = filtered_df.groupby("DayOfWeek")["CTR"].mean().reindex(dow_order).reset_index()

fig = px.line(
    ctr_day,
    x="DayOfWeek",
    y="CTR",
    markers=True,
    title="Average CTR by Day of Week"
)

st.plotly_chart(fig, use_container_width=True)

# Data Preview
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(100), use_container_width=True)