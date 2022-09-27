"""Методы для проверки ответов наших запросов"""
import json

from requests import Response

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print("Успешно!!! Статус код = " + str(responce.status_code))
        else:
            print("Провал!!! Статус код = " + str(responce.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(responce: Response, expected_value):
        token = json.loads(responce.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")