#!/usr/bin/env python
# coding: utf-8

# ## Importing and creating

# In[1]:


import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# In[2]:


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# In[3]:


bot = telegram.Bot(token='1251587981:AAHtr1P_OitR86lnJUWgtbqy7W7vikqo_1M')
print(bot.get_me())


# In[4]:


updater = Updater(token='1251587981:AAHtr1P_OitR86lnJUWgtbqy7W7vikqo_1M', use_context=True)


# In[5]:


dispatcher = updater.dispatcher


# ## Handlers

# ### Start

# In[6]:


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Длительность обучения составляет около 1 часа ⏰\n\n"
                             "Если во время обучения тебе нужно будет сделать перерыв, "
                             "не переживай, я запомню где ты остановился, и потом мы сможем "
                             "продолжить обучение с этого места 👌")
    keyboard = [['Хочу начать обучение 😎',
                 'Не хочу обучаться 😔',
                 'К началу обучения']]
    markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Выбор за тобой ⬇️',
                             reply_markup=markup)


# In[7]:


start_handler = CommandHandler('start', start)


# In[8]:


dispatcher.add_handler(start_handler)


# ### Begin learning

# In[9]:


def begin_learning(update, context):
    if update.message.text == 'Хочу начать обучение 😎':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Отлично!\n\nМаркетинг-план - это план твоего карьерного роста.\n"
                                 "Каждый раз по мере твоего продвижения по плану компании ты будешь "
                                 "получать все большее и большее вознаграждение.\nВот как раз это мы "
                                 "с тобой сегодня и изучим.")
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} начал обучение")
        keyboard = [['Количество человек в команде 👩‍🦰👨🧑‍🦰'],
                    ['Решение руководства компании 😎'],
                    ['Товарооборот команды 💰'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='А пока ответь на вопрос - что обеспечит рост твоего бизнеса?',
                                 reply_markup=markup)
    
    elif update.message.text == 'Не хочу обучаться 😔':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Заглянул из любопытства?")
        keyboard = [['Хочу начать обучение 😎',
                     'К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Тебя ждет много всего увлекательного! Давай обучаться',
                                 reply_markup=markup)
    
    else:
        start(update, context)


# In[10]:


begin_learning_handler = MessageHandler(Filters.text(['Хочу начать обучение 😎',
                                                      'Не хочу обучаться 😔',
                                                      'К началу обучения']), 
                                        begin_learning)


# In[11]:


dispatcher.add_handler(begin_learning_handler)


# ### Business growth

# In[12]:


def business_growth(update, context):
    if update.message.text == 'Количество человек в команде 👩‍🦰👨🧑‍🦰':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Отчасти ты прав. Но нужно уточнение.\n\nДавай представим такую ситуацию: "
                                 "завтра мы найдем с тобой 100 человек и зарегистрируем их в наш бизнес.\n\n"
                                 "Компания нам заплатит за перепись населения? Конечно же нет. Поэтому давай "
                                 "оставим эту работу Росстату, который специализируется на этом.\n\nЭто то же "
                                 "самое, если тебе принесут 100 тарелок, но они пустые. Навряд ли ты будешь сыт.")
        keyboard = [['Количество человек в команде 👩‍🦰👨🧑‍🦰'],
                    ['Решение руководства компании 😎'],
                    ['Товарооборот команды 💰'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Давай думать дальше', 
                                 reply_markup=markup)
    
    elif update.message.text == 'Решение руководства компании 😎':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Нет, дорогой друг\n\nОснователи компании тут не при чем. "
                                 "Они дали нам инструмент - маркетинг план, согласно которому мы самостоятельно "
                                 "развиваем свой бизнес, ты сам себе руководитель.\n\nУспешность твоего бизнеса "
                                 "зависит только от тебя и слаженности работы твоей команды.")
        keyboard = [['Количество человек в команде 👩‍🦰👨🧑‍🦰'],
                    ['Решение руководства компании 😎'],
                    ['Товарооборот команды 💰'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Давай думать дальше', 
                                 reply_markup=markup)
    
    elif update.message.text == 'Товарооборот команды 💰':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Именно, молодец!\n\nКак и любая торговая организация, которая платит своим "
                                 "работникам зарплату за товарооборот, компания Орифлейм также платит своим "
                                 "партнерам за организацию товарооборота.\n\nЧем выше товарооборот, тем выше твое "
                                 "звание 😎\n\nЧем выше твое звание, тем выше твой доход 💰")
        keyboard = [['Заниматься продажами 🛍️'],
                    ['Строить партнерско-потребительскую сеть 🕸️'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='А как организовать товарооборот? Выбери один из вариантов ⬇️',
                                 reply_markup=markup)
    
    else:
        begin_learning(update, context)


# In[13]:


business_growth_handler = MessageHandler(Filters.text(['Количество человек в команде 👩‍🦰👨🧑‍🦰',
                                                       'Решение руководства компании 😎',
                                                       'Товарооборот команды 💰',
                                                       'К началу обучения']),
                                         business_growth)


# In[14]:


dispatcher.add_handler(business_growth_handler)


# ### Turnover management

# In[15]:


def turnover_management(update, context):
    if update.message.text == 'Заниматься продажами 🛍️':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Такой вариант, конечно, имеет место быть 👍🏻, однако, продажи – это активный вид "
                                 "дохода, то есть когда работаешь - получаешь доход, а когда не работаешь - не получаешь "
                                 "😦\nВыходит, чтобы зарабатывать на продажах, нужно каждый раз находить новых людей, "
                                 "которые купят у тебя товар.\n\nЕсли тебе нравится рекомендовать продукцию, то это "
                                 "отличный вариант заработка здесь и сейчас, пока развиваешь бизнес 👍🏻, в этом тебе "
                                 "помогут красочные каталоги и сайт компании Орифлейм 😉\n\nНо все же не все люди любят "
                                 "продавать, более интересный вид дохода - пассивный, когда ты один раз поработал "
                                 "как следует 💪 и продолжаешь получать за это вознаграждение всю свою жизнь 😍\n\n"
                                 "P.S. Такой доход можно даже передавать по наследству 👶🏻")
        keyboard = [['Строить партнерско-потребительскую сеть 🕸️'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Хочешь узнать, как этого достичь? 😉 Тогда изучи возможность построения "
                                 "партнерско-потребительской сети 😎😎😎",
                                 reply_markup=markup)
    
    elif update.message.text == 'Строить партнерско-потребительскую сеть 🕸️':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Молодец, верный выбор! 💪\n\nКогда мы занимаемся обычными продажами, мы строим "
                                 "потребительскую сеть, но она крайне нестабильная. Сегодня у нас купили товар – завтра "
                                 "нет.\n\nНамного стабильнее партнерско - потребительская сеть. Мы строим сеть партнеров, "
                                 "которые одновременно выступают и потребителями: ты покупаешь что-то для себя "
                                 "и находишь других людей, которые также с удовольствием покупают продукцию для себя "
                                 "и ищут таких же партнеров-потребителей.\nПостепенно бизнес становится "
                                 "саморазвивающимся. Если цепочка не будет останавливаться, товарооборот будет "
                                 "постоянно расти 😉")
        keyboard = [['Необязательно 😌'],
                    ['Да, самому тоже нужно заказывать 🙋‍♂️'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Как думаешь, а обязательно ли самому что-то заказывать?', 
                                 reply_markup=markup)

    else:
        begin_learning(update, context)


# In[16]:


turnover_management_handler = MessageHandler(Filters.text(['Заниматься продажами 🛍️',
                                                           'Строить партнерско-потребительскую сеть 🕸️',
                                                           'К началу обучения']), 
                                             turnover_management)


# In[17]:


dispatcher.add_handler(turnover_management_handler)


# ### Self_order

# In[18]:


def self_order(update, context):
    if update.message.text == 'Необязательно 😌':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Ты прав, это делать не обязательно. "
                                 "Но давай будем друг с другом честны, ты же моешься и чистишь зубы? 🤔 "
                                 "Зачем тебе ходить в магазин и оставлять там свои деньги, если они тебе "
                                 "за это только скажут: «Спасибо за покупки! Приходите к нам еще»\n\n"
                                 "Не лучше ли теперь всё покупать в своем интернет-магазине? "
                                 "Ведь каждому партнеру с первого дня регистрации компания дает возможность "
                                 "приобретать продукцию со скидкой от 20% до 80%!\n"
                                 "Кроме того, у тебя, как у официального партнера компании, теперь появится "
                                 "возможность получать возврат части средств со своих покупок обратно на счет, "
                                 "и эти деньги можно будет использовать при следующих покупках 😍\n\n"
                                 "Поэтому свой магазин лучше чужих, согласен? 😊")
        keyboard = [['Узнать причину'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Но есть еще одна причина, почему стоит начать делать заказы сразу ⬇️",
                                 reply_markup=markup)
    
    elif update.message.text in ['Да, самому тоже нужно заказывать 🙋‍♂️','Узнать причину']:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Всё очевидно и просто, делай покупки с выгодой для себя. "
                                 "Но главный секрет еще и в том, что люди, которых ты будешь приглашать "
                                 "в бизнес, будут брать пример именно с тебя. И если ты не научишься менять "
                                 "обычный магазин на интернет-магазин Орифлэйм, этого не будут делать и твои "
                                 "партнеры 😞\n\nПоэтому начинать надо всегда и во всем с себя 😎\n"
                                 "Научись менять обычный магазин на интернет-магазин Орифлэйм и этому же научи "
                                 "других своих партнеров. Тогда товарооборот в твоей команде будет с каждым "
                                 "разом только возрастать 👏🏻")
        keyboard = [['Конечно, расскажи! 😍'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Хочешь узнать где искать людей? 🤓', 
                                 reply_markup=markup)
    
    else:
        begin_learning(update, context)


# In[19]:


self_order_handler = MessageHandler(Filters.text(['Необязательно 😌',
                                                  'Да, самому тоже нужно заказывать 🙋‍♂️',
                                                  'Узнать причину',
                                                  'К началу обучения']),
                                    self_order)


# In[20]:


dispatcher.add_handler(self_order_handler)


# ### Find_people

# In[21]:


def find_people(update, context):
    if update.message.text == 'Конечно, расскажи! 😍':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Везде! У нас регулярно проходят вебинары на тему поиска людей. "
                                 "Обучайся, выбирай подходящий для тебя метод и стартуй 💪🏻\n\n"
                                 "🌐 Интернет даёт широчайшие возможности для поиска и территориально "
                                 "ограничиваться не стоит. Наверняка ты уже слышал, что компания Орифлэйм "
                                 "развивается не только в России, но и в других странах мира.\n\n")
        keyboard = [['Что за валюта? 🧐'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Но как компании сделать так, чтобы каждый из нас, в какой бы стране мы "
                                 "не находились, понимал какой товарооборот ему и его команде нужно "
                                 "организовать, чтобы достигнуть нового звания и выйти на хороший доход? 👀\n\n"
                                 "Ответ найден, нужна единая валюта ⬇️",
                                 reply_markup=markup)

    else:
        begin_learning(update, context)


# In[22]:


find_people_handler = MessageHandler(Filters.text(['Конечно, расскажи! 😍',
                                                   'К началу обучения']),
                                     find_people)


# In[23]:


dispatcher.add_handler(find_people_handler)


# ### Single_currency

# In[24]:


def single_currency(update, context):
    if update.message.text == 'Что за валюта? 🧐':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Компания Орифлэйм ввела такую условную единицу, как бонусный балл (ББ).\n\n"
                                 "Каждый товар имеет определенное количество ББ. У всех товаров разные ББ."
                                 "Именно поэтому, когда ты делаешь заказ, за него тебе присваивается определенное "
                                 "количество баллов ✅\n\n"
                                 """____________________
Например:
Мыло – 2 ББ
Шампунь – 9 ББ
Тушь – 4 ББ
ИТОГО твой заказ составил – 15 ББ
____________________\n\n"""
                                 "Делая заказ, ты организуешь личный товарооборот. Но купить себе – это пол "
                                 "дела. Нужно научиться организовывать общий товарооборот.")
        keyboard = [['Конечно хочу! 🤗'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Хочешь узнать как это сделать? 😎",
                                 reply_markup=markup)

    else:
        begin_learning(update, context)


# In[25]:


single_currency_handler = MessageHandler(Filters.text(['Что за валюта? 🧐',
                                                   'К началу обучения']),
                                     single_currency)


# In[26]:


dispatcher.add_handler(single_currency_handler)


# ### Common_turnover

# In[27]:


def common_turnover(update, context):
    if update.message.text == 'Конечно хочу! 🤗':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Здесь начинается самое интересное. В отличии от других проектов, в нашем "
                                 "мы регистрируем одного человека под другого, независимо от того, кто кого "
                                 "пригласил ☝️.\nЭто позволяет каждому новому партнеру, который только "
                                 "присоединился и начал обучаться, уже видеть рост товарооборота в своей команде. "
                                 "В результате, к моменту когда закончится обучение, он уже будет начинать бизнес "
                                 "не с нуля, у него уже будет создан какой-то товарооборот в команде.\n\n"
                                 "____________________\n"
                                 "Давай рассмотрим пример.\n"
                                 "Ты пришел к нам в проект и сделал свой заказ, например, на 50 ББ.\n"
                                 "После тебя пришел Вася и сделал заказ на 30 ББ.\n"
                                 "После Васи пришла Катя и сделала заказ на 80 ББ.\n"
                                 "А потом пришла Оля и сделала заказ на 60 ББ.\n"
                                 "____________________\n"
                                 "Все эти люди (Вася, Катя, Оля) пришли после тебя, а значит – это твоя "
                                 "персональная группа (команда). Их покупки засчитываются тебе в общий товарооборот.")
        link_1 = 'AgACAgIAAxkBAANjXrbdzMIR8p0lBe32jPK5uhFIAAH5AAJ3qTEbJZCZStu0P2kQv-M0srS3DgAEAQADAgADcwAD27AFAAEZBA'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Причем, надо понимать, что будут приходить разные люди:\n"
                                 "👉🏻 обычные покупатели 👩🏻 👛 (им бизнес не нужен вообще, но покупать со скидкой "
                                 "они хотят);\n👉🏻 партнеры 😎 которые, как и ты, тоже хотят зарабатывать, а значит, "
                                 "тоже будут заниматься поиском людей.\n\n"
                                 "Соответственно, к тебе обязательно будут приходить люди, которых ты будешь "
                                 "обучать сути бизнеса и они будут делать заказы для себя. Остальные будут "
                                 "просто потребителями. Но те, кто придет на бизнес, тоже начнут приглашать "
                                 "людей и обучать их тому же.\n\n"
                                 "Теперь над развитием общего бизнеса ты уже будешь работать не один. "
                                 "А, значит, процесс пойдет быстрее 😃")
        link_2 = 'AgACAgIAAxkBAANoXrbmDIQWOlV3Ps3j_4HVCuneKDgAAiupMRs435hKOOubwd1tbPZFsrcOAAQBAAMCAANzAAOPtgUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Команда активных партнеров будет постепенно разрастаться.\n"
                                 "Будет расти и общий товарооборот твоей персональной группы (обычные "
                                 "покупатели + партнеры-потребители).\n"
                                 "В нашем примере он условно составил 220 ББ.\n")
           
        keyboard = [['Идем дальше 💪'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Давай разбираться дальше. Для чего же нам знать общее количество "
                                 "ББ нашей группы? ⬇️",
                                 reply_markup=markup)

    else:
        single_currency(update, context)


# In[28]:


common_turnover_handler = MessageHandler(Filters.text(['Конечно хочу! 🤗',
                                                   'К началу обучения']),
                                         common_turnover)


# In[29]:


dispatcher.add_handler(common_turnover_handler)


# ### Total_bonus_rate

# In[30]:


def total_bonus_rate(update, context):
    if update.message.text == 'Идем дальше 💪':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Знание общего количества ББ в твоей персональной группе позволит "
                                 "тебе планировать свой рост по карьерной лестнице. Для этого ты должен "
                                 "понимать какой нужно организовать товарооборот в команде, чтобы закрыть "
                                 "новое звание.")
        keyboard = [['Что такое маркетинг-план? 🤷‍♀️'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Компания позаботилась о том, чтобы у каждого из нас было четкое видение "
                                 "бизнеса, и разработала маркетинг-план ⬇️",
                                 reply_markup=markup)

    else:
        single_currency(update, context)


# In[31]:


total_bonus_rate_handler = MessageHandler(Filters.text(['Идем дальше 💪',
                                                   'К началу обучения']),
                                         total_bonus_rate)


# In[32]:


dispatcher.add_handler(total_bonus_rate_handler)


# ### Marketing_plan

# In[33]:


def marketing_plan(update, context):
    if update.message.text == 'Что такое маркетинг-план? 🤷‍♀️':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="На следующей картинке представлен план твоего роста до первого значимого "
                                 "звания \"Директор\". Это и есть твой маркетинг-план.\nЗвание растет по мере роста "
                                 "товарооборота в твоей команде.\n\n Директор - это:\n"
                                 "💎 общий товарооборот 7 500 ББ\n"
                                 "💎 доход на уровне 30 000 руб. каждые 3 недели.\n"
                                 "💎 единоразовая премия 1000 $\n"
                                 "💎 участие в \"Автомобильной программе\" - получаешь брендированный "
                                 "автомобиль или забираешь деньгами\n\n"
                                 "По мере роста товарооборота в твоей команде, будет расти твои звание и доход. "
                                 "Обрати внимание, чем выше объем ББ в команде, тем выше твое звание.")
        link_1 = 'AgACAgIAAxkBAANqXrrnr-b34EDPEwwl7wh-ZxHzEuYAAlSuMRvlkNhJZM9nND84fztCIsEOAAQBAAMCAANtAANW-gUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Для того, чтобы получить первое звание \"Консультант 3%\" общий товароборот "
                                 "в твоей группе(команде) должен достигнуть 150 ББ\n\nДавай вернемся к ранее "
                                 "рассмотренному примеру, к твоей персональной группе (ты, Вася, Катя, Оля) ⬇️")
        link_2 = 'AgACAgIAAxkBAANjXrbdzMIR8p0lBe32jPK5uhFIAAH5AAJ3qTEbJZCZStu0P2kQv-M0srS3DgAEAQADAgADcwAD27AFAAEZBA'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Товарооборот в вашей группе составил 220 ББ - он даже немного превысил 150 ББ. "
                                 "Поздравляю, ты достиг должности \"Консультант 3%\"! 👍\n\nСтавь себе новую цель 🎯 "
                                 "\"Консультант 6%\"\nВ рассмотренном примере, чтобы стать \"Консультантом 6%\" тебе "
                                 " не хватало 230 ББ (450 ББ - 220 ББ = 230 ББ).\nДопустим ты и твои партнеры хорошо "
                                 " поработали и нашли еще новых партнеров (Света, Таня, Гоша, Рита), товарооборот "
                                 "твоей персональной группы составил 450 ББ. Поздравляю, ты достиг уровня "
                                 "\"Консультант 6%\"! И это только начало! 😎\n\nСледующая ступень уже "
                                 "\"Менеджер 9%\" 💪\nТоварооборот группы \"Менеджера 9%\" - 900 ББ. Как мы помним, "
                                 "у вас в группе он уже достиг 450 ББ.")
        keyboard = [['Продать продукции на 450 ББ 🛍️'],
                    ['Найти еще партнеров 🙋'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Что думаешь делать?",
                                 reply_markup=markup)

    else:
        single_currency(update, context)


# In[34]:


marketing_plan_handler = MessageHandler(Filters.text(['Что такое маркетинг-план? 🤷‍♀️',
                                                   'К началу обучения']),
                                         marketing_plan)


# In[35]:


dispatcher.add_handler(marketing_plan_handler)


# ### Manager_reach

# In[36]:


def manager_reach(update, context):
    if update.message.text == 'Продать продукции на 450 ББ 🛍️':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Как вариант! Почему бы и нет?!\nНо плохо только одно, что в следующий "
                                 "отчетный период снова придется продавать продукцию на это же количество ББ, "
                                 "чтобы поддержать свой уровень. Потом - снова 🙄\n\nНе сильно ли это хлопотно, "
                                 "мой друг? Да и завтра могут сложиться обстоятельства, что мы не сможем уделить "
                                 "продажам нужного количества времени, например, заболеем. И что, наш бизнес "
                                 "встанет в ступор? 😱")
        keyboard = [['Найти еще партнеров 🙋'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="А не проще ли найти партнеров, которые сами себе что-то "
                                 "купят? В этом случае не придется беспокоиться о сохранении товарооборота на "
                                 "нужном уровне. Интернесно, правда? Давай лучше рассмотрим этот вариант 🤝⬇️",
                                 reply_markup=markup)
    elif update.message.text == 'Найти еще партнеров 🙋':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Все верно!\n\nБизнес растет только тогда, когда в него приходят новые люди.\n"
                                 "Осталось понять, сколько примерно людей нужно пригласить, чтобы ты вышел на "
                                 "новый уровень \"Менеджер 9%\".\n\nЧто мы имеем сейчас:\nТоварооборот твоей "
                                 "персональной группы = 450 ББ.\nВ твоей команде уже 8 человек (Вася, Оля, Катя, "
                                 "Света, Таня, Гоша, Рита и ты).\nCредний заказ в твоей команде составляет: "
                                 "450 / 8 = 50-60 ББ\n\nДо уровня \"Менеджер 9%\" (900 ББ) тебе не хватает 450 ББ. "
                                 "Значит, чтобы прирасти еще на 450 ББ, тебе нужно пригласить в команду "
                                 "дополнительно еще 8-9 чел. (450 ББ / 50-60 ББ) 🤓")
        keyboard = [['Как же это сделать? 👀'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Да, на это может уйти некоторое время. Но у меня для тебя отличная "
                                 "новость\nЭТОТ ПРОЦЕСС МОЖНО УСКОРИТЬ 😊",
                                 reply_markup=markup)

    else:
        single_currency(update, context)


# In[37]:


manager_reach_handler = MessageHandler(Filters.text(['Продать продукции на 450 ББ 🛍️',
                                                     'Найти еще партнеров 🙋',
                                                     'К началу обучения']),
                                         manager_reach)


# In[38]:


dispatcher.add_handler(manager_reach_handler)


# ### Starting_program

# In[39]:


def starting_program(update, context):
    if update.message.text == 'Как же это сделать? 👀':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Компания даёт замечательную возможность новым консультантам попробовать "
                                 "топовые продукты по льготной цене. Это стартовая программа и она действует "
                                 "ТОЛЬКО ДЛЯ НОВЫХ ПАРТНЁРОВ!\n\nВ каждой стране условия программы немного "
                                 "отличаются, поэтому подробно о них тебе расскажет твой наставник. Не стесняйся, "
                                 "задавай ему много вопросов! Наставник заинтересован, чтобы ты получил максимум "
                                 "выгоды, и научит как это сделать без личных затрат! ☝️\n\n"
                                 "А сейчас почитай условия стартовой программы в России!\nЭто дополнительные "
                                 "бонусы и выгоды, которые ты можешь получить сразу, но все зависит от твоего "
                                 "желания! 😉")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Каждый новый зарегестрированный Консультант Орифлейм может стать участником "
                                 "Стартовой программы и получать наборы лучших продуктов по выгодной цене.\n\n"
                                 "✨ Шаг 1\nРазмести суммарный заказ на 100 ББ и более в каталоге, следующем "
                                 "после каталога регистрации, и получи один из премиальных ароматов Орифлейм всего "
                                 "за 199 рублей.")
        link_1 = 'AgACAgIAAxkBAANrXrxGDKfrVwIn4yErFx-DvSodtxsAAoGvMRuJ6OFJJMyNjmx9_lqFJ3eRLgADAQADAgADbQADLDgDAAEZBA'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="✨ Шаг 2\nРазмести суммарный заказ на 100 ББ и более в каталоге, "
                                 "следующем после каталога, в котором выполнен Шаг 1, и получи набор продуктов "
                                 "декоративной косметики из серии Giordani Gold: Губная помада «Икона стиля» "
                                 "(Оттенок «классический розовый»), Антивозрастная тональная основа (Оттенок "
                                 "«слоновая кость») и Универсальная супертушь для ресниц всего за 199 рублей.")
        link_2 = 'AgACAgIAAxkBAANsXrxIaGjF0zE1kCnssGpr8dbHI2oAAp2tMRuZAVBI3IPoGKaPRtNXxcIPAAQBAAMCAANtAAOSgAUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="✨ Шаг 3\nРазмести суммарный заказ на 100 ББ и более в каталоге, "
                                 "следующем после каталога, в котором выполнен Шаг 2, и получи набор продуктов "
                                 "для ухода серии NovAge: Ночная маска для интенсивного восстановления кожи и "
                                 "Увлажняющая эссенция для лица всего за 199 рублей.")
        link_3 = 'AgACAgIAAxkBAANtXrxJEp4SFkbg5ppi0w_SjC0DwpcAAp6tMRuZAVBIEwfSGWrbGwJEwcIPAAQBAAMCAANtAANyhQUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_3)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="✨ Шаг 4\nРазмести суммарный заказ на 100 ББ и более в каталоге, следующем "
                                 "после каталога, в котором выполнен Шаг 3, и получи набор продуктов серии "
                                 "Wellness: Комплекс «Омега-3» и Сухая смесь для коктейля «Нэчурал Баланс» "
                                 "(Клубничный вкус) всего за 199 рублей.")
        link_4 = 'AgACAgIAAxkBAANuXrxJnDWb4vi95_orQW8gXo4xzcwAAp-tMRuZAVBIJ8Vf48yd97n9AAFRkS4AAwEAAwIAA20AA98HAgABGQQ'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_4)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Подарочки - это всегда приятно 🎁\nПройдя все 4 шага Стартовой программы, "
                                 "ты сможешь собрать подарки общей стоимостью более 7 000 руб.\n\n"
                                 "Поэтому каждый из наших партнёров, кто приходит именно в бизнес, "
                                 "с удовольствием проходит Стартовую программу.\n\n"
                                 "Собрав все подарки, ты сможешь оставить их себе или сделать приятное своим "
                                 "близким 😊\nТак ты сможешь сформировать у них лояльность к продукции, и они "
                                 "потом будут заказывать именно у тебя, что поможет тебе легко "
                                 "делать ЛТО 😉\n\nПройдя стартовую программу, ты сможешь научить тому же других "
                                 "партнеров, что позволит твоему бизнесу развиваться еще стремительнее 💪🏻")
        keyboard = [['Хорошо, давай разберемся 🙂'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Предлагаю детальнее разобраться, почему правильно начинать бизнес "
                                 "именно со стартовой программы ⬇️",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[40]:


starting_program_handler = MessageHandler(Filters.text(['Как же это сделать? 👀',
                                                        'К началу обучения']),
                                         starting_program)


# In[41]:


dispatcher.add_handler(starting_program_handler)


# ### Starting_program_continued

# In[42]:


def starting_program_continued(update, context):
    if update.message.text == 'Хорошо, давай разберемся 🙂':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Всё просто! Когда человек приходит в новый для себя бизнес, он берет "
                                 "пример с другого, как дети с родителей. Соответственно, если ты будешь "
                                 "проходить стартовую программу, то это будут делать и твои партнеры 👍🏻\n\n"
                                 "В итоге, пока ты и твои партнёры будут проходить стартовую программу, "
                                 "общий товарооборот твоей персональной группы успеет дорасти до 1800 ББ, "
                                 "а это уже уровень \"Менеджер 12%\", на котором ты начнешь получать доход, "
                                 "превышающий твои расходы на заказы.\n\nСовсем скоро твой бизнес уйдет в плюс. 😉")
        keyboard = [['Конечно, иначе зачем я здесь! 🤗'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Потом начнется самое интересное 🤗\nХочешь узнать, как будут начисляться "
                                 "деньги за твою работу?",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[43]:


starting_program_continued_handler = MessageHandler(Filters.text(['Хорошо, давай разберемся 🙂',
                                                        'К началу обучения']),
                                         starting_program_continued)


# In[44]:


dispatcher.add_handler(starting_program_continued_handler)


# ### Money_accrual

# In[45]:


def money_accrual(update, context):
    if update.message.text == 'Конечно, иначе зачем я здесь! 🤗':
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} прошел пол пути 💪")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Для того, чтобы понимать, как начисляются деньги, давай условно "
                                 "установим, что:\n▫️ Цена для партнеров: 1 ББ = 40 руб\n▫️ Цена из каталога "
                                 "для обычных покупателей: 1 ББ = 50 руб.\n\nКомпания начинает начислять деньги "
                                 "с объёма ЛТО = 150 ББ.\n\nВ этом случае ты помимо подарков по Стартовой "
                                 "программе автоматом получишь следующие привилегии:\n🔅 20% скидка на все "
                                 "продукты;\n🔅 10% бонус со своих покупок обратно на свой счет;\n🔅 доступ к "
                                 "специальным предложениям каталога «Премьер-Клуб» (скидки от 20 до 80%);\n"
                                 "🔅 набор из 5 каталогов Орифлэйм по льготной цене (для тех, кто любит "
                                 "продавать).\n\nЗаметь, что при ЛТО = 150 ББ компания уже возвращает деньги, "
                                 "хоть пока только и с личных покупок. Но плюсы уже очевидны!")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="ПРИМЕР 1:\n\nТы сделал заказ на 150 ББ, получаешь: (150 ББ * 50 руб.) * 10% "
                                 "= 750 руб. обратно на свой счёт.\nЭти деньги сможешь использовать в последующих "
                                 "покупках. Но хочется же больше денег, правда?\n\nТакая возможность "
                                 "открывается, когда объем ЛТО = 150 ББ и выше.\n\n150 ББ – это гарантированный "
                                 "минимум, при котором компания понимает, что ты - ПАРТНЁР и тебе необходимо "
                                 "начислять объемную скидку с твоей команды.\n\nПо результатам каталога, компания "
                                 "выплатит тебе бОльшую из сумм:\n▫️ 10%-ный бонус с твоих покупок;\n▫️ Объемную "
                                 "скидку с покупок твоей группы\n\nОбъемная скидка это возврат части средств (%) "
                                 "с твоих покупок и покупок нижестоящих партнеров, имеющих меньший уровень "
                                 "процента.")

        keyboard = [['Пример 2 ✅'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Легче разобраться на еще одном примере ⬇️",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[46]:


money_accrual_handler = MessageHandler(Filters.text(['Конечно, иначе зачем я здесь! 🤗',
                                                        'К началу обучения']),
                                         money_accrual)


# In[47]:


dispatcher.add_handler(money_accrual_handler)


# ### Example_2

# In[48]:


def example_2(update, context):
    if update.message.text == 'Пример 2 ✅':
        link_1 = 'AgACAgIAAxkBAANvXr2Jv8ITk1D5-uU5Ncac-rpRW-EAAkKtMRu4cfFJ8_8T1P3JTaxRE96TLgADAQADAgADbQADOFsAAhkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Как рассчитать свой доход?\nКак видишь из рисунка - ты и Вася являетесь "
                                 "\"Консультантами 3%\", между вами нет разницы в процентном уровне. "
                                 "В результате, тебе не будет начислен доход с покупок Васи (ты и Вася это твоя "
                                 "персональная группа). Тебе полагаются только бонусы с личного заказа.\n\n"
                                 "Компания сравнивает 2 варианта и выплатит тот, который больше:\n1️⃣ Объемная "
                                 "скидка только с твоего заказа (150 ББ * 40 руб. – НДС)*3% = 147 руб.\n2️⃣ 10% "
                                 "бонус с твоих покупок по цене каталога (150 ББ * 50 руб.) * 10% = 750 руб.\n\n"
                                 "Исходя из этого расчета Компания вернет на твой счет консультанта 750 руб.")

        keyboard = [['Конечно интересно, рассказывай! 😌'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="А что произойдет, если у тебя будет процентный отрыв от "
                                 "нижестоящих партнеров? Интересно узнать?",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[49]:


example_2_handler = MessageHandler(Filters.text(['Пример 2 ✅',
                                                 'К началу обучения']),
                                   example_2)


# In[50]:


dispatcher.add_handler(example_2_handler)


# ### Example_3

# In[51]:


def example_3(update, context):
    if update.message.text == 'Конечно интересно, рассказывай! 😌':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Тогда давай рассмотрим Пример 3")
        link_1 = 'AgACAgIAAxkBAANwXr2OHBxaavRJ9P_TxlKiSB6C88EAAkWtMRu4cfFJA6GWQu-0zBnLQsKSLgADAQADAgADbQAD__wBAAEZBA'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Как видишь, между тобой и членами твоей группы появился процентный отрыв. "
                                 "Твой уровень \"Консультант 6%\" выше уровня твоих нижестоящих партнеров "
                                 "\"Консультант 3%\". В результате, тебе будет начислен процентный доход со всех "
                                 "покупок твоей группы (твои, Васины и Катины):\n1️⃣  С личного заказа - "
                                 "(150 ББ * 40 руб. – НДС)*6% = 295 руб.\n2️⃣ С покупок партнеров - "
                                 "(300 ББ * 40 руб. – НДС)*(6% - 3%) = 295 руб.\nИтого: 590 руб\n\n"
                                 "✳️ или 10% бонус с твоих покупок по цене каталога (150 ББ * 50 руб.) * "
                                 "10% = 750 руб.\n\nКак ты уже догадался, хоть твой доход от работы команды "
                                 "вырос, но он еще меньше, твоего 10%-ного бонуса. Исходя из этого расчета "
                                 "Компания опять вернет на твой счет консультанта 750 руб. 🤷‍♀️")

        keyboard = [['Ну давай 🙂'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="А давай, наконец, рассмотрим пример, где твой доход будет зависеть от "
                                 "роста команды, а не от твоего личного заказа 😅",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[52]:


example_3_handler = MessageHandler(Filters.text(['Конечно интересно, рассказывай! 😌',
                                                 'К началу обучения']),
                                   example_3)


# In[53]:


dispatcher.add_handler(example_3_handler)


# ### Example_4

# In[54]:


def example_4(update, context):
    if update.message.text == 'Ну давай 🙂':
        link_1 = 'AgACAgIAAxkBAANxXr2S-i5A2qLejMg9s2oVn5Bm2vYAAkitMRu4cfFJ7DBLpnGazBCKDMEOAAQBAAMCAANtAAOMFAYAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Как видишь, твой уровень вырос до \"Менеджера 9%\" и он выше уровня "
                                 "твоих нижестоящих партнеров.\nЗначит тебе будет начислен доход с покупок группы:\n"
                                 "1️⃣ С личного заказа - (150 ББ * 40 руб. – НДС)*9% = 443 руб.\n"
                                 "2️⃣ С покупок партнеров - ((300+300+150)ББ * 40 руб. – НДС)*(9% - 3%) = 1476 руб.\n"
                                 "Итого: 443+1476=1919 руб.\n\n✳️ или 10%-ный бонус с твоих покупок по цене каталога "
                                 "(150 ББ * 50 руб.) * 10% = 750 руб.\n\nТы уже догадался сколько начислят на "
                                 "твой счет?\nИсходя из этого расчета Компания вернет на твой счет консультанта "
                                 "1919 руб.")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Итак, давай еще раз перечислим два главных принципа получения дохода со "
                                 "своих нижестоящих партнеров:\n👍🏻 личный заказ не мене чем на 150 ББ\n"
                                 "👍🏻 процентный отрыв или разница в званиях между тобой и нижестоящими "
                                 "партнерами.\n\nИ это только начало 😉\n\nЧем выше будет твое звание, тем бОльший доход ты будешь получать 💰")
        keyboard = [['Хочу, рассказывай скорее! 🤗'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Хочешь знать, как увеличить процентный отрыв от нижестоящих "
                                 "партнеров и повысить свой доход? ⬇️",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[55]:


example_4_handler = MessageHandler(Filters.text(['Ну давай 🙂',
                                                 'К началу обучения']),
                                   example_4)


# In[56]:


dispatcher.add_handler(example_4_handler)


# ### Percent_gap

# In[57]:


def percent_gap(update, context):
    if update.message.text == 'Хочу, рассказывай скорее! 🤗':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Для того, чтобы процентный отрыв был всегда, мы разработали "
                                 "специальную систему роста персональной группы ⬇️")
        link_1 = 'AgACAgIAAxkBAANyXr6inenUjuRsmco0O684rNOV9EMAAoupMRsh_NhLYv8p-x7JYVS7AAH1DgAEAQADAgADcwADk6ABAAEZBA'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Нужно последовательно развивать каждую команду:\n\n"
                                 "👉🏻 проведи 10 регистраций людей в первую команду;\n"
                                 "👉🏻 открывай вторую команду и регистрируй по очереди - 2 чел. во вторую команду,"
                                 "1 чел. в первую команду и т.д;\n👉🏻 продолжай до тех пор, пока не найдешь 2 "
                                 "ключевых партнеров в первой команде;\n👉🏻 открывай третью команду и регистрируй "
                                 "опять по очереди - 2 чел. в третью команду, 1 чел. во вторую команду и т.д;\n"
                                 "👉🏻  продолжай до тех пор, пока не найдешь по 2 ключевых партнера во вторую и "
                                 "третью команды.\n\nКогда ты будешь параллельно развивать несколько команд, твой "
                                 "процентный уровень (звание) всегда будет превышать процентный уровень (звание) "
                                 "твоих нижестоящих партнеров.\n\nА, значит, процентный отрыв будет постоянным "
                                 "и объемная скидка будет начисляться с покупок всех нижестоящих партнеров.\n\n"
                                 "Конечно, при условии, что у тебя ЛТО будет не менее 150 ББ. 😉")
        keyboard = [['Пример 5 ✅'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Чтобы закрепить материал, давай рассмотрим еще один пример ⬇️",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[58]:


percent_gap_handler = MessageHandler(Filters.text(['Хочу, рассказывай скорее! 🤗',
                                                 'К началу обучения']),
                                    percent_gap)


# In[59]:


dispatcher.add_handler(percent_gap_handler)


# ### Example_5

# In[60]:


def example_5(update, context):
    if update.message.text == 'Пример 5 ✅':
        link_1 = 'AgACAgIAAxkBAANzXr6nQ3aFd0MTyvwJTGJ6xqV5h_MAAoypMRsh_NhLGkiR2nGIvEvT-fQOAAQBAAMCAANzAAN3oAEAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Допустим, у тебя 3 команды, общий товарооборот этих команд "
                                 "составляет 7500 ББ.\n\nУрааа!!! Ты открыл звание Директора 🎉🎉🎉\n\n"
                                 "Теперь главное не останавливаться, ведь чтобы закрыть звание Директора, "
                                 "нужно подтвердить объем 7500 ББ в любые 8 из 17 последующих каталогов. "
                                 "Это значит, что нужно продолжать рекрутировать, чтобы товарооборот твоей группы "
                                 "постоянно рос 💪\n\nПосле того, как ты убедишься, что в каждой из трех "
                                 "твоих команд есть ключевые партнёры – люди, которые тебя повторяют "
                                 "(обучаются ➡️ делают ЛТО ➡️ приглашают людей), можешь начинать развивать "
                                 "следующие три команды 👌 \n\nЕсли же тебя будет устраивать твой доход, то "
                                 "можешь не развивать новые команды, а просто поддерживать те, которые ты уже "
                                 "создал, помогая своим партнерам.")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Итак, давай еще раз перечислим два главных принципа получения дохода со "
                                 "своих нижестоящих партнеров:\n👍🏻 личный заказ не мене чем на 150 ББ\n"
                                 "👍🏻 процентный отрыв или разница в званиях между тобой и нижестоящими "
                                 "партнерами.\n\nИ это только начало 😉\n\nЧем выше будет твое звание, тем бОльший доход ты будешь получать 💰")
        keyboard = [['Да, хочу зарабатывать больше 🤝'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Но мы же знаем, что аппетит приходит во время еды ☺️\n"
                                 "Скажи, хотел бы ты зарабатывать еще больше?",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[61]:


example_5_handler = MessageHandler(Filters.text(['Пример 5 ✅',
                                                 'К началу обучения']),
                                   example_5)


# In[62]:


dispatcher.add_handler(example_5_handler)


# ### Director_plan

# In[63]:


def director_plan(update, context):
    if update.message.text == 'Да, хочу зарабатывать больше 🤝':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Отлично! Давай посмотрим, как ты сможешь увеличить свой доход.\nНа картинке "
                                 "представлен план твоего роста уже с уровня Директора ⬇️")
        link_1 = 'AgACAgIAAxkBAAN0Xr6vpxAKlgET2qgxbe4G5zs49A0AAo2pMRsh_NhLOzbsYfzgF6zooTkPAAQBAAMCAANzAAOfcAEAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="После того как ты достиг уровня Директора тебе важно научить других своих "
                                 "партнеров сделать то же самое, а именно помочь им стать Директорами 🌟\n\n"
                                 "Как это сделать?\nМы помним, что на протяжении всего времени пока ты шел к "
                                 "званию Директора, ты активно рекрутировал, твоя команда росла и развивалась.\n"
                                 "Под тобой обязательно нашлись партнеры, которые тоже стали активно приглашать "
                                 "других людей 🗣👥\n\nСоответственно, тот общий товарооборот, который "
                                 "организуется под тобой, также является общим товарооборотом и для нижестоящих "
                                 "партнеров. Разница лишь в том, что им не засчитываются покупки партнеров, "
                                 "которые пришли раньше них и находятся выше.\n\nНапример, после тебя пришла Катя. "
                                 "Ты научил ее рекрутировать, и вы вместе развиваете вашу персональную группу и "
                                 "приглашаете людей.")
        link_2 = 'AgACAgIAAxkBAAN1Xr6-b6PNgDRYUlMe4qufby4RohcAAo6pMRsh_NhLKYzBk87ARI8b9LcOAAQBAAMCAANzAAM_igMAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="У Кати та же персональная группа, что и у тебя. Ей засчитываются покупки "
                                 "всех партнеров, которые пришли после нее. Но ей не засчитывается твои покупки, "
                                 "потому что ты пришел раньше.\n\nТакое же правило действуют и для остальных "
                                 "партнеров. Что это означает? 😊\n\nВсе просто! Если ты научил Катю также "
                                 "хорошо строить и развивать свои команды, вскоре после тебя звание Директора "
                                 "откроет и она 👏🏻👏🏻👏🏻")
        link_3 = 'AgACAgIAAxkBAAN2Xr7AP17KHAcSEWEuV-CtsShVLycAAo-pMRsh_NhLYCd4Jcu68CI_9fQOAAQBAAMCAANzAAMjnwEAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_3)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Смотри, ты вырастил первого директора, и тебе присваивается звание "
                                 "Старшего Директора 🎉\n\nСтарший директор:\n💰 твой доход - около 50 000 руб. "
                                 "за 3 недели;\n💰 единоразовая премия 1 500 $;\n\nВскоре у тебя вырастит Директор "
                                 "и во второй команде, а значит, ты откроешь звание Золотого Директора:\n💰 твой "
                                 "доход - около 75 000 руб. за 3 недели;\n💰 единоразовая премия 2 000$\n\n"
                                 "Так ты сможешь выращивать бесконечное количество Директоров, которые будут "
                                 "продолжателями твоего бизнеса. Здесь нет ограничений в росте и доходе, вопрос "
                                 "только в твоих целях и упорстве при их достижении 💪")
        keyboard = [['Ты прав 😍'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Нет ничего приятнее, чем баловать себя всякими покупками и при этом "
                                 "зарабатывать 😉",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[64]:


director_plan_handler = MessageHandler(Filters.text(['Да, хочу зарабатывать больше 🤝',
                                                 'К началу обучения']),
                                   director_plan)


# In[65]:


dispatcher.add_handler(director_plan_handler)


# ### Final_message

# In[66]:


def final_message(update, context):
    if update.message.text == 'Ты прав 😍':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Ну вот и всё 😊\n\nТы успешно прошел моё обучение и покорил "
                                 "маркетинг-план компании Орифлэйм! Теперь ты точно знаешь, что сделать, чтобы "
                                 "быстрее начать получать тот доход, о котором ты мечтаешь 👍🏻\n\nНужно всего "
                                 "лишь обуздать три кита:\n🐳 Регулярно обучаться\n🐳 Делать личные заказы "
                                 "(на 150 ББ)\n🐳 Организовать поток людей и обучать их делать тоже самое")
        keyboard = [['Я готов! 🙋‍♂️'],
                    ['Пожалуй, я пас 🙅'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="В завершение предлагаю пройти контрольный тест. В нем всего 10 вопросов.\n\n"
                                 "Готов показать класс напоследок? 😜\n\nP.S. Если пока не готов, "
                                 "можешь вернуться позже 😊",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[67]:


final_message_handler = MessageHandler(Filters.text(['Ты прав 😍',
                                                 'К началу обучения']),
                                   final_message)


# In[68]:


dispatcher.add_handler(final_message_handler)


# ### Start_test

# In[69]:


def start_test(update, context):
    if update.message.text == 'Я готов! 🙋‍♂️':
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} начал проходить тест 👌")
        keyboard = [['Бесплатный подарочек 🤗'],
                    ['Условная единица стоимости товара 💵']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 1️⃣\nЧто такое бонусный балл (ББ)?",
                                 reply_markup=markup)
    elif update.message.text == 'Пожалуй, я пас 🙅':
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} решил не проходить тест 🤷‍♀️")
        keyboard = [['Я готов! 🙋‍♂️']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Не беда, начнешь как только будешь готов 👌",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[70]:


start_test_handler = MessageHandler(Filters.text(['Я готов! 🙋‍♂️',
                                               'Пожалуй, я пас 🙅',
                                               'К началу обучения']),
                                   start_test)


# In[71]:


dispatcher.add_handler(start_test_handler)


# ### Test_q1

# In[72]:


def test_q1(update, context):
    if update.message.text == 'Бесплатный подарочек 🤗':
        keyboard = [['Бесплатный подарочек 🤗'],
                    ['Условная единица стоимости товара 💵']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Подарочек это хорошо 🙃 но надо подумать еще 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Условная единица стоимости товара 💵':
        keyboard = [['Лагерь труда и отдыха 🏖️'],
                    ['Личный товарооборот 🛍️'],
                    ['Лучший товар Орифлейм 🏆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nБонусный балл – это условная единица "
                                 "стоимости товара в Орифлейм. Когда в следующий раз будешь делать заказ, обрати "
                                 "внимание, что у каждого товара свой бонусный балл 😉")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 2️⃣\nЧто такое ЛТО?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[73]:


test_q1_handler = MessageHandler(Filters.text(['Бесплатный подарочек 🤗',
                                                'Условная единица стоимости товара 💵']),
                                 test_q1)


# In[74]:


dispatcher.add_handler(test_q1_handler)


# ### Test_q2

# In[75]:


def test_q2(update, context):
    if update.message.text == 'Лагерь труда и отдыха 🏖️':
        keyboard = [['Лагерь труда и отдыха 🏖️'],
                    ['Личный товарооборот 🛍️'],
                    ['Лучший товар Орифлейм 🏆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Отличная версия 😂 но мы все пришли сюда строить бизнес, а не отдыхать, "
                                 "поэтому надо подумать еще 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Лучший товар Орифлейм 🏆':
        keyboard = [['Лагерь труда и отдыха 🏖️'],
                    ['Личный товарооборот 🛍️'],
                    ['Лучший товар Орифлейм 🏆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Точно! Тут не поспоришь, у Компании очень много продукции, которая "
                                 "заслуживает наивысшей оценки 🏆 но надо подумать еще 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Личный товарооборот 🛍️':
        keyboard = [['Месяц 😳'],
                    ['3 недели 🤞'],
                    ['Квартал 📆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nЛТО - это личный товарооборот, а именно "
                                 "заказы, которые проходят через твой Личный кабинет.\n\nЗаказы могут быть "
                                 "твои или твоих друзей и близких, главное, чтобы они проходили через твой "
                                 "Личный кабинет ☝️")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 3️⃣\nСколько длится один каталог?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[76]:


test_q2_handler = MessageHandler(Filters.text(['Лагерь труда и отдыха 🏖️',
                                               'Личный товарооборот 🛍️',
                                               'Лучший товар Орифлейм 🏆']),
                                 test_q2)


# In[77]:


dispatcher.add_handler(test_q2_handler)


# ### Test_q3

# In[78]:


def test_q3(update, context):
    if update.message.text == 'Месяц 😳':
        keyboard = [['Месяц 😳'],
                    ['3 недели 🤞'],
                    ['Квартал 📆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Не совсем 🤷‍♂️ Это на обычной работе расчетный период - месяц. "
                                 "Думай дальше 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Квартал 📆':
        keyboard = [['Месяц 😳'],
                    ['3 недели 🤞'],
                    ['Квартал 📆']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Уууу, квартал - это целых три месяца 😳\nЕсли мы будем получать зарплату "
                                 "раз в три месяца, нам будет очень грустно и тяжело. Думаем еще 😉",
                                 reply_markup=markup)
    elif update.message.text == '3 недели 🤞':
        keyboard = [['Обязательно 😎'],
                    ['Нет, можно делать заказ когда захочется 😌']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nКаталог длится 3 недели, а значит, мы имеем "
                                 "возможность получать зарплату каждые три недели, это 17 зарплат в году 😍\n"
                                 "Здорово, правда?")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 4️⃣\nОбязательно ли делать заказ самому каждый каталог?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[79]:


test_q3_handler = MessageHandler(Filters.text(['Месяц 😳',
                                               '3 недели 🤞',
                                               'Квартал 📆']),
                                 test_q3)


# In[80]:


dispatcher.add_handler(test_q3_handler)


# ### Test_q4

# In[81]:


def test_q4(update, context):
    if update.message.text == 'Нет, можно делать заказ когда захочется 😌':
        keyboard = [['Обязательно 😎'],
                    ['Нет, можно делать заказ когда захочется 😌']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Такой вариант, конечно, имеет место быть, но только если ты пришел "
                                 "просто пользоваться продукцией, а не развивать свой бизнес. По другому тебе "
                                 "будет сложно построить стабильную структуру.\n\nПодумай сам, если ты будешь делать "
                                 "заказы время от времени и твои партнеры, глядя на тебя, будут делать то же "
                                 "самое, сможете ли вы планировать свой рост и рассчитывать друг на друга? "
                                 "Конечно же нет 👎🏼\n\nПоэтому думаем дальше 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Обязательно 😎':
        keyboard = [['Твои подписчики в Instagram 🤙'],
                    ['Твоя команда 👩‍💼🙍‍♂️🙎🏻']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nВсегда нужно начинать с себя. Делай заказ "
                                 "каждый каталог и обучай тому же своих партнеров, тогда вам проще будет "
                                 "спланировать свой бизнес, и понять сколько людей нужно еще пригласить в команду, "
                                 "чтобы выйти на новый уровень 🤝")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 5️⃣\nЧто такое Персональная группа?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[82]:


test_q4_handler = MessageHandler(Filters.text(['Обязательно 😎',
                                               'Нет, можно делать заказ когда захочется 😌']),
                                 test_q4)


# In[83]:


dispatcher.add_handler(test_q4_handler)


# ### Test_q5

# In[84]:


def test_q5(update, context):
    if update.message.text == 'Твои подписчики в Instagram 🤙':
        keyboard = [['Твои подписчики в Instagram 🤙'],
                    ['Твоя команда 👩‍💼🙍‍♂️🙎🏻']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Большое количество подписчиков в instagram это конечно же хорошо, ведь "
                                 "они потенциально могут стать твоим будущими партнерами по бизнесу 😎 но это "
                                 "неверный ответ на вопрос, думай еще 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Твоя команда 👩‍💼🙍‍♂️🙎🏻':
        keyboard = [['5 000 ББ 💰'],
                    ['7 500 ББ 💰💰'],
                    ['10 000 ББ 💰💰💰']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nПерсональная группа – это те люди, которые зарегистрированы под тобой, "
                                 "независимо от того, в какой из твоих команд они находятся,"
                                 "и от того, кто из твоих партнеров пригласил их в бизнес.")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 6️⃣\nСколько ББ должно быть в твоей персональной группе, чтобы "
                                 "открыть звание Директора?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[85]:


test_q5_handler = MessageHandler(Filters.text(['Твои подписчики в Instagram 🤙',
                                               'Твоя команда 👩‍💼🙍‍♂️🙎🏻']),
                                 test_q5)


# In[86]:


dispatcher.add_handler(test_q5_handler)


# ### Test_q6

# In[87]:


def test_q6(update, context):
    if update.message.text == '5 000 ББ 💰':
        keyboard = [['5 000 ББ 💰'],
                    ['7 500 ББ 💰💰'],
                    ['10 000 ББ 💰💰💰']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Не совсем 🤷‍♀️\n5 000 ББ - это конечно внушительная сумма, но, к сожалению "
                                 "ее не достаточно, чтобы открыть звание Директора. Нужно больше, думай дальше 😉",
                                 reply_markup=markup)
    elif update.message.text == '10 000 ББ 💰💰💰':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Молодец! Отличный ответ! 💪🏻\n\nЕсли у тебя в персональной группе будет "
                                 "10 000 ББ, то ты мегакрут и гарантированно откроешь звание Директора! Однако, "
                                 "чтобы достичь звание Директора, достаточно будет и 7 500 ББ 😉")
        keyboard = [['Акция для новых партнеров 🎁'],
                    ['Стартовый набор новичка 📦'],
                    ['Программа обучения 🎓']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 7️⃣\nЧто такое Стартовая программа?",
                                 reply_markup=markup)
    elif update.message.text == '7 500 ББ 💰💰':
        keyboard = [['Акция для новых партнеров 🎁'],
                    ['Стартовый набор новичка 📦'],
                    ['Программа обучения 🎓']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nКак только у тебя в Персональной группе "
                                 "будет 7 500 ББ, ты откроешь звание Директора 😎\n\nПричем не важно, сколько "
                                 "команд у тебя будет. Считаться будут ББ со всех команд 😉")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 7️⃣\nЧто такое Стартовая программа?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[88]:


test_q6_handler = MessageHandler(Filters.text(['5 000 ББ 💰',
                                               '7 500 ББ 💰💰',
                                               '10 000 ББ 💰💰💰']),
                                 test_q6)


# In[89]:


dispatcher.add_handler(test_q6_handler)


# ### Test_q7

# In[90]:


def test_q7(update, context):
    if update.message.text == 'Стартовый набор новичка 📦':
        keyboard = [['Акция для новых партнеров 🎁'],
                    ['Стартовый набор новичка 📦'],
                    ['Программа обучения 🎓']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Стартовый набор – это набор пробников, который может приобрести каждый "
                                 "партнер, настроенный заниматься продажами. Но мы говорим о Стартовой программе, "
                                 "думай дальше 😉",
                                 reply_markup=markup)
    elif update.message.text == 'Программа обучения 🎓':
        keyboard = [['Акция для новых партнеров 🎁'],
                    ['Стартовый набор новичка 📦'],
                    ['Программа обучения 🎓']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Да, действительно, обучение на старте – это основной залог успеха в "
                                 "бизнесе.\n\nОднако обучение должно быть не только в начале твоего пути. "
                                 "Обучаться нужно непрерывно - только так можно углубить свои знания и укрепить "
                                 "мотивацию и веру в бизнес ☝️\n\nНо мы так и не разобрались, что же такое "
                                 "Стартовая программа 🙂",
                                 reply_markup=markup)
    elif update.message.text == 'Акция для новых партнеров 🎁':
        keyboard = [['50 ББ 💵'],
                    ['100 ББ 💵'],
                    ['150 ББ 💵']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\nСтартовая программа – это возможность для "
                                 "новых партнеров принять участие в акции и собрать подарки 🎁 общей стоимостью "
                                 "свыше 14 000 руб. 😍\n\nВ акции могут принять участие только новые партнеры и "
                                 "только один раз. Вступить в программу можно в течение 21 дня с момента "
                                 "регистрации в Компании.\n\nПодробности можешь узнать у своего "
                                 "спонсора(наставника) 🤓")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 9️⃣\nПри каком минимальном объеме ЛТО Компания платит объемную скидку с покупок "
                                 "твоей персональной группы (структуры)?",
                                 reply_markup=markup)
    
    else:
        single_currency(update, context)


# In[91]:


test_q7_handler = MessageHandler(Filters.text(['Акция для новых партнеров 🎁',
                                               'Стартовый набор новичка 📦',
                                               'Программа обучения 🎓']),
                                 test_q7)


# In[92]:


dispatcher.add_handler(test_q7_handler)


# ### Test_q8

# In[93]:


def test_q8(update, context):
    if update.message.text == '50 ББ 💵':
        keyboard = [['50 ББ 💵'],
                    ['100 ББ 💵'],
                    ['150 ББ 💵']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Холодно 🥶\nПри таком ЛТО Компания не начислит тебе объемную скидку с "
                                 "покупок твоей персональной группы 🤷‍♂️, думай еще 😉",
                                 reply_markup=markup)
    elif update.message.text == '100 ББ 💵':
        keyboard = [['50 ББ 💵'],
                    ['100 ББ 💵'],
                    ['150 ББ 💵']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Тепло, но не совсем точно 😏\nПри таком ЛТО Компания не начислит тебе "
                                 "объемную скидку с покупок твоей персональной группы 🤷‍♂️, думай еще 😉",
                                 reply_markup=markup)
    elif update.message.text == '150 ББ 💵':
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} прошел тест 💪")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Молодец! Верный ответ! 💪🏻\n\n150 ББ – это тот объем ЛТО, который "
                                 "позволяет Компании видеть в тебе партнера, а значит, каждый каталог тебе "
                                 "будет начисляться процент со всех покупок нижестоящих партнеров 😉")
        markup = telegram.ReplyKeyboardRemove()
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Поздравяю, тест пройден! 🎊🎉🎊\n\nТеперь, надеюсь, тебе стало понятно как "
                                 "строится наш бизнес, а также как правильнее в нем стартовать.\n\nЖелаю тебе "
                                 "успехов! Свяжись со своим наставником, чтобы обсудить дальнейшие действия ☺️",
                                 reply_markup=markup)
    else:
        single_currency(update, context)


# In[94]:


test_q8_handler = MessageHandler(Filters.text(['50 ББ 💵',
                                               '100 ББ 💵',
                                               '150 ББ 💵']),
                                 test_q8)


# In[95]:


dispatcher.add_handler(test_q8_handler)


# ### Start polling

# In[96]:


updater.start_polling()

