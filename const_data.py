class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site'


class Endpoints:
    create_user = f'{Urls.main_url}/api/auth/register'
    login_user = f'{Urls.main_url}/api/auth/login'
    delete_user = f'{Urls.main_url}/api/auth/user'
    change_user_data = f'{Urls.main_url}/api/auth/user'
    create_order = f'{Urls.main_url}/api/orders'
    get_user_order = f'{Urls.main_url}/api/orders'


class UserData:
    existent_user = {
        "email": "piligrim@ya.ru",
        "password": "piligrim94",
        "name": "scott"
    }


class ResponseData:
    existent_user_text = "User already exists"
    user_without_field_text = "Email, password and name are required fields"
    incorrect_data_text = "email or password are incorrect"
    unauthorized_text = "You should be authorised"
    empty_hash_text = "Ingredient ids must be provided"
    get_orders_text = "orders"


class Ingredients:
    valid_hash = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    invalid_hash = {"ingredients": ["11111111111111111111111"]}
    empty_hash = {"ingredients": []}
