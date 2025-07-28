import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# App config
st.set_page_config(page_title="Breast Cancer Subtype Predictor", layout="centered")

# Header
st.title("🧬 Breast Cancer Subtype Predictor")
st.markdown("Upload gene expression data to classify a patient's PAM50 molecular subtype.")

# Load model
@st.cache_resource
def load_classifier():
    return load_model("metabric_subtype_classifier.h5")

model = load_classifier()

# Subtype labels
subtypes = ["Luminal A", "Luminal B", "HER2-enriched", "Basal-like", "Claudin-low", "Normal-like"]

# File upload
uploaded_file = st.file_uploader("📂 Upload a single-row CSV file (z-score gene expression)", type="csv")

if uploaded_file is not None:
    try:
        input_df = pd.read_csv(uploaded_file, index_col=0)
        st.write("✅ Data preview:", input_df.head())

        # Ensure correct shape
        X = input_df.values
        if X.shape[0] == 1:
            pred_probs = model.predict(X)
            pred_idx = np.argmax(pred_probs)
            confidence = pred_probs[0][pred_idx]

            st.success(f"🎯 Predicted Subtype: **{subtypes[pred_idx]}**")
            st.markdown(f"🔬 Confidence: **{confidence:.2%}**")

            st.bar_chart(pd.Series(pred_probs[0], index=subtypes))

        else:
            st.warning("Please upload only **one patient row** at a time.")

    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

else:
    st.info("💡 Upload your test file or [try a sample input CSV](https://yourdomain.com/sample_input.csv)")
