from aiogram import Bot, Dispatcher, types, executor
from gtts import gTTS
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('5844747637:AAEsILZzg92wsvPW5zVz0J9nYfvtJX0Qxk4')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Open Web Site', web_app=WebAppInfo(url='iaspizzhutvoiip.stotring1233.repl.co/telegram/html')))

        await bot.send_photo(msg.chat.id, 'https://mega-u.ru/wp-content/uploads/2022/12/105-3.jpg', reply_markup=markup)

@dp.message_handler(content_types=['text'])
async def echo(msg):
        tts = gTTS(msg.text, lang='ru')
        tts.save(f'{msg.from_user.id}.mp3')
        await msg.answer_voice(open(f'{msg.from_user.id}.mp3', 'rb'))
    
executor.start_polling(dp)



#ссылка на бота - https://t.me/SSSRSSSbot