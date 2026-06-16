import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.DataFrame({
   "Name":["Arjun","Kartik","Amit","Vikrant","Ankit"],
   "Class":[10,10,11,12,10],  
   "Rollno":[101,102,103,104,105],
   "Obtained_marks":[97,76,95,79,80] 
})
fig=px.sunburst(df,path=["Class","Name"],values="Rollno",title="Student by class and roll no")
st.plotly_chart(fig)

