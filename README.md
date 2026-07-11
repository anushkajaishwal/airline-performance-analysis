#  Airline Operational Performance & Delay Prediction Engine

An end-to-end data analytics and data science project that combines **Descriptive Analytics (Power BI)** to audit historical flight delays and **Predictive Analytics (Machine Learning using Python)** to forecast operational delay states in real-time.

---

##  Project Architecture & Workflow
1. **Data Cleaning & Imputation:** Handled missing values using statistical Median Imputation for numeric attributes and localized token masking for categorical entries to preserve dataset volume.
2. **Descriptive Analytics:** Engineered a Power BI Dashboard utilizing advanced DAX measures to analyze delay causes, carrier efficiency, and airport congestion points.
3. **Feature Engineering & Transformation:** Applied One-Hot Encoding to categorical columns (`carrier_name`, `airport`) to eliminate ordinal bias and integrated route capacity features (`arr_flights`).
4. **Predictive Modeling:** Developed a sequential learning pipeline using **Gradient Boosting (XGBoost/GBM framework)** tuned with weighted balancing to handle severe class disparity.

---

##  Machine Learning Model Performance Comparison

During development, the model evolved through three structural phases to tackle the extreme class imbalance (97% Delayed vs 3% On-Time flights). Below is the comprehensive benchmark matrix:

| Metric Name | Model 1 (Standard RF) | Model 2 (Balanced RF) | Model 3 (Tuned Gradient Boosting) |
| :--- | :---: | :---: | :---: |
| **Overall Model Accuracy** | 96.96% | 70.76% | **90.64%** |
| **Delayed Flight Recall** | 99.99% | 71.01% | **90.58%** |
| **On-Time Flight Recall** | 0.26% (Fail) | 62.55% | **92.38%** |

###  Core Engineering Insights (Why Model 3 Won):
* **Label Encoding vs One-Hot Encoding:** Shifting away from Label Encoding eliminated false mathematical hierarchies (e.g., Airport ID 3 > Airport ID 1), streamlining feature isolation.
* **Volume Density Mapping:** Adding the `arr_flights` feature provided the model with crucial context regarding air traffic congestion.
* **Sequential Error Correction:** Using Gradient Boosting allowed the pipeline to train sequentially, with each new tree directly optimizing the classification errors made by the previous ones.

---

##  Power BI Dashboard Highlights
* **Core DAX Metrics:** Automated key performance indicators (KPIs) including Average Delay Minutes, Year-over-Year Operational Volatility, and Carrier Risk Indexes.
* **Root-Cause Segmentation:** Divided delays into structural pillars: Air Carrier Issues, Weather Disruptions, National Aviation System (NAS) Gridlocks, and Security/Late Aircraft propagation.
* **Scannable UI/UX:** Built using dynamic tooltips, conditional formatting heatmaps, and clear page hierarchies for executive decision-making.

---

## 🛠️ Tech Stack & Libraries Used
* **Data Visualization:** Microsoft Power BI Desktop (DAX, Power Query)
* **Language/Environment:** Python 3.11 (VS Code / PowerShell terminal)
* **Data Wrangling:** Pandas, NumPy
* **Machine Learning Framework:** Scikit-Learn (`GradientBoostingClassifier`, `RandomForestClassifier`, `train_test_split`)

---

## 🚀 How to Run the Predictive Engine Local Setup

1. Clone this repository to your local system:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/airline-performance-analysis.git](https://github.com/YOUR_GITHUB_USERNAME/airline-performance-analysis.git)
