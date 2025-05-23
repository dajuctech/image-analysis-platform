import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Load metadata
METADATA_CSV = "data/metadata.csv"
LOG_DIR = "logs/"

st.set_page_config(layout="wide")
st.title("📈 Image Processing BI Dashboard")

# Section 1: Metadata Overview
st.header("🧾 Uploaded Image Metadata")
if os.path.exists(METADATA_CSV):
    df = pd.read_csv(METADATA_CSV)
    st.dataframe(df.tail(10))

    st.subheader("Image Class Distribution")
    if 'predicted_class' in df.columns:
        st.bar_chart(df['predicted_class'].value_counts())
    else:
        st.info("No 'predicted_class' column found. Please ensure prediction is logged to metadata.")
else:
    st.warning("Metadata file not found!")

# Section 2: Upload Trend Analysis
st.header("📅 Upload Activity Trends")
timestamps = []

for log_file in os.listdir(LOG_DIR):
    if log_file.endswith(".log"):
        with open(os.path.join(LOG_DIR, log_file)) as f:
            for line in f:
                if "Uploaded file" in line:
                    try:
                        ts = line.split(" - ")[0]
                        timestamps.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S,%f"))
                    except Exception:
                        continue

if timestamps:
    df_time = pd.DataFrame(timestamps, columns=["timestamp"])
    df_time["date"] = df_time["timestamp"].dt.date
    counts = df_time["date"].value_counts().sort_index()
    st.line_chart(counts)
else:
    st.info("No upload timestamps found in logs.")

# Section 3: Brightness Trends (if available)
st.header("💡 Image Brightness Insights")
if os.path.exists(METADATA_CSV):
    df = pd.read_csv(METADATA_CSV)
    if 'brightness' in df.columns:
        st.line_chart(df['brightness'].rolling(10).mean())
    else:
        st.warning("Brightness column not found in metadata.")
