import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="TOPSIS - 102317089", layout="centered")

st.title("📊 TOPSIS Decision Maker")
st.subheader("Roll Number: 102317089")

# --- TOPSIS CALCULATION LOGIC ---
def calculate_topsis(data, weights, impacts):
    # Numeric data extraction (excluding first column)
    matrix = data.iloc[:, 1:].values.astype(float)
    
    # 1. Normalization
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    
    # 2. Weighted Normalization
    weighted_matrix = norm_matrix * weights
    
    # 3. Ideal Best and Worst
    ideal_best = []
    ideal_worst = []
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(weighted_matrix[:, i]))
            ideal_worst.append(min(weighted_matrix[:, i]))
        else:
            ideal_best.append(min(weighted_matrix[:, i]))
            ideal_worst.append(max(weighted_matrix[:, i]))
            
    # 4. Distance Calculation
    s_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    s_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))
    
    # 5. Performance Score
    score = s_worst / (s_best + s_worst)
    return score

# --- USER INTERFACE ---
uploaded_file = st.file_uploader("Upload Input CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())
    
    col1, col2 = st.columns(2)
    with col1:
        weights_str = st.text_input("Weights (comma separated)", "1,1,1,1")
    with col2:
        impacts_str = st.text_input("Impacts (+/- separated)", "+,+,-,+")
        
    if st.button("Calculate TOPSIS"):
        try:
            weights = [float(w) for w in weights_str.split(',')]
            impacts = impacts_str.split(',')
            
            # Basic Validation
            if len(weights) != (df.shape[1]-1) or len(impacts) != (df.shape[1]-1):
                st.error("Error: Weights aur Impacts ki count columns (excluding 1st) ke barabar honi chahiye!")
            else:
                scores = calculate_topsis(df, weights, impacts)
                df['Topsis Score'] = scores
                df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)
                
                st.success("Success! Results are ready.")
                st.write("### Results Table", df)
                
                # Download Result
                csv = df.to_csv(index=False)
                st.download_button("Download Result CSV", csv, "result_102317089.csv", "text/csv")
        except Exception as e:
            st.error(f"Something went wrong: {e}")