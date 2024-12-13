
from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

@dag(
    dag_id="dag_upload_csv_to_gcs",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['customer', 'upload'],
)
def dag_upload_csv_to_gcs():

    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='/home/adminabhi/gitrepo/usa_customer_shopping_trends/data/shopping_trends.csv',
        dst='data/shopping_trends.csv',
        bucket='usa-customer-shopping-trends',
        gcp_conn_id='airflow_2_gcs',
        mime_type='text/csv',
    )

dag_upload_csv_to_gcs()