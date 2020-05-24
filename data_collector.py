import json
import boto3
import subprocess
import sys

def install(package):
    subprocess.check_call([
        sys.executable, 
        "-m", 
        "pip", 
        "install", 
        "--target",
        "/tmp",
        package])
        
install('yfinance')

sys.path.append('/tmp')

import yfinance 

def lambda_handler(event, context):

    data = yfinance .download("FB SHOP BYND NFLX PINS SQ TTD OKTA SNAP DDOG", start = "2020-05-14", end = "2020-05-15", interval = "1m")
    data = data[['High', 'Low']].stack().reset_index()
    data = data.rename(columns = {'Datetime': 'ts', 'level_1': 'name', 'High': 'high', 'Low': 'low'})
    data = data.sort_values(by = ['name', 'ts'])
    data['ts'] = data['ts'].map(lambda x: str(x))
    
    fh = boto3.client("firehose", "us-east-2")

    for _, row in data.iterrows():
        
        as_jsonstr = json.dumps(row.to_dict())

        fh.put_record(DeliveryStreamName = "STA9760-Stream-Finance-Data", 
                      Record = {"Data": as_jsonstr.encode('utf-8')})

    return {'statusCode': 200,
            'body': json.dumps(f'Done! Recorded: {as_jsonstr}')}