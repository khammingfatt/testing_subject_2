import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
import base64

# Set page config
st.set_page_config(
    page_title="HDB Resale Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Helper function to set background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_image(bin_file):
    if os.path.exists(bin_file):
        bin_str = get_base64_of_bin_file(bin_file)
        page_bg_img = '''
        <style>
        [data-testid="stAppViewContainer"] {
            background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,%s");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        
        [data-testid="stForm"] {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 24px 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply background image
set_bg_image('images/background.png')

# Custom CSS for a premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        text-align: center;
        margin-top: 20px;
        border-left: 5px solid #ff4b4b;
    }
    .prediction-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #2c3e50;
    }
    .stSelectbox, .stNumberInput {
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    model_path = 'src/random_forest_model.joblib'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Model file not found at {model_path}")
        return None

model = load_model()

# Define Categories
planning_areas = sorted([
    "Ang Mo Kio", "Bedok", "Bishan", "Bukit Batok", "Bukit Merah", 
    "Bukit Panjang", "Bukit Timah", "Changi", "Choa Chu Kang", 
    "Clementi", "Downtown Core", "Geylang", "Hougang", "Jurong East", 
    "Jurong West", "Kallang", "Marine Parade", "Novena", "Outram", 
    "Pasir Ris", "Punggol", "Queenstown", "Rochor", "Sembawang", 
    "Sengkang", "Serangoon", "Tampines", "Tanglin", "Toa Payoh", 
    "Western Water Catchment", "Woodlands", "Yishun"
])

full_flat_types = sorted([
    "1 ROOM Improved", "2 ROOM 2-room", "2 ROOM DBSS", "2 ROOM Improved", 
    "2 ROOM Model A", "2 ROOM Premium Apartment", "2 ROOM Standard", 
    "3 ROOM DBSS", "3 ROOM Improved", "3 ROOM Model A", 
    "3 ROOM New Generation", "3 ROOM Premium Apartment", "3 ROOM Simplified", 
    "3 ROOM Standard", "3 ROOM Terrace", "4 ROOM Adjoined flat", 
    "4 ROOM DBSS", "4 ROOM Improved", "4 ROOM Model A", "4 ROOM Model A2", 
    "4 ROOM New Generation", "4 ROOM Premium Apartment", 
    "4 ROOM Premium Apartment Loft", "4 ROOM Simplified", "4 ROOM Standard", 
    "4 ROOM Terrace", "4 ROOM Type S1", "5 ROOM Adjoined flat", 
    "5 ROOM DBSS", "5 ROOM Improved", "5 ROOM Improved-Maisonette", 
    "5 ROOM Model A", "5 ROOM Model A-Maisonette", "5 ROOM Premium Apartment", 
    "5 ROOM Premium Apartment Loft", "5 ROOM Standard", "5 ROOM Type S2", 
    "EXECUTIVE Adjoined flat", "EXECUTIVE Apartment", "EXECUTIVE Maisonette", 
    "EXECUTIVE Premium Apartment", "EXECUTIVE Premium Maisonette", 
    "MULTI-GENERATION Multi Generation"
])

# App Title
st.title("🏠 HDB Resale Price Predictor")
st.markdown("Enter the details of the HDB flat to estimate its resale price.")

# Form for user input
with st.form("prediction_form"):
    # Row 1
    r1_col1, r1_col2 = st.columns(2)
    with r1_col1:
        floor_area_sqft = st.number_input("Floor Area (sqft)", min_value=300, max_value=3000, value=1000)
    with r1_col2:
        planning_area = st.selectbox("Planning Area", planning_areas)
        
    # Row 2
    r2_col1, r2_col2 = st.columns(2)
    with r2_col1:
        full_flat_type = st.selectbox("Flat Type & Model", full_flat_types)
    with r2_col2:
        hdb_age = st.number_input("HDB Age (Years)", min_value=0, max_value=99, value=15, help="Age as of Year 2021.")
        
    # Row 3
    r3_col1, r3_col2 = st.columns(2)
    with r3_col1:
        mid_storey = st.number_input("Mid Storey", min_value=1, max_value=50, value=5, help="Midpoint of the floor range")
    with r3_col2:
        mrt_dist = st.number_input("Distance to MRT (m)", min_value=0, max_value=5000, value=500)
        
    # Row 4
    r4_col1, r4_col2 = st.columns(2)
    with r4_col1:
        mall_within_2km = st.number_input("No. of Malls within 2km", min_value=0, max_value=20, value=2)
    with r4_col2:
        hawker_within_2km = st.number_input("No. of Hawker Centers within 2km", min_value=0, max_value=20, value=3)

    st.markdown("<hr style='margin: 0.8em 0;'>", unsafe_allow_html=True)
    st.subheader("Amenities & Features")
    c3, c4, c5 = st.columns(3)
    with c3:
        commercial = st.radio("Has Commercial Units?", ["No", "Yes"], help="Indicates if the block contains retail or commercial spaces (e.g., shops, clinics, or eateries).")
    with c4:
        carpark = st.radio("Has Multistorey Carpark?", ["No", "Yes"])
    with c5:
        pavilion = st.radio("Has Precinct Pavilion?", ["No", "Yes"], help="Indicates if the block has a pavilion.")

    submit = st.form_submit_button("Predict Resale Price")

if submit:
    if model:
        # Prepare input data
        # 1. Base Features
        input_data = {
            "floor_area_sqft": float(floor_area_sqft),
            "mid_storey": float(mid_storey),
            "hdb_age": float(hdb_age),
            "mrt_nearest_distance": float(mrt_dist),
            "Mall_Within_2km": float(mall_within_2km),
            "Hawker_Within_2km": float(hawker_within_2km),
            "commercial": 1.0 if commercial == "Yes" else 0.0,
            "multistorey_carpark": 1.0 if carpark == "Yes" else 0.0,
            "precinct_pavilion": 1.0 if pavilion == "Yes" else 0.0
        }
        
        # 2. One-Hot Encoding for Full Flat Type
        for fft in full_flat_types:
            input_data[f"full_flat_type_{fft}"] = 1.0 if full_flat_type == fft else 0.0
            
        # 3. One-Hot Encoding for Planning Area
        for pa in planning_areas:
            input_data[f"planning_area_{pa}"] = 1.0 if planning_area == pa else 0.0
            
        # Create DataFrame to ensure correct column order
        # The model expects features in the order they were during training.
        # Based on the notebook, the order is: base features, then flat_type dummies, then planning_area dummies.
        
        # Construct the exact feature list
        feature_order = [
            "floor_area_sqft", "mid_storey", "hdb_age", 
            "mrt_nearest_distance", "Mall_Within_2km", 
            "Hawker_Within_2km", "commercial",
            "multistorey_carpark", "precinct_pavilion"
        ]
        # Add full_flat_type dummies (alphabetical)
        for fft in full_flat_types:
            feature_order.append(f"full_flat_type_{fft}")
        # Add planning_area dummies (alphabetical)
        for pa in planning_areas:
            feature_order.append(f"planning_area_{pa}")
            
        # Create DF and reorder
        df_input = pd.DataFrame([input_data])
        df_input = df_input[feature_order]
        
        # Make prediction
        prediction = model.predict(df_input)[0]
        
        # Display result
        st.markdown(f"""
            <div class="prediction-box">
                <p style="color: #7f8c8d; margin-bottom: 5px;">Estimated Resale Price</p>
                <div class="prediction-value">${prediction:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.balloons()
    else:
        st.error("Model not loaded. Please check the joblib file.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #95a5a6;'>Any Debs</p>", unsafe_allow_html=True)
