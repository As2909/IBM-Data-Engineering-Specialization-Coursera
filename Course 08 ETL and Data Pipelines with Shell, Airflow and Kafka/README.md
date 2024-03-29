## Project Description
For this project, the ELT is performed with the support of Airflow and Kafka. Assume you are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setup that use different file formats.  
In [the first Hands-on lab](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/Part1.pdf) your job is to collect data available in different formats and, consolidate it into a single file. As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. In [the second Hands-on lab](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/Part2.pdf) your job is to create a data pipe line that collects the streaming data and loads it into a database.

## Tasks and Solutions
- Task 1.1: Define DAG arguments (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/dag_args.png)
- Task 1.2: Define the DAG (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/dag_definition.png)
- Task 1.3: Create a task to download data (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/unzip_data.png)
- Task 1.4: Create a task to extract data from csv file (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/extract_data_from_csv.png)
- Task 1.5: Create a task to extract data from tsv file (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/extract_data_from_tsv.png)
- Task 1.6: Create a task to extract data from fixed width file (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/extract_data_from_fixed_width.png)
- Task 1.7: Create a task to consolidate data extracted from previous tasks (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/consolidate_data.jpg.png)
- Task 1.8: Transform the data (2 pts)\
For this task, we can use the SELECT function to query the size of the database from information_schema.tables or using the show table status\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/transform.png)
- Task 1.9: Define the task pipeline (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/task_pipeline.png)
- Task 1.10: Submit the DAG (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/submit_dag.jpg.png)
- Task 1.11: Unpause the DAG (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/unpause_dag.png)
- Task 1.12: Monitor the DAG (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/dag_runs.png)
- Task 2.1: Start Zookeeper (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/start_zookeeper.png)
Task 2.2: Start Kafka server (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/start_kafka.png)
- Task 2.3: Create a topic named toll (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/create_toll_topic.png)
- Task 2.4: Download the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/download_simulator.png)
- Task 2.5: Configure the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/configure_simulator.png)
- Task 2.6: Run the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/simulator_output.png)
- Task 2.7: Configure streaming_data_reader.py (2pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/streaming_reader_code.png)
- Task 2.8: Run streaming_data_reader.py (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/data_reader_output.png)
- Task 2.9: Health check of the streaming data pipeline (1pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2008%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week%205/output_rows.png)
