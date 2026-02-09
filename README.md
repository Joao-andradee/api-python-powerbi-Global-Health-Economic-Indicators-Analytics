# Global Health & Economic Indicators Analysis

## Overview
This project analyzes the relationship between **economic capacity**, **health expenditure**, and **population health outcomes** across countries over time.  
It demonstrates end-to-end analytics skills, including API data extraction, Python automation, dimensional modeling, and interactive Power BI reporting.

---

## Business Questions
- How does GDP per capita relate to life expectancy?
- What is the relationship between health spending and under-5 mortality?
- Do higher-income countries experience diminishing health returns?
- Which countries outperform or underperform relative to their economic capacity?
- How have global health indicators evolved over time and by decade?

---

## Data Sources
- **World Bank Open Data API**
  - Life expectancy at birth
  - Under-5 mortality rate
- **Python-generated CSV files**
  - GDP per capita
  - Health expenditure per capita

**Time range:** 2000–2023  
**Granularity:** Country-level, annual data

---

## Tools & Technologies
- Python (requests, pandas)
- REST APIs
- Power BI Desktop
- Power Query (M)
- DAX
- Dimensional modeling (Star Schema)
- Data visualization and analytics

---

## Data Model
Star schema design for performance and scalability.

### Fact Tables
- `fact_gdp_pc`
- `fact_health_spend_pc`
- `fact_life_expectancy`
- `fact_under5_mortality_api`

### Dimension Tables
- `dim_country`
- `dim_year`

---

## Power BI Report Pages
- **Home Page** – Navigation and report overview
- **Executive Summary** – Global KPIs and high-level insights
- **Economic vs Health Correlation** – Relationships, clusters, and outliers
- **Country Deep Dive** – Country-level time series analysis
- **Indicator Trends** – Global and decade-based trends
- **Data & Methodology** – Data sources, transformations, and model design

---

## Key Insights
- Higher GDP per capita generally aligns with higher life expectancy
- Increased health spending is associated with lower under-5 mortality
- Life expectancy gains flatten in high-income countries
- Countries with similar income levels can have very different health outcomes

---

## Skills Demonstrated
- API integration and automation
- Python data extraction and transformation
- Dimensional modeling and star schema design
- Power BI dashboard development
- Analytical storytelling and insight generation
- Integration of multiple data sources

---

## Contact
For questions or collaboration, connect with me on LinkedIn.

