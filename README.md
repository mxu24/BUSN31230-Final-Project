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

### 🎯 Core Dashboard Strategic Goal
> **"This dashboard helps public health officials, community policymakers, and urban planners make better decisions about resource allocation and food-access zoning by showing the geographic and statistical correlations between poverty, obesity, and fast-food density."**

---

## 🔬 2. Core Hypotheses
* **Hypothesis 1 (Socioeconomic Correlation):** U.S. counties with higher poverty rates will exhibit a statistically significant positive correlation with adult obesity rates and a higher concentration of fast-food points of interest (POIs).
* **Hypothesis 2 (Density vs. Raw Count):** Raw restaurant counts are highly confounded by population scale. Normalizing the data into **fast-food density metrics** (e.g., locations per 10,000 capita or per square mile) will yield a much stronger, more accurate predictor of county obesity rates than raw counts.
* **Hypothesis 3 (Chain Composition Effect):** The specific brand or category mix matters. Saturated clusters of specific menu styles (e.g., burger or fried chicken chains) will correlate with sharper drops in community health metrics compared to areas with a more balanced fast-food ecosystem.

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

---

## 🖥️ 4. Dashboard Visual Planning & Strategy

### Planned Layout Hierarchy
* **Level 1 (Macro View):** Dual-Axis Choropleth Map highlighting national geographic overlap hotspots.
* **Level 2 (Analytical View):** Multivariable Scatterplot to isolate correlation lines between poverty (X-axis), obesity (Y-axis), and fast-food density (Marker Size).
* **Level 3 (Micro View):** Dynamically filtered Bar Charts breaking down dominant fast-food subcategories for selected high-risk vs. low-risk counties.

### Planned Interactive System
* `[ ]` **Global State/County Filters:** Allows local officials to drill directly down into their own jurisdictions.
* `[ ]` **Demographic Parameter Switchers:** Switches views across different age brackets using the CDC demographic data layers.
* `[ ]` **Top-N Dynamic Filter:** Lets users isolate the top 50 most "at-risk" counties in the nation instantly.

---

## 🧠 5. Course Reflection & Synthesis Workbook

### PART 1 — Core Skills Reflection

#### 1.1 Skills Assessment
| Concept / Skill | Why It Matters to This Project | Team Confidence Level (1–5) |
| :--- | :--- | :--- |
| **Gestalt Principles** | Ensuring users group spatial high-risk areas naturally using color proximity. | `[ ]` |
| **Preattentive Processing**| Highlighting extreme outliers in obesity via distinct color anchors. | `[ ]` |
| **Tableau Level of Detail (LOD)** | Calculating county-level densities independent of dashboard filters. | `[ ]` |
| **Exploratory vs. Explanatory**| Allowing deep user drill-downs while pointing out key systemic takeaways. | `[ ]` |

#### 1.2 Most Important Insight
*✏️ [Insert your team's single most important takeaway regarding data visualization for strategic business / public policy decisions here]*

#### 1.3 Evolution of Your Thinking
* **Initial Beliefs:** *[e.g., We thought making maps look nice was the main challenge...]*
* **Current Understanding:** *[e.g., We realize that structuring data integrity and normalization matters far more than aesthetic flourishes...]*
* **Recognized Early Mistakes:** *[e.g., Using raw counts instead of per-capita calculations would have just mapped population centers...]*

---

### PART 2 — Defining the Business & Policy Problem

#### 2.1 Specific Problem Statement
*✏️ [Refine your final business problem statement here once the dashboard is finalized. Make it highly metric- and decision-driven.]*

#### 2.2 Stakeholder Needs & Actions Supported
| Key Stakeholder | Decision to be Made | Why It Matters / Operational Impact |
| :--- | :--- | :--- |
| **Public Health Director** | *[e.g., Allocating SNAP nutrition matches]* | Optimizes budget delivery to high-risk zones. |
| **Zoning Commissioner** | *[e.g., Reviewing fast-food building bans]* | Limits density growth in already saturated food deserts. |

---

### PART 3 — Dashboard Execution Strategy

#### 3.1 Metrics Framework
| KPI Metric | Technical Operational Definition | Target / Benchmark Context |
| :--- | :--- | :--- |
| **Fast Food Density** | Outlets per 10,000 residents. | National county median. |
| **Poverty Prevalence** | % of families living below federal poverty line. | State vs. Federal averages. |
| **Obesity Prevalence** | % of adult population with BMI $\ge$ 30. | Healthy People 2030 targets. |

#### 3.2 Key Visual Analytics Answered
1. **Question:** *[e.g., Do southern counties display a tighter correlation between poverty and obesity than midwestern ones?]*
   * **Visualization Strategy:** *[e.g., Trendlines segmented by US Geographic Region.]*
2. **Question:** *[Insert Question]*
   * **Visualization Strategy:** *[Insert Idea]*

---

### PARTS 5 & 6 — Storytelling, Design Choices & Actions

#### 5.1 Color & Visual Hierarchy Strategy
*✏️ [Explain your choice of palette (e.g., desaturated tones for baseline data, with an intense, high-contrast warm color for overlapping poverty-obesity zones). Explain how you handled accessibility and cognitive load constraints.]*

#### 6.1 Central Narrative & Action Matrix
| Discovered Data Pattern | Strategic Insight | Recommended Action |
| :--- | :--- | :--- |
| *[e.g., High-Poverty Rural Cluster]* | *[e.g., High obesity despite lower raw restaurant count due to zero fresh food alternatives.]* | *[e.g., Fund mobile grocery bus initiatives.]* |
| *[Insert Pattern]* | *[Insert Insight]* | *[Insert Action]* |

---

### PART 7 — Final Dashboard Production Gallery
*Once your final presentation dashboard is published, export screenshots or wireframes and drop them here.*


---

### PART 8 — Critical Evaluation & Post-Mortem

#### 8.1 Remaining Limitations & Data Gaps
*✏️ [Acknowledge the gaps in your restaurant dataset here. For example: "Our fast food location count relies on combined public Kaggle tables which represent a subset of the industry rather than a commercial real-time registry (like InfoUSA). Results should be treated as a programmatic proof of concept."]*

#### 8.2 Simplification Opportunities
*✏️ [What did you decide to cut out or remove from your initial draft to keep the dashboard clear, legible, and focused?]*

---

## 🏁 6. Final Project Milestone Checklist
* **Business & Policy Logic**
  * [x] Clear problem statement built
  * [x] Primary and secondary stakeholders defined
  * [ ] Actionable policy decisions fully supported
* **Data Quality & Modeling**
  * [x] Relevant datasets sourced and referenced
  * [x] Cleaning pipeline drafted for brand name standardizations
  * [ ] Calculated fields for per-capita density implemented in Tableau
* **Visual Polish & Delivery**
  * [ ] Intentional, accessible color palette configured
  * [ ] Interactivity via parameters and dynamic actions tested
  * [ ] Executive summary compiled for presentation slide deck
