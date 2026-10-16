"""
make_report_figures.py
Generates 21 high-resolution, print-optimized figures for the Samsung Sales Analysis PBL Report.
Target: A4 print width 15.5 cm (6.1 in) and 13.0 cm (5.1 in), 300 DPI, minimum 9pt text, B&W distinct.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pywaffle import Waffle

# --- Output Directory ---
out_dir = "/Users/gonaboyinavamsi/Desktop/Zxcvbnm,.:1/src/sem2/DA/pbl /report_figures"
os.makedirs(out_dir, exist_ok=True)

# --- Global RC Parameters ---
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.8,
    "lines.markersize": 5,
    "savefig.dpi": 300,
    "figure.dpi": 100,
})

# Custom Palette suitable for color and distinct in grayscale
COLOR_PRIMARY = "#1F4E79"    # Steel navy blue
COLOR_SECONDARY = "#D95F02"  # Distinct burnt orange
COLOR_ACCENT = "#555555"     # Mid grey
COLOR_LIGHT = "#CCCCCC"      # Light grey
COLOR_GREEN = "#2E7D32"      # Dark forest green

# Helper to style spines and grid
def style_ax(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#444444")
    ax.spines["bottom"].set_color("#444444")
    ax.grid(True, linestyle="--", alpha=0.3, color="#888888")

# --- Load & Clean Dataset ---
csv_path = "/Users/gonaboyinavamsi/Desktop/Zxcvbnm,.:1/src/sem2/DA/pbl /samsung_global_sales_dataset.csv"
df = pd.read_csv(csv_path)

# Cleaning steps matching the notebook
df['customer_age_group'] = df['customer_age_group'].str.replace('–', '-')
df['storage'] = df['storage'].fillna('Not_Applicable')
df['previous_device_os'] = df['previous_device_os'].fillna('Unknown')
median_rating = df['customer_rating'].median()
df['customer_rating'] = df['customer_rating'].fillna(median_rating)
df['log_revenue'] = np.log1p(df['revenue_usd'])
df['is_5g_clean'] = df['is_5g'].map({'Yes': '5G', 'No': 'Non-5G', True: '5G', False: 'Non-5G', 1: '5G', 0: 'Non-5G'})

print("--- DATA INTEGRITY CHECK ---")
print(f"Total Rows: {len(df):,}")
print(f"Europe Revenue: ${df[df['region']=='Europe']['revenue_usd'].sum()/1e6:.2f}M")
print(f"Asia Revenue: ${df[df['region']=='Asia']['revenue_usd'].sum()/1e6:.2f}M")
print(f"Smart TV Revenue: ${df[df['category']=='Smart TV']['revenue_usd'].sum()/1e6:.2f}M")
yr_revs = df.groupby('year')['revenue_usd'].sum() / 1e6
for yr, val in yr_revs.items():
    print(f"  {yr} Revenue: ${val:.2f}M")
ret_pcts = df['return_status'].value_counts(normalize=True) * 100
for st, val in ret_pcts.items():
    print(f"  Return status {st}: {val:.1f}%")
corr_val = df[['unit_price_usd', 'revenue_usd']].corr().iloc[0, 1]
print(f"Unit price vs revenue correlation: {corr_val:.2f}")
print("----------------------------\n")

# =========================================================================
# SECTION 3: DATA CLEANING CHARTS
# =========================================================================

# --- 1. fig01_outlier_boxplots.png (Two-panel: 6.1 x 3.4 in) ---
fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.4))
for ax in axes:
    style_ax(ax)

sns.boxplot(y=df['unit_price_usd'], ax=axes[0], color=COLOR_PRIMARY,
            boxprops=dict(edgecolor='black', linewidth=1),
            medianprops=dict(color='yellow', linewidth=2),
            flierprops=dict(marker='o', markersize=3, alpha=0.35, color='black'))
axes[0].set_title("Unit Price (USD)")
axes[0].set_ylabel("Unit Price (USD)")
axes[0].set_ylim(0, 5800)

sns.boxplot(y=df['revenue_usd'], ax=axes[1], color=COLOR_SECONDARY,
            boxprops=dict(edgecolor='black', linewidth=1),
            medianprops=dict(color='yellow', linewidth=2),
            flierprops=dict(marker='o', markersize=3, alpha=0.35, color='black'))
axes[1].set_title("Revenue (USD)")
axes[1].set_ylabel("Revenue (USD)")
axes[1].set_ylim(0, 50000)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig01_outlier_boxplots.png"), dpi=300, facecolor="white")
plt.close()

# --- 2. fig02_revenue_log_transform.png (Two-panel: 6.1 x 3.4 in) ---
fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.4))
for ax in axes:
    style_ax(ax)

axes[0].hist(df['revenue_usd'], bins=30, color=COLOR_PRIMARY, edgecolor='black', linewidth=0.6, alpha=0.85)
axes[0].set_title("Original Revenue Distribution")
axes[0].set_xlabel("Revenue (USD)")
axes[0].set_ylabel("Number of Transactions")

axes[1].hist(df['log_revenue'], bins=30, color=COLOR_SECONDARY, edgecolor='black', linewidth=0.6, alpha=0.85)
axes[1].set_title("Log-Transformed Revenue")
axes[1].set_xlabel("log(1 + Revenue in USD)")
axes[1].set_ylabel("Number of Transactions")

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig02_revenue_log_transform.png"), dpi=300, facecolor="white")
plt.close()

# =========================================================================
# SECTION 5: DATA VISUALIZATION CHARTS
# =========================================================================

# --- 3. fig03_units_by_region_pandas.png (Vertical bar: 6.1 x 3.8 in) ---
# Strictly drawn with df.plot(kind="bar") as requested
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

units_by_reg = df.groupby('region')['units_sold'].sum().sort_values(ascending=False)
bars = units_by_reg.plot(kind="bar", color=COLOR_PRIMARY, edgecolor="black", linewidth=0.6, ax=ax)
ax.set_xlabel("Geographic Region")
ax.set_ylabel("Units Sold")
ax.set_xticklabels(units_by_reg.index, rotation=40, ha="right")

for bar in ax.patches:
    h = bar.get_height()
    ax.annotate(f"{int(h):,}",
                (bar.get_x() + bar.get_width() / 2, h + 150),
                ha="center", va="bottom", fontsize=8.5, color="black")

ax.set_ylim(0, units_by_reg.max() * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig03_units_by_region_pandas.png"), dpi=300, facecolor="white")
plt.close()

# --- 4. fig04_matplotlib_subplots.png (Two-panel: 6.1 x 3.4 in) ---
fig, axes = plt.subplots(1, 2, figsize=(6.1, 3.4))
for ax in axes:
    style_ax(ax)

yr_units = df.groupby('year')['units_sold'].sum()
axes[0].plot(yr_units.index, yr_units.values, marker='s', color=COLOR_PRIMARY, linewidth=2, markersize=6)
axes[0].set_title("Annual Units Sold")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Units Sold")
axes[0].set_xticks([2021, 2022, 2023, 2024])
for x, y in zip(yr_units.index, yr_units.values):
    axes[0].annotate(f"{y:,}", (x, y + 40), ha="center", fontsize=8.5)
axes[0].set_ylim(8500, 9600)

top5_cat = df.groupby('category')['revenue_usd'].sum().sort_values(ascending=False).head(5) / 1e6
top5_cat = top5_cat.sort_values(ascending=True) # horizontal from bottom to top
axes[1].barh(top5_cat.index, top5_cat.values, color=COLOR_SECONDARY, edgecolor='black', linewidth=0.6)
axes[1].set_title("Top 5 Categories by Revenue")
axes[1].set_xlabel("Revenue (USD Millions)")
for bar in axes[1].patches:
    w = bar.get_width()
    axes[1].annotate(f"${w:.2f}M", (w + 0.1, bar.get_y() + bar.get_height()/2),
                     ha="left", va="center", fontsize=8.5)
axes[1].set_xlim(0, top5_cat.max() * 1.25)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig04_matplotlib_subplots.png"), dpi=300, facecolor="white")
plt.close()

# --- 5. fig05_revenue_by_region.png (Horizontal bar: 6.1 x 3.8 in) ---
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

reg_rev = (df.groupby('region')['revenue_usd'].sum().sort_values(ascending=True) / 1e6)
bars = ax.barh(reg_rev.index, reg_rev.values, color=COLOR_PRIMARY, edgecolor="black", linewidth=0.6)
ax.set_xlabel("Revenue (USD Millions)")
ax.set_ylabel("Geographic Region")

for bar in bars:
    w = bar.get_width()
    ax.annotate(f"${w:.2f}M", (w + 0.15, bar.get_y() + bar.get_height()/2),
                ha="left", va="center", fontsize=8.5)

ax.set_xlim(0, reg_rev.max() * 1.18)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig05_revenue_by_region.png"), dpi=300, facecolor="white")
plt.close()

# --- 6. fig06_revenue_by_category.png (Horizontal bar, 11 categories: 6.1 x 4.0 in) ---
plt.figure(figsize=(6.1, 4.0))
ax = plt.gca()
style_ax(ax)

cat_rev = (df.groupby('category')['revenue_usd'].sum().sort_values(ascending=True) / 1e6)
bars = ax.barh(cat_rev.index, cat_rev.values, color=COLOR_PRIMARY, edgecolor="black", linewidth=0.6)
ax.set_xlabel("Revenue (USD Millions)")
ax.set_ylabel("Product Category")

for bar in bars:
    w = bar.get_width()
    ax.annotate(f"${w:.2f}M", (w + 0.08, bar.get_y() + bar.get_height()/2),
                ha="left", va="center", fontsize=8.5)

ax.set_xlim(0, cat_rev.max() * 1.18)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig06_revenue_by_category.png"), dpi=300, facecolor="white")
plt.close()

# --- 7. fig07_5g_vs_non5g.png (Vertical bar with hatching: 6.1 x 3.4 in) ---
plt.figure(figsize=(6.1, 3.4))
ax = plt.gca()
style_ax(ax)

g5_rev = (df.groupby('is_5g_clean')['revenue_usd'].sum().loc[['Non-5G', '5G']] / 1e6)
colors = [COLOR_PRIMARY, COLOR_SECONDARY]
hatches = ['//', '..']
bars = ax.bar(g5_rev.index, g5_rev.values, color=colors, edgecolor='black', linewidth=0.8, width=0.45)

for bar, h in zip(bars, hatches):
    bar.set_hatch(h)
    h_val = bar.get_height()
    ax.annotate(f"${h_val:.2f}M\n({h_val/g5_rev.sum()*100:.1f}%)",
                (bar.get_x() + bar.get_width()/2, h_val + 0.35),
                ha="center", va="bottom", fontsize=9, fontweight="bold")

ax.set_ylabel("Revenue (USD Millions)")
ax.set_xlabel("Hardware Connectivity")
ax.set_ylim(0, g5_rev.max() * 1.25)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig07_5g_vs_non5g.png"), dpi=300, facecolor="white")
plt.close()

# --- 8. fig08_yearly_revenue.png (Line with markers: 6.1 x 3.4 in) ---
plt.figure(figsize=(6.1, 3.4))
ax = plt.gca()
style_ax(ax)

yr_rev = df.groupby('year')['revenue_usd'].sum() / 1e6
ax.plot(yr_rev.index, yr_rev.values, marker='o', color=COLOR_PRIMARY, linewidth=2.2, markersize=7)

for x, y in zip(yr_rev.index, yr_rev.values):
    ax.annotate(f"${y:.2f}M", (x, y + 0.035), ha="center", va="bottom", fontsize=9, fontweight="bold")

ax.set_xticks([2021, 2022, 2023, 2024])
ax.set_xlabel("Calendar Year")
ax.set_ylabel("Revenue (USD Millions)")
ax.set_ylim(5.45, 6.05)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig08_yearly_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 9. fig09_monthly_revenue.png (Line Jan to Dec: 6.1 x 3.4 in) ---
plt.figure(figsize=(6.1, 3.4))
ax = plt.gca()
style_ax(ax)

month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]
mo_rev = (df.groupby('month')['revenue_usd'].sum() / 1e6).reindex(month_order)
months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

x_indices = list(range(1, 13))
y_vals = mo_rev.values
ax.plot(x_indices, y_vals, marker='D', color=COLOR_PRIMARY, linewidth=2.0, markersize=5.5)

# Label key min and max points (using 1-based integer x-coordinates)
min_idx = int(np.argmin(y_vals)) + 1
max_idx = int(np.argmax(y_vals)) + 1
min_val = float(np.min(y_vals))
max_val = float(np.max(y_vals))

ax.annotate(f"Lowest: ${min_val:.2f}M", (min_idx, min_val - 0.08),
            ha="center", fontsize=8.5, fontweight="bold", color="#A00000")
ax.annotate(f"Peak: ${max_val:.2f}M", (max_idx, max_val + 0.05),
            ha="center", fontsize=8.5, fontweight="bold", color=COLOR_PRIMARY)

ax.set_xticks(x_indices)
ax.set_xticklabels(months_short)
ax.set_xlabel("Calendar Month")
ax.set_ylabel("Revenue (USD Millions)")
ax.set_ylim(1.50, 2.25)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig09_monthly_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 10. fig10_regional_area.png (Stacked area: 6.1 x 3.8 in) ---
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

piv_reg = df.pivot_table(index='year', columns='region', values='revenue_usd', aggfunc='sum') / 1e6
# Sort columns by total revenue descending
col_order = piv_reg.sum().sort_values(ascending=False).index
piv_reg = piv_reg[col_order]

# Grayscale-distinct palette
area_colors = [
    "#1F4E79", "#2B5C8F", "#4682B4", "#708090",
    "#D95F02", "#E67E22", "#F39C12", "#A6ACAF"
]

ax.stackplot(piv_reg.index, piv_reg.T.values, labels=piv_reg.columns, colors=area_colors[:len(col_order)], alpha=0.9)
ax.set_xticks([2021, 2022, 2023, 2024])
ax.set_xlabel("Calendar Year")
ax.set_ylabel("Stacked Revenue (USD Millions)")
ax.set_ylim(0, 6.5)
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=False, fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig10_regional_area.png"), dpi=300, facecolor="white")
plt.close()

# --- 11. fig11_histograms.png (3-panel: 6.1 x 3.2 in) ---
fig, axes = plt.subplots(1, 3, figsize=(6.1, 3.2))
for ax in axes:
    style_ax(ax)

axes[0].hist(df['revenue_usd'], bins=25, color=COLOR_PRIMARY, edgecolor='black', linewidth=0.5, alpha=0.85)
axes[0].set_title("Raw Revenue (USD)", fontsize=9)
axes[0].set_xlabel("Revenue ($)")
axes[0].set_ylabel("Count")

axes[1].hist(df['log_revenue'], bins=25, color=COLOR_SECONDARY, edgecolor='black', linewidth=0.5, alpha=0.85)
axes[1].set_title("Log Revenue", fontsize=9)
axes[1].set_xlabel("log(1 + Rev)")
axes[1].set_ylabel("Count")

axes[2].hist(df['customer_rating'], bins=15, color=COLOR_ACCENT, edgecolor='black', linewidth=0.5, alpha=0.85)
axes[2].set_title("Customer Rating", fontsize=9)
axes[2].set_xlabel("Rating (Stars)")
axes[2].set_ylabel("Count")

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig11_histograms.png"), dpi=300, facecolor="white")
plt.close()

# --- 12. fig12_boxplot_by_category.png (Horizontal boxplot: 6.1 x 4.0 in) ---
# Note: Horizontal layout makes 11 category labels perfectly readable
plt.figure(figsize=(6.1, 4.0))
ax = plt.gca()
style_ax(ax)

# Order categories by median revenue ascending so highest is at top
cat_order = df.groupby('category')['revenue_usd'].median().sort_values(ascending=True).index

sns.boxplot(data=df, y='category', x='revenue_usd', order=cat_order, ax=ax,
            color=COLOR_PRIMARY,
            boxprops=dict(edgecolor='black', linewidth=0.8),
            medianprops=dict(color='yellow', linewidth=1.5),
            flierprops=dict(marker='o', markersize=2.5, alpha=0.3))

ax.set_ylabel("Product Category")
ax.set_xlabel("Revenue (USD)")
ax.set_xlim(0, 48000)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig12_boxplot_by_category.png"), dpi=300, facecolor="white")
plt.close()

# --- 13. fig13_discount_vs_revenue.png (Scatter: 6.1 x 3.6 in) ---
plt.figure(figsize=(6.1, 3.6))
ax = plt.gca()
style_ax(ax)

ax.scatter(df['discount_pct'], df['revenue_usd'], color=COLOR_PRIMARY, alpha=0.35, s=12, edgecolors='none')
# Add horizontal trendline (OLS)
m, b = np.polyfit(df['discount_pct'], df['revenue_usd'], 1)
x_vals = np.array([0, 20])
ax.plot(x_vals, m * x_vals + b, color='red', linestyle='--', linewidth=1.8, label=f"Trend line (slope ≈ 0, r = -0.04)")

ax.set_xlabel("Promotional Discount (%)")
ax.set_ylabel("Revenue (USD)")
ax.set_xlim(-0.5, 20.5)
ax.set_ylim(-500, 50000)
ax.legend(loc="upper right", frameon=True, fontsize=8.5)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig13_discount_vs_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 14. fig14_units_vs_revenue.png (Scatter: 6.1 x 3.6 in) ---
plt.figure(figsize=(6.1, 3.6))
ax = plt.gca()
style_ax(ax)

ax.scatter(df['units_sold'], df['revenue_usd'], color=COLOR_SECONDARY, alpha=0.35, s=14, edgecolors='none')
m, b = np.polyfit(df['units_sold'], df['revenue_usd'], 1)
x_vals = np.array([1, 10])
ax.plot(x_vals, m * x_vals + b, color=COLOR_PRIMARY, linestyle='--', linewidth=1.8, label=f"Trend line (r = +0.49)")

ax.set_xlabel("Units Sold (Quantity)")
ax.set_ylabel("Revenue (USD)")
ax.set_xticks(range(1, 11))
ax.set_xlim(0.5, 10.5)
ax.set_ylim(-500, 50000)
ax.legend(loc="upper left", frameon=True, fontsize=8.5)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig14_units_vs_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 15. fig15_bubble_price_revenue.png (Bubble: 6.1 x 3.8 in) ---
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

# Top categories mapped, others to Other to keep legend clean and readable
top_cats = ['Smart TV', 'Galaxy S', 'Galaxy Z', 'Galaxy Tab', 'Appliances']
df['cat_grouped'] = df['category'].apply(lambda x: x if x in top_cats else 'Other')

palette_bubble = {
    'Smart TV': '#1F4E79',
    'Galaxy S': '#D95F02',
    'Galaxy Z': '#7570B3',
    'Galaxy Tab': '#1B9E77',
    'Appliances': '#E7298A',
    'Other': '#999999'
}

for cat_name, col in palette_bubble.items():
    sub = df[df['cat_grouped'] == cat_name]
    ax.scatter(sub['unit_price_usd'], sub['revenue_usd'],
               s=sub['units_sold'] * 12, color=col, alpha=0.35, edgecolors='none', label=cat_name)

ax.set_xlabel("Unit Price (USD)")
ax.set_ylabel("Revenue (USD)")
ax.set_xlim(-50, 5600)
ax.set_ylim(-500, 50000)
ax.legend(loc="upper left", frameon=True, fontsize=8, title="Category (Size = Units)")

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig15_bubble_price_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 16. fig16_return_pie.png (Pie chart: 5.1 x 4.0 in) ---
plt.figure(figsize=(5.1, 4.0))
ax = plt.gca()

ret_data = df['return_status'].value_counts()
# Percentage & name on slice, distinct B&W shades
pie_colors = ["#1F4E79", "#D95F02", "#CCCCCC"]
labels = [f"{idx}\n{val:,} ({val/len(df)*100:.1f}%)" for idx, val in zip(ret_data.index, ret_data.values)]

wedges, texts = ax.pie(
    ret_data.values,
    labels=labels,
    colors=pie_colors,
    startangle=140,
    textprops=dict(fontsize=9, fontweight="bold"),
    wedgeprops=dict(edgecolor="black", linewidth=0.8)
)
ax.axis("equal")

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig16_return_pie.png"), dpi=300, facecolor="white")
plt.close()

# --- 17. fig17_return_waffle.png (Waffle chart: 5.1 x 4.0 in) ---
ret_pct_waffle = (df['return_status'].value_counts(normalize=True)*100).round().astype(int).to_dict()

fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=ret_pct_waffle,
    colors=["#1F4E79", "#D95F02", "#A6ACAF"],
    figsize=(5.1, 4.0),
    legend={
        'loc': 'lower center',
        'bbox_to_anchor': (0.5, -0.15),
        'ncol': 3,
        'frameon': False,
        'fontsize': 9
    }
)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig17_return_waffle.png"), dpi=300, facecolor="white")
plt.close()

# --- 18. fig18_top10_countries.png (Horizontal bar: 6.1 x 3.8 in) ---
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

top10 = (df.groupby('country')['revenue_usd'].sum().sort_values(ascending=True).tail(10) / 1e3)
bars = ax.barh(top10.index, top10.values, color=COLOR_PRIMARY, edgecolor="black", linewidth=0.6)
ax.set_xlabel("Revenue (USD Thousands)")
ax.set_ylabel("Country")

for bar in bars:
    w = bar.get_width()
    ax.annotate(f"${w:.1f}K", (w + 6, bar.get_y() + bar.get_height()/2),
                ha="left", va="center", fontsize=8.5)

ax.set_xlim(0, top10.max() * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig18_top10_countries.png"), dpi=300, facecolor="white")
plt.close()

# --- 19. fig19_regplot_price_revenue.png (Seaborn regplot: 6.1 x 3.8 in) ---
plt.figure(figsize=(6.1, 3.8))
ax = plt.gca()
style_ax(ax)

# Plot sample for clean dots plus line
sample_sub = df.sample(3000, random_state=42)
sns.regplot(data=sample_sub, x='unit_price_usd', y='revenue_usd', ax=ax,
            scatter_kws={'alpha': 0.20, 'color': COLOR_PRIMARY, 's': 12},
            line_kws={'color': 'red', 'linewidth': 2.0, 'label': 'Regression Line (r = +0.68)'})

ax.set_xlabel("Unit Catalog Price (USD)")
ax.set_ylabel("Revenue (USD)")
ax.set_xlim(-50, 5600)
ax.set_ylim(-500, 50000)
ax.legend(loc="upper left", frameon=True, fontsize=8.5)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig19_regplot_price_revenue.png"), dpi=300, facecolor="white")
plt.close()

# --- 20. fig20_lmplot_by_5g.png (Seaborn lmplot: 6.1 x 3.8 in) ---
# Set height and aspect so width = height * aspect = 3.8 * (6.1/3.8) = 6.1 in
sample_lm = df.sample(3000, random_state=42)
g = sns.lmplot(
    data=sample_lm,
    x='unit_price_usd',
    y='revenue_usd',
    hue='is_5g_clean',
    palette={'5G': COLOR_PRIMARY, 'Non-5G': COLOR_SECONDARY},
    height=3.8,
    aspect=6.1/3.8,
    scatter_kws={'alpha': 0.20, 's': 12},
    line_kws={'linewidth': 2.0},
    legend=False
)
ax = g.ax
style_ax(ax)
ax.set_xlabel("Unit Catalog Price (USD)")
ax.set_ylabel("Revenue (USD)")
ax.set_xlim(-50, 5600)
ax.set_ylim(-500, 50000)
ax.legend(title="Connectivity", loc="upper left", frameon=True, fontsize=8.5)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig20_lmplot_by_5g.png"), dpi=300, facecolor="white")
plt.close()

# =========================================================================
# SECTION 6: STATISTICAL ANALYSIS CHARTS
# =========================================================================

# --- 21. fig21_correlation_heatmap.png (Correlation heatmap: 5.1 x 4.4 in) ---
plt.figure(figsize=(5.1, 4.4))
ax = plt.gca()

corr_cols = ['unit_price_usd', 'discount_pct', 'units_sold', 'revenue_usd', 'customer_rating']
labels = ['Price', 'Discount', 'Units', 'Revenue', 'Rating']
corr_matrix = df[corr_cols].corr()

sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="Blues",
            xticklabels=labels, yticklabels=labels, ax=ax,
            cbar_kws={'shrink': 0.85, 'label': 'Pearson Correlation (r)'},
            annot_kws={'size': 9.5, 'weight': 'bold'})

ax.set_xticklabels(labels, rotation=0, ha="center")
ax.set_yticklabels(labels, rotation=0, va="center")

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig21_correlation_heatmap.png"), dpi=300, facecolor="white")
plt.close()

print("All 21 figures generated successfully!")
