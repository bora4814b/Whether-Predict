import streamlit as st
import pickle 


st.title("Wheather Pridiction App")
pn=st.number_input("Enter Presipitation")
maxt=st.number_input("Enter Maximum Temprature")
mint=st.number_input("Enter Minimum Temprature")
ws=st.number_input("Enter wind speed")
button=st.button("Predict")
if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,ws]])[0]
    st.markdown(f"Today wheather situation : {res}")