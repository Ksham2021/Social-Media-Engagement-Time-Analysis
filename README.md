# Social-Media-Engagement-Time-Analysis
Analysis of social media post engagement based on posting time using Python and Gradio UI.
Social Media Engagement Time Analysis
## Project Overview:
This project analyzes social media post engagement based on posting time to identify the optimal time for posting content. Engagement is calculated using likes, comments, and shares. The analysis is visualized through graphs and an interactive UI built using Gradio in Google Colab.

## Objectives:
Analyze how posting time affects user engagement
Identify peak engagement hours
Visualize engagement trends using graphs
Provide an interactive UI for easy analysis

## Technologies Used:
Programming Language: Python
Libraries: Pandas, Matplotlib, Gradio
Platform: Google Colab (Google Studio)

## Dataset Description:
The dataset used in this project is a dummy dataset, created for academic purposes as permitted.
It simulates real-world social media engagement patterns.
Dataset file: social_media_dummy_data.csv
Dataset Columns:
post_id – Unique identifier for each post
post_time – Hour of posting (0–23)
likes – Number of likes
comments – Number of comments
shares – Number of shares
Engagement Formula:
Engagement = Likes + Comments + Shares

## Methodology:
Load the dataset using Pandas
Calculate engagement for each post
Group engagement data by posting hour
Visualize engagement trends using a line graph
Detect the peak engagement time
Display results using a Gradio-based UI

## User Interface (Gradio):
The UI is developed using Gradio within Google Colab.
It displays:
Engagement trend graph
Best time to post result
This makes the analysis interactive and easy to understand.

## How to Run the Project (Google Colab):
Open Google Colab
Upload social_media_dummy_data.csv
Install dependencies:
!pip install gradio pandas matplotlib
Run the notebook cells
Launch the Gradio interface to view the UI

## Results:
Engagement varies significantly with posting time.
The highest engagement is observed during evening hours.
Best time to post: 20:00 hours

## Conclusion:
This project demonstrates how posting time impacts social media engagement. Using Python-based data analysis and a Gradio UI, the optimal posting time is identified effectively. The approach can help content creators and marketers improve audience engagement.

## Author:
Kumari Shambhavi
(Individual Minor Project – AI/ML)

## License:
This project is created for academic purposes only.
