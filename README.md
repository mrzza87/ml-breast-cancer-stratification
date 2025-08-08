#  Breast Cancer Subtype Classification Using Deep Learning

This project applies a deep neural network to classify molecular subtypes of breast cancer using gene expression profiles from the METABRIC dataset. The model supports precision oncology by enabling more accurate, faster, and personalized treatment decisions.

---

##  Business Objective

Current breast cancer diagnostic methods are manual, time-consuming, and often imprecise. Our solution uses machine learning to:
- Improve diagnostic accuracy (≥75% test accuracy, high F1 score)
- Enable faster, consistent subtype classification for treatment planning
- Provide explainable outputs to build clinician trust
- Reduce manual review time through pre-classification
- Support scalable deployment across hospital systems

---

##  Model Overview

| Component         | Details                                               |
|------------------|--------------------------------------------------------|
| Model Type        | Multi-Layer Perceptron (MLP) for multi-class classification |
| Target Variable   | `pam50_+_claudin-low_subtype` (6 subtypes: LumA, LumB, HER2, Basal, Claudin-low, Normal) |
| Features          | Top 500 most variable gene expression z-scores       |
| Metrics           | Accuracy, Macro F1, ROC AUC, Confusion Matrix        |
| Framework         | TensorFlow / Keras                                   |

---

##  Data Sources

- **Gene expression data**: ~20,000 genes per sample (z-score normalized)
- **Labels**: Pathologist-annotated cancer subtype
- **Source**: [`METABRIC_RNA_Mutation.csv`](https://www.kaggle.com/datasets/raghadalharbi/breast-cancer-gene-expression-profiles-metabric)

---

## ⚙Pipeline

1. Data cleaning + label encoding  
2. Top gene selection via variance thresholding  
3. Feature scaling (StandardScaler)  
4. Model training with callbacks (EarlyStopping, ReduceLROnPlateau)  
5. Evaluation: Accuracy, F1 Score, ROC, Confusion Matrix  
6. Patient-level predictions with confidence scores

---

##  Key Results

- **Test Accuracy**: ~76%  
- **Macro F1 Score**: ~0.75  
- **Weighted F1 Score**: ~0.76–0.77  
- Strong performance across common subtypes; room to improve rare classes

---

## � Proof of Concept – `patient_A`

- Age 55, Stage IIa, HER2+, ER+, PR–
- Model confidently predicted `HER2-enriched` subtype  
- Visualized using PCA & UMAP overlays  
- **Impact**: Supports HER2-targeted therapy → avoids broad chemo toxicity

---

##  Visualizations

- PCA and UMAP cluster plots (with patient overlay)  
- Confusion matrix heatmap  
- ROC curves per subtype  
- Confidence bar chart for patient-level prediction  
- Training/validation loss and accuracy curves

---

##  Compliance & Deployment

- PDPA 2012, Health Information Bill (2025-ready)  
- HSA AI-SaMD pathway supported  
- Modular deployment via HEALIX platform or Flask app

---

##  What’s Next?

- Link predictions to clinical endpoints (OS, DFS)  
- Improve rare subtype prediction with advanced architectures (1D CNN, XGBoost)  
- Deploy on real-world patient registries across Asia  
- Prepare for HSA sandbox and market launch

---

##  References

- Cortés et al., NEJM (2022)  
- Escrivá-de-Romaní et al., Therapeutic Advances in Oncology (2022)  
- Modi et al., JCO (2022)  
- Loibl et al., Lancet Oncology (2021)

---

##  Authors

Team 3 – Cancer Subtype Classification (Scenario 5, Genomics)



