# Airline Operational Efficiency & Delay Cause Analytics

A comprehensive Data Analytics project built in **Power BI Desktop** using a dataset spanning multiple years of flight records. This project focuses on evaluating operational health, identifying bottlenecks, and breaking down the primary drivers behind flight delays.

## 📊 Live Dashboard Previews
<img width="1320" height="732" alt="image" src="https://github.com/user-attachments/assets/bbdf8183-7847-41e8-9175-58f150d09de1" />

<img width="1300" height="731" alt="image" src="https://github.com/user-attachments/assets/fc67b38a-2632-40e4-b3a3-af7a20190f6c" />

## 🚀 Key Features & Architectural Highlights
* **Star Schema Data Modeling:** Engineered a robust dimensional model by separating data into fact and dimension tables, connected via optimal `One-to-Many (1:*)` relationships.
* **Power Query ETL Pipeline:** Standardized mixed-text formats, split complex strings to extract clean geographic properties (City, State, Airport Name), handled null values, and generated explicit continuous timeline indexes using M-Code.
* **Explicit DAX Measures:** Wrote robust calculations using time intelligence and filter-context manipulations (e.g., `DIVIDE`, `SUM`, `CALCULATE`) rather than relying on default implicit fields.
* **Advanced AI Visuals & UI/UX:** Implemented interactive slicers, structured negative space grids, dynamic data labels, and a **Decomposition Tree** for user-driven root-cause exploration.

---

## 💡 Core DAX Measures Used
// 1. Total Flights Logged
Total_Flights = SUM('Airline_Delay_Cause'[arr_flights])

// 2. Delayed Flights Count (>15 Mins)
Delayed_Flights = SUM('Airline_Delay_Cause'[arr_del15])

// 3. On-Time Performance Rating (OTP %)
On_Time_Performance_% = DIVIDE([Total_Flights] - [Delayed_Flights], [Total_Flights], 0)

// 4. Cumulative Delay Asset Tracking
Total_Delay_Minutes = SUM('Airline_Delay_Cause'[arr_delay])
