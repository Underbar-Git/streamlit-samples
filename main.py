import streamlit as st
import pandas as pd
import numpy as np

def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )
    
st.title('Pandas 차트 구현 예')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)




st.markdown("# 바코드 읽기?")
pic = st.camera_input("바코드를 촬영하시죠.")
if pic:
    
    import pyzbar.pyzbar as pyzbar
    decoded = pyzbar.decode(pic)
    st.write(decoded)



redirect_button("https://toss.me/underbars","여기를 눌러 송금을..")
