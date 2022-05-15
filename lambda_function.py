import json
from services import FindAllService, SaveService, DeleteService
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


available_services = [
    FindAllService(),
    SaveService(),
    DeleteService()
]


def lambda_handler(event, context):
    method = event['httpMethod']
    
    logger.info('Request recebida, metodo=%s', method)
    
    for service in available_services:
        if service.supports(method):
            return service.process(event)
    return {
        'statusCode': 405,
        'body': json.dumps({"message": "Método não disponível"}),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
