# Socioeconomic Foodscapes
### *Analyzing the Intersection of Poverty, Obesity, and Fast Food Density in the United States*

---

## Project Team & Course Context
* **Course:** BUSN 32130 Data Visualization
* **Institution:** University of Chicago Booth School of Business
* **Team:** Brandt Burgdorf, Serge Wen, Maggie Xu

---

## Project Motivation
While adult obesity is frequently framed as an isolated matter of personal lifestyle, it is deeply intertwined with systemic socioeconomic factors and local food environments. This project explores how a community’s commercial environment and economic status influence public health outcomes. 

This dashboard is intended to help public health officials, community policymakers, and urban planners make better decisions about resource allocation and food-access zoning by showing the geographic and statistical correlations between poverty, obesity, and fast-food density."

---

## Core Hypothesis
U.S. counties with higher poverty rates will exhibit a statistically significant positive correlation with adult obesity rates and a higher concentration of fast-food points of interest (POIs).

---

### Data Sources & Architecture

| Data Source | Type | Scope / Limitations |
| :--- | :--- | :--- |
| [US Fast Food Restaurants (Kaggle)](https://www.kaggle.com/datasets/khushishahh/fast-food-restaurants-across-us) | CSV | 10,000 geolocated entries. Not a complete census. |
| [Global McDonald's Stores (Kaggle)](https://www.kaggle.com/datasets/forveryou/mcdonalds-stores-data) | CSV | Complete 2023 global corporate roster. |
| [Top 50 Fast Food Chains (Kaggle)](https://www.kaggle.com/datasets/stetsondone/top50fastfood) | CSV | National brand metrics & categories. | 
| [US Poverty Data (US Census Bureau)](https://www.census.gov/data/datasets/2023/demo/saipe/2023-state-and-county.html) | CSV | Comprehensive 2023 SAIPE state/county metrics. |
| [Geolocated Obesity Rates (CDC PLACES)](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) | API / CSV | Comprehensive county-level health prevalence. |
| [Adult Obesity Prevalence (CDC)](https://www.cdc.gov/obesity/data-and-statistics/adult-obesity-prevalence-maps.html) | Report Data | Layered age-bracket/demographic groups. |

### Data Preparation
1. **Deduplication & Standardization:** Cleaning fast-food chain nomenclature (e.g., standardizing `McDonalds`, `McDonald's`, and `mcdonalds`) to ensure proper grouping.
2. **Spatial Join / Aggregation:** Translating point-level coordinate data (Latitude/Longitude) into unique US County FIPS codes using GIS tools / Tableau spatial blending. Extrapolate additional datapoints to create larger more complete dataset overall. Our final dataset had over 25k rows.
3. **Feature Engineering:** Creating calculated fields for population-normalized metrics within Tableau:
   $$\text{Fast Food Density} = \left( \frac{\text{Total Restaurants}}{\text{County Population}} \right) \times 10,000$$

---

## Application of Class Principles

The team’s most important takeaway is that **normalization and data structure matter more than raw visual complexity**. 

We used **Gestalt principles of similarity and proximity** by keeping all risk-related views in a consistent color family and grouping related charts close together, so users can naturally connect the map, scatterplot, and ranked county views as part of one story. Additionally, we used **visual hierarchy** by placing the macro geographic view first, then the analytical correlation views, and finally the county/category drill-down views. We used **preattentive attributes** such as darker color intensity for higher-risk counties and larger mark size for higher fast-food density so that extreme cases stand out before users even read the labels. Lastly, we applied **exploratory vs. explanatory balance** by making the dashboard interactive enough for drill-down, but still structured around a clear narrative: where risk is highest, what factors are associated with it, and what actions might follow.

---

| Discovered Data Pattern | Strategic Insight | Recommended Action |
| :--- | :--- | :--- |
| **High-Poverty Southern Cluster** | The South contains the largest concentration of high-risk counties (**987**), suggesting a structural rather than isolated pattern. | Prioritize regional nutrition-access funding, obesity prevention, and healthy retail incentives in Southern counties. |
| **High Poverty + High Obesity Overlap** | Counties above the national poverty benchmark of **14.6%** often also sit above the national obesity benchmark of **33.2%**. | Use poverty-obesity overlap to target preventative health outreach and food-access interventions. |
| **Fast-Food Density as a Better Signal Than Raw Count** | County fast-food density is much more informative than raw restaurant count because it controls for population scale. | Use density-based thresholds, not raw location totals, when screening high-priority counties. |
| **Category Concentration Risk** | Burger and chicken categories account for the largest estimated location totals in the analytical file, indicating category dominance rather than balanced food environments. | Use category-mix monitoring when evaluating whether new fast-food permits worsen local concentration. |
| **County-Level Outliers** | Some counties dramatically exceed average poverty, obesity, and risk thresholds and appear repeatedly at the top of county rankings. | Treat top-ranked counties as immediate intervention candidates for pilot programs and resource testing. |


---

### AI Usage Statement

* **Data Wrangling & Exploratory Python Visualization:** AI was utilized to write initial exploratory Python scripts to inspect the underlying structure of the original datasets. This helped identify data quality anomalies, structural gaps, missing coordinates, and text discrepancies across thousands of rows. We also used AI for initial drafts of Python visualizations.
* **Data Cleaning & Standardization Workflow:** AI assisted in designing the logical workflows required to standardize data and ensure data aggregation within Tableau would not result in duplicate counts. AI also helped embed US county census data into our main data source that otherwise did not exist in our original tables. It was also instructed to extrapolate data to create a larger more thorough dataset for use in chloropleth main map. 
* **Tableau Visualization Technical Instructions:** AI provided step-by-step guidance on fixing diagrams natively within Tableau but did not directly create our final dashboard itself.
