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

This dashboard is intended to help public health officials, community policymakers, and urban planners make better decisions about resource allocation and food-access zoning by showing the geographic and statistical correlations between poverty, obesity, and fast-food density.

---

## Core Hypothesis
U.S. counties with higher poverty rates will exhibit a statistically significant positive correlation with adult obesity rates and a higher concentration of fast-food locations.

---

### Data Sources

| Data Source | Type | Scope / Limitations |
| :--- | :--- | :--- |
| [US Fast Food Restaurants (Kaggle)](https://www.kaggle.com/datasets/khushishahh/fast-food-restaurants-across-us) | CSV | 10,000 geolocated entries. Not a complete census. |
| [Global McDonald's Stores (Kaggle)](https://www.kaggle.com/datasets/forveryou/mcdonalds-stores-data) | CSV | Complete 2023 global corporate roster. |
| [Top 50 Fast Food Chains (Kaggle)](https://www.kaggle.com/datasets/stetsondone/top50fastfood) | CSV | National brand metrics & categories. | 
| [US Poverty Data (US Census Bureau)](https://www.census.gov/data/datasets/2023/demo/saipe/2023-state-and-county.html) | CSV | Comprehensive 2023 SAIPE state/county metrics. |
| [Geolocated Obesity Rates (CDC PLACES)](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) | API / CSV | Comprehensive county-level health prevalence. |
| [Adult Obesity Prevalence (CDC)](https://www.cdc.gov/obesity/data-and-statistics/adult-obesity-prevalence-maps.html) | Report Data | Layered age-bracket/demographic groups. |

---
## Data Patterns and Recommended Actions

| Discovered Data Pattern | Strategic Insight | Recommended Action |
| :--- | :--- | :--- |
| **High-Poverty Southern Cluster** | The South contains the largest concentration of high-risk counties (**987**), suggesting a structural rather than isolated pattern. | Prioritize regional nutrition-access funding, obesity prevention, and healthy retail incentives in Southern counties. |
| **High Poverty + High Obesity Overlap** | Counties above the national poverty benchmark of **14.6%** often also sit above the national obesity benchmark of **33.2%**. | Use poverty-obesity overlap to target preventative health outreach and food-access interventions. |
| **Fast-Food Density as a Better Signal Than Raw Count** | County fast-food density is much more informative than raw restaurant count because it controls for population scale. | Use density-based thresholds, not raw location totals, when screening high-priority counties. |
| **Category Concentration Risk** | Burger and chicken categories account for the largest estimated location totals in the analytical file, indicating category dominance rather than balanced food environments. | Use category-mix monitoring when evaluating whether new fast-food permits worsen local concentration. |
| **County-Level Outliers** | Some counties dramatically exceed average poverty, obesity, and risk thresholds and appear repeatedly at the top of county rankings. | Treat top-ranked counties as immediate intervention candidates for pilot programs and resource testing. |

---

## Additional Notes

Please view the "Additional Notes" file for more detail on our data preparation, dashboard design process, application of class principles, project limitations and assumptions.

---

### AI Usage Statement

* AI was utilized to write initial exploratory Python scripts to inspect the underlying structure of the original datasets. This helped identify data quality anomalies, structural gaps, missing coordinates, and text discrepancies across thousands of rows. We also used AI for initial drafts of Python visualizations.
* AI assisted in designing the logical workflows required to standardize data and ensure data aggregation within Tableau would not result in duplicate counts. AI also helped embed US county census data into our main data source that otherwise did not exist in our original tables. It was also instructed to extrapolate data to create a larger more thorough dataset for use in chloropleth main map. 
* AI provided step-by-step guidance on fixing diagrams natively within Tableau but did not directly create our final dashboard itself.
