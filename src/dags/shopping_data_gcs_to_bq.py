from __future__ import annotations

import os
from datetime import datetime

from airflow.models.dag import DAG
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryDeleteDatasetOperator,
    BigQueryGetDatasetOperator,
    BigQueryUpdateDatasetOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.utils.dates import days_ago

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    'shopping_data_gcs_to_bq',
    default_args=default_args,
    description='Load CSV data from GCS to BigQuery',
    schedule_interval=None,  # You can set this to a cron schedule if needed
    start_date=days_ago(1),
    catchup=False,
    tags=['example'],
) as dag:

    create_sales_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_sales_dataset',
        project_id = 'usa-customer-shopping-trends',
        dataset_id='sales',
        gcp_conn_id='airflow_2_gcs',
        location = 'europe-west4',
        if_exists = 'ignore'
    )

    load_sales_data_to_bq = GCSToBigQueryOperator(
        task_id = 'load_sales_data_to_bq',
        bucket = 'usa-customer-shopping-trends',
        source_objects = 'data/shopping_trends.csv',
        destination_project_dataset_table = 'usa-customer-shopping-trends.sales.shopping_trends',
        gcp_conn_id = 'airflow_2_gcs',
        write_disposition="WRITE_TRUNCATE",
        source_format="CSV",
        schema_fields = [
            {"name": "Customer_ID", "type": "INTEGER", "mode": "REQUIRED"},
            {"name": "Age", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "Gender", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Item_Purchased", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Category", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Purchase_Amount_USD", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "Location", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Size", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Color", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Season", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Review_Rating", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "Subscription_Status", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "Payment_Method", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Shipping_Type", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Discount_Applied", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "Promo_Code_Used", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "Previous_Purchases", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "Preferred_Payment_Method", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Frequency_of_Purchases", "type": "STRING", "mode": "NULLABLE"}
        ]
    )

    create_sales_dataset >> load_sales_data_to_bq



    # # Define the BigQuery table creation task using an external SQL file
    # create_bq_table = BigQueryInsertJobOperator(
    #     task_id='create_bigquery_table',
    #     configuration={
    #         "query": {
    #             "query": "{{ task_instance.xcom_pull(task_ids='read_sql_file') }}",
    #             "useLegacySql": False,
    #         }
    #     },
    # )

    # # Task to read the SQL file
    # def read_sql_file(**kwargs):
    #     with open('/path/to/your/schema_definition.sql', 'r') as file:  # Replace with the actual path to your SQL file
    #         sql_query = file.read()
    #     return sql_query

    # read_sql_task = PythonOperator(
    #     task_id='read_sql_file',
    #     python_callable=read_sql_file
    # )

    # # Define the GCS to BigQuery task
    # load_csv_to_bq = GCSToBigQueryOperator(
    #     task_id='gcs_to_bigquery',
    #     bucket='your-gcs-bucket-name',  # Replace with your GCS bucket name
    #     source_objects=['path/to/your-file.csv'],  # Replace with the path to your CSV file
    #     destination_project_dataset_table='your-project.your_dataset.your_table',  # Replace with your BigQuery table
    #     schema_fields=[
    #         {'name': 'column1', 'type': 'STRING', 'mode': 'NULLABLE'},
    #         {'name': 'column2', 'type': 'INTEGER', 'mode': 'NULLABLE'},
    #         # Add more columns as per your schema
    #     ],
    #     write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
    #     source_format='CSV',
    #     skip_leading_rows=1,  # Skip header row if your CSV has one
    #     field_delimiter=',',
    # )

    # Set task dependencies
    #read_sql_task >> create_bq_table >> load_csv_to_bq
