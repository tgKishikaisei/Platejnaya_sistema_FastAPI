from database.models import User, Card
from database import get_db


#　регистрация (учитель)


# функция проверки номера телефона и пароля


# функция добовление карты ползователя


# функция получение данных ползователя по user_id


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



