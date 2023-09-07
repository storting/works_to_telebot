import json
import requests
import telebot
from telebot import types






bot = telebot.TeleBot("6676568390:AAGMnIjtwoatJKjjpQBq49sUvczAChIvraw", parse_mode=None)
API_weather = '9d15bace01ea0751de8736bb688beff9'





flag = False
weather = 0


class Main_keyboard:

    
    def __init__(self, msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Url') 
        btn2 = types.KeyboardButton('Meme')
        btn3 = types.KeyboardButton('Weather')
        markup.row(btn1)
        markup.row(btn2, btn3)  
        self.click(msg)
        
    def click(self, msg):
        global flag 
        
        if msg.text == 'Url':
            flag = True
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Twitch', url='https://www.twitch.tv/storting_')       
            btn2 = types.InlineKeyboardButton('YouTube', url='https://www.youtube.com/channel/UCg7qiChcgDiHpWCo53iR8Xg')
            markup.row(btn1, btn2)
            bot.send_message(msg.chat.id, "Pls follow <3", reply_markup=markup)
            
            
        elif msg.text == 'Meme':
            flag = True
            bot.send_photo(msg.chat.id, 'https://image.winudf.com/v2/image1/Y29tLndhbGxwYXBlci53YWxscGFwZXJzLkFsbE1lbWVzQW5\
                                        kVHJvbGxTYXJjYXNtUGljc1dhbGxwYXBlcnNhbmRCYWNrZ3JvdW5kc19zY3JlZW5fMTBfMTYwMDEwMTE4Nl8wNzg/screen-6.jpg?fakeurl=1&type=.jpg')
        elif msg.text == 'Weather':
            bot.send_message(msg.chat.id, 'In what city?')
            global weather 
            weather = 1
           
    
    def get_weather(self, msg):
        global weather 
        global flag
        global API_weather
        city = msg.text.strip().lower()
        res =  requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_weather}&units=metric')
        data = json.loads(res.text)
        weather = 0
        bot.send_message(msg.chat.id, f'<b>Weather</b> in <u>{msg.text}</u> {data["main"]["temp"]}°', parse_mode="HTML")


@bot.message_handler(commands=['start'])
def start(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Url') 
    btn2 = types.KeyboardButton('Meme')
    btn3 = types.KeyboardButton('Weather')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(msg.chat.id, f'Hello, {msg.from_user.first_name}', reply_markup=markup)
    Main_keyboard(msg)

@bot.message_handler(content_types=['text'])
def weatherr(msg):
    global weather 
    global flag
    Main_keyboard(msg)
    if weather < 3:
        weather += 1
    if weather == 3:
        Main_keyboard(msg).get_weather(msg)
    flag = False   

@bot.message_handler(content_types=['photo', 'text'])
def reply(msg):
    global flag
    Main_keyboard(msg)
    if flag == False:
        bot.reply_to(msg, 'I do not know what it is(')
    flag = False 

@bot.message_handler(content_types=['voice'])
def reply(msg):
    bot.send_message(msg.chat.id)
    Main_keyboard(msg)
    


bot.polling(none_stop=True)


#ссылка на бота - https://t.me/test123412252534534543Bot