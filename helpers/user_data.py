import requests
from faker import Faker
from const_data import Endpoints


def generate_random_user_data():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    data = {
        "email": email,
        "password": password,
        "name": name
    }

    return data


def generate_random_user_data_without_email():
    fake = Faker()
    password = fake.password()
    name = fake.first_name()
    data = {
        "email": "",
        "password": password,
        "name": name
    }

    return data


def generate_random_user_data_without_password():
    fake = Faker()
    email = fake.email()
    name = fake.first_name()
    data = {
        "email": email,
        "password": "",
        "name": name
    }

    return data


def generate_random_user_data_without_name():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    data = {
        "email": email,
        "password": password,
        "name": ""
    }

    return data


def register_new_user():
    login_pass = []
    data = generate_random_user_data()
    response = requests.post(Endpoints.create_user, data=data)
    if response.status_code == 200:
        login_pass.append(data.get("email"))
        login_pass.append(data.get("password"))
        login_pass.append(data.get("name"))

    return login_pass


def delete_user(token):
    return requests.delete(Endpoints.delete_user, headers={"Authorization": token})
