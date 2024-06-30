import allure
from helpers.user_data import *
from const_data import ResponseData


class TestLoginUser:
    @allure.title("Успешная авторизация юзера с верным логином и паролем")
    def test_login_user(self):
        data = register_new_user()
        response = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response.json()['accessToken']
        delete_user(token)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Неуспешная авторизация юзера с неверным логином и паролем")
    def test_login_courier_with_non_existent_data(self):
        data = generate_random_user_data()
        response = requests.post(Endpoints.login_user, json=data)

        assert response.status_code == 401
        assert ResponseData.incorrect_data_text in response.text
