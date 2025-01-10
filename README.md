# USA Customer Shopping Trends

## Project Overview

This project analyses shopping trends among customers in the USA. By examining factors such as age, gender, location, and purchase behaviour, it provides valuable insights into customer preferences and trends. The data is sourced from a CSV file, processed using Apache Airflow and dbt (data build tool), and visualised using Power BI. The dataset used is the [Customer Shopping Trends Dataset](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset) from Kaggle.

## Architecture
![Architecture](/diagrams/Architecture.jpg)

The project architecture comprises the following components:

1. **Data Source**: A CSV file containing customer shopping data.
2. **Google Cloud Storage (GCS)**: Used to store the CSV file.
3. **BigQuery**: Hosts the data for analysis after being loaded from GCS.
4. **Apache Airflow**: Orchestrates the workflow, including uploading data to GCS and loading it into BigQuery.
5. **dbt**: Executes data quality checks and performs data transformations within BigQuery.
6. **Power BI**: Visualises customer data for intuitive trend analysis.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/abhiiiiiiijit/usa_customer_shopping_trends.git
   ```

2. **Install Dependencies using Poetry**:
   ```sh
   poetry install
   ```

3. **Configure Google Cloud**:
    - Create a Google Cloud project.
    - Enable the BigQuery and GCS APIs.
    - Create a GCS bucket to store the CSV file.
    - Set up a service account and download the JSON key file.


4. **Set Up Apache Airflow**:

    - Configure Airflow to use the Google Cloud service account key (the JSON file downloaded in the previous step).
    - There are two DAGs (Directed Acyclic Graphs):
        - Uploading data to GCS (dag_upload_csv_to_gcs ).
        - Loading data into BigQuery, transformation and data quality checks using dbt (shopping_data_gcs_to_bq ).


5. **Deploy dbt Models**:
   - Set up a profiles.yml file to connect dbt to your BigQuery project.
   - Deploy and run dbt models.


7. **Visualize Data with Power BI**:
   - Connect Power BI to BigQuery.
   - Create dashboards and reports to visualize customer shopping trends.

## Usage

To execute the project, follow these steps:

1. **Activate Virtual Environment**:
   ```sh
   source venv/bin/activate
   ```

2. **Run Airflow DAG**:
    Start the Airflow web server and scheduler:
    ```sh
    - airflow webserver --port 8080
    - airflow scheduler
    ```

   - Access the Airflow web interface at `http://localhost:8080`.
   - Trigger the two DAG's to start the data pipeline.
      ```
         dag_upload_csv_to_gcs
         shopping_data_gcs_to_bq
      ```

3. **Analyze Data**:
   - Use Power BI to connect to BigQuery and create visualisations of customer shopping trends.


