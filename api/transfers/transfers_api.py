from main import app
from api.transfers.transfer_models import P2PDent
from database.transfer_service import get_card_history


# Запрос на перевод денег между картами
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    # Функция перевода денег
    result = transfer_data
    print(result)

    # если перевод успешный, то status: 1
    return {'status': 1, 'message': result}

# функция получение последных трансакции ползователя
@app.get('/api/monitoring')
async def user_payment(user_id: int):
    result = get_card_history(user_id)

    print(result)

    return {'status': 1, 'message': result}

