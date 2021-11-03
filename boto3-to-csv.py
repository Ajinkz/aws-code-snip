import csv
import boto3
import pandas as pd (optional)

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    

for obj in s3.Bucket('apstore').objects.all():
    print(obj)
    

# using csv module
obj = s3.Bucket('<bucket-name>').Object('test2021-11-03.csv').get()
data = obj['Body'].read().decode('utf-8').splitlines()
lines = csv.reader(data)
headers = next(lines)
print('headers: %s' %(headers))

with open('s3file.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f,lineterminator='\n')
    # Add headers
    writer.writerow(headers)
    
    for line in lines:
        print(line)
        writer.writerow(line)
        
        
'''
ALTERNATIVE WAY USING PANDAS
'''
foo = pd.read_csv(obj['Body'], index_col=0)
