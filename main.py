import telebot
import config
from telebot import types


# инициализация
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык", reply_markup=markup)

# русский язык
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🌐 Список объектов')
        btn2 = types.KeyboardButton('🌎 Показать объекты на карте')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выбран язык: Русский")
        bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=markup)
        
    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык", reply_markup=markup)
        
    elif message.text == '🌐 Список объектов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🤓 Музеи')
        btn2 = types.KeyboardButton('🚀 Космодромы')
        btn3 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '😎 Выберите категорию', reply_markup=markup)
        
    elif message.text == '🤓 Музеи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🤓 Музей космонавтики на ВДНХ')
        btn2 = types.KeyboardButton('🤓 Звёздный городок')
        btn3 = types.KeyboardButton('🤓 Музей истории космонавтики имени К. Э. Циолковского')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn6)
        bot.send_message(message.from_user.id, '😎 Выберите категорию', reply_markup=markup)
        
    elif message.text == '🤓 Музей космонавтики на ВДНХ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад к музеям')
        markup.add(btn1)
        a = open('media/VDNH.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Музей космонавтики на ВДНХ, Москва\n \nНаверное, это самый известный музей в стране. В памяти мгновенно всплывает знакомый образ — маленькая ракета на огромном постаменте, устремлённая ввысь. Это монумент «Покорителям космоса», под которым и спрятался сам музей. Он был открыт в 1981 году к 20-летию первого полёта человека в космос. Музей большой: 8 залов, более 93 000 объектов. В залах выставлены не только космические инструменты и "агрегаты", но и личные вещи людей из космической отрасли. Например, пальто и шляпа главного конструктора Королёва, в которых он провожал Гагарина 12 апреля 1961 года.\n \nТочный адрес: пр-т Мира, 111, Москва', reply_markup=markup)

    elif message.text == '🤓 Звёздный городок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад к музеям')
        markup.add(btn1)
        a = open('media/ZGMOSCOW.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Звёздный городок\n \nЗвёздный городок располагается в 25 км от Москвы, недалеко от Щёлкова. Он был открыт в 1960 году. Тогда попасть на закрытый военный объект можно было только по специальным пропускам. Но даже сейчас, когда Звёздный городок принимает туристические группы, пропускной режим строгий. Чтобы оказаться на территории, необходимо указать не только ФИО, гражданство, но и профессию, место работы и жительства.\n \nВнутри вы увидите реальные аппараты, на которых тренируются космонавты. Например, центрифугу — огромное сооружение с радиусом вращения 18 м, имитирующее условия перегрузок. Чтобы смоделировать состояние невесомости, в Звёздном городке создана гидролаборатория. Это круглый бассейн с водой диаметром 23 м и глубиной 12 м. Помимо космонавтов сюда опускаются водолазы. Их задача — следить за тем, чтобы космонавт не всплыл на поверхность или не утонул. В Звёздном городке, как и в Музее космонавтики на ВДНХ, можно увидеть макет станции «Мир».\n \nТочный адрес: Звездный Городок, Московская обл.', reply_markup=markup)

    elif message.text == '🤓 Музей истории космонавтики имени К. Э. Циолковского':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Назад к музеям')
        markup.add(btn1)
        a = open('media/KALUGA.jpg', 'rb')
        bot.send_photo(message.from_user.id, a, 'Музей истории космонавтики имени К. Э. Циолковского в Калуге\n \nКалугу называют родиной космонавтики. Здесь в 1967 году начал работу первый в мире и крупнейший в России музей космической направленности при непосредственном участии Королёва и Гагарина. В 2021 году было открыто новое здание. И только ради него стоит проехать 180 км от Москвы до Калуги.\n На музей нужно закладывать минимум полдня, а то и целый. Помимо исторического и нового зданий работают планетарий и обсерватория. А ещё уличная экспозиция ракетно-космической техники с ракетой-носителем «Восток», солнечной электростанцией и инсталляцией «Поехали». Это произнесённое во время старта Гагариным слово стало известно во всём мире. Сбоку от музейного комплекса располагается парк имени Циолковского, посередине которого похоронен учёный\n \nТочный адрес: ул. Академика Королева, 2, Калуга, Калужская обл.', reply_markup=markup)

    elif message.text == '🔙 Назад к музеям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🤓 Музей космонавтики на ВДНХ')
        btn2 = types.KeyboardButton('🤓 Звёздный городок')
        btn3 = types.KeyboardButton('🤓 Музей истории космонавтики имени К. Э. Циолковского')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn6)
        bot.send_message(message.from_user.id, '😎 Выберите категорию', reply_markup=markup)

    elif message.text == '🔙 Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🌐 Список объектов')
        btn2 = types.KeyboardButton('🌎 Показать объекты на карте')
        btn3 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=markup)
        
    elif message.text == '🚀 Космодромы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🚀 Байконур')
        btn2 = types.KeyboardButton('🚀 Плесецк')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn6)
        bot.send_message(message.from_user.id, '😎 Выберите категорию', reply_markup=markup)
        
    elif message.text == '🚀 Байконур':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton('🔙 К космодромам')
        markup.add(btn6)
        a = open('media/BR.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Байконур - второй в СССР , а также крупнейший (по площади) в мире действующий космодром, основанный в Советском Союзе (на территории Казахской ССР) 12 февраля 1955 года и введённый в эксплуатацию 15 мая 1957 года.\n \nРасположен на территории Кызылординской области Республики Казахстан между городом Казалинском и посёлком Жосалы, вблизи посёлка Тюратам. Из-за близости к этому посёлку космодром в международных спутниковых справочниках обозначается как «Tyuratam Missile and Space Complex» (TTMTR). Занимает площадь 6717 км².\n \nКосмодром и город Байконур (до 1995 года — город Ленинск) вместе образуют комплекс «Байконур», состоящий из 15 стартовых комплексов девяти типов для запусков ракет-носителей, 4 пусковых установок для испытаний межконтинентальных баллистических ракет, 11 монтажно-испытательных корпусов (МИК) и прочей инфраструктуры.\n \nТочный адрес: Байконур, пр. академика Королева, д. 33.', reply_markup=markup)

    elif message.text == '🚀 Плесецк':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton('🔙 К космодромам')
        markup.add(btn6)
        a = open('media/Plesetsk.jpg', 'rb')
        bot.send_photo(message.from_user.id, a, 'Плесецк - советский и российский космодром, обеспечивающий часть российских космических программ, связанных с оборонными, а также прикладными, научными и коммерческими пусками непилотируемых космических аппаратов. Единственный действующий космодром в Европе и самый северный космодром на планете\n \nТочный адрес: Плесецк, Архангельская область', reply_markup=markup)

    elif message.text == '🔙 К космодромам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🚀 Байконур')
        btn2 = types.KeyboardButton('🚀 Плесецк')
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1, btn2, btn6)
        bot.send_message(message.from_user.id, '😎 Выберите категорию', reply_markup=markup)
        
    elif message.text == '🌎 Показать объекты на карте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn6)
        a = open('media/Map.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Карта доступна по' + ' [ссылке](https://www.google.com/maps/d/u/0/edit?mid=14sdvp1tNcDz_09MgNIcrUyJDo-R2QFk&usp=sharing)', reply_markup=markup, parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть