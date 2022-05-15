import boto3
from utils import build_car_from_dynamo

dynamodb = boto3.client('dynamodb')


def find_all():
    items = dynamodb.scan(TableName='carros')["Items"]
    cars = []
    for car in items:
        cars.append(build_car_from_dynamo(car))
    return cars


def save(carro):
    dynamodb.put_item(
        TableName='carros',
        Item={
            'id': {"S": str(carro.id)},
            "fabricante": {"S": str(carro.fabricante)},
            "modelo": {"S": str(carro.modelo)},
            "ano": {"S": str(carro.ano)},
            "preco": {"S": str(carro.preco)}
        }
    )
    return carro


def delete_by_id(id):
    dynamodb.delete_item(
        TableName='carros',
        Key={
            'id': {"S": id}
        },
        ConditionExpression="attribute_exists (id)"
    )
