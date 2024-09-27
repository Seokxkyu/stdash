import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Model Statistics", page_icon="📈")

st.title('Model Statistics')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

df['request_time'] = pd.to_datetime(df['request_time'])
df['req_time'] = df['request_time'].dt.strftime("%Y-%m-%d %H")

df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['pred_time'] = df['prediction_time'].dt.strftime("%Y-%m-%d %H")

model_stats = df.groupby(['request_user', 'prediction_model']).agg({
    'prediction_time': ['mean', 'max', 'min', 'count']
}).reset_index()

model_stats.columns = ['request_user', 'prediction_model', 'avg_prediction_time', 'max_prediction_time', 'min_prediction_time', 'request_count']

model_stats

st.header('요청 별 활용 모델 통계')
plt.figure(figsize=(12,8))
ax = model_stats.pivot(index='request_user', columns='prediction_model', values='request_count').plot(kind='barh', stacked=True)
plt.title('Number of Requests per User and Model')
plt.ylabel('Request Count')
ax.legend(title='Prediction Model', prop={'size': 8})
st.pyplot(plt)
