import json
from utils import http_response, build_car_from_body, generic_json_message, CAR_VALID_JSON_FORMART
from repository import *
import boto3

dynamodb = boto3.client('dynamodb')


class FindAllService:

    def process(self, event):
        try:
            items = find_all()
            cars = []
            for car in items:
                cars.append(build_car_from_dynamo(car))
            response = json.dumps(cars, default=lambda o: o.__dict__, indent=4)
            return http_response(response, 200)
        except:
            return http_response(generic_json_message("Ocorreu um problema. Tente novamente mais tarde"), 500)

    def supports(self, operation):
        return operation == "GET"


class SaveService:

    def process(self, event):
        try:
            body = json.loads(event["body"])
            car = build_car_from_body(body)
            saved_car = save(car)
            return http_response(json.dumps({"carro_id": saved_car.id}), 201)
        except (TypeError, KeyError):
            return http_response(generic_json_message("Não conseguimos salvar. Tente salvar utilizando o seguinte formato: " + CAR_VALID_JSON_FORMART), 400)
        except ValueError:
            return http_response(generic_json_message("Utilize numero inteiro para o campo 'ano' e numero decimal para o campo 'preco'. Exemplo: ano: 2022 e preco: 15.4"), 400)
        except Exception as e:
            print(e)
            return http_response(generic_json_message("Ocorreu um problema. Tente novamente mais tarde"), 500)

    def supports(self, operation):
        return operation == "POST"


class DeleteService:

    def process(self, event):
        response = None
        status_code = None
        try:
            id = event['pathParameters']['id']
            delete_by_id(id)
            response = "carro apagado com sucesso"
            status_code = '204'
        except:
            response = "Nenhum carro encontrado com o id informado"
            status_code = '404'
        return http_response(generic_json_message(response), status_code)

    def supports(self, operation):
        return operation == "DELETE"
