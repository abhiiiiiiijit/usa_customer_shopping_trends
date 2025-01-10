# USA Customer Shopping Trends

## Project Overview

This project aims to analyze shopping trends of customers in the USA. By examining various factors such as age, gender, location, and purchase behavior, we can gain insights into customer preferences and trends. The data is sourced from a CSV file and processed using Apache Airflow and dbt (data build tool) and finally visualised using Power BI. The dataset used is from Kaggle [customer shopping dataset](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset).

## Architecture
![Architecture](/diagrams/Architecture.jpg)

The project architecture consists of the following components:

1. **Data Source**: A CSV file containing customer shopping data.
2. **Google Cloud Storage (GCS)**: The CSV file is uploaded to GCS for storage.
3. **BigQuery**: The data from GCS is loaded into BigQuery for analysis.
4. **Apache Airflow**: Orchestrates the workflow of uploading data to GCS and loading it into BigQuery.
5. **dbt**: Performs data quality checks and transformations on the data in BigQuery.
6. **Power BI**: Visualised customer data for easy trend analysis.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/usa_customer_shopping_trends.git
   cd usa_customer_shopping_trends

## 2. Set Up Google Cloud

- Create a Google Cloud project.
- Enable the BigQuery and GCS APIs.
- Create a GCS bucket to store the CSV file.
- Set up a service account and download the JSON key file.

## 3. Configure Airflow

- Install Apache Airflow: Follow the official [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html).
- Set up Airflow to use the Google Cloud service account key.
- Configure DAGs (Directed Acyclic Graphs) for:
  - Uploading data to GCS.
  - Loading data into BigQuery.

## 4. Install dbt Core

- Install dbt by following the [dbt documentation](https://docs.getdbt.com/dbt-cli/installation).
- Configure dbt to connect to your BigQuery project by setting up a `profiles.yml` file.

---

## Usage

### 1. Upload Data to GCS

```sh
Run the Airflow DAG `dag_upload_csv_to_gcs` to upload the CSV file to GCS.
