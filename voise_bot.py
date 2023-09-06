from aiogram import Bot, Dispatcher, types, executor
from gtts import gTTS

bot_audio = Bot('5844747637:AAEsILZzg92wsvPW5zVz0J9nYfvtJX0Qxk4')
dp = Dispatcher(bot_audio)

@dp.message_handler()
async def echo(msg):
        tts = gTTS(msg.text, lang='ru')
        tts.save(f'{msg.from_user.id}.mp3')
        await msg.answer_voice(open(f'{msg.from_user.id}.mp3', 'rb'))
    
executor.start_polling(dp)



#ссылка на бота - https://t.me/SSSRSSSbot