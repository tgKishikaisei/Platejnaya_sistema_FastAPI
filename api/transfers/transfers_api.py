from main import app
from .transfer_models import  P2PDent
from pydantic import BaseModel


@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    # Funksiya perevoda deneg
    result = transfer_data
    print(result)

    # yesli kod uspeshniy, to status
    return {'status': 1, 'message': result}


# функция получение последных трансакции ползователя
@app.get('/api/monitoring')
async def user_payment(user_id: P2PDent):
    result = user_id
    print(result)

    return {'status': 1, 'message': result}

