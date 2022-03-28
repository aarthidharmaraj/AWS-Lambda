import json
import boto3

dynamodb=boto3.resource('dynamodb')
## to get an item from database
table=dynamodb.Table('Planets') ##database and table created in lambda database
def lambda_handler(event,context):
    response=table.get_item(
        key={
            'id':'mercury'
        }
    )
    print(response)
    return {
        'statusCode':200,
        'body': response
    }
    
## to put an item to a database
table=dynamodb.Table('Planets') ##database and table created in lambda database
def lambda_handler(event,context):
    table.put_item(
        Item={
            'id':'mercurynew',
            'temp':'cold'
        }
    )
    response={
        'message':'Item added successfully'
    }
    return {
        'statusCode':200,
        'body': response
    }