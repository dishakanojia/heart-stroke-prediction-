Heart Disease Prediction

A machine learning-based heart disease prediction web application built
using KNN, Scikit-learn, Pandas, NumPy, Joblib, and Streamlit.

The application takes patient health parameters as input and uses a
trained K-Nearest Neighbors (KNN) model to predict the presence of heart
disease.

🚀 Live Demo

Open the Streamlit App

📂 GitHub Repository

View the GitHub
Repository

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

KNN (K-Nearest Neighbors)

Joblib

Streamlit

📁 Project Structure

heart-stroke-prediction-/
│
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── heart.csv
├── HeartdiseaseFinal.ipynb
├── requirements.txt
└── README.md

🧠 Machine Learning Workflow

Load and explore the heart disease dataset.

Clean and preprocess the data.

Encode categorical variables where required.

Scale numerical features using StandardScaler.

Train a KNN classification model.

Save the trained model, scaler, and expected columns using Joblib.

Build an interactive Streamlit interface.

Deploy the application using Streamlit Community Cloud.

💻 Run Locally

Clone the repository:

git clone https://github.com/dishakanojia/heart-stroke-prediction-.git
cd heart-stroke-prediction-

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.

📊 Model

The project uses a K-Nearest Neighbors (KNN) classification model
trained on heart disease-related patient parameters.

The following saved files are used by the application:

KNN_heart.pkl --- trained KNN model

scaler.pkl --- fitted feature scaler

columns.pkl --- expected feature columns

⚠️ Disclaimer

This application is an educational machine learning project and should
not be used as a substitute for professional medical diagnosis or
treatment.

👩‍💻 Author

Disha Kanojia

B.Tech Electronics & Communication Engineering
Netaji Subhas University of Technology (NSUT), Delhi
