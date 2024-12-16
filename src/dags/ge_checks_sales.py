from __future__ import annotations
from airflow.decorators import dag, task
from datetime import datetime, timedelta

from airflow.utils.dates import days_ago
from airflow.models.dag import DAG
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from great_expectations.data_context.types.base import (
    DataContextConfig,
    CheckpointConfig
)

# Define default arguments for the DAG
default_args = {
    'owner': 'Abhijit',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define variables (update paths and configs)
ge_root_dir = "/path/to/your/great_expectations"  # Replace with your GE root directory
example_data_context_config = DataContextConfig(  # Replace with your GE data context config
    datasources={},
    stores={},
    expectations_store_name="expectations_store",
    validations_store_name="validations_store",
    evaluation_parameter_store_name="evaluation_parameter_store",
    plugins_directory=None,
    config_version=2.0,
    validation_operators={},
)
example_checkpoint_config = CheckpointConfig(  # Replace with your GE checkpoint config
    name="example_checkpoint",
    config_version=1.0,
    class_name="Checkpoint",
    run_name_template=None,
    validations=[]
)

# Define the DAG
with DAG(
    'ge_checks_sales',
    default_args=default_args,
    description='Great Expectations checks',
    schedule_interval=None,  # You can set this to a cron schedule if needed
    start_date=days_ago(1),
    catchup=False,
    tags=['ge', 'data quality'],
) as dag:

    ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
        task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="taxi.pass.chk",
    )

    ge_data_context_config_with_checkpoint_config_pass = GreatExpectationsOperator(
        task_id="ge_data_context_config_with_checkpoint_config_pass",
        data_context_config=example_data_context_config,
        checkpoint_config=example_checkpoint_config,
    )

    ge_data_context_root_dir_with_checkpoint_name_pass >> ge_data_context_config_with_checkpoint_config_pass