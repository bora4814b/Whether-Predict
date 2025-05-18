import streamlit as st
import pickle

st.title("Weather prediction App..")
pn=st.number_input('Enter Precipitation')
maxt=st.number_input('Enter max Temp')
mint=st.number_input('Enter mix Temp')
wind=st.number_input("ENter Win speed")
button=st.button('Predict')
if button:
    lr=pickle.load(open('wp.pkl','rb'))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"Today Weather Situatiom: {res}")