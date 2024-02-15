import telebot
from telebot.apihelper import ApiTelegramException
from telebot import types
import time
import sqlite3
bot = telebot.TeleBot('6197037736:WG2EzRVw4U_ABRxkY')
notsubchik = 'Для доступа к боту подпишитесь на канал💡'
fileee = open('chatids.txt', 'r')
ju = set();a = None;balans = None;lolkek = None;b = set();idpolzz = None;v = set();p = set()
minvivod = 100
minpopol = 100
admin_id = 1796627731
ban_time = None
vivodcol = 0
for line in fileee:
    ju.add(line.strip())
fileee.close()
banned_users = set();cartinochki = set()
flex = 0.7
@bot.message_handler(commands=['start'])
def start(message):
    popolnenia = sqlite3.connect('popolnenia.sql')
    pcur = popolnenia.cursor()
    pcur.execute('CREATE TABLE IF NOT EXISTS pop (id int primary key, cheki varchar,orid)')
    pcur.close()
    popolnenia.close()
    vivodi = sqlite3.connect('vivodi.sql')
    vcur = vivodi.cursor()
    vcur.execute('CREATE TABLE IF NOT EXISTS viv (id int primary key, cheki varchar,orid'
                 ')')
    vcur.close()
    vivodi.close()
    global banned_users
    if a in banned_users:
        time.sleep(int(ban_time))
        banned_users.remove(str(a))
    else:


        time.sleep(0.1)
        if not str(message.chat.id) in ju:
            baza = sqlite3.connect('baza.sql')
            cur = baza.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS users (id int primary key, name varchar(50),balans int (50))')
            cur.execute('INSERT OR REPLACE INTO users (id, name ) VALUES("%s","%s")' % (
            message.from_user.id, message.from_user.username ,))
            baza.commit()
            cur.close()
            baza.close()
            fileee = open('chatids.txt', 'a')
            fileee.write(str(message.chat.id) + '\n')
            ju.add(message.chat.id)
        if message.chat.type == 'private':
         #   my_channel_id = "-1002037721518"
          #  user_id = message.from_user.id
          #  member = bot.get_chat_member(chat_id=my_channel_id, user_id=user_id)
          #  statuses = ('creator', 'administrator', 'member')
            #if member.status in statuses:
                global kkkk
                if message.from_user.id == admin_id:
                    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    but2 = types.KeyboardButton('💵Пополнить')
                    but45 = types.KeyboardButton('🍯Вывести')
                    but54 = types.KeyboardButton('👨Профиль')
                    button.row(but54, but45, but2)
                    but4 = types.KeyboardButton('🔢Калькулятор')
                    button.row(but4)
                    but6 = types.KeyboardButton('Информация📖')
                    but5 = types.KeyboardButton('ТехПоддержка🧑‍💻')
                    but12 = types.KeyboardButton('Отзывы⚡')
                    button.row(but6, but5, but12)
                    adminbut = types.KeyboardButton('ADMINPANEL🧑‍💻')
                    button.row(adminbut)
                    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYD9lyMtYbTUVEOXgPXSKj0jIV5nqkgAC3TkAAibmkEvWOX4d2geVrjQE')
                    bot.send_message(message.chat.id, 'Привет,админ❤️‍🔥', reply_markup=button)

                else:
                    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    but2 = types.KeyboardButton('💵Пополнить')
                    but45 = types.KeyboardButton('🍯Вывести')
                    but54 = types.KeyboardButton('👨Профиль')
                    button.row(but54,but45,but2)
                    but4 = types.KeyboardButton('🔢Калькулятор')
                    button.row(but4)
                    but6 = types.KeyboardButton('Информация📖')
                    but5 = types.KeyboardButton('ТехПоддержка🧑‍💻')
                    but12 = types.KeyboardButton('Отзывы⚡')
                    button.row(but6, but5, but12)
                    file = open('./photo_5404556833064078945_y.jpg', 'rb')
                    bot.send_photo(message.chat.id, file,
                                   'Добро пожаловать в лучший шоп голды StonksGold🍯 \n🔆 Для продолжения выбери нужную команду на клавиатуре\n❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «ТехПоддержка🧑‍💻»',
                                   reply_markup=button)
                    bot.send_sticker(message.chat.id,
                                     'CAACAgIAAxkBAAELYD9lyMtYbTUVEOXgPXSKj0jIV5nqkgAC3TkAAibmkEvWOX4d2geVrjQE')

         #   else:
          #      notsub = types.InlineKeyboardMarkup()
          #      notsub1 = types.InlineKeyboardButton('Подписаться', url='https://t.me/StonksGold')
          #      notsub.row(notsub1)
          #      file = open('./photo_5404556833064078945_y.jpg', 'rb')
          #      bot.send_photo(message.chat.id, file, notsubchik, reply_markup=notsub)


