import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Set up the Streamlit app configuration
st.set_page_config(page_title="Model Accuracy Statistics", page_icon="📈")

# Title of the app
st.title('Model Accuracy Statistics')

# Function to load the data from the API
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

accuracy_stats = df.groupby('prediction_model').agg(
    total_predictions=('correct', 'size'),
    correct_predictions=('correct', 'sum')
)

accuracy_stats['accuracy'] = accuracy_stats['correct_predictions'] / accuracy_stats['total_predictions']
accuracy_stats = accuracy_stats.reset_index()

st.dataframe(accuracy_stats)

st.header('Accuracy per Model')

plt.figure(figsize=(12, 8))
ax = accuracy_stats.plot(kind='bar', x='prediction_model', y='accuracy', legend=False, figsize=(12, 8))

plt.title('Model Accuracy')
plt.xlabel('Prediction Model')
plt.ylabel('Accuracy')
plt.xticks(rotation=45)

st.pyplot(plt)
