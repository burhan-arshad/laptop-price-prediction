import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')

model=joblib.load('laptop_price_model.pkl')
scaler=joblib.load('Laptop_scaler.pkl')
numeric_cols=joblib.load('Laptop_num_Columns.pkl')
expected_cols=joblib.load('laptop_columns.pkl')

st.title("Laptop Price Predictor")
st.markdown("Fill the Data and Get Price Prediction in Euros")

company=st.selectbox('Company', ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple', 'MSI', 'Toshiba'])
type_name=st.selectbox('Type',['Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook']) 
ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64]) 
weight = st.number_input('Weight (kg)', 0.5, 5.0, 2.0) 
inches = st.slider('Screen Size (inches)', 10.0, 18.0, 15.6) 
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes']) 
ips = st.selectbox('IPS Panel', ['No', 'Yes']) 
x_res = st.selectbox('Horizontal Resolution', [1366, 1920, 2560, 3840]) 
y_res = st.selectbox('Vertical Resolution', [768, 1080, 1440, 2160]) 
cpu_brand = st.selectbox('CPU', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other Intel', 'AMD']) 
cpu_speed = st.slider('CPU Speed (GHz)', 0.9, 3.6, 2.5) 
gpu_brand = st.selectbox('GPU Brand', ['Intel', 'Nvidia', 'AMD']) 
os = st.selectbox('Operating System', ['Windows 10', 'No OS', 'Linux', 'macOS']) 
ssd = st.selectbox('SSD (GB)', [0, 128, 256, 512, 1000]) 
hdd = st.selectbox('HDD (GB)', [0, 500, 1000, 2000])

if st.button('Predict price'):
    ppi=((x_res**2 + y_res**2) ** 0.5) / inches 
    raw = { 
        'Inches': inches, 
        'Ram': ram, 
        'Weight': weight, 
        'Touchscreen': 1 if touchscreen == 'Yes' else 0, 
        'IPS': 1 if ips == 'Yes' else 0, 
        'X_res': x_res, 
        'Y_res': y_res, 
        'PPI': ppi, 
        'Cpu_speed_GHz': cpu_speed, 
        'SSD': ssd, 
        'HDD': hdd, 
        'Company_' + company: 1, 
        'TypeName_' + type_name: 1, 
        'OpSys_' + os: 1, 
        'Cpu_brand_' + cpu_brand: 1, 
        'Gpu_brand_' + gpu_brand: 1, 
    
     }

    input_df = pd.DataFrame([raw]) 
    for col in expected_cols: 
        if col not in input_df.columns: 
            input_df[col] = 0 
    input_df = input_df[expected_cols] 
  
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols]) 
    prediction = model.predict(input_df)[0] 
  
    st.success(f'Estimated Price: €{prediction:,.2f}') 