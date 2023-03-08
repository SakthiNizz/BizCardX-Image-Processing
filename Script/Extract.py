import streamlit as st
import matplotlib.pyplot as plt
import cv2
import easyocr
import pylab
from IPython.display import Image
plt.rcParams['figure.figsize'] = 8,16
reader = easyocr.Reader(['en'])
def extract(img):
    st.spinner('Loading...')
    output = reader.readtext(img)
    l = []
    for i in range(len(output)):
        l.append(output[i][1])
    name=[]
    n=[]
    m=[]
    w=[]
    a=[]
    b=[]
    for i in range(len(l)):
        if i == 0 or i==len(l)-1:
            name.append(l[i])
        elif i == 1:
            des = l[i]
        elif '-' in l[i]:
            n.append(l[i])
        elif '@' in l[i]:
            m.append(l[i])
        elif '.com' in l[i]:
            w.append(l[i])
        else:
            a.append(l[i])
    st.write('Extracted Infromation from the uploaded Image : \n')  
    st.write('Name : ',*name)
    st.write('Designation : ',des)
    st.write('Contact Number : ',*n)
    st.write("Mail-id : ",*m)
    st.write('Website-URL : ', *w)
    b = [x.lower() for x in name]
    for i in a[:]:
        if i in b:
            a.remove(i)
    st.write('Address : ',*a)