
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model_fixed.pkl")
encoders = joblib.load("label_encoders_fixed.pkl")

st.set_page_config(page_title="Ahmedabad House Price Predictor", layout="centered")
st.title("🏠 Ahmedabad House Price Predictor")

location = st.selectbox("📍 Location", encoders["Location"].classes_)
bhk = st.selectbox("🛏️ BHK", [1, 2, 3, 4])
area = st.number_input("📐 Total Area (sq ft)", min_value=200, max_value=10000, step=50)
condition = st.selectbox("🔧 Condition", encoders["Condition"].classes_)
furnishing = st.selectbox("🛋️ Furnishing", encoders["Furnishing"].classes_)
floor_level = st.selectbox("🏢 Floor Level", encoders["Floor_Level"].classes_)
balcony_view = st.selectbox("🌇 Balcony View", encoders["Balcony_View"].classes_)
property_age = st.slider("🏗️ Property Age (years)", 0, 30, 5)
total_floors = st.slider("🏙️ Total Floors in Building", 3, 20, 10)
has_parking = st.selectbox("🚗 Parking Available", ["Yes", "No"])
amenity_score = st.slider("🏬 Nearby Amenities Score (1-10)", 1, 10, 5)
year_of_sale = st.selectbox("📅 Year of Sale", [2021, 2022, 2023, 2024, 2025])

input_data = {
    "Location": encoders["Location"].transform([location])[0],
    "BHK": bhk,
    "Total_Area_Sqft": area,
    "Condition": encoders["Condition"].transform([condition])[0],
    "Furnishing": encoders["Furnishing"].transform([furnishing])[0],
    "Floor_Level": encoders["Floor_Level"].transform([floor_level])[0],
    "Nearby_Amenities_Score": amenity_score,
    "Property_Age": property_age,
    "Total_Floors": total_floors,
    "Has_Parking": 1 if has_parking == "Yes" else 0,
    "Balcony_View": encoders["Balcony_View"].transform([balcony_view])[0],
    "Year_Of_Sale": year_of_sale
}
input_df = pd.DataFrame([input_data])

if st.button("🔍 Predict House Price"):
    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: ₹ {int(predicted_price):,}")

    importances = model.feature_importances_
    importance_df = pd.DataFrame({
        "Feature": input_df.columns,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False)
    st.subheader("📊 Feature Importance")
    st.bar_chart(importance_df.set_index("Feature"))

    ages = list(range(0, 31, 5))
    prices = []
    for age in ages:
        input_data["Property_Age"] = age
        age_df = pd.DataFrame([input_data])
        prices.append(model.predict(age_df)[0])
    age_price_df = pd.DataFrame({
        "Age": ages,
        "Predicted Price": prices
    })
    st.subheader("📉 Price vs Property Age")
    st.line_chart(age_price_df.set_index("Age"))
