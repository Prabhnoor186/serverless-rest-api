import json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    method = event['httpMethod']
    path   = event['path']

    if method == 'GET' and path == '/items':
        result = table.scan()
        return response(200, result['Items'])

    elif method == 'GET':
        item_id = event['pathParameters']['id']
        result  = table.get_item(Key={'id': item_id})
        item    = result.get('Item')
        return response(200, item) if item else response(404, {'error': 'Not found'})

    elif method == 'POST':
        body = json.loads(event['body'])
        table.put_item(Item=body)
        return response(201, {'message': 'Created', 'item': body})

    elif method == 'DELETE':
        item_id = event['pathParameters']['id']
        table.delete_item(Key={'id': item_id})
        return response(200, {'message': 'Deleted'})

    return response(400, {'error': 'Unsupported method'})

def response(status, body):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }