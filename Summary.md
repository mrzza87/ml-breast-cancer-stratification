## 🤖 Model Architecture Summary: Deep Neural Network (MLP)

### 🔬 Objective:
Classify **breast cancer molecular subtypes** using **gene expression profiles**  
from the METABRIC dataset.

### 🧠 Model Type:
Multi-Layer Perceptron (MLP)  
Supervised deep learning model for **multi-class classification**

### 🎯 Target Variable:
**`pam50_+_claudin-low_subtype`**  
Subtypes:
- Luminal A (LumA)
- Luminal B (LumB)
- HER2-enriched
- Basal-like
- Claudin-low
- Normal  
(Excluded: NC due to insufficient samples)

---

### 🧱 Architecture:

| Layer Type        | Details |
|-------------------|---------|
| `Input`           | 500 most variable gene expression features |
| `Dense(128)`      | ReLU activation, L2 regularization |
| `Dropout(0.3)`    | Regularization |
| `Dense(64)`       | ReLU activation, L2 regularization |
| `Dropout(0.2)`    | Regularization |
| `Dense(7)`        | Softmax activation for 7-class output |

---

### ⚙️ Training Details:

- **Loss Function**: `categorical_crossentropy`
- **Optimizer**: `Adam`
- **Callbacks**:
  - `EarlyStopping(patience=5)`
  - `ReduceLROnPlateau(factor=0.5, patience=3)`
- **Class Imbalance**: Handled using `class_weight='balanced'`
- **Feature Engineering**: Used top 500 genes by variance

---

### ✅ Performance Summary:

- **Test Accuracy**: ~0.76
- **Macro Avg F1**: ~0.75
- **Weighted Avg F1**: ~0.76–0.77

This model provides a strong balance between precision and generalization  
for real-world biomedical application 💖

