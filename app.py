
from email.mime import image
from email.utils import collapse_rfc2231_value
import streamlit as st

# Penulisan text
st.title('Testing Streamlit')
st.header('Cara menginstall')
st.subheader('1. buka website streamlit')
st.caption('cari website resmi ya')
st.text('download dan install visual studio code, kemudian install streamlit menggunakan terminal, bisa pip atau pip3 tergantung versi masing-masing')
st.write('thats it, happy ngoding')

# Display element: st.metric()
st.metric(label="Kucing Persia",value=10,delta=2)
st.metric(label="Kucing Mainecoon",value=7,delta=-1)
st.metric(label="Kucing Kampung",value=100,delta=21,delta_color="off")

#st.columns() 
col1, col2, col3, col4  = st.columns(4)
col1.metric("Temperature","25 ºC","1.2 ºC")
col2.metric("Wind","9 kph","-8%")
col3.metric("Humidity","87%","4%")
col4.metric("Rain","1.6mm")

#Display style tanpa st.write
import pandas as pd
df = pd.DataFrame({
    'first column':[1,2,3,4,6,7],
    'second column':[10,20,30,40,60,70]
})

df

#Media element image
from PIL import Image
image=Image.open('/Users/ryryrizki/Documents/Justin Bieber Concert/Tiket Justin.png')
st.image(image,caption="receipt tiker konser JB")

#Media element sound
audio_file=open('/Users/ryryrizki/Documents/digitalent/Data/JB - Off My Face.mp3','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/wav')


#buat side bar
import streamlit as st

st.sidebar.title("Streamlit Learning")
st.sidebar.button("Module 1")
st.sidebar.radio("Module",["1","2","3"])