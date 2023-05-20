import streamlit as st
view = [100, 150, 30]
st.write('# 계절학기 교과목 추천')
st.write('## 수강 가능 교과목')
view
st.write('## 수강 후기')
st.bar_chart(view)
import pandas as pd
st.write('## 교과목 세부 정보')
sview = pd.Series(view)
sview
