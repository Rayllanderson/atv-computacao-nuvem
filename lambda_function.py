import json
from services import *

available_services = [
    GetOperation(),
    PostOperation(),
    DeleteOperation()
]


def lambda_handler(event, context):
    operation = event['httpMethod']
    
    for service in available_services:
        if service.supports(operation):
            return service.process(event)
    return {
        'statusCode': 405,
        'body': json.dumps({"message": "Método não disponível"}),
        'headers': {
        'Content-Type': 'application/json',
        }
    }
    
