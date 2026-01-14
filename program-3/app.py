import streamlit as st
import pandas as pd
import numpy as np
import os
from topsis_pkg import main # Aapka banaya hua logic import kar rahe hain

st.set_page_config(page_title="TOPSIS Web App - 102317089", layout="centered")

st.title("📊 TOPSIS Decision Maker")
st.write("Upload your CSV file, specify weights and impacts, and get the results instantly.")

# 1. File Upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data", data.head())

    # 2. Inputs
    weights = st.text_input("Enter Weights (comma separated)", "1,1,1,1")
    impacts = st.text_input("Enter Impacts (+ or - comma separated)", "+,+,-,+")
    
    if st.button("Calculate TOPSIS"):
        # Temporary files for processing
        data.to_csv("temp_input.csv", index=False)
        
        try:
            # Calling your package logic
            import sys
            from io import StringIO
            
            # Mocking command line arguments for your existing main()
            sys.argv = ['topsis', 'temp_input.csv', weights, impacts, 'temp_result.csv']
            main()
            
            # Display results
            if os.path.exists("temp_result.csv"):
                result_df = pd.read_csv("temp_result.csv")
                st.success("✅ TOPSIS calculation successful!")
                st.write("### Results", result_df)
                
                # Download Button
                st.download_button(
                    label="Download Result CSV",
                    data=result_df.to_csv(index=False),
                    file_name="102317089-result.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error: {e}")