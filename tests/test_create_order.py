import allure
from helpers.user_data import *
from const_data import *


class TestCreateOrder:
    @allure.title("Проверяем создание заказа с валидными ингредиентами авторизованным юзером")
    def test_create_order_with_correct_ingredients(self):
        data = register_new_user()
        response_login = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response_login.json()['accessToken']
        response = requests.post(Endpoints.create_order,
                                 headers={"Authorization": token}, json=Ingredients.valid_hash)
        delete_user(token)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Проверяем создание заказа с невалидными ингредиентами авторизованным юзером")
    def test_create_order_with_incorrect_ingredients(self):
        data = register_new_user()
        response_login = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response_login.json()['accessToken']
        response = requests.post(Endpoints.create_order,
                                 headers={"Authorization": token}, json=Ingredients.invalid_hash)
        delete_user(token)

        assert response.status_code == 500

    @allure.title("Проверяем создание заказа с валидными ингредиентами неавторизованным юзером")
    def test_create_order_by_unauthorized_user(self):
        response = requests.post(Endpoints.create_order, json=Ingredients.valid_hash)

        assert response.status_code == 200
        assert response.json().get("success") is True
        # можно создать заказ неавторизованным юзером, поэтому в ответе проверяется 200 и True

    @allure.title("Проверяем создание заказа без ингредиентов авторизованным юзером")
    def test_create_order_without_ingredients(self):
        data = register_new_user()
        response_login = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response_login.json()['accessToken']
        response = requests.post(Endpoints.create_order,
                                 headers={"Authorization": token}, json=Ingredients.empty_hash)
        delete_user(token)

        assert response.status_code == 400
        assert ResponseData.empty_hash_text in response.text
