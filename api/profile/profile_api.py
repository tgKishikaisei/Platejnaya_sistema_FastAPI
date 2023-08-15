from main import app
from .profile_models import UserDent, CardDent
from fastapi import Body

# Регистрация ползователя
@app.post('/api/register-user')
async def user_registration(user_data: UserDent):
    print(UserDent)


    # После регистрации выдать айди пользователя
    return {'status': 1, 'message': 'Registration completed'}



# Вход в аккаунт
@app.post('/api/login-user')
async def login_user(phone_number: int = Body, password: str = Body):
    print(phone_number, password)
    # Проверка данных
    checker = None



    # если данные верны отправляем юзер
    return {'status': 1, 'message': 'Login_on'}

# Добовление карты в базу
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    # Вызов функции из бд для добовление карты в базу
    result = card_data
    print(card_data)

    # Если успешно доболена карты, то status 1
    return {'status': 1, 'message': result}


# выход данных о ползователя
@app.get('/api/user-data')
async def get_user_data(user_id: UserDent):
    result = user_id
    print(user_id)

    return {'status': 1, 'message': result}



#
@app.get('/api/user-cards')
async def get_user_cards(user_id: UserDent, card_id: CardDent):
      if user_id:
          result = card_id,user_id

          print(card_id)

          return {'status': 1, 'message': result}
