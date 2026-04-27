#!/usr/bin/env python
# coding: utf-8

# ### **Problem Definition**
# 
# **Core Concept:**
# Convert "static" transaction logs into "dynamic" decision support.
# 
# #### **1. Challenges**
# * **Data Silos**: Revenue and behavior data are disconnected, making it hard to identify risk.
# * **Manual Delay**: Traditional reporting is too slow to capture rapid customer churn.
# 
# #### **2. Solutions**
# * **Automated RFM**: Instant customer segmentation based on Recency, Frequency, and Monetary value.
# * **Interactive Insights**: 3D dashboards and AI-driven business narratives for rapid decision-making.
# 
# #### **3. Goal**
# Maximize Marketing ROI by shifting from "mass marketing" to "precision retention."

# In[135]:


import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
import plotly.io as pio
from IPython.display import Markdown, display

pio.renderers.default = "iframe"

def generate_automated_business_report(csv_path='data.csv'):
    try:
        # _Step 1: Robust data loading with multiple encoding support_
        df = None
        for enc in ['ISO-8859-1', 'utf-8', 'gbk']:
            try:
                df = pd.read_csv(csv_path, encoding=enc)
                break
            except: continue
        
        if df is None:
            return None

        # _Step 2: Column name cleaning and automated mapping_
        df.columns = df.columns.str.strip().str.replace(r'[^\w\s]', '', regex=True)
        mapping = {
            'User': ['CustomerID', 'Customer ID', 'UserID', 'User'],
            'Date': ['InvoiceDate', 'OrderDate', 'Date'],
            'Qty': ['Quantity', 'Qty'],
            'Price': ['UnitPrice', 'Price'],
            'Inv': ['InvoiceNo', 'Invoice No']
        }
        for std, vars in mapping.items():
            for v in vars:
                match = [c for c in df.columns if c.lower().replace(" ", "") == v.lower().replace(" ", "")]
                if match: 
                    df.rename(columns={match[0]: std}, inplace=True)
                    break

        # _Step 3: Data transformation and RFM modeling_
        df = df.dropna(subset=['User']).copy()
        df['Date'] = pd.to_datetime(df['Date'])
        df['Sales'] = df['Qty'] * df['Price']
        
        now = df['Date'].max() + dt.timedelta(days=1)
        rfm = df.groupby('User').agg({
            'Date': lambda x: (now - x.max()).days,
            'Inv': 'nunique',
            'Sales': 'sum'
        }).rename(columns={'Date':'R', 'Inv':'F', 'Sales':'M'})
        
        rfm = rfm[rfm['M'] > 0]

        # _Step 4: Automated customer segmentation using quantiles_
        rfm['RS'] = pd.qcut(rfm['R'], 5, labels=[5,4,3,2,1])
        rfm['FS'] = pd.qcut(rfm['F'].rank(method='first'), 5, labels=[1,2,3,4,5])

        def seg_logic(row):
            r, f = int(row['RS']), int(row['FS'])
            if r >= 4 and f >= 4: return 'Champions'
            if f >= 4 and r <= 2: return 'At Risk VIP'
            if r >= 4 and f <= 2: return 'Potential New'
            return 'Regular'
        rfm['Segment'] = rfm.apply(seg_logic, axis=1)

        # _Step 5: Extract key metrics for automated business narrative_
        total_m = rfm['M'].sum()
        stats = rfm.groupby('Segment').agg({'M':['sum','count'], 'R':'mean'})
        stats.columns = ['rev', 'cnt', 'r_avg']
        
        def get_v(seg, col): return stats.loc[seg, col] if seg in stats.index else 0

        champ_share = (get_v('Champions', 'rev') / total_m) * 100 if total_m > 0 else 0
        risk_rev = get_v('At Risk VIP', 'rev')
        risk_cnt = int(get_v('At Risk VIP', 'cnt'))
        new_ratio = (get_v('Potential New', 'cnt') / len(rfm)) * 100 if len(rfm) > 0 else 0

        report = f"""
# Customer Asset Quality Analysis Report (Automated)

**To: Marketing Director / Head of Sales** **Active Customers: {len(rfm):,} | Total Asset Value: ${total_m:,.2f}**

---

### 1. Core Asset Insights
Through 3D modeling of behavioral data, we have identified the following key characteristics:
* **Revenue Pillar**: The [Champions] group contributes **{champ_share:.1f}%** of the total revenue. These high-loyalty assets are the foundation of profit.
* **Churn Warning**: **{risk_cnt}** high-value VIPs are currently "At Risk", involving a potential loss of **${risk_rev:,.2f}**.
* **Growth Bottleneck**: [Potential New] customers account for **{new_ratio:.1f}%** of the base, but most are stuck at a single purchase.

### 2. Strategic Recommendations
* **Immediate Intervention**: Launch 1-on-1 retention programs for high-risk assets worth **${risk_rev:,.2f}**.
* **Protect the Core**: Allocate specialized budgets for Champions to maintain their activity coordinates.
* **Drive Progression**: Implement "14-day post-purchase" automated triggers for new customers to break frequency barriers.

---
"""
        display(Markdown(report))
        return rfm

    except Exception as e:
        print(f"Analysis Failed: {e}")
        return None

# _Execution and global variable assignment_
rfm = generate_automated_business_report('data.csv')


# In[131]:


from IPython.display import Markdown, display
import plotly.express as px

# _Calculating revenue distribution across segments_
rev_stats = rfm.groupby('Segment')['M'].sum()
total_rev = rev_stats.sum()
top_segment = rev_stats.idxmax()
top_pct = (rev_stats.max() / total_rev) * 100 if total_rev > 0 else 0

md_text_1 = f"""
### 📊 [Dashboard 1] Revenue Contribution by Customer Layer
* **Observation**: The [**{top_segment}**] segment is the primary driver, contributing **{top_pct:.1f}%** of sales.
* **Strategic Implication**: Marketing budgets should be weighted according to these contribution ratios.
"""
display(Markdown(md_text_1))

fig_pie = px.pie(
    rev_stats.reset_index(), 
    values='M', names='Segment', hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_pie.update_layout(margin=dict(t=20, b=20, l=0, r=0))
fig_pie.show()


# In[132]:


from IPython.display import Markdown, display
import plotly.express as px

# _Calculating quantile limits to prevent outlier distortion_
m_limit = rfm['M'].quantile(0.95)
f_limit = rfm['F'].quantile(0.98)

md_text_2 = f"""
### 🌌 [Dashboard 2] 3D Customer Asset Monitoring
* **Visualization Note**: Data is capped at the 95th percentile of value (${m_limit:,.0f}) and 98th percentile of frequency ({f_limit:.0f} times) for clarity.
* **Strategic Implication**: Focus on high-value spheres shifting towards the right (Higher R values), indicating imminent churn risk.
"""
display(Markdown(md_text_2))

# _Rendering 3D scatter plot with enhanced marker size_
fig_3d = px.scatter_3d(
    rfm, x='R', y='F', z='M', color='Segment', size='M', size_max=30, opacity=0.8,
    range_z=[0, m_limit], range_y=[0, f_limit],
    labels={'R':'Recency (Days)', 'F':'Frequency (Count)', 'M':'Monetary (Value)'},
    template="plotly_dark"
)
fig_3d.update_layout(
    scene=dict(aspectratio=dict(x=1, y=1, z=2.5)), 
    margin=dict(l=0, r=0, b=0, t=20)
)
fig_3d.show()


# In[133]:


from IPython.display import Markdown, display
import plotly.express as px

# _Defining business risk tiers based on recency_
def get_risk_tier(r):
    if r <= 30: return 'A. Active (0-30 days)'
    if r <= 90: return 'B. Fluctuating (31-90 days)'
    if r <= 180: return 'C. Warning (91-180 days)'
    return 'D. Dormant (180 days+)'

rfm['Risk_Tier'] = rfm['R'].apply(get_risk_tier)

# _Aggregating data avoiding potential KeyError on index columns_
risk_stats = rfm.groupby('Risk_Tier').agg(avg_m=('M', 'mean'), count=('M', 'size')).reset_index()

high_risk_row = risk_stats[risk_stats['Risk_Tier'].str.contains('C.')]
avg_risk_val = high_risk_row['avg_m'].values[0] if not high_risk_row.empty else 0
risk_count = high_risk_row['count'].values[0] if not high_risk_row.empty else 0

md_text_3 = f"""
### ⚠️ [Dashboard 3] Average Asset Value by Risk Tier
* **ROI Projection**: There are **{int(risk_count)}** customers in the "Warning" stage, with an average historical value of **${avg_risk_val:,.2f}**.
* **Strategic Implication**: Use this average value as a benchmark to determine the maximum Customer Retention Cost (CRC) for reactivation campaigns.
"""
display(Markdown(md_text_3))

fig_bar = px.bar(
    risk_stats, x='Risk_Tier', y='avg_m', color='avg_m', text_auto='.1f',
    labels={'Risk_Tier': 'Lifecycle Stage', 'avg_m': 'Avg Contribution ($)'},
    template="plotly_white", 
    color_continuous_scale="RdYlGn_r"
)
fig_bar.update_layout(margin=dict(t=20, b=0, l=0, r=0))
fig_bar.show()

