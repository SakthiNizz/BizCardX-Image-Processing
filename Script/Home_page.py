import streamlit as st
from PIL import Image
from Extract import extract
from Db import insert
import os

def load_image(image_file):
	img = Image.open(image_file)
	return img

st.title('BizCardX-Image Processing')
st.sidebar.success("Home")
st.header("Image Processing")
image_file = st.file_uploader("Upload Images", type= ["png","jpg","jpeg"])

if image_file is not None:
        st.write('Image Details : ')
        file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
        st.write(file_details)
        a = load_image(image_file)
        st.image(a)
        option = st.radio('To Extract Text from Image :',('','Yes','No'))
        if option == 'Yes':
                st.write('File must be in Saved before extracting all information, Click...')
                if st.button('Save'):
                        with open(os.path.join("C:/Users/91638/OneDrive/Desktop/learning/image_process/", image_file.name),"wb") as f:
                            f.write((image_file).getbuffer())
                            st.success("File Saved")
                        extract(image_file.name)
        elif option == 'No':
                st.write('Thank You!')
        else:
                st.write('')
        st.write('Press button to insert the extracted data with Image in DB')
        if st.button('Insert'):
               insert(image_file.name)