import allure
from helpers.user_data import *
from const_data import *


class TestChangeData:

    @allure.title("Проверяем изменение данных с авторизованным юзером")
    def test_change_user_data(self):
        data = register_new_user()
        response_login = requests.post(Endpoints.login_user, json={"email": data[0], "password": data[1]})
        token = response_login.json()['accessToken']
        update_data = generate_random_user_data()
        response = requests.patch(Endpoints.change_user_data, headers={"Authorization": token},
                                  json={"email": update_data.get("email"),
                                        "name": update_data.get("name"),
                                        "password": update_data.get("password")})
        delete_user(token)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Проверяем, что данные поменять нельзя с неавторизованным юзером")
    def test_change_unauthorized_user_data(self):
        update_data = generate_random_user_data()
        response = requests.patch(Endpoints.change_user_data, json=update_data)

        assert response.status_code == 401
        assert ResponseData.unauthorized_text in response.text
