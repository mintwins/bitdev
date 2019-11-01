import json
from datetime import datetime
import os
import boto3
from xcoin_api_client import *
import pprint

def lambda_handler(event, context):


    api_key = os.environ.get("api_key");
    api_secret = os.environ.get("api_secret_key");


    rgParams = {
    	"order_currency" : "BTC",
    	"payment_currency" : "KRW"
    };


    #
    # public api
    #
    # /public/ticker
    # /public/recent_ticker
    # /public/orderbook
    # /public/recent_transactions

    result = xcoinApiCall("/public/ticker", rgParams).json()
    data = json.dumps(result)
    print(result)
    print(data)

	# Get the current datetime for the file name
    now = str(datetime.today())

	# Export the data to S3
    client = boto3.client('s3')
    response = client.put_object(Bucket="bitdev.xcoin",
					Body=data,
					Key='ticker/{}.json'.format(now))
