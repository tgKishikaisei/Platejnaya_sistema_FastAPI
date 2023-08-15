from database.models import User,Card, Transactions
from database import get_db


##　перевод денег
def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db())

    card_from_db = db.query(Card).filter_by(card_from).first()
    card_to_db = db.query(Card).filter_by(card_from).first()

    # proverka yest li eti karti
    if card_from_db and card_to_db:
        # proverka dostatochno li deneg
        if card_from_db.card_balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount

            new_transaction = Transactions(card_from=card_from,
                                           card_to=card_to,
                                           amount=amount,
                                           transaction_date=transaction_date)

            db.add(new_transaction)
            db.commit()
            return True
        return 'не достаточна денег'
    return 'карты нету'




## мониторинг по card_id истории плотежей
def get_card_history(user_id):
    db = next(get_db())

    if user_id:
        exact_user_card = db.query(Transactions).filter_by(id=user_id).all()

        return {'status': 1, 'message': exact_user_card}

    return {"status": 0, "message": "ошибка в данных"}
