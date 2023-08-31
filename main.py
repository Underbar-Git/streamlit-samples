import streamlit as st
import pandas as pd
import numpy as np

st.title('매출을 여기서 췌-ㅋ')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.button('토스 후원'):
    link = '[Toss](https://toss.me/underbars)'
    st.markdown(link, unsafe_allow_html=True)
