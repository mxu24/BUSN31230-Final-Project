# 🍔 Socioeconomic Foodscapes
### *Analyzing the Intersection of Poverty, Obesity, and Fast Food Density in the United States*

---

## 👥 Project Team & Course Context
* **Course:** BUSN 32130 Data Visualization
* **Institution:** University of Chicago Booth School of Business
* **Authors:** Brandt Burgdorf, Serge Wen, Maggie Xu
* **Project Status:** 🚧 *In Progress (Awaiting Final Dashboard Elements)*

---

## 📝 1. Project Domain & Motivation
While adult obesity is frequently framed as an isolated matter of personal lifestyle, it is deeply intertwined with systemic socioeconomic factors and local food environments. This project explores how a community’s commercial environment and economic status influence public health outcomes. 

By analyzing county-level datasets across the United States, this analytical dashboard models the geographical and statistical relationships between **high poverty rates, elevated adult obesity rates, and an intense density of fast-food venues**. Our core objective is to evaluate whether lower-income regions face structural inequalities in food access—specifically, whether they are disproportionately saturated with fast food, which acts as a barrier to healthier, more affordable alternatives.

Our final production dataset contains **25,144 rows**, representing **3,143 unique U.S. counties** after county-level aggregation and chain/category joins. At the county level, the dataset shows a **national poverty benchmark of 14.6%** and a **national adult obesity benchmark of 33.2%**. Across counties in our final file, the **median poverty rate is 17.8%**, the **median obesity rate is 31.9%**, and the **mean fast-food density is approximately 9.7 locations per 10,000 residents**. These values suggest that many counties in the analytical sample sit above national poverty benchmarks even before risk layering is applied.

### 🎯 Core Dashboard Strategic Goal
> **"This dashboard helps public health officials, community policymakers, and urban planners make better decisions about resource allocation and food-access zoning by showing the geographic and statistical correlations between poverty, obesity, and fast-food density."**

---

## 🔬 2. Core Hypotheses
* **Hypothesis 1 (Socioeconomic Correlation):** U.S. counties with higher poverty rates will exhibit a statistically significant positive correlation with adult obesity rates and a higher concentration of fast-food points of interest (POIs).
* **Hypothesis 2 (Density vs. Raw Count):** Raw restaurant counts are highly confounded by population scale. Normalizing the data into **fast-food density metrics** (e.g., locations per 10,000 capita or per square mile) will yield a much stronger, more accurate predictor of county obesity rates than raw counts.
* **Hypothesis 3 (Chain Composition Effect):** The specific brand or category mix matters. Saturated clusters of specific menu styles (e.g., burger or fried chicken chains) will correlate with sharper drops in community health metrics compared to areas with a more balanced fast-food ecosystem.

### Preliminary Quantitative Findings
* At the county level, **poverty and obesity move together very strongly** in our integrated dataset, with a correlation of approximately **0.98**.
* **Fast-food density per 10,000 residents** is also positively associated with both poverty and obesity; its correlation with poverty is approximately **0.78**.
* We identify **1,334 counties** as `"High Risk"`, which is approximately **42.4%** of all counties in the final analytical file.
* Regional concentration is highly uneven: the **South contains 987 high-risk counties**, far more than the Midwest (**261**), West (**83**), or Northeast (**3**).
* These patterns support our view that raw spatial restaurant count alone is insufficient; normalized density and county-level structural context matter more.

---

## 🗃️ 3. Data Strategy & Pipeline

### Data Sources & Architecture

