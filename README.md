Strategic CRM & Marketing Decision Support System
Advanced Customer Analytics via RFM Modeling & 3D Visualization

1. Project Overview
This project is a data-driven decision-making tool designed for Marketing Specialists and Sales Executives. It transforms raw transactional data (sourced from Kaggle) into a high-level CRM strategy. By utilizing the RFM (Recency, Frequency, Monetary) framework, the system provides actionable insights into customer behavior, allowing leads to optimize retention efforts and marketing spend.


2. Key Features
Automated CRM Insight Engine: Dynamically generates an executive summary focusing on high-value assets and churn risks.

Behavioral Segmentation: Classifies customers into four strategic categories: Champions, At-Risk VIPs, Potential New, and Regular Customers.

Interactive 3D Asset Map: A multidimensional visualization that allows sales teams to "see" their customer database in a 3D space.

ROI Benchmarking: Calculates the average historical value of warning-tier customers to set maximum retention budget thresholds.


3. Technology Stack & Dependencies
This project is developed using the Anaconda distribution and requires the following Python libraries:

Pandas & NumPy: For data cleaning and mathematical modeling.

Plotly: For interactive 3D and 2D data visualization.

IPython: For rendering dynamic Markdown reports.

Datetime: For temporal analysis.


4. How to Use
Data Preparation: Download your transactional dataset from Kaggle.

File Naming: Place the dataset in the project root directory and rename it to data.csv.

Environment Setup: Open your Anaconda Navigator or Prompt and ensure plotly and pandas are installed.

Execution: Open CRM-Sales-Decision-Suite.ipynb and select "Run All Cells" from the menu.


5. Expected Results & Outputs
Executive Briefing: A textual report summarizing total asset value and current churn threats.

Revenue Contribution Chart: A pie chart identifying which segments drive the majority of sales.

3D Customer Radar: An interactive dark-themed plot for tactical account review.

Lifecycle Bar Chart: A risk-tier analysis providing benchmarks for marketing intervention ROI.


6. Strategic Value for Sales & CRM
The primary goal of this tool is to provide Sales Operations with a clear roadmap:

Where to spend? Target segments with the highest revenue contribution.

Whom to save? Immediately identify high-value VIPs in the "Warning" zone.

How to grow? Implement triggers for "Potential New" customers to increase purchase frequency.


7. Data Source
The raw data used for testing this pipeline is sourced from Kaggle (Public Datasets).

Author: Xiaoxi Du/XJTLU IBSS Accounting/2472054

Date: April 2026

Tools: Anaconda / Jupyter Notebook / Python 3.x
