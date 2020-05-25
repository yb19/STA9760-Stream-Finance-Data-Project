# STA9760-Stream-Finance-Data-Project
This is the repository for the STA9760 Streaming Finance Data with AWS Lambda Project by leveraging AWS Lambda, Kinesis, and Athena. The dataset is one full day’s worth of stock high and low prices for each selected company on May 14th, 2020, at an one minute interval, collected from [yfinance](https://pypi.org/project/yfinance/) module.

## Outline
This project is divided into four parts:
- Part 1: DataTransformer
- Part 2: DataCollector
- Part 3: DataAnalyzer
- Part 4: Analysis

## Part 1: DataTransformer
First, I create a Kinesis Firehose Delivery Stream. This stream has a Lambda function that transforms the record and streams it into an S3 bucket. 

## Part 2: DataCollector
Then, I write another Lambda function that is triggered from a simple URL call. On trigger, it will grab stock price data and place it into the delivery defined in the DataTransformer. 

**Lambda function URL: https://9yqekzjgog.execute-api.us-east-2.amazonaws.com/default/STA9760-Stream-Finance-Lambda.**

## Part 3: DataAnalyzer
Then, I configure AWS Glue, pointing it to the S3 Bucket that I created in my DataTransformer. This will allow us to now interactively query the S3 files generated by the DataTransformer using AWS Athena to gain insight into our streamed data. In Athena, I write and run a query that gives us the highest hourly stock “high” price per selected company.

## Part 4: Analysis
Finally, I leverage Jupyter Notebook that takes the results.csv file from DataAnalyzer and generates a few visualizations on the data that I accumulated. 

## DataCollector AWS Lambda configuration page
![lambda](https://github.com/yb19/STA9760-Stream-Finance-Data-Project/blob/master/assets/lambda.png?raw=true)

## Kinesis Firehose Delivery Stream Monitoring page
![kinesis](https://github.com/yb19/STA9760-Stream-Finance-Data-Project/blob/master/assets/kinesis.png?raw=true)