@bot.message_handler(content_types=['text','photo'])
def buttonsss(message):
    global banned_users
    global a
    if a in banned_users:
        time.sleep(int(ban_time))
        try:
            banned_users.remove(str(a))
        except:
            return()
    else:
        if message.chat.type == 'private':
            if message.text == '🍯Вывести':
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYFJlyM1FkKgahdm53ZPpLtwRjgcuBwACvjwAArIRkUu4JWT98YCLqzQE')
                bot.send_message(message.chat.id,'🍯Напиши количество голды,которое хочешь вывести')
                bot.register_next_step_handler(message, vivod)
            if message.text == 'ADMINPANEL🧑‍💻':
                if message.chat.id == admin_id:
                    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYEFlyMxrqLfI4NpNBilMXjVmXEYGBgACkjwAAi3nkEtwmptv_LHdqDQE')
                    inftut = types.InlineKeyboardMarkup()
                    inftutbaza = types.InlineKeyboardButton('🤖База данных', callback_data='bazaa')
                    intut2 = types.InlineKeyboardButton('🛑Бан Пользователя', callback_data='ban')
                    intut1 = types.InlineKeyboardButton('🌀Рассылка', callback_data='rassylka')
                    inftut.row(intut1, intut2)
                    inftut4 = types.InlineKeyboardButton('🧑‍💻Изменить баланс пользователю', callback_data='cheki')
                    inftut3 = types.InlineKeyboardButton('🧑‍💻Написать пользователю', callback_data='soobsh')
                    inftut.row(inftut3,inftut4)
                    inftut5 = types.InlineKeyboardButton('📉Изменить курс', callback_data='cucurs')
                    inftut.row(inftut5,inftutbaza)
                    minvivod = types.InlineKeyboardButton('💎Изменить минимальный вывод', callback_data='minvivod')
                    minpopol = types.InlineKeyboardButton('💎Изменить минимальное пополнение', callback_data='minpopol')
                    inftut.row(minvivod)
                    inftut.row(minpopol)
                    v = types.InlineKeyboardButton('💎Выводы', callback_data='v')
                    p = types.InlineKeyboardButton('💎Пополнения', callback_data='p')
                    inftut.row(v,p)
                    photooo = open('photo_5404556833064078945_y.jpg','rb')
                    bot.send_photo(message.chat.id, photooo ,'🧑‍💻Добро пожаловать в админ панель! \n\n\n           **********************************************            \n\n\n🔐Выберите действие:', reply_markup=inftut)
                else:
                    bot.send_message(message.chat.id,'Нет доступа!')
            if message.text == '👨Профиль':
                baza = sqlite3.connect('baza.sql')
                cur = baza.cursor()
                cur.execute('SELECT * FROM users WHERE id = %s' % (message.from_user.id))
                arka = cur.fetchall()
                for el in arka:
                    if el[2] == None:
                        bot.send_sticker(message.chat.id,
                                         'CAACAgIAAxkBAAELYJNlyOSyVE7O-MP4JnpTkv4Lmjyw6gACUEAAAnDgkUtzxLADbS7ULTQE'
                                         )
                        adnin = types.InlineKeyboardMarkup()
                        adnun = types.InlineKeyboardButton('💰Пополнить баланс', callback_data='popol')
                        adnin.row(adnun)
                        f = open('photo_5404556833064078945_y.jpg' , 'rb')
                        bot.send_photo(message.chat.id,f , '🙋‍♂️‍Привет, ' + str(message.from_user.first_name) +'\n🆔Ваш id: ' + str(message.from_user.id) + '\n💵Ваш баланс: 0' , reply_markup=adnin)
                    else:
                        bot.send_sticker(message.chat.id,
                                         'CAACAgIAAxkBAAELYJNlyOSyVE7O-MP4JnpTkv4Lmjyw6gACUEAAAnDgkUtzxLADbS7ULTQE'
                                         )
                        f = open('photo_5404556833064078945_y.jpg' , 'rb')
                        adnin = types.InlineKeyboardMarkup()
                        adnun = types.InlineKeyboardButton('💰Пополнить баланс', callback_data='popol')
                        adnin.row(adnun)
                        bot.send_photo(message.chat.id,f ,'🙋‍♂️Привет, ' + str(message.from_user.first_name) + '\n🆔Ваш id: ' + str(message.from_user.id) + '\n💵Ваш баланс: ' + f'{el[2]}',reply_markup = adnin)
                baza.close()
            if message.text == 'Отзывы⚡':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAELYI1lyOPPbHU6Dd7oYSdzEu4we9Gi2QACcToAAlWKkUu2X7qog2ZWfzQE')
                inftut = types.InlineKeyboardMarkup()
                intut1 = types.InlineKeyboardButton('Наш канал💡', url='https://t.me/StonksGold')
                inftut.row(intut1)
                bot.send_message(message.chat.id, '📃 Ссылка на наш канал с отзывами.', reply_markup=inftut)
            if message.text == 'Информация📖':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAELYJFlyOQKTeuFgi_3boO2oLbpYqI1yQACT0AAAmMbkEtyjplf3zjn0TQE')
                infbut = types.InlineKeyboardMarkup()
                inf1 = types.InlineKeyboardButton('Наш канал💡', url='https://t.me/StonksGold')
                infbut.row(inf1)
                inf2 = types.InlineKeyboardButton('Курс📉', callback_data='COURSE')
                inf3 = types.InlineKeyboardButton('Админ🧑‍💻', url = 'https://t.me/BOMONTl')
                infbut.row(inf2, inf3)
                bot.send_message(message.chat.id, ' 📋 Выберите нужный пункт', reply_markup=infbut)
            if message.text == 'ТехПоддержка🧑‍💻':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAELYI9lyOPvHVU_f5DB2gmpPr_4zmrJ6wACfjcAApsTkUsn729BeKtSNDQE')

                inline = types.InlineKeyboardMarkup()
                inb1 = types.InlineKeyboardButton('Частые вопросы', callback_data='Question')
                inb2 = types.InlineKeyboardButton('Написать админу🧑‍💻', url = 'https://t.me/BOMONTl')
                inline.add(inb1, inb2)
                bot.send_message(message.chat.id,
                                 'Если вы хотите что то узнать,нажмите на "Частые вопросы" , если не нашли ответ,нажмите "Написать админу🧑‍💻 ',
                                 reply_markup=inline)
            if message.text == '🔢Калькулятор':
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYItlyOOR0hdSb3K53T9DmB8ac0KObwACQD0AAqpNiEuJkF71Jj3aIDQE')
                bot.send_message(message.chat.id, '⭐Назовите количество голды,которое вы хотите купить: ')
                bot.register_next_step_handler(message, calculate)
            if message.text == '💵Пополнить':
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE'
                                 )
                bot.send_message(message.chat.id,
                                 '⭐Назовите количество рублей,на которое вы хотите пополнить аккаунт: ')
                bot.register_next_step_handler(message, bg)