| Data Source | Type | Scope / Limitations | Operational Role |
| :--- | :--- | :--- | :--- |
| [US Fast Food Restaurants (Kaggle)](https://www.kaggle.com/datasets/khushishahh/fast-food-restaurants-across-us) | CSV | 10,000 geolocated entries. Not a complete census. | Baseline spatial mapping & point-density proof of concept. |
| [Global McDonald's Stores (Kaggle)](https://www.kaggle.com/datasets/forveryou/mcdonalds-stores-data) | CSV | Complete 2023 global corporate roster. | Used to scale up US coverage and reduce missing-record biases. |
| [Top 50 Fast Food Chains (Kaggle)](https://www.kaggle.com/datasets/stetsondone/top50fastfood) | CSV | National brand metrics & categories. | Joins subcategories (e.g., Burgers, Chicken) and average sales data. |
| [US Poverty Data (US Census Bureau)](https://www.census.gov/data/datasets/2023/demo/saipe/2023-state-and-county.html) | API / CSV | Comprehensive 2023 SAIPE state/county metrics. | Primary socioeconomic baseline layer. |
| [Geolocated Obesity Rates (CDC PLACES)](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb/about_data) | API / CSV | Comprehensive county-level health prevalence. | Primary public health outcome dataset. |
| [Adult Obesity Prevalence (CDC)](https://www.cdc.gov/obesity/data-and-statistics/adult-obesity-prevalence-maps.html) | Report Data | Layered age-bracket/demographic groups. | Used for granular demographic filters. |

### Data Preparation & Cleansing Workflow
1. **Deduplication & Standardization:** Cleaning fast-food chain nomenclature (e.g., standardizing `McDonalds`, `McDonald's`, and `mcdonalds`) to ensure proper grouping.
2. **Spatial Join / Aggregation:** Translating point-level coordinate data (Latitude/Longitude) into unique US County FIPS codes using GIS tools / Tableau spatial blending.
3. **Feature Engineering:** Creating calculated fields for population-normalized metrics within Tableau:
   $$\text{Fast Food Density} = \left( \frac{\text{Total Restaurants}}{\text{County Population}} \right) \times 10,000$$
4. **Data Blending Matrix:** Linking all cleaned tables together inside Tableau using **County FIPS Codes** as the primary relational key.

### Final Analytical Dataset Snapshot
* **Rows:** 25,144
* **Unique Counties:** 3,143
* **Regions Covered:** Northeast, Midwest, South, West
* **Urbanicity Layer:** Urban, Suburban, Rural
* **Core Outcome Variables:** Poverty rate, obesity rate, fast-food density, risk score, intervention priority score
* **Chain / Category Layer:** Chain, category, estimated locations, sales per location, estimated total sales, category concentration

### Quantitative Summary of County-Level Variables
| Metric | Value |
| :--- | :--- |
| National Poverty Average | **14.6%** |
| National Obesity Average | **33.2%** |
| Median County Poverty Rate | **17.8%** |
| Median County Obesity Rate | **31.9%** |
| Mean County Fast Food Density | **9.7 locations / 10,000 residents** |
| Median County Fast Food Density | **9.7 locations / 10,000 residents** |
| Mean Composite Risk Score | **91.2** |
| Highest Composite Risk Score | **139.2** |

---

## 🖥️ 4. Dashboard Visual Planning & Strategy

### Planned Layout Hierarchy
* **Level 1 (Macro View):** Dual-Axis Choropleth Map highlighting national geographic overlap hotspots.
* **Level 2 (Analytical View):** Multivariable Scatterplot to isolate correlation lines between poverty (X-axis), obesity (Y-axis), and fast-food density (Marker Size).
* **Level 3 (Micro View):** Dynamically filtered Bar Charts breaking down dominant fast-food subcategories for selected high-risk vs. low-risk counties.

### Current Dashboard Components
* **KPI Tiles:** Fast-food density, total locations, high-risk county count, average risk score
* **Risk Map:** County-level geographic hot spot view
* **Poverty vs. Obesity Scatterplot:** County-level analytical view with size and color encoding
* **Regional Risk View:** Geographic comparison across macro-regions
* **Top Fast Food Chains:** Brand concentration layer
* **Fast Food Category Mix:** Category-level composition view
* **Highest Risk Counties:** Ranked county comparison for targeting and storytelling


### Design Logic Behind the Dashboard
The dashboard layout follows a deliberate reading path. Users first see a macro-level risk summary, then a geographic map for spatial context, then a scatterplot for analytical relationship testing, and finally ranked or category-level views for diagnosis and action. This sequencing applies the class idea that effective dashboards should reduce cognitive load by moving from overview to detail rather than forcing users to decode every element at once.


### Planned Interactive System
* `[x]` **Global State/County Filters:** Allows local officials to drill directly down into their own jurisdictions.
* `[ ]` **Demographic Parameter Switchers:** Switches views across different age brackets using the CDC demographic data layers.
* `[x]` **Top-N Dynamic Filter / Ranked County View:** Supports quick isolation of the highest-risk counties for targeting.
* `[x]` **Map-to-Detail Interaction:** Clicking or filtering geographic views updates lower-level charts such as county rankings and category mix.

---

## 🧠 5. Course Reflection & Synthesis Workbook

### PART 1 — Core Skills Reflection

#### 1.1 Skills Assessment
| Concept / Skill | Why It Matters to This Project | Team Confidence Level (1–5) |
| :--- | :--- | :--- |
| **Gestalt Principles** | Ensuring users group spatial high-risk areas naturally using color proximity. | `4` |
| **Preattentive Processing**| Highlighting extreme outliers in obesity via distinct color anchors. | `4` |
| **Tableau Level of Detail (LOD)** | Calculating county-level densities independent of dashboard filters. | `5` |
| **Exploratory vs. Explanatory**| Allowing deep user drill-downs while pointing out key systemic takeaways. | `4` |

#### 1.2 Most Important Insight
The team’s most important takeaway is that **normalization and data structure matter more than raw visual complexity**. A visually attractive dashboard can still mislead if it maps raw restaurant counts rather than density or if it duplicates counties through chain-level joins. The strongest business and policy insight comes from using the right level of aggregation, especially county-level LOD logic, before refining aesthetics.

#### 1.2A Application of Class Principles
We intentionally applied several class principles in the dashboard design. First, we used **Gestalt principles of similarity and proximity** by keeping all risk-related views in a consistent color family and grouping related charts close together, so users can naturally connect the map, scatterplot, and ranked county views as part of one story. Second, we used **visual hierarchy** by placing the macro geographic view first, then the analytical correlation views, and finally the county/category drill-down views. Third, we used **preattentive attributes** such as darker color intensity for higher-risk counties and larger mark size for higher fast-food density so that extreme cases stand out before users even read the labels. Fourth, we applied **exploratory vs. explanatory balance** by making the dashboard interactive enough for drill-down, but still structured around a clear narrative: where risk is highest, what factors are associated with it, and what actions might follow.

#### 1.3 Evolution of Your Thinking
* **Initial Beliefs:** *We initially believed that the most difficult part of the project would be making the dashboard visually polished and map-heavy enough to look persuasive.*
* **Current Understanding:** *We now understand that the hardest and most important step is preserving county-level analytical integrity. The dashboard only becomes meaningful after de-duplication, FIPS-based blending, and per-capita normalization are handled correctly.*
* **Recognized Early Mistakes:** *Our earliest drafts over-relied on raw counts and repeated county records from chain-level joins. That would have over-emphasized large-population counties and weakened the credibility of the analysis.*

---

### PART 2 — Defining the Business & Policy Problem

#### 2.1 Specific Problem Statement
This project addresses a public-policy allocation problem: **Which U.S. counties should public-health and community-development stakeholders prioritize when high poverty, high adult obesity, and high fast-food density overlap?** More specifically, the dashboard helps identify counties where food-access conditions may justify targeted interventions such as zoning review, nutrition program support, healthy retail incentives, or mobile food access initiatives.

#### 2.2 Stakeholder Needs & Actions Supported
| Key Stakeholder | Decision to be Made | Why It Matters / Operational Impact |
| :--- | :--- | :--- |
| **Public Health Director** | Allocate obesity-prevention and nutrition-access resources across counties. | Improves the precision of limited public-health budgets by targeting structurally vulnerable counties. |
| **Zoning Commissioner** | Review whether highly saturated counties should restrict additional fast-food concentration. | Helps local governments avoid reinforcing food deserts and high-risk retail clustering. |
| **Community Development Office** | Identify where to support healthier food retail alternatives or incentive programs. | Encourages intervention where poverty and food-access barriers are jointly concentrated. |
| **Urban / Regional Planner** | Compare county food environments across region and urban-rural type. | Supports place-based planning rather than one-size-fits-all policy responses. |

---

### PART 3 — Dashboard Execution Strategy

#### 3.1 Metrics Framework
| KPI Metric | Technical Operational Definition | Target / Benchmark Context |
| :--- | :--- | :--- |
| **Fast Food Density** | Outlets per 10,000 residents. | Compared against the county median of approximately **9.7**. |
| **Poverty Prevalence** | % of county population living below poverty thresholds. | Compared against the national benchmark of **14.6%**. |
| **Obesity Prevalence** | % of adult population with BMI $\ge$ 30. | Compared against the national benchmark of **33.2%**. |
| **Composite Risk Score** | Multi-factor score blending poverty, obesity, and fast-food conditions. | Higher values indicate more severe structural risk. |
| **Intervention Priority Score** | Weighted decision-support score for resource targeting. | Used to surface counties most appropriate for intervention. |

#### 3.2 Key Visual Analytics Answered
1. **Question:** *Do counties with higher poverty also tend to have higher adult obesity?*  
   * **Visualization Strategy:** County-level scatterplot with poverty on the X-axis and obesity on the Y-axis, with fast-food density encoded through mark size and risk percentile through color.
2. **Question:** *Where are the highest-risk counties geographically concentrated?*  
   * **Visualization Strategy:** County choropleth risk map using composite risk score and risk bucket encoding.
3. **Question:** *Which counties should decision-makers prioritize first?*  
   * **Visualization Strategy:** Ranked county table / bar chart showing the highest composite risk and intervention priority values.
4. **Question:** *What kinds of fast-food ecosystems dominate selected counties?*  
   * **Visualization Strategy:** Dynamically filtered category and chain mix charts linked to county selection on the dashboard.
5. **Question:** *Are there meaningful regional differences?*  
   * **Visualization Strategy:** Regional comparison charts and macro segmentation by South, Midwest, West, and Northeast.

---

### PARTS 5 & 6 — Storytelling, Design Choices & Actions

#### 5.1 Color & Visual Hierarchy Strategy
We use a **progressive warm-to-cool risk palette** to make risk concentration immediately legible without overwhelming the viewer. Lower-risk counties are shown in lighter or cooler tones, while higher-risk counties move into warmer, more saturated colors. This helps users immediately identify extreme counties through preattentive processing. To reduce cognitive overload, we avoided assigning too many meanings to the same color system: maps and risk views consistently use color for risk severity, while scatterplots use mark size for density and tooltips for detail. We also kept dashboard layout hierarchical: macro geographic context first, then analytical correlation, then micro chain/category explanation.

#### 5.2 Typeface Selection & Readability
We selected a **clean sans-serif typeface strategy** in Tableau because the dashboard needs to be legible in both presentation mode and dashboard drill-down mode. Larger KPI figures and section titles are used to establish hierarchy, while supporting labels and tooltips remain smaller but consistent. We avoided decorative fonts because they would weaken readability, especially on maps and dense county views. In practice, our type choices support clarity, scanning speed, and professional tone rather than stylistic novelty.

#### 5.3 Additional Principle Applications in the Dashboard
* **Similarity:** Risk-related colors remain consistent across the choropleth map and ranked county views, so users do not have to relearn the encoding from chart to chart.
* **Proximity:** Related charts are placed near one another so the viewer reads the dashboard from macro context to detailed diagnosis.
* **Figure/Ground:** We used neutral backgrounds and restrained gridlines so the data marks, not the chart furniture, receive attention first.
* **Alignment and Repetition:** KPI cards, titles, and supporting views use repeated formatting patterns to reduce unnecessary visual noise.
* **Color economy:** We limited the number of “jobs” assigned to color. Color mainly signals risk severity, while size signals density and position signals correlation.

#### 6.1 Central Narrative & Action Matrix
| Discovered Data Pattern | Strategic Insight | Recommended Action |
| :--- | :--- | :--- |
| **High-Poverty Southern Cluster** | The South contains the largest concentration of high-risk counties (**987**), suggesting a structural rather than isolated pattern. | Prioritize regional nutrition-access funding, obesity prevention, and healthy retail incentives in Southern counties. |
| **High Poverty + High Obesity Overlap** | Counties above the national poverty benchmark of **14.6%** often also sit above the national obesity benchmark of **33.2%**. | Use poverty-obesity overlap to target preventative health outreach and food-access interventions. |
| **Fast-Food Density as a Better Signal Than Raw Count** | County fast-food density is much more informative than raw restaurant count because it controls for population scale. | Use density-based thresholds, not raw location totals, when screening high-priority counties. |
| **Category Concentration Risk** | Burger and chicken categories account for the largest estimated location totals in the analytical file, indicating category dominance rather than balanced food environments. | Use category-mix monitoring when evaluating whether new fast-food permits worsen local concentration. |
| **County-Level Outliers** | Some counties dramatically exceed average poverty, obesity, and risk thresholds and appear repeatedly at the top of county rankings. | Treat top-ranked counties as immediate intervention candidates for pilot programs and resource testing. |

---

### PART 7 — Final Dashboard Production Gallery
*Once your final presentation dashboard is published, export screenshots or wireframes and drop them here.*

#### Suggested Gallery Inserts
* Main Dashboard full screenshot
* Risk Map screenshot
* Poverty vs. Obesity scatterplot screenshot
* Highest Risk Counties screenshot
* FF Category Mix screenshot with county drill-down

---

### PART 8 — Critical Evaluation & Post-Mortem

#### 8.1 Remaining Limitations & Data Gaps
Our fast-food location count relies on combined public Kaggle tables and estimated chain expansion logic rather than a live commercial retail registry. This means the dashboard should be interpreted as a **programmatic proof of concept**, not a real-time census of all fast-food establishments. In addition, chain/category joins introduce repeated county rows, which required careful county-level LOD handling in Tableau to avoid double counting. Some of the strongest correlations in the final dataset are partly influenced by the way the composite risk system was engineered, so those statistics should be interpreted as dashboard-support evidence rather than standalone causal proof.

Additional limitations include the fact that county-level averages can hide within-county neighborhood differences, some fast-food coverage remains incomplete even after enrichment, and obesity and poverty measures are public-agency estimates rather than direct observation. Because of this, the dashboard is strongest as a screening and prioritization tool rather than a final causal model.

#### 8.2 Key Assumptions
* We assume **county** is the most reasonable decision-making unit because poverty and obesity data are available consistently at that level.
* We assume **fast-food density per 10,000 residents** is a more meaningful measure than raw count for comparing counties of very different population sizes.
* We assume the integrated restaurant data captures enough of the fast-food environment to reveal broad structural patterns, even though it is not a perfect census.
* We assume composite risk and intervention priority scores are useful for ranking and screening, but not a substitute for local policy judgment.

#### 8.3 Simplification Opportunities
To keep the dashboard readable, we chose not to overload it with too many simultaneous demographic and geographic layers. We cut several ideas from the initial draft, including excessive chain-by-chain breakdowns, redundant regional maps, and too many competing color encodings. We also simplified the narrative so that the dashboard answers three main questions clearly: **Where is risk highest? Why is it high? What should a stakeholder do next?**

---

## 🧾 9. Selected Quantitative Findings for Presentation Use
* **Counties represented:** 3,143
* **High-risk counties:** 1,334 (**42.4%**)
* **Mean composite risk score:** **91.2**
* **Highest composite risk score:** **139.2**
* **Median poverty rate:** **17.8%**
* **Median obesity rate:** **31.9%**
* **Mean fast-food density:** **9.7 per 10,000 residents**
* **Regional high-risk counties:** South **987**, Midwest **261**, West **83**, Northeast **3**
* **Largest categories by estimated locations:** Chicken, Burger, Coffee, Pizza
* **Top chains by estimated locations in the integrated file:** Chick-fil-A, KFC, Dunkin, Subway, Starbucks, McDonald’s