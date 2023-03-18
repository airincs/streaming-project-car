import yfinance
from datetime import datetime, timedelta
import json
import boto3

def run_car_stream():
  today = datetime.now().date()
  start_date = today - timedelta(days=4)
  end_date = today - timedelta(days=1)
  interval = '5m'
  firehose = boto3.client("firehose", "us-east-2")

  companies = ['HMC', 'NSANY', 'TM', 'VLKAF', 'MBGAF', 'BMWYY']

  for company in companies:
        download = yfinance.Ticker(company).history(start=start_date, end=end_date, interval=interval)

        for index, rows in download.iterrows():
                    as_jsonstr = json.dumps({"high":rows["High"], "low":rows["Low"], "ts":index.strftime('%Y-%m-%d %X'), "name":company})
                    firehose.put_record(DeliveryStreamName="car-streaming-firehose", Record={"Data": as_jsonstr.encode('utf-8')})