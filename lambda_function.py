import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Books')

def lambda_handler(event, context):
    response = table.scan()
    books = response.get('Items', [])
    for book in books:
        book['price'] = float(book['price'])
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(books)
    }
