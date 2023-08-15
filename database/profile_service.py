from database.models import User, Card
from database import get_db
from datetime import datetime

#　регистрация
def register_user_db(profile_photo, name, surname, phone_number, email, city, reg_date, password):
    db = next(get_db())

    new_user = User(
        profile_photo=profile_photo,
        name=name,
        surname=surname,
        phone_number=phone_number,
        email=email,
        city=city,
        password=password,
        reg_date=datetime.now()
    )
    # добовляем в базу
    db.add(new_user)

    # сохрони в базе
    db.commit()

    return new_user


# функция проверки номера телефона и пароля
def phone_number(phone_number: int):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number).first()

    # Если есть совподения
    if checker:
        return False

    # А если нет совподение
    return True


# функция добовление карты ползователя
def add_card_user(user_id, card_number, exp_date, card_name):
    db = next(get_db())

    new_user_card = Card(user_id=user_id, card_number=card_number, exp_date=exp_date, card_name=card_name)

    db.add(new_user_card)
    db.commit()

    return "Карта добавлен"

# функция получение данных ползователя по user_id
def user_id_informations(user_id):
    db = next(get_db())

    exact_user_info = db.query(User).filter_by(id=user_id).first()

    if exact_user_info:
        return exact_user_info

    return 'Ошибка в данных'


## Получите его карты или определенную карту ползователя
def get_all_or_exact_card_db(card_id, user_id):
    db = next(get_db())

    # if we need all cards of user
    if user_id == 0:
        exact_user_card = db.query(Card).filter_by(user_id).all()

        return {'status': 1, 'message': exact_user_card}

    # if we need exact card
    elif card_id:
        exact_card = db.query(Card).filter_by(user_id).first()

        return {'status': 1, 'message': exact_card}

    else:
        all_cards = db.query(Card).all()

        return {'status': 1, 'message': all_cards}



