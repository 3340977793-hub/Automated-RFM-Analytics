# Strategic CRM & Marketing Decision Support System
### *Advanced Customer Analytics via RFM Modeling & 3D Visualization*

---

## 1. Project Overview
This project is a **professional data-driven decision-making tool** specifically designed for **Marketing Specialists** and **Sales Executives**. 

By transforming raw transactional data (sourced from **Kaggle**) into a high-level CRM strategy, the system bridges the gap between raw data and business action. Utilizing the **RFM (Recency, Frequency, Monetary)** framework, it provides deep insights into customer behavior, allowing leadership to optimize retention efforts and maximize marketing ROI.

---

## 2. Key Features
* **Automated Insight Engine**: Dynamically generates a textual executive summary focusing on high-value assets and immediate churn threats.
* **Behavioral Segmentation**: Automatically classifies the database into four actionable categories: 
    * `Champions` (High-value, High-loyalty)
    * `At-Risk VIPs` (High-value, but drifting away)
    * `Potential New` (New joiners with growth potential)
    * `Regular Customers` (The baseline population)
* **Interactive 3D Asset Map**: A multidimensional radar visualization that allows sales teams to explore their customer base in a 3D digital space.
* **ROI Benchmarking**: Calculates the **average historical value** of warning-tier customers to help managers set scientific budget thresholds for reactivation.

---

## 3. Technology Stack
This project is built within the **Anaconda** distribution environment:
* **Language**: `Python 3.x`
* **Core Libraries**:
    * `Pandas` & `NumPy`: For heavy-duty data cleaning and RFM modeling.
    * `Plotly`: For high-end interactive 3D and 2D visualization.
    * `IPython`: For rendering dynamic business narratives.
    * `Datetime`: For temporal churn analysis.

---

## 4. Execution Guide
1.  **Prepare Data**: Download a transactional dataset from Kaggle.
2.  **File Setup**: Rename the file to **`data.csv`** and place it in the project root directory.
3.  **Environment**: Open your **Anaconda Prompt** and ensure `plotly` and `pandas` are installed:
    ```bash
    pip install pandas plotly
    ```
4.  **Run**: Launch **Jupyter Notebook**, open `CRM-Sales-Decision-Suite.ipynb`, and select **"Run All Cells"**.

---

## 5. Expected Strategic Outputs
The system outputs four distinct decision-support modules:
* **[I] Executive Briefing**: A Markdown report summarizing total asset value and risk metrics.
* **[II] Revenue Distribution**: A pie chart identifying core revenue drivers.
* **[III] 3D Customer Radar**: A tactical tool for account-level review and gap analysis.
* **[IV] Risk-Tier ROI Chart**: A benchmark for determining marketing intervention costs.

---

## 6. Business Impact
This system empowers **Sales Operations** to answer three critical questions:
1.  **"Where to spend?"** → Target segments with the highest revenue contribution.
2.  **"Whom to save?"** → Intervene with high-value VIPs in the "Warning" zone.
3.  **"How to grow?"** → Implement automated triggers for "Potential New" customers to break frequency barriers.

---

**Author:** Xiaoxi Du/XJTLU IBSS Accounting/2472054

**Date:** April 2026  
**Status:** Final Submission / Functional Portfolio  
**Development Environment:** Anaconda Distribution
