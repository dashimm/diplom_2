import allure
from helpers.user_data import *
from const_data import *


class TestGetOrder:
    @allure.title("Проверяем получение заказов конректного юзера")
    def test_get_user_orders(self):
        data = register_new_user()
        response_login = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response_login.json()['accessToken']
        requests.post(Endpoints.create_order,
                      headers={"Authorization": token}, json=Ingredients.valid_hash)

        response = requests.get(Endpoints.get_user_order, headers={"Authorization": token})
        delete_user(token)

        assert response.status_code == 200
        assert ResponseData.get_orders_text in response.text

    @allure.title("Проверяем, что неавторизованный юзер не может получить список заказов")
    def test_get_orders_by_unauthorized_user(self):
        response = requests.get(Endpoints.get_user_order)

        assert response.status_code == 401
        assert ResponseData.unauthorized_text in response.text
