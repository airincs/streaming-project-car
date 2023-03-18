# Streaming Project on AWS - NASDAQ Performance :red_car:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

### Technologies and Services Used
- Airflow
- Python
- Various AWS Services: EC2, S3, Kinesis Firehose, Redshift
- PowerBI
- Linux + Bash Commands
- API: yfinance https://pypi.org/project/yfinance/

## Purpose? Why?
The goal of this data engineering project was to pull NASDAQ stock information about 3 Japanese and 3 German car manufacturers, to transform that data, and to load that date into a warehouse (where we can then generate a PowerBI report from). In order to perform this ETL project, we will be using AWS cloud services.

## Extraction
### API: yfinance Overview
"yfinance offers a threaded and Pythonic way to download market data from Yahoo!Ⓡ finance." - documentation.
We will be using yfinance to pull relevant data about the 6 total car makes.

![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/yfinance.PNG)

### Python Scripting + Airflow
In order to pull data from this API, we will be triggering a Python script via Airflow (The Python script and DAG are located in this repository).
Airflow was initialized and run on an EC2 instance! This allows us to easily access Airflow from the cloud, and it also allows Airflow to run non-stop, allowing the scheduling to function correctly. The Python script pushes the API's json data to Kinesis Firehose. An example CSV of the data can be found in this repository.

![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/Airflow%20Startup.PNG)
![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/Airflow%20Dag.PNG)

### Kinesis Firehose + S3 Bucket
Kinesis Firehose takes the pulled data from the Python script and pushes it to a S3 Bucket.

![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/firehose%20name.PNG)
![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/jsonoutput.PNG)
![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/carbuckets3.PNG)

### Redshift + PowerBI
We then copy the JSON data from the S3 Bucket into Redshift. We convert the JSON data into CSV in order to easily store it. We then connect to Redshift via PowerBI and create a high-level report of the data.

![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/redshift%20query.PNG)
![alt text](https://github.com/airincs/streaming-project-car/blob/main/images/PowerBI.PNG)
