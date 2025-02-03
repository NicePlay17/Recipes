import hashlib
# SHA256
def login:
    считываем из pydantic модели json юзера 
    
    pydantic стучится в бд и проверяет есть ли такой логин с юзером
    если он есть проверяем его пароль в хэш
    ЕСЛИ ХЭШИ совпадают то формируем Json Webtoken JWT отправляем его в ответе клиенту

    JWT - шифр, в котором шифруются данные юзера
    вы можете туда положить все что угодно про юзера
    например его имя, срок действия

    python jose
    jose - python 2

    token = jose
    token lifetime

    return token


def register:

def reset_password:


Перед отправкой данного запроса прикрепляю заголовок Authorization: Bearer JWT

http://localhost:8000/auth/profile

def get_user_profile: