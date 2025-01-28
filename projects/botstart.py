import config

import json

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters



# Збереження даних
def save_user_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)

# Завантаження даних
def load_user_data():
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}
    
    return user_data


def is_integer(value):
    try:
        # Спробуємо перетворити значення в ціле число
        int_value = int(value)
        # Перевірка на рівність введеного значення і його цілої частини
        return True
    except ValueError:
        # Якщо виникає помилка при перетворенні, значить це не ціле число
        return False



# Привітання та початкове меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Основні кнопки
    reply_keyboard = [["Показати підручник", "Допомога", "Вихід"]]

    await update.message.reply_text(
        "Привіт! Оберіть одну з опцій нижче:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )

# Обробка вибору "Показати дати"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    if user_message == "Показати підручник":
        # Створення інлайн-кнопок
        keyboard = [
            [InlineKeyboardButton("Алгебра 9. Істер", callback_data="а9іster")],
            [InlineKeyboardButton("Алгебра 8. Істер", callback_data="а8іster")],
            [InlineKeyboardButton("Алгебра 7. Істер", callback_data="а7іster")],
            [InlineKeyboardButton("Геометрія 9. Істер", callback_data="h9іster")],
            [InlineKeyboardButton("Геометрія 8. Істер", callback_data="h8іster")],
            [InlineKeyboardButton("Геометрія 7. Істер", callback_data="h7іster")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("Оберіть підручник:", reply_markup=reply_markup)
    elif user_message == "Допомога":
        await update.message.reply_text("Цей бот допомагає вам обирати дати.")
    elif user_message == "Вихід":
        await update.message.reply_text("До побачення!", reply_markup=None)
    elif is_integer(user_message):
        await update.message.reply_text(f"Ви ввели номер {user_message}. Чекайте відповіді")
        # Вказуємо ім'я файлу зображення в тій самій папці, де знаходиться скрипт
        image_path = "111.png"  # Замініть на ім'я вашого файлу
        # Надсилаємо зображення користувачу
        await update.message.reply_photo(photo=open(image_path, 'rb'))
        
    else:
        await update.message.reply_text("Невідома команда. Спробуйте ще раз.")

# Обробка натискання на інлайн-кнопку
async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Відповідає Telegram, щоб закрити завантаження

    user_id = query.from_user.id
    selected_date = query.data

    # Зберігаємо дату для користувача
    user_data[user_id] = selected_date
    save_user_data()

    await query.edit_message_text(text=f"Ви обрали книгу: {selected_date}")
    await query.message.reply_text("Ця книга збережена для вас до кінця поточної сесії!")
    await query.message.reply_text("Надішліть мені номер із підручника і я надішлю вам відповідь")

# Використання збереженої дати
async def show_saved_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    print(user_id, user_data)
    if user_id in user_data:
        saved_date = user_data[user_id]        
        await update.message.reply_text(f"Ваша збережена дата: {saved_date}")
    else:
        await update.message.reply_text("У вас поки немає збереженої дати.")

# Основна функція
def main():
    load_user_data()
    # Ініціалізація бота
    app = Application.builder().token(config.TOKEN).build()

    # Додавання обробників
    app.add_handler(CommandHandler("start", start))  # Стартова команда
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обробка текстових повідомлень
    app.add_handler(CallbackQueryHandler(inline_button_handler))  # Обробка натискань на інлайн-кнопки
    app.add_handler(CommandHandler("show_date", show_saved_date))  # Команда для показу збереженої дати

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    # Словник для збереження даних користувачів
    user_data = load_user_data()
    main()
