import mysql.connector
import streamlit as st
import cv2
import easyocr
import pylab
from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 8,16
reader = easyocr.Reader(['en'])

def load_image(image_file):
    img = Image.open(image_file)
    return img

def insert(img):
    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sakthi@123",
  auth_plugin='mysql_native_password'
  )
    mycursor = mydb.cursor()
    mycursor.execute("use image_db")
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
    A = ' '.join(name)
    B = ' '.join(n)
    C = ' '.join(m)
    D = ' '.join(w)
    E = ' '.join(a)
    F = load_image(img)
    mycursor.execute(f"INSERT INTO Image_Processing VALUES ('{A}','{des}','{B}','{C}','{D}','{E}','{F}')")
    st.success("Uploaded Successfully!",icon='✅')
