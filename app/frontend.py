import io
import requests
from PIL import Image
import streamlit as st

work_corres = {'Object Detection' : 'OD', 'Semantic Segmentation' : 'SS'}
st.set_page_config(layout="wide")

def main():
    st.title("Pipe for MM Model")
    work = st.sidebar.selectbox("작업 선택", ("Object Detection", "Semantic Segmentation"))
    st.header(work)
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image_byte = uploaded_file.getvalue()
        upfile = {'files' : image_byte}
        
        show_img = Image.open(io.BytesIO(image_byte))
        st.image(show_img, caption='Uploaded Image')
        
        if st.button('Start work'):
            st.write("Classifying...")
                        
            response = requests.post(f"http://localhost:30011/{work_corres[work]}", files=upfile)
            show_img3 = Image.open(io.BytesIO(response.content))

            st.image(show_img3, caption='Uploaded Image')

main()