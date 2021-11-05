import telebot
from telebot import types

bot = telebot.TeleBot('2045372836:AAHarw0A9WZS_H_j_fwOnU3JFwwT2FKV5Ew')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Vk')
	markup.add(btn1)
	send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nСоцаильные сети игрока Алана Абдулина"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "начать тест заново":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Создание игр')
		markup.add(btn1)

		final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"

	elif get_message_bot == "создание игр":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Под мобильные телефоны')
		btn2 = types.KeyboardButton("Начать тест заново")
		markup.add(btn1, btn2)
		final_message = "Отлично, геймдев крутая тема, но под что хочется разрабатывать?"
	elif get_message_bot == "под мобильные телефоны":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))
		final_message = "Для разработки игр под мобильные устройства зачастую используется игровой движок <a href='https://itproger.com/tag/unity'>Unity</a>\nДвижок прост в изучении и вы можете просмотреть курсы по нему по кнопке ниже"
	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Создание игр')
		markup.add(btn1)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)