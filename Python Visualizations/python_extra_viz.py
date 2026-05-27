import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # required for 3D plotting


# ============================================================
# 1. COPY / PASTE YOUR FILE PATH HERE
# ============================================================

FILE_PATH = r"C:\Users\brand\OneDrive\Desktop\Tableau Final Project\Final_Production_Tableau_Dataset_CENSUS_GEOGRAPHY.csv"


def load_data(file_path: str) -> pd.DataFrame:
    if file_path.lower().endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.lower().endswith((".xlsx", ".xls")):
        return pd.read_excel(file_path)
    else:
        raise ValueError("File must be a .csv, .xlsx, or .xls file.")


df = load_data(FILE_PATH)

output_dir = os.path.dirname(FILE_PATH)
if output_dir == "":
    output_dir = "."

county_cols = [
    "County_FIPS",
    "Dashboard_Label",
    "State",
    "State_Abbrev",
    "Region",
    "Urban_Rural"
]

county_metrics = {
    "Population": "max",
    "Poverty_Rate_Pct": "mean",
    "Obesity_Rate_Pct": "mean",
    "Fast_Food_Per_10K": "mean",
    "Composite_Risk_Score": "mean",
    "Risk_Percentile": "mean",
    "Fast_Food_Locations": "max"
}

county_df = (
    df.groupby(county_cols, as_index=False)
      .agg(county_metrics)
)

# Optional sampling so scatterplots remain readable
sample_n = min(2500, len(county_df))
plot_df = county_df.sample(sample_n, random_state=42)


plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    plot_df["Poverty_Rate_Pct"],
    plot_df["Obesity_Rate_Pct"],
    s=plot_df["Fast_Food_Per_10K"] * 8,
    c=plot_df["Risk_Percentile"],
    alpha=0.55
)

plt.xlabel("Poverty Rate (%)")
plt.ylabel("Obesity Rate (%)")
plt.title("County Poverty vs. Obesity\nBubble Size = Fast-Food Density, Color = Risk Percentile")

# Trend line
x = plot_df["Poverty_Rate_Pct"]
y = plot_df["Obesity_Rate_Pct"]
coef = np.polyfit(x, y, 1)
trend = np.poly1d(coef)
plt.plot(np.sort(x), trend(np.sort(x)), linewidth=2)

plt.colorbar(scatter, label="Risk Percentile")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "graph_1_poverty_vs_obesity.png"), dpi=300)
plt.close()


regions = ["Northeast", "Midwest", "South", "West"]
box_data = [
    county_df.loc[county_df["Region"] == region, "Composite_Risk_Score"].dropna()
    for region in regions
]

plt.figure(figsize=(9, 6))
plt.boxplot(box_data, labels=regions, showmeans=True)

plt.xlabel("Region")
plt.ylabel("Composite Risk Score")
plt.title("Distribution of County Risk Scores by U.S. Region")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "graph_2_regional_risk_boxplot.png"), dpi=300)
plt.close()


category_df = (
    df.groupby("Category", as_index=False)["Estimated_Locations"]
      .sum()
      .sort_values("Estimated_Locations", ascending=True)
)

plt.figure(figsize=(10, 6))
plt.barh(category_df["Category"], category_df["Estimated_Locations"])

plt.xlabel("Estimated Locations")
plt.ylabel("Fast-Food Category")
plt.title("Estimated Fast-Food Locations by Category")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "graph_3_fast_food_category_mix.png"), dpi=300)
plt.close()


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

p = ax.scatter(
    plot_df["Poverty_Rate_Pct"],
    plot_df["Obesity_Rate_Pct"],
    plot_df["Fast_Food_Per_10K"],
    c=plot_df["Risk_Percentile"],
    alpha=0.65
)

ax.set_xlabel("Poverty Rate (%)")
ax.set_ylabel("Obesity Rate (%)")
ax.set_zlabel("Fast-Food Locations per 10K")
ax.set_title("Bonus 3D View: Poverty, Obesity, and Fast-Food Density")

fig.colorbar(p, ax=ax, label="Risk Percentile", shrink=0.65)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "graph_4_3d_risk_scatter.png"), dpi=300)
plt.close()


print("Graphs created successfully:")
print("1. graph_1_poverty_vs_obesity.png")
print("2. graph_2_regional_risk_boxplot.png")
print("3. graph_3_fast_food_category_mix.png")
print("4. graph_4_3d_risk_scatter.png")