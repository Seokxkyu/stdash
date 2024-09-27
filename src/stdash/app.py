import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN Model build')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

df['request_time'] = pd.to_datetime(df['request_time'])
df['req_time'] = df['request_time'].dt.strftime("%Y-%m-%d %H")
df_req = df.groupby('req_time').count()
df_req

df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['pred_time'] = df['prediction_time'].dt.strftime("%Y-%m-%d %H")
df_pred = df.groupby('pred_time').count()
df_pred

st.header('요청 / 처리 건수(h)')
plt.bar(df_req.index, df_req['num'])
plt.plot(df_pred.index, df_pred['num'], 'ro-')
plt.title('Requests by Date and Time')
plt.xlabel('Date and Time')
plt.ylabel('Number of Requests')
plt.xticks(rotation = 45)
st.pyplot(plt)
