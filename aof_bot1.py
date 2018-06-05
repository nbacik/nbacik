###importing telebot API - will need only this
import telebot

###our token and bot init
bot = telebot.TeleBot("MAH:605872298:AAFd4MxH7_jvZaghCpNr8r1p_Pw7pfHkq5Y")



###handler for start and help command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.send_message(message.chat.id, "Дратути! \nЭтот бот создан для обратной связи с каналом Apeture On Full[HD] - https://t.me/aofullhd \nВы таки хочете нам шо-то сказать? \nПошлите нам что угодно - картинку, видосик, ссылочку, стикер - даже просто пожелания, и в$



yopta = ['ДА', 'ДАА', 'ДААА', 'YES', 'АГА', 'ЫЫЫ', 'Ы', 'DA', 'DAA', 'DAAA']




###simple about_us info
@bot.message_handler(commands=['about', 'wassup'])
def send_info (message):
        bot.send_message(message.chat.id, "[HD] Photos! \n \nБот написан и протестиро$



###handler for everything text - forwards message to admins
@bot.message_handler(content_types=['text'])
def echo_text(message):
        if message.text.upper() in yopta:
                bot.send_message(message.chat.id, 'Спасибо ёпта :3')
                bot.forward_message(173888171, message.chat.id, message.message_id)###Seymur
                bot.forward_message(471864146, message.chat.id, message.message_id)###Togrul
                
        else:
                bot.send_message(message.chat.id, "Мы получили ваше сообщение, спасибо! \nЕсли вы хотите чтоб мы упомянули вас - ответьте ДА")
                bot.forward_message(173888171, message.chat.id, message.message_id)###Seymur
                bot.forward_message(471864146, message.chat.id, message.message_id)###Togrul
 





###handler for everything except stickers - forwards message to admins
@bot.message_handler(content_types=['photo', 'document', 'audio', 'voice', 'video_note', 'location'])
def echo_pic(message):
        bot.send_message(message.chat.id, "Мы получили ваше сообщение, спасибо! \nЕсли вы хотите чтоб мы упомянули вас - ответьте ДА")
        bot.forward_message(173888171, message.chat.id, message.message_id)###Seymur
        bot.forward_message(471864146, message.chat.id, message.message_id)###Togrul


			 
###separate handler for stickers as it is not visible whom is sticker forwarded from - asks for additional info
@bot.message_handler(content_types=['sticker'])
def echo_all(message):
        bot.send_message(message.chat.id, "Так как вы прислали стикер - напишите пару слов о нем, чтоб мы знали что с ним делать")
        bot.forward_message(173888171, message.chat.id, message.message_id)###Seymur
        bot.forward_message(471864146, message.chat.id, message.message_id)###Togrul




###line below can be used for user name retrieval
#+'\n'+message.from_user.first_name)
###yes you probably ask why don't I use this for sticker handling
### well, fuck you, that's why

###poll
bot.polling()
