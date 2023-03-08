import streamlit as st
import mysql.connector
import pandas as pd

st.sidebar.success("Database")
st.write('Press to view the existing Data!')
if st.button('Press'):
    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sakthi@123",
auth_plugin='mysql_native_password'
)
    mycursor = mydb.cursor()
    mycursor.execute("use image_db")
    mycursor.execute("SELECT * FROM Image_Processing")
    l = []
    for x in mycursor:
        l.append(x)
    df = pd.DataFrame(l, columns=['Name','Desgination','Contact_No','Mail-id','Website','Address','Image'] )
    st.write(df.to_html(escape=False), unsafe_allow_html=True)

st.write('Press, To Delete some data in existing Database')
a = st.text_input('Enter the Data Name, that you wants to delete : ')
if st.button('Delete'):
    if len(a)>0:
        st.success('Row Deleted Successfully')
    else:
        st.warning('No Row Affected')