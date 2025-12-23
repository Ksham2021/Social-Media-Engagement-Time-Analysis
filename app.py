import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Social Media Engagement Time Analysis")

df = pd.read_csv("social_media_dummy_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

df["engagement"] = df["likes"] + df["comments"] + df["shares"]
hourly_engagement = df.groupby("post_time")["engagement"].mean()

st.subheader("Engagement vs Posting Time")
fig, ax = plt.subplots()
ax.plot(hourly_engagement.index, hourly_engagement.values)
ax.set_xlabel("Posting Time (Hour)")
ax.set_ylabel("Average Engagement")
ax.set_title("Engagement Trend")
st.pyplot(fig)

best_time = hourly_engagement.idxmax()
st.success(f"Best time to post is {best_time}:00 hours")
