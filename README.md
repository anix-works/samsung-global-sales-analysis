# Samsung Global Product Sales Analysis (2021–2024)

**Comparative Sales and Trends Analysis** using Python: data cleaning, exploratory analysis, statistical testing and visualization on 15,500 Samsung sales records.

| | |
|---|---|
| **University** | ITM University Gwalior, School of Computing and Intelligent Systems |
| **Course** | Data Analytics Using Python (CSL0312) |
| **Program** | B.Tech. CSE (Artificial Intelligence & Machine Learning), Semester III, Section F |
| **Academic Session** | July–Dec 2026 |
| **Project Type** | Project-Based Learning (PBL) Mini Project |
| **Domain** | Finance and Economics |
| **Author** | Gonaboyina Vamsi (BETN1AI25160) |
| **Faculty Mentor** | Dr. Sanjay Jain |

---

## Project Overview

A company that sells in many countries needs to know which markets and products earn the most, whether discounts help, and how customers behave. This project answers those questions using the Samsung Global Product Sales dataset.

The work is **data analytics only**. No machine learning model was built.

**Main objectives**
1. Clean and prepare the data (missing values, outliers, encoding, scaling).
2. Summarize sales by region, category, year and customer group.
3. Show the results with charts and give a short observation for each.
4. Test the findings with correlation and one-way ANOVA.

---

## Dataset

- **Name:** Samsung Global Product Sales Dataset
- **Source:** Kaggle (ashyou09)
- **Link:** https://www.kaggle.com/datasets/ashyou09/samsung-global-product-sales-dataset
- **Size:** 15,500 records, 28 columns
- **Period:** 1 January 2021 to 31 December 2024
- **Coverage:** 52 countries, 8 regions, 11 product categories, 7 sales channels

---

## Repository Structure

```
samsung-global-sales-analysis/
│
├── README.md
├── data_analytics_sales_samsung.ipynb      # Main notebook (all code and outputs)
├── PBL_Report_Gonaboyina_Vamsi.docx        # Project report (Word)
├── PBL_Report_Gonaboyina_Vamsi.pdf         # Project report (PDF)
│
├── data/
│   └── samsung_global_sales_dataset.csv    # Dataset (see note below)
│
└── report_figures/                         # Charts used in the report (PNG)
```

> **Note:** If the CSV file is not included in `data/`, download it from the Kaggle link above and place it in the `data/` folder.

---

## What the Notebook Covers

1. **Understanding the dataset:** structure, summary statistics, basic insights.
2. **Data cleaning and preprocessing:** missing values, duplicate and quality checks, wrangling, outliers (IQR), encoding (ordinal, binary, one-hot), standardization and normalization (Min-Max, Z-score, log transform), skewness.
3. **Exploratory analysis:** descriptive statistics, grouping and aggregation, pivot tables, transformation, filtration, joining and merging.
4. **Correlation and ANOVA:** Pearson correlation matrix and three one-way ANOVA tests.
5. **Data visualization:** Pandas plotting, Matplotlib basics, and line, area, histogram, bar, pie, box, scatter, bubble and waffle charts. Seaborn is used for regression plots.

---

## Key Findings

- Total revenue is **$22.91M** from **36,580 units** sold in 15,500 sales.
- **Europe (34.5%) and Asia (29.4%)** together give about 64% of revenue.
- **Smart TV (24.3%), Galaxy S (20.6%) and Galaxy Z (12.1%)** are the top three categories.
- **5G products** give 37.2% of revenue from about a third of sales and earn more per sale ($1,681 vs $1,379).
- **Discount has almost no link to revenue** (correlation about −0.04).
- ANOVA shows **no significant difference** in revenue across regions (p = 0.8964) or customer segments (p = 0.9174), or in rating across categories (p = 0.0867).
- About **85.9%** of sales were kept, **9.2%** returned and **4.9%** exchanged.

---

## How to Run

### Option 1: Google Colab (easiest)
1. Open [Google Colab](https://colab.research.google.com) and choose **File → Upload notebook**.
2. Upload `data_analytics_sales_samsung.ipynb`.
3. Upload `samsung_global_sales_dataset.csv` to the Colab files panel.
4. Check the file path at the top of the notebook (`DATA_PATH`) and run all cells.

### Option 2: Run on your computer
```bash
git clone https://github.com/<your-username>/samsung-global-sales-analysis.git
cd samsung-global-sales-analysis
pip install numpy pandas matplotlib seaborn scipy pywaffle jupyter
jupyter notebook data_analytics_sales_samsung.ipynb
```
Change `DATA_PATH` at the top of the notebook to `data/samsung_global_sales_dataset.csv` before running.

---

## Libraries Used

`numpy` · `pandas` · `matplotlib` · `seaborn` · `scipy` · `pywaffle`

---

## AI Tool Declaration

Claude (by Anthropic) was used to help draft and format the report text from my notebook results. The Python code, analysis and numbers were run and checked by me.

---

## Author

**Gonaboyina Vamsi**
B.Tech. CSE (AI & ML), ITM University Gwalior
Roll No.: BETN1AI25160
