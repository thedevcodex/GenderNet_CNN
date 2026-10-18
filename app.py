import streamlit as st
from tensorflow.keras.utils import load_img
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('Gender_model1.keras')

st.set_page_config (
    page_title="GenderNet CNN",
    page_icon = "https://img.icons8.com/?size=100&id=1665&format=png&color=000000",
    layout = 'wide',
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp{
        background: linear-gradient(135deg, #0B1D16,#163D2B,
        #245A3C);
      
}
div.stButton > button {
    background-color: red;
    color: white;
    border: none;
    border-radius: 10px;
}
</style>

""",unsafe_allow_html=True)






st.title("GenderNet CNN")
st.caption("CNN-Powered Image Classification | Built by devcodex")  

tab1,tab2,tab3 = st.tabs(["Home","Prediction","About"])

with tab1:
    st.markdown("""
       # 🧠 Welcome to GenderNet CNN

### AI-Powered Image Classification

GenderNet CNN is a deep learning project built using a **Convolutional Neural Network (CNN)** to classify uploaded images into the model's trained classes: Female and Male.

✨ **Key Features**

- 🖼️ Upload an image for prediction
- 🧠 CNN-based image classification
- ⚡ Simple and interactive interface

**Built with:** Python · TensorFlow/Keras · Streamlit

*Built by devcodex | AI & Deep Learning Project*

**Note:** Predictions are model-generated classifications and may be incorrect. They do not determine a person's actual gender identity.


""")

with tab2:
    image_uploader = st.file_uploader(
        "Upload Male or Female Image",
        ['jpg','jpeg','webp','png']
    )
    if image_uploader:
        col1,col2,col3 = st.columns([1,2,1])
        with col2:    
            st.image(image_uploader,width=800)
            st.write(" ")
            button_pred = st.button("Prediction")
            if button_pred:
                img = load_img(image_uploader,target_size=(128,128))
                img_arr = np.array(img)/255.0
                img_arr = np.expand_dims(img_arr,axis=0)
                pred = model.predict(img_arr)
                if pred[0][0] >(0.5):
                    st.warning("Male")
                else:
                    st.warning('Female')


with tab3:
    st.markdown("""
# 🧠 About GenderNet CNN

### Project Overview
GenderNet CNN is an image classification project developed using **Convolutional Neural Networks (CNNs)** with TensorFlow/Keras. The model is trained to classify images into two learned categories: Female and Male.

### 🎯 Project Objectives
- Understand how CNNs process and learn image features.
- Apply deep learning techniques to image classification.
- Build an interactive web application using Streamlit.
- Explore the practical implementation of a deep learning model.

### ⚙️ Technologies Used
- **Python** — Core programming language
- **TensorFlow & Keras** — CNN model development and training
- **NumPy** — Numerical operations
- **Pillow (PIL)** — Image processing
- **Streamlit** — Interactive web application

### 🔄 How It Works
1. Upload an image through the application.
2. The image is resized and preprocessed to match the model's input requirements.
3. The trained CNN analyzes the image and generates a prediction.
4. The application displays the predicted class.

### ⚠️ Limitations
The model may produce incorrect predictions depending on image quality, lighting, dataset diversity, and training performance. Its output is a prediction of the trained image categories and does not establish a person's actual gender identity.

### 👨‍💻 Developer
**Built by devcodex**

An AI and Deep Learning learning project focused on understanding and applying CNN-based image classification.  """)