def bg(message):
    try:
        global flex
        num_gold = message.text
        res = int(int(num_gold) // float(flex))
        inli = types.InlineKeyboardMarkup()
        ink1 = types.InlineKeyboardButton('Тинькофф⭐', callback_data='tinkoff')
        inli.row(ink1)
        ink2 = types.InlineKeyboardButton('СБП⚡', callback_data='SBP')
        inli.row(ink2)
        bot.send_message(message.chat.id, '💰На ' + str(num_gold) + 'р можно купить ' + str(
            res) + ' голды' '\n📖Нажмите на любой способ оплаты ниже чтобы продолжить', reply_markup=inli)
    except:
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == ('vivodiii'):
        global vivodcol
        vivodir = sqlite3.connect('vivodi.sql')
        vcur = vivodir.cursor()
        rka = vcur.execute('SELECT orid FROM viv')



        vcur.close()
        vivodir.close()

    global p
    if callback.data == ('p'):
        bot.send_sticker(callback.message.chat.id,
                         'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE')
        bot.send_message(admin_id, '💰Текущие запросы на пополнения:')
    global v
    if callback.data == ('v'):
        global vivodcol
        bot.send_sticker(callback.message.chat.id,
                         'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE')
        k = types.InlineKeyboardMarkup()
        if vivodcol == 0:
            bot.send_message(admin_id,'⭐Запросов на выводы в данный момент нет')
        else:

            for i in range(vivodcol):
                ink2 = types.InlineKeyboardButton('Заказ #' + str(vivodcol), callback_data='vivodiii')
                k.row(ink2)
            bot.send_message(admin_id,'💰Текущие запросы на выводы:',reply_markup = k)

    if callback.data == ('minvivod'):
        bot.send_sticker(callback.message.chat.id,'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE')
        bot.send_message(callback.message.chat.id, 'Введите минимальный вывод')
        bot.register_next_step_handler(callback.message,minivivod)
    if callback.data == ('minpopol'):
        bot.send_sticker(callback.message.chat.id,'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE')
        bot.send_message(callback.message.chat.id, 'Введите минимальное пополнение')
        bot.register_next_step_handler(callback.message, minipopol)
    if callback.data == ('cheki'):
        bot.send_message(callback.message.chat.id,'Введите ID пользователя,которому хотите изменить баланс')
        bot.register_next_step_handler(callback.message,izmenbalans)
    if callback.data == ('bazaa'):
        baza = sqlite3.connect('baza.sql')
        cur = baza.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        info = ''
        for p in users:
            info += f'id: {p[0]},username:{p[1]},balans:{p[2]}\n'
        bot.send_message(admin_id,info)
        cur.close()
        baza.close()
    if callback.data == ('cucurs'):
        bot.send_message(callback.message.chat.id,'📉Введите новый курс')
        bot.register_next_step_handler(callback.message, flexik)
    if callback.data == ('soobsh'):
        bot.send_message(callback.message.chat.id,'Введите айди пользователя,которому хотите отправить сообщение,для отмены напишите: 17511111')
        bot.register_next_step_handler(callback.message, soobsh1)
    if callback.data == ('ban'):
        bot.send_message(callback.message.chat.id,
                         'Введите айди пользователя,которого хотите заблокировать,для отмены напишите: 17511111')
        bot.register_next_step_handler(callback.message, banpolz)
    if callback.data == ("rassylka"):
        bot.send_message(callback.message.chat.id,
                         'Введите текст,который вы хотите разослать,для отмены напишите: 17511111')
        bot.register_next_step_handler(callback.message, rassylka)
    if callback.data == ('tinkoff'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        inlip = types.InlineKeyboardMarkup()
        inp2 = types.InlineKeyboardButton('Отправить чек админу и пополнить🧑‍💻', callback_data='checkoplati')
        inlip.row(inp2)
        bot.send_message(callback.message.chat.id, '💰Чтобы купить голду переведите деньги на этот счет:\n\nТинькофф: \nСбер:\n \nЧтобы продолжить отправьте чек в чат', reply_markup=inlip)
        bot.register_next_step_handler(callback.message, vivodi)
    if callback.data == ('SBP'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        inlip = types.InlineKeyboardMarkup()
        inp2 = types.InlineKeyboardButton('Отправить чек админу и вывести🧑‍💻', callback_data='checkoplati')
        inlip.row(inp2)
        bot.send_message(callback.message.chat.id, '💰Чтобы купить голду переведите деньги на этот счет:\n\nТинькофф: \nСбер:\n \nЧтобы продолжить нажмите на кнопку', reply_markup=inlip)
    if callback.data == ('inf'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        infbut1 = types.InlineKeyboardMarkup()
        inf11 = types.InlineKeyboardButton('Наш канал💡', url='https://t.me/StonksGold')
        infbut1.row(inf11)
        inf22 = types.InlineKeyboardButton('Курс📉', callback_data='COURSE')
        inf33 = types.InlineKeyboardButton('Админ🧑‍💻', url = 'https://t.me/BOMONTl')
        infbut1.row(inf22, inf33)
        bot.send_message(callback.message.chat.id, ' 📋 Выберите нужный пункт', reply_markup=infbut1)
    if callback.data == ('COURSE'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        coursebut = types.InlineKeyboardMarkup()
        cbut1 = types.InlineKeyboardButton('Назад↩', callback_data='inf')
        coursebut.row(cbut1)
        bot.send_message(callback.message.chat.id, 'Курс на данный момент : '+ str(flex), reply_markup=coursebut)
    if callback.data == ('Question'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        abs = types.InlineKeyboardMarkup()
        abs1 = types.InlineKeyboardButton('1', callback_data='1')
        abs.row(abs1)
        abs2 = types.InlineKeyboardButton('2', callback_data='2')
        abs3 = types.InlineKeyboardButton('3', callback_data='3')
        abs4 = types.InlineKeyboardButton('4', callback_data='4')
        abs.row(abs2, abs3, abs4)
        bot.send_message(callback.message.chat.id,
                         "1. Почему так долго проверяют чек?"  "\n2. Почему так долго выводят голду?"
                         "\n3. Сколько по времени выводят голду?"
                         "\n4. Безопасно ли у вас покупать?", reply_markup=abs)
    if callback.data == ('Question1'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        abs1 = types.InlineKeyboardMarkup()
        abs11 = types.InlineKeyboardButton('1', callback_data='1')
        abs1.row(abs11)
        abs22 = types.InlineKeyboardButton('2', callback_data='2')
        abs33 = types.InlineKeyboardButton('3', callback_data='3')
        abs44 = types.InlineKeyboardButton('4', callback_data='4')
        abs1.row(abs22, abs33, abs44)
        bot.send_message(callback.message.chat.id, "\n1. Почему так долго проверяют чек?"
                                                   "\n2. Почему так долго выводят голду?"
                                                   "\n3. Сколько по времени выводят голду?"
                                                   "\n4. Безопасно ли у вас покупать?", reply_markup=abs1)
    if callback.data == ('1'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        vvv = types.InlineKeyboardMarkup()
        vv1 = types.InlineKeyboardButton('Назад↩', callback_data='Question1')
        vv2 = types.InlineKeyboardButton('Связаться🧑‍💻', url = 'https://t.me/BOMONTl')
        vvv.row(vv1, vv2)
        bot.send_message(callback.message.chat.id,
                         'Чеки проверяются в ручную, а не автоматически. Сотрудники не смогут проверить чек, если вы пополнили в позднее время или раннее вечером. До 24 часов занимает проверка чека.',
                         reply_markup=vvv)
    if callback.data == ('2'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        vvc = types.InlineKeyboardMarkup()
        vc1 = types.InlineKeyboardButton('Назад↩', callback_data='Question1')
        vc2 = types.InlineKeyboardButton('Связаться🧑‍💻', url = 'https://t.me/BOMONTl')
        vvc.row(vc1, vc2)
        bot.send_message(callback.message.chat.id,
                         'Вывод золота занимает до 24 часов. Но мы стараемся как можно быстрее вывести вам золото. Возможно сотрудник взял перерыв или ваш скин трудно найти',
                         reply_markup=vvc)
    if callback.data == ('3'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        vva = types.InlineKeyboardMarkup()
        va1 = types.InlineKeyboardButton('Назад↩', callback_data='Question1')
        va2 = types.InlineKeyboardButton('Связаться🧑‍💻', callback_data='Question1')
        vva.row(va1, va2)
        bot.send_message(callback.message.chat.id,
                         'Вывод золота происходит до 24 часов от запроса на вывод. Но в большинстве вывод происходит от нескольких минут до часа.',
                         reply_markup=vva)
    if callback.data == ('4'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        vvg = types.InlineKeyboardMarkup()
        vg1 = types.InlineKeyboardButton('Назад↩', callback_data='Question1')
        vg2 = types.InlineKeyboardButton('Связаться🧑‍💻', url = 'https://t.me/BOMONTl')
        vvg.row(vg1, vg2)
        bot.send_message(callback.message.chat.id,
                         'Весь товар, который продаётся в боте, получен честным путём. Если вы сомневаетесь в безопасности, то лучше покупать в игре.',
                         reply_markup=vvg)
    if callback.data == ('popol'):
        bot.send_sticker(callback.message.chat.id, 'CAACAgIAAxkBAAELYF1lyM-3NAXjW8-hs28SzZC-KLuAewACTj4AAnMJkEsCp674u5wXtTQE'
                         )
        bot.send_message(callback.message.chat.id,
                         '⭐Назовите количество рублей,на которое вы хотите пополнить аккаунт: ')
        bot.register_next_step_handler(callback.message, bg)

def minipopol(message):
    global minpopol
    try:
        minpopol = int(message.text)
        bot.send_sticker('CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
    except:
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')
def minivivod(message):
    global minvivod
    try:
        minvivod = int(message.text)
        bot.send_sticker('CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
    except:
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')
def vivod(message):
    try:

       a = message.text
       baza = sqlite3.connect('baza.sql')
       cur = baza.cursor()
       ark = cur.execute('SELECT * FROM users WHERE id = %s' % (message.from_user.id))
       for el in ark:
          aboba = str(el[2])
          if not int(aboba) < int(a):

              if int(a) < minvivod:
                  bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
                  bot.send_message(message.chat.id, 'Минимальный вывод от' + str(minvivod) + 'голды(')
              else:
                  bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAELYGRlyNFLMYQBMJvM5t4KbnjoJeg7KAACsz4AAugOkUuKMiCe15hJNTQE')
                  adnin = types.InlineKeyboardMarkup()
                  adnun = types.InlineKeyboardButton('Написать админу🧑‍💻', url = 'https://t.me/BOMONTl')
                  adnin.row(adnun)
                  bot.send_message(message.chat.id, 'Чтобы вывести ' + a + ' голды,напишите администратору этого бота❤️‍🔥',reply_markup=adnin)
          else:
              bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
              adnin = types.InlineKeyboardMarkup()
              adnun = types.InlineKeyboardButton('💰Пополнить', callback_data='popol')
              adnin.row(adnun)
              bot.send_message(message.chat.id, 'Не хватает денег,пополните баланс,чтобы купить голду(',
                             reply_markup=adnin)
       cur.close()
       baza.close()
    except ValueError:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
        adnin = types.InlineKeyboardMarkup()
        adnun = types.InlineKeyboardButton('💰Пополнить', callback_data='popol')
        adnin.row(adnun)
        bot.send_message(message.chat.id, 'Не хватает денег,пополните баланс,чтобы купить голду(',
                         reply_markup=adnin)

    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')





def izmenbalans(message):
    global lolkek
    global ju
    bot.delete_message(message.chat.id,message.message_id)
    lolkek = message.text
    if lolkek in ju:
        bot.send_message(message.chat.id,'Введите число рублей на которое хотите изменить баланс пользователя')
        bot.register_next_step_handler(message,izmenbalans2)
    else:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
        bot.send_message(admin_id, 'Этот человек не пользовался ботом,введите /start')
def izmenbalans2(message):
    try:
        global lolkek
        balik = message.text
        baza = sqlite3.connect('baza.sql')
        cur = baza.cursor()
        rec = cur.execute('SELECT * FROM users WHERE id = %s' % (lolkek))
        for el in rec:
             cur.execute('INSERT OR REPLACE INTO users (balans,id,name) VALUES ("%s" , "%s" , "%s")' % (int(balik),lolkek,el[1]))
        baza.commit()
        cur.close()
        baza.close()
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')
def calculate(message):
    try:
        global flex
        num_usd = message.text
        res = int(int(num_usd) * float(flex))
        bot.send_message(message.chat.id, 'Вам нужно: ' + str(res) + (' рублей'))
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAELYGZlyNFhh2QPum5SUpwyD_DSV5wDoQACcz0AAoDGkEtMYjXeFSAavDQE')
        bot.send_message(message.chat.id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')

def soobsh1(message):
    try:
        global idpolzz
        idpolzz = message.text
        if '17511111' in idpolzz:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(admin_id, 'Отправка сообщения отменена,нажмите /start')
        else:
            if str(idpolzz) in ju:
               bot.delete_message(message.chat.id, message.message_id)
               bot.send_message(admin_id, 'Введите сообщение,которое хотите отправить пользователю')
               bot.register_next_step_handler(message, soobsh2)
            else:

               bot.delete_message(message.chat.id, message.message_id)
               bot.send_message(admin_id, 'Этот человек не пользовался ботом,введите /start')
    except:
        return
def banpolz(message):
    try:
        global a
        a = message.text
        if '17511111' in a:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(admin_id, 'Бан отменен отменена,нажмите /start')
        else:
            if str(a) in ju:
                bot.delete_message(message.chat.id, message.message_id)
                banned_users.add(str(a))
                bot.send_message(admin_id, 'Введите время,на которое хотите забанить пользователя(1 = 1сек)')
                bot.register_next_step_handler(message, bantime)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(admin_id, 'Этот человек не пользовался ботом,введите start')
    except:
        return

def soobsh2(message):
    global idpolzz
    mes = message.text
    bot.send_message(idpolzz,'Сообщение от админа:\n ' + '\n' + str(mes))
    inlip = types.InlineKeyboardMarkup()
    inp2 = types.InlineKeyboardButton('Отправить еще🧑‍💻', callback_data='soobsh')
    inlip.row(inp2)
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
    bot.send_message(admin_id,'Сообщение отправлено!',reply_markup=inlip)

def bantime(message):
    global ban_time
    try:
        bot.delete_message(message.chat.id, message.message_id)
        ban_time = message.text
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
        bot.send_message(admin_id, 'Туда его!Пользователь забанен на ' + str(ban_time) + ' секунд')
        bot.send_message(a,'🛑Вы были забанены на ' +str(ban_time) + ' секунд,команды будут не доступны')
    except:
        bot.send_message(admin_id, 'Ошибочка,это не число!Нажмите на кнопку меню или /start для продолжения)')


def rassylka(message):
    a = message.text
    if '17511111' in a:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(admin_id, 'Рассылка отменена,нажмите /start')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
        bot.delete_message(message.chat.id, message.message_id)
        for user in ju:
            bot.send_message(user, str(a))
def flexik(message):
    a = message.text
    global flex
    flex = a
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELYGxlyNQbfmCwhSyiojxqssOPcrz-5AACYD4AAhS3kEuAf-hSXTF99DQE')
bot.message_handler(content_types=['photo','text'])
def vivodi(message):
    global vivodcol
    p = message.photo[-1].file_id
    vivodcol += 1
    vivodir = sqlite3.connect('vivodi.sql')
    vcur = vivodir.cursor()
    vcur.execute('INSERT INTO viv (id,cheki,orid) VALUES ("%s" , "%s","%s")' % (message.from_user.id , p,vivodcol))
    vcur.close()
    vivodir.close()

    bot.send_photo(admin_id, p)

bot.polling(none_stop=True)