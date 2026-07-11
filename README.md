#  Airline Operational Performance & Predictive Delay Engine

An end-to-end data analytics and data science engineering project that bridges **Descriptive Analytics (Power BI)** to diagnose historical bottleneck trends and **Predictive Analytics (Python / Machine Learning)** to forecast operational delay states in real-time.

---

##  1. Descriptive Analytics Framework (Power BI Dashboard)

The descriptive tier focuses on converting raw chaotic flight logs into structured business insights. Using advanced data modeling, data split queries, and relational integrity, this interactive engine analyzes why operational breakdowns happen.

###  Dashboard Preview & Interface
<img width="1343" height="726" alt="image" src="https://github.com/user-attachments/assets/78f93016-9cfd-4785-a35e-bc619b8aefac" />
<img width="1347" height="733" alt="image" src="https://github.com/user-attachments/assets/fac88a7b-cc53-4ba5-bfc1-55d677d8ddf8" />



###  Core Components & Analytical Depth:
* **Root-Cause Disruption Segmentation:** Developed deep dimensional slicing across five core operational disruption drivers: Air Carrier Issues, Extreme Weather Dynamics, National Aviation System (NAS) Gridlocks, Security Inefficiencies, and Late Aircraft propagation delay cycles.
* **Operational Volume & Risk KPIs:** Built critical diagnostic indicators using advanced **DAX measures** to compute Average Delay Minutes, Flight Volume Density, and Carrier Risk Profiles to benchmark overall operational efficiency.
* **UX/UI for Executive Decision Making:** Integrated dynamic cross-filtering, conditional formatting heatmaps, and tooltips to isolate heavily affected regional hubs instantly.

---

##  2. Predictive Analytics Engine (Python / Machine Learning)

To complement historical insights, a predictive pipeline was engineered using **Scikit-Learn** to determine the structural probability of flight delays (`is_delayed`) based on dynamic inputs: Carrier, Airport Code, Month, and Traffic Density.

###  The Machine Learning Challenge & Evolution
The dataset suffered from an extreme class imbalance (~97% Delayed vs ~3% On-Time flights). A naive model would simply learn to guess "Delayed" for every flight to score high accuracy while failing to detect on-time states. To combat this **Accuracy Paradox**, the pipeline was structurally evolved across three phases:

| Performance Metric | Model 1 (Standard RF) | Model 2 (Balanced RF) | Model 3 (Tuned Gradient Boosting) |
| :--- | :---: | :---: | :---: |
| **Overall System Accuracy** | 96.96% | 70.76% | **90.64%** |
| **Delayed Flight Recall (Catch Rate)** | 99.99% | 71.01% | **90.58%** |
| **On-Time Flight Recall (Catch Rate)** | 0.26% (FAIL) | 62.55% | **92.38%** |

###  Optimization Strategy (Why Model 3 Achieved 90.64% Performance):
1. **Data Imputation & Volume Preservation:** Instead of aggressively dropping sparse rows, **Median Imputation** was implemented on traffic metrics (`arr_flights`) to preserve data structural integrity.
2. **One-Hot Encoding Shift:** Transitioned away from `LabelEncoder` to `pd.get_dummies()` for high-cardinality values (`airport`, `carrier_name`). This eliminated false mathematical hierarchies (e.g., Airport 3 > Airport 1), allowing independent category weight assignments.
3. **Sequential Boosting Weights:** Deployed a `GradientBoostingClassifier` parameterized with dynamic sample scaling. Unlike parallel architectures, the boosting mechanism trains trees sequentially, forcing each new tree to directly learn from and correct the errors made by previous iterations.

---

##  Tech Stack & Architecture
* **Descriptive Interface:** Microsoft Power BI Desktop (Power Query, Data Modeling, DAX)
* **Core Language:** Python 3.11
* **Data Wrangling:** Pandas, NumPy
* **Machine Learning Framework:** Scikit-Learn (`GradientBoostingClassifier`, `RandomForestClassifier`, `train_test_split`)

---

##  Local Execution Setup

1. Clone this repository to your machine:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/airline-performance-analysis.git](https://github.com/YOUR_GITHUB_USERNAME/airline-performance-analysis.git)
