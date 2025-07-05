🏡 Ahmedabad House Price Prediction App
This is a real-world machine learning application that predicts house prices in Ahmedabad, India using various property features like location, BHK, total area, furnishing, property age, and more. The app is built with Streamlit and powered by a Random Forest Regressor model.

🔗 Live Demo
👉 https://ahmedabad-house-price-app-paras0202.streamlit.app/

📌 Features
Predict house price based on:

📍 Location (e.g., Satellite, Bopal)

🛏️ BHK

📐 Total Area in Sqft

🏢 Property Age

🚪 Furnishing & Floor Level

🚗 Parking Availability

🌳 Balcony View

📊 Nearby Amenities Score

Shows property price depreciation with age

Real-time predictions via a clean web UI

🧠 Tech Stack
Layer Technology
📊 Machine Learning scikit-learn, pandas
🧮 Model RandomForestRegressor
🧱 Backend Python, joblib
🌐 Frontend (UI) Streamlit
🗂️ Deployment Streamlit Cloud

🗃️ Project Structure
bash
Copy
Edit
ahmedabad_house_price_project/
├── app.py # Streamlit app
├── requirements.txt # Required libraries
├── house_price_model_fixed.pkl # Trained model
├── label_encoders_fixed.pkl # Label encoders
├── ahmedabad_real_estate_dataset_updated.csv # Dataset
├── Ahmedabad_House_Price_Prediction.ipynb # Notebook (EDA + training)
└── .gitignore
🚀 How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Paras0202/ahmedabad-house-price-app.git
cd ahmedabad-house-price-app
Create virtual environment:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate # for Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📈 Model Overview
Algorithm: Random Forest Regressor

Target: Estimated_Price

Key Feature Impact:

Property age reduces price

Higher BHK and better furnishing increase price

Location and amenities play a significant role

👨‍💻 Author
Developed by Paras Dudhat

LinkedIn Profile www.linkedin.com/in/paras-dudhat

📄 License
MIT License
