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

df


df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['pred_time'] = df['prediction_time'].dt.strftime("%Y-%m-%d %H")

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time']=df['request_time'].dt.strftime('%Y-%m-%d %H')

count=df.groupby('request_time').size()

plt.bar(count.index,count.values)
plt.plot(count.index,count.values,color='red',linestyle='-',marker='o')
plt.plot(count.index,count.values,color='red',linestyle='-',marker='o')
plt.xticks(rotation = 45)
plt.title("Requests by Date and Time")
plt.xlabel("Date and Time")
plt.ylabel("Number of Requests")

#화면 출력
st.pyplot(plt)
