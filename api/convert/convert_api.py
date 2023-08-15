import requests

from main import app



# Получить курс ЦБ и нашего сервиса
@app.get('/api/get-currency')
async def currency_rate():
    # подкючение к json или api ЦБ
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()

    # Получаем курс необходимых валют
    usr_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']

    # выдаем ответ
    return {'status': 1, 'rates': {'USD': usr_rate,
                                   'EUR': eur_rate,
                                   'RUB': rub_rate
                                   }}

