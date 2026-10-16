# Comparative Sales and Trends Analysis (Samsung Global Product Sales)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange.svg)](https://jupyter.org/)
[![Course](https://img.shields.io/badge/Course-CSL0312%20Data%20Analytics-green.svg)](#)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](#)

A comprehensive data analytics project investigating **15,500 international commercial transactions** ($22.91M gross revenue) from 2021 to 2024 across 52 sovereign nations, 11 hardware categories, and 8 global regions.

---

## 📌 Project Overview
* **Institution:** ITM University Gwalior
* **School:** School of Computing and Intelligent Systems
* **Course:** Data Analytics Using Python (`CSL0312`)
* **Author / Team Leader:** Gonaboyina Vamsi (Roll No: `BETN1AI25160`)
* **Faculty Mentor:** Dr. Sanjay Jain
* **Domain:** Finance and Economics
* **Dataset:** Samsung Global Product Sales Dataset ([Kaggle](https://www.kaggle.com/datasets/ashyou09/samsung-global-sales-dataset))

---

## 📂 Repository Structure

```text
├── data_analytics_sales_samsung.ipynb   # Executable Jupyter notebook with all EDA and statistical tests
├── samsung_global_sales_dataset.csv     # Cleaned raw dataset (15,500 records x 28 columns)
├── PBL_Report_Gonaboyina_Vamsi.docx     # Formal academic project report in Word (.docx) format
├── PBL_Report_Gonaboyina_Vamsi.pdf      # Complete academic report export in PDF (.pdf) format
├── make_report_figures.py               # Standalone script to regenerate all 21 publication figures
├── figures_list.csv                     # Metadata mapping of all 21 print-ready figures
├── report_figures/                      # 300 DPI high-resolution chart images
│   ├── fig01_outlier_boxplots.png
│   ├── fig02_revenue_log_transform.png
│   ├── ...
│   └── fig21_correlation_heatmap.png
└── README.md                            # Comprehensive project overview and documentation
```

---

## 📊 Key Findings & Empirical Insights

1. **Revenue Engines:** Samsung generated **$22,911,258.88 USD** from **36,580 units**. The distribution is right-skewed (mean ticket: $1,478.15 vs median ticket: $739.38).
2. **Top Hardware Lines:** **Smart TVs** rank #1 with **$5.56M USD** (24.3%), followed by **Galaxy S smartphones** at **$4.73M USD** (20.6%) and **Galaxy Z foldables** at **$2.77M USD** (12.1%).
3. **Core Geographic Regions:** **Europe** ($7.90M, 34.5%) and **Asia** ($6.73M, 29.4%) account for **63.9%** of worldwide revenue. Regional differences are driven by order volume rather than transaction size.
4. **5G Price Premium:** 5G-capable devices contributed **37.2%** of revenue from 32.7% of orders, commanding a **+21.9% average pricing premium** ($1,681.17 vs $1,379.43 USD).
5. **Promotional Ineffectiveness:** Discount percentage shows near-zero linear correlation with revenue ($r = -0.04$). Broad-based discounts do not stimulate larger monetary purchases.
6. **ANOVA Hypothesis Testing (alpha = 0.05):**
   * Revenue across Regions: $F = 0.4105, p = 0.8964$ (No significant difference)
   * Revenue across Customer Segments: $F = 0.2373, p = 0.9174$ (No significant difference)
   * Satisfaction Rating across Categories: $F = 1.6482, p = 0.0867$ (No significant difference)
7. **Order Fulfillment:** **85.9%** of orders were kept, **9.2%** returned, and **4.9%** exchanged. Galaxy Z foldables had the highest return rate at **10.9%**.

---

## 🛠️ Technologies Used
* **Language:** Python 3.9+
* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`, `pywaffle`
* **Statistical Computing:** `scipy.stats`
* **Document Formatting:** `python-docx`

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/anix-works/samsung-global-sales-analysis.git
cd samsung-global-sales-analysis

# Install required dependencies
pip install pandas numpy matplotlib seaborn scipy pywaffle python-docx

# Regenerate all 21 high-resolution figures
python make_report_figures.py

# Launch the Jupyter Notebook
jupyter notebook data_analytics_sales_samsung.ipynb
```

---

## 📜 License & Acknowledgments
Dataset provided by [ashyou09 on Kaggle](https://www.kaggle.com/datasets/ashyou09/samsung-global-sales-dataset). Project submitted for academic evaluation at ITM University Gwalior.
