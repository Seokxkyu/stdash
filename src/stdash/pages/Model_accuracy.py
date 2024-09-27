import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Model Accuracy Statistics", page_icon="📈")

st.title('Model Accuracy Statistics')

def load_data():
    url = 'http://43.202.66.118:8077/all'  # Replace with your API URL
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

df['request_time'] = pd.to_datetime(df['request_time'])
df['prediction_time'] = pd.to_datetime(df['prediction_time'])

df['correct'] = df['label'] == df['prediction_result']

accuracy_stats = df.groupby(['request_user', 'prediction_model']).agg(
    total_predictions=('correct', 'size'),
    correct_predictions=('correct', 'sum')
)

accuracy_stats['accuracy'] = accuracy_stats['correct_predictions'] / accuracy_stats['total_predictions']
accuracy_stats = accuracy_stats.reset_index()

st.dataframe(accuracy_stats)

st.header('Accuracy per User and Model')

plt.figure(figsize=(12, 8))
pivot_table = accuracy_stats.pivot(index='request_user', columns='prediction_model', values='accuracy')
ax = pivot_table.plot(kind='barh', stacked=True, figsize=(12, 8))

plt.title('Accuracy per User and Model')
plt.xlabel('Accuracy')
plt.ylabel('Request User')

st.pyplot(plt)
