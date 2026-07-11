import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, recall_score

# =====================================================================
# 1. ADVANCED DATA CLEANING LAYER (Imputation Framework)
# =====================================================================
print(" Loading flight dataset...")
df = pd.read_csv("Airline_Delay_Cause.csv")

print(" Executing Data Cleaning & Imputation Pipeline...")

# A. Continuous Data Cleaning: Fill missing flight counts with Median
if 'arr_flights' in df.columns:
    median_flights = df['arr_flights'].median()
    df['arr_flights'] = df['arr_flights'].fillna(median_flights)

# B. Target Columns Cleaning: Fill missing target values with 0 (Assuming On-Time if missing)
if 'arr_del15' in df.columns:
    df['arr_del15'] = df['arr_del15'].fillna(0)

# C. Categorical Data Cleaning: Fill any blank strings with 'UNKNOWN'
df['carrier_name'] = df['carrier_name'].fillna('UNKNOWN')
df['airport'] = df['airport'].fillna('UNKNOWN')

# Target Definition
df['is_delayed'] = np.where(df['arr_del15'] > 0, 1, 0)

# ---------------------------------------------------------------------
# Data Setup for Model 1 & Model 2 (Label Encoding)
# ---------------------------------------------------------------------
feature_cols_base = ['carrier_name', 'airport', 'month']
X_base = df[feature_cols_base].copy()

le_carrier = LabelEncoder()
le_airport = LabelEncoder()
X_base['carrier_name'] = le_carrier.fit_transform(X_base['carrier_name'])
X_base['airport'] = le_airport.fit_transform(X_base['airport'])
y = df['is_delayed']

X_train_b, X_test_b, y_train, y_test = train_test_split(
    X_base, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------------------------------------------------------------
# Data Setup for Model 3 (Advanced Feature Engineering & One-Hot Encoding)
# ---------------------------------------------------------------------
print("⚙️ Engineering High-Density Operational Matrix for Model 3...")
feature_cols_adv = ['carrier_name', 'airport', 'month', 'arr_flights']
X_advanced = pd.get_dummies(df[feature_cols_adv], columns=['carrier_name', 'airport'], drop_first=True)

X_train_a, X_test_a, _, _ = train_test_split(
    X_advanced, y, test_size=0.2, random_state=42, stratify=y
)

# =====================================================================
# 2. MODEL 1: STANDARD RANDOM FOREST (No class weights)
# =====================================================================
print("\n🌲 Training Model 1: Standard Random Forest (No class weights)...")
model_standard = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
model_standard.fit(X_train_b, y_train)
y_pred_std = model_standard.predict(X_test_b)

# =====================================================================
# 3. MODEL 2: BALANCED RANDOM FOREST (With class_weight='balanced')
# =====================================================================
print("🌲 Training Model 2: Balanced Random Forest (Balanced Weights)...")
model_balanced = RandomForestClassifier(n_estimators=100, max_depth=12, class_weight='balanced', random_state=42, n_jobs=-1)
model_balanced.fit(X_train_b, y_train)
y_pred_bal = model_balanced.predict(X_test_b)

# =====================================================================
# 4. MODEL 3: HIGH-PERFORMANCE GRADIENT BOOSTING (Optimized Engine)
# =====================================================================
print(" Training Model 3: Tuned Gradient Boosting Classifier (Max Accuracy)...")
model_boosting = GradientBoostingClassifier(n_estimators=150, learning_rate=0.1, max_depth=6, random_state=42)

# Dynamic sample weights to balance the boosting process internally
computed_weights = np.where(y_train == 0, len(y_train) / (2 * (len(y_train) - sum(y_train))), len(y_train) / (2 * sum(y_train)))
model_boosting.fit(X_train_a, y_train, sample_weight=computed_weights)
y_pred_boost = model_boosting.predict(X_test_a)

# =====================================================================
# 5. ULTIMATE COMPARISON MATRIX GENERATION
# =====================================================================
print("\n" + "="*85)
print("📊 THE ULTIMATE DATA SCIENCE COMPARISON MATRIX (WITH DATA CLEANING)")
print("="*85)

metrics_data = {
    "Metric Name": [
        "Overall Model Accuracy", 
        "Delayed Flight Recall (Catching Delays)", 
        "On-Time Flight Recall (Catching On-Time)"
    ],
    "Model 1 (Standard)": [
        f"{accuracy_score(y_test, y_pred_std)*100:.2f}%",
        f"{recall_score(y_test, y_pred_std, pos_label=1)*100:.2f}%",
        f"{recall_score(y_test, y_pred_std, pos_label=0)*100:.2f}%"
    ],
    "Model 2 (Balanced)": [
        f"{accuracy_score(y_test, y_pred_bal)*100:.2f}%",
        f"{recall_score(y_test, y_pred_bal, pos_label=1)*100:.2f}%",
        f"{recall_score(y_test, y_pred_bal, pos_label=0)*100:.2f}%"
    ],
    "Model 3 (Tuned Boosting)": [
        f"{accuracy_score(y_test, y_pred_boost)*100:.2f}%",
        f"{recall_score(y_test, y_pred_boost, pos_label=1)*100:.2f}%",
        f"{recall_score(y_test, y_pred_boost, pos_label=0)*100:.2f}%"
    ]
}

df_metrics = pd.DataFrame(metrics_data)
print(df_metrics.to_string(index=False))

print("="*85)
print("   CONCEPT MEMO FOR FUTURE ME:")
print("-> Data Cleaning: Missing numeric columns ko Median se aur categorical ko 'UNKNOWN' se fill kiya.")
print("   Isse row deletion ruki aur model ko calculations ke liye zyada mathematical points mile.")
print("-> Model 3 Advanced Optimization: Cleaned input matrix + One-Hot Encoding + Gradient Boosting Engine.")
print("="*85)