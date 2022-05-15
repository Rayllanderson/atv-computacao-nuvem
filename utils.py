import uuid
import json
from model import Carro


def http_response(response_body, status_code):
    return {
        'statusCode': str(status_code),
        'body': response_body,
        'headers': {
            'Content-Type': 'application/json',
        }
    }


def generic_json_message(message):
    return json.dumps({"message": message})


def build_car_from_body(body):
    id = str(uuid.uuid4())
    fabricante = body["fabricante"]
    modelo = body["modelo"]
    ano = int(body["ano"])
    preco = float(body["preco"])
    return Carro(id, fabricante, modelo, ano, preco)


def build_car_from_dynamo(item):
    if item:
        id = item["id"]["S"]
        fabricante = item["fabricante"]["S"]
        modelo = item["modelo"]["S"]
        ano = int(item["ano"]["S"])
        preco = float(item["preco"]["S"])
        return Carro(id, fabricante, modelo, ano, preco)


CAR_VALID_JSON_FORMART = '{"fabricante": "Ford", "modelo": "Ka", "ano": 2010, "preco": 11000}'
