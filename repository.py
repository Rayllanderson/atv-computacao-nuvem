import boto3

dynamodb = boto3.client('dynamodb')


def find_all():
    return dynamodb.scan(TableName='carros')["Items"]


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
