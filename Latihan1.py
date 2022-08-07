from sre_constants import SUCCESS
import streamlit as st

#1 create widget
import time
st.balloons()
st.progress(100)
with st.spinner("Loading"): time.sleep(2)

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build app with streamlit")
st.exception(RuntimeError("RuntimeError exception"))

#2 create sidebar 
st.sidebar.title("Streamlit Learning")
st.sidebar.button("Module 1")
st.sidebar.radio("Module",["1","2","3"])

#3 widgte
st.checkbox('yes')
st.button("click")
st.radio("Gender",["Male","Female"])
st.selectbox("Gender",["Male","Female"])
st.multiselect("Gender",["Male","Female","Other"])
st.select_slider("Gender",["Male","Female","Other"])
st.slider('Number',0,50)

#6 formula math
st.markdown("markdown")
st.code("x=2022")
st.latex(r'''a+a r^1+a r^2+a r^3 ''') # untuk nulis persamaan


#9 line chart
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(10,2),
    columns=["x","y"])
st.line_chart(df)

#12 area chart
df=pd.DataFrame(
    np.random.randn(10,2),
    columns=["x","y"])
st.area_chart(df)

#13 Map
df=pd.DataFrame(np.random.randn(500,2)/[50,50]+[37.76, -122.4],
columns=['lat','lon'])
st.map(df)
