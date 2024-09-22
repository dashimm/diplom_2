from const_data import *
import allure
from helpers.user_data import *
from const_data import Endpoints


class TestCreateUser:
    @allure.title("Создание уникального юзера со всеми обязательными данными")
    def test_create_user(self):
        data = generate_random_user_data()
        response = requests.post(Endpoints.create_user, json=data)
        token = response.json()['accessToken']
        delete_user(token)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание существующего юзера возвращает ошибку")
    def test_create_existent_user(self):
        data = UserData.existent_user
        response = requests.post(Endpoints.create_user, json=data)

        assert response.status_code == 403
        assert ResponseData.existent_user_text in response.text

    @allure.title("Создание юзера без имейла возвращает ошибку")
    def test_create_user_without_email(self):
        data = generate_random_user_data_without_email()
        response = requests.post(Endpoints.create_user, json=data)

        assert response.status_code == 403
        assert ResponseData.user_without_field_text in response.text

    @allure.title("Создание юзера без пароля возвращает ошибку")
    def test_create_user_without_password(self):
        data = generate_random_user_data_without_password()
        response = requests.post(Endpoints.create_user, json=data)

        assert response.status_code == 403
        assert ResponseData.user_without_field_text in response.text

    @allure.title("Создание юзера без имени возвращает ошибку")
    def test_create_user_without_name(self):
        data = generate_random_user_data_without_name()
        response = requests.post(Endpoints.create_user, json=data)

        assert response.status_code == 403
        assert ResponseData.user_without_field_text in response.text
