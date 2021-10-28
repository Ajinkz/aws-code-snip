"""
Lambda function to fetch data from redshift and convert into csv 
"""


import json
import psycopg2
import csv

def lambda_handler(event, context):

    conn = psycopg2.connect(dbname='dev',
                            host = 'redshift-cluster-1.czaygp0man3j.us-east-1.redshift.amazonaws.com',
                            port = '5439',
                            user = 'awsuser',
                            password = 'Awsuser123')
    cur = conn.cursor()
    query = '''
    select * from category
    '''
    cur.execute(query)
    data = cur.fetchall()
    print("Query:",query)
    cols = list(map(lambda x: x[0], cur.description))
    print("column:", cols)
    print("OUTPUT:",data)
    #str_data = json.dumps(cur.fetchall())
    
    # path to file
    filename = '/tmp/test.csv'
    
    # write sql output onto csv file
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f,lineterminator='\n')
        
        # Add headers
        writer.writerow(cols)
        
        # add data from tuple into each row of csv
        for tup in data:
            writer.writerow(tup)
            
        print("file written successfully")
    
    # checking row count of csv file
    rowcount  = 0
    #iterating through the whole file
    for row in open(filename):
        rowcount+= 1
        #printing the result
    print("Number of rows:", rowcount)
    
    cur.close()
    conn.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps("Succeed !")
    }
