# Customer Purchase Pattern Analysis

This project focuses on leveraging data analytics to uncover insights into customer purchase behaviours in the United States of America. By analysing transactional data, the project identifies patterns, trends, and key factors influencing purchasing decisions. The analysis aims to provide actionable insights for businesses to optimise their marketing strategies, inventory management, and customer engagement initiatives. This is an end to end data analytics project right from data ingestion, transformation, data quality checks and finishing with building a dashboard. I will be using the [customer shopping dataset](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset) from Kaggle for building the dashboard. The pipeline architecture supports not only this particular data engineering workflow. It can be used to support large volume of complex bigdata.

## Architecture

![Customer diagram](/diagrams/Architecture.jpg)

### Apache Airflow
I am using Apache Airflow for managing workflows for this project. This is an amazing open source tool which I used to build two DAGs one for uploading the CSV data from local to GCS and the second one to ingest data to Google Bigquery and then transform and do data quality checks the data using DBT. 

### DBT



### Github

### Google Cloud Storage

### Google Bigquery

### Looker/Power BI/Tableau







## Key Features:
Data Preprocessing: Cleaning and transforming raw data to ensure accuracy and consistency.

Exploratory Data Analysis (EDA): Detailed visualisations and statistical summaries to reveal significant trends and anomalies in customer behaviour.

Segmentation: Categorising customers based on purchase frequency, monetary value, and other key metrics.
Trend Analysis: Identifying seasonal trends, peak purchasing periods, and product preferences.
Predictive Insights: Implementing machine learning models to predict future purchasing behaviours and customer lifetime value.
Tools and Technologies:
Programming Languages: Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn).
Data Visualisation: Interactive dashboards using Looker or Power BI.
Databases: BigQuery for structured data management.
Workflow manager: Apache Airflow


#### Outcomes:

Comprehensive insights into customer purchasing habits.
Data-driven recommendations for enhancing business operations.
Customised reporting for stakeholder decision-making.
This repository is designed for analysts, data scientists, and business strategists interested in exploring and understanding customer purchase patterns in depth.