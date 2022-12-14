import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('2021 서울교통공사 지하철 월별 하차 인원')

df = pd.read_csv('./monthly_subway_statistics_in_seoul.csv', encoding='CP949')
df.set_index = df['연번']

# if st.button('data copyright link'):
#     st.write('https://www.data.go.kr/data/15044247/fileData.do')