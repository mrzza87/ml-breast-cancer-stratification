# 🧬 Scenario 5: Genomics - Cancer Subtype Classification using Gene Expression Data (Deep Learning)

## 📌 Business Objective

To build a deep learning model that classifies breast cancer subtypes using gene expression profiles from tumor samples.  
This supports **personalized medicine** by helping pathologists:
- ✅ Improve diagnosis speed & accuracy  
- ✅ Align patients with targeted therapies (e.g., hormone therapy or HER2 inhibitors)  
- ✅ Reduce overtreatment and improve outcomes  

---

## 🎯 Target Variable

**`pam50_+_claudin-low_subtype`**  
A categorical label indicating breast cancer molecular subtype:
- Luminal A (LumA)  
- Luminal B (LumB)  
- HER2-enriched  
- Basal-like  
- Claudin-low  

---

## 🧬 Data Sources

- **Dataset**: `METABRIC_RNA_Mutation.csv` from Kaggle  
- Includes:
  - Gene expression z-scores  
  - Mutation status for many cancer-related genes  
  - Clinical subtype labels and demographic info  

📌 [Kaggle METABRIC Dataset](https://www.kaggle.com/datasets/raghadalharbi/breast-cancer-gene-expression-profiles-metabric)

---

## 🛠️ Feature Engineering

**Input Features:**
- Gene expression columns (z-scores)
- *(Optional)* Mutation status as binary features

**Preprocessing Steps:**
- Drop rows with missing subtype labels
- One-hot encode target variable
- *(Optional)* Select top variance genes
- Ensure all input features are numeric and standardized

---

## 🤖 Model Selection

**Primary Model:**  
- Deep Neural Network (Multi-Layer Perceptron) using TensorFlow or PyTorch

**Architecture:**
- Input: Number of selected genes (e.g., 500–2000)
- Hidden Layers: 2–3 Dense layers with ReLU + Dropout
- Output Layer: Softmax for multi-class classification

**Baseline Models:**  
- Logistic Regression  
- Random Forest  

---

## 📏 Validation Strategy

- Split: 70% Train / 15% Validation / 15% Test
- Optional: Stratified K-Fold Cross-Validation

**Evaluation Metrics:**
- Accuracy  
- F1-Score (Macro + Per Class)  
- Confusion Matrix  
- ROC-AUC (Per Class)  

---

## 💻 Implementation

**Language & Tools:**
- Python  
- Libraries: `Pandas`, `NumPy`, `Scikit-learn`, `TensorFlow/Keras` or `PyTorch`

**Pipeline Steps:**
1. Load and clean the dataset  
2. Encode subtype labels  
3. Select and scale features  
4. Build and train deep learning model  
5. Evaluate and tune  
6. Save model and predictions  

---

## 📊 Visualization & Reporting

- 📈 PCA/UMAP plots showing gene expression clusters  
- 📊 Confusion matrix heatmap  
- 📉 ROC curve per subtype  
- 📉 Training/validation loss and accuracy curves  

**Final report includes:**
- Business Objective  
- Dataset Summary  
- Model Architecture  
- Evaluation Results  
- Clinical Relevance  

---

