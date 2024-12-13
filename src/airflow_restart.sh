#!/bin/bash

# Function to rollback and exit on error
rollback_and_exit() {
    echo "An error occurred. Rolling back..."
    deactivate
    exit 1
}


export AIRFLOW__CORE__DAGS_FOLDER=/home/adminabhi/gitrepo/usa_customer_shopping_trends/src/dags  || rollback_and_exit

export AIRFLOW__CORE__LOAD_EXAMPLES=False  || rollback_and_exit

export AIRFLOW__CORE__TEST_CONNECTION=enabled  || rollback_and_exit

echo "Starting the Web Server and Scheduler..."
nohup airflow webserver --port 8080 > airflow_webserver.log 2>&1 & 
nohup airflow scheduler > airflow_scheduler.log 2>&1 &
echo "Web server and scheduler started."

echo "Access the Airflow Web UI by opening a web browser and navigating to http://localhost:8080"

