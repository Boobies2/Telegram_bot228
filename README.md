# Telegram_bot228

![[Pasted image 20250317132140.png]]
### как бот работает в целом

1. Пользователь отправляет сообщение боту в Telegram.
2. Бот получает это сообщение через библиотеку `python-telegram-bot`.
3. Бот сохраняет сообщение в Redis для будущего использования.
4. Бот отправляет пользователю ответ, подтверждая, что сообщение сохранено.

### 1. получение сообщения

когда пользователь отправляет сообщение боту в Telegram, это сообщение передается на сервер tg, который обрабатывает запрос и передает его вашему боту через tg Bot API

### 2. подключение к боту через `python-telegram-bot`

бот использует библиотеку `python-telegram-bot`, которая облегчает работу с tg Bot api. эта библиотека предоставляет инструменты для взаимодействия с ботом, обработки сообщений и обработки команд

### 3. обработка команд и сообщений

Пример обработчика команды `/start`:

```python
async def start(update: Update, context: CallbackContext):  
    await update.message.reply_text("я сохранять ваше саабщение в редиска о великий гаспадиннн")
```

этот обработчик отвечает пользователю приветственным сообщением когда он отправляет команду `/start`

Для обработки всех сообщений которые не являются командами используется `MessageHandler`:

```python
async def save_message(update: Update, context: CallbackContext):  
    message = update.message.text  
  
    r.lpush('messages', message)  
  
    saved_count = r.llen('messages')  
  
    await update.message.reply_text(f"о преподобный ваше сообщение услышали сами боги! сичас на вашем счету {saved_count} социального рейтинга")
```

этот обработчик:

1. получает текст сообщения с помощью `update.message.text`
2. сохраняет сообщение в Redis с помощью метода `lpush` который добавляет сообщение в список
3. отправляет подтверждение пользователю что его сообщение сохранено в базе данных редиски

### 4. подключение к Redis

для хранения сообщений бот использует **редиска** — это база данных в памяти, которая позволяет быстро хранить и извлекать данные. бот подключается к редиске следующим образом:

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
```

- `host='localhost'` — это адрес сервера Redis. В данном случае используется локальный сервер Redis.
- `port=6379` — это стандартный порт, на котором работает Redis.
- `db=0` — это номер базы данных Redis, к которой происходит подключение.

после установления соединения с Redis, бот сохраняет текст сообщений в Redis с использованием команды `lpush`, которая добавляет сообщение в список Redis.

### 5. запуск бота

для того чтобы бот начал работать, нужно вызвать функцию `updater.start_polling()`:

```python
updater.start_polling()
updater.idle()
```

- `start_polling()` — это метод, который запускает процесс отслеживания новых сообщений от пользователей. Бот будет регулярно проверять новые сообщения и передавать их в обработчики.
- `idle()` — эта функция позволяет боту продолжать работать, пока не будет остановлен вручную.

### 7. взаимодействие с Redis

все сообщения, которые отправляют пользователи боту, сохраняются в **Redis** в списке под названием `messages`. Это позволяет вам легко извлекать все сохраненные сообщения, если это необходимо.

можно подключиться к редиске и проверить содержимое списка с помощью `redis-cli` или через питон, используя библиотеку redis.


### Как использовать бота

1. запуск редиски на докере.
2. запуск файла с ботом:
    
    ```bash
    python tg_bot.py
    ```
    
3. пишем боту что он лох попущенный


