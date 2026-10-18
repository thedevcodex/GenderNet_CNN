# 🧠 GenderNet CNN

### CNN-Powered Image Classification

GenderNet CNN is a deep learning web application built using **Convolutional Neural Networks (CNNs)** to classify uploaded images into the model's trained categories: Female and Male.

The application is developed using TensorFlow/Keras and Streamlit, providing a simple interface for image-based predictions.

## ✨ Features

- 🖼️ Upload an image for classification
- 🧠 CNN-based image prediction
- ⚡ Interactive Streamlit interface
- 🎨 Custom gradient background and styled UI
- 📱 Simple and user-friendly design

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Streamlit

## ⚙️ How It Works

1. Upload an image using the application.
2. The image is resized to match the model's expected input dimensions.
3. The image is preprocessed before prediction.
4. The trained CNN predicts one of its learned classes.
5. The predicted class is displayed in the application.

## 📂 Project Structure

```text
GenderNet-CNN/
├── app.py
├── Gender_Model1.keras
├── requirements.txt
└── README.md
```

## 🚀 Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/thedevcodex/GenderNet-CNN.git
cd GenderNet-CNN
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
streamlit run app.py
```

## 🌐 Deployment

This application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

Connect your GitHub repository, select `app.py` as the main file, and deploy.

## ⚠️ Disclaimer

This project is intended for educational purposes. Predictions may be inaccurate due to dataset limitations, image quality, lighting, and other factors. The model predicts learned image categories and cannot determine a person's actual gender identity.

## 🌐 Live Demo

🚀 **Try GenderNet CNN online:**  
[Launch GenderNet CNN](https://gendernetcnn-thedevcodex.streamlit.app/)

Explore the CNN-powered image classification app directly in your browser.


## 👨‍💻 Developer

**devcodex**

AI & Deep Learning Project

