#!/usr/bin/env python
# coding: utf-8

# ## Importing and creating

# In[1]:


from Configs import second_token
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# In[2]:


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# In[3]:


bot = telegram.Bot(token=second_token)
print(bot.get_me())


# In[4]:


updater = Updater(token=second_token, use_context=True)


# In[5]:


dispatcher = updater.dispatcher


# ## Handlers

# ### Start

# In[6]:


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Начнем обучение 👩‍🎓\n\n"
                             "За организаторскую работу компания Oriflame выплачивает своим партнерам до 33% с "
                             "товарооборота 💰. Эти выплаты она разделила на несколько видов заработка.")
    keyboard = [['Посмотреть видео 🎥',
                 'К началу обучения']]
    markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Подробнее обо всех видах заработка, доступных в Oriflame, "
                             "ты узнаешь из следующего видео ⬇️",
                             reply_markup=markup)


# In[7]:


start_handler = CommandHandler('start', start)


# In[8]:


restart_handler = MessageHandler(Filters.text(['К началу обучения']),
                                 start)


# In[9]:


dispatcher.add_handler(start_handler)


# In[10]:


dispatcher.add_handler(restart_handler)


# ### First video

# In[11]:


def first_video(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='https://www.youtube.com/watch?v=8W4D2vksaxI&feature', 
                             disable_web_page_preview=False)
    context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} начал смотреть первое видео")
    keyboard = [['Начать тестирование 🤓'],
                ['К началу обучения']]
    markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Чтобы понять как усвоилась информация из видео, давай пройдем небольшой тест.\n'
                             "Если будет сложно, разберемся вместе 😉",
                                 reply_markup=markup)
    
   


# In[12]:


first_video_handler = MessageHandler(Filters.text(['Посмотреть видео 🎥']), 
                                        first_video)


# In[13]:


dispatcher.add_handler(first_video_handler)


# ### Discount_question

# In[14]:


def discount_question(update, context):
    keyboard = [['0% 🤷‍♀️'],
                ['10% 😌'],
                ['20% 😎'],
                ['К началу обучения']]
    markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 1️⃣\n\nКакую скидку получит новый партнер при покупке в онлайн-магазине "
                                 "Oriflame сразу после регистрации?", 
                                 reply_markup=markup)


# In[15]:


discount_question_handler = MessageHandler(Filters.text(['Начать тестирование 🤓']),
                                         discount_question)


# In[16]:


dispatcher.add_handler(discount_question_handler)


# ### Turnover discount

# In[17]:


def turnover_discount(update, context):
    if update.message.text == '0% 🤷‍♀️':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Наша Компания любит своих новых партнеров по бизнесу, поэтому сразу после "
                                 "регистрации предоставляет каждому новому консультанту скидку на любой товар, "
                                 "купленный через свой личный кабинет ☝️")
        keyboard = [['0% 🤷‍♀️'],
                    ['10% 😌'],
                    ['20% 😎'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Попробуй другой вариант ответа 😉",
                                 reply_markup=markup)
    
    elif update.message.text == '10% 😌':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Не угадал, наша Компания более щедрая для своих новых партнеров 😌")
        keyboard = [['0% 🤷‍♀️'],
                    ['10% 😌'],
                    ['20% 😎'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Думай еще 😉', 
                                 reply_markup=markup)

    elif update.message.text == '20% 😎':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Все верно!\n\nПокупай себе и своим близким, и плати на 20% меньше начиная с самого "
                                 "первого заказа!\n\nТакая экономия при покупке средств личной гигиенты позволит "
                                 "среднестатистической семье купить себе новый хороший телевизор на сэкономленные "
                                 "за год деньги 🤓")
        keyboard = [['10% 🙂'],
                    ['15% 😃'],
                    ['22% 🤩'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Вопрос 2️⃣\n\nКакую максимальную объемную скидку от личного товарооборота (ЛТО) "
                                 "может получить партнер компании Oriflame?", 
                                 reply_markup=markup)


# In[18]:


turnover_discount_handler = MessageHandler(Filters.text(['0% 🤷‍♀️',
                                                         '10% 😌',
                                                         '20% 😎']),
                                           turnover_discount)


# In[19]:


dispatcher.add_handler(turnover_discount_handler)


# ### Max turnover discount

# In[20]:


def max_turnover_discount(update, context):
    if update.message.text == '10% 🙂':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Не совсем 🤷‍♀️\n\nТакую скидку Компания начислит своему партнеру, если по "
                                 "итогам каталога он организует личный товарооборот до 900 ББ (около 40 000 руб.)")
        keyboard = [['10% 🙂'],
                    ['15% 😃'],
                    ['22% 🤩'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Попробуй другие варианты 😉",
                                 reply_markup=markup)
    
    elif update.message.text == '15% 😃':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Такую скидку ты сможешь получить дополнительно к основной (20%), если "
                                 "по итогам каталога организуешь личный товарооборот на 3000 ББ "
                                 "(около 120 000 руб.)\n\nНо это не максимально возможная скидка")
        keyboard = [['10% 🙂'],
                    ['15% 😃'],
                    ['22% 🤩'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text='Давай подумаем еще 😉', 
                                 reply_markup=markup)
    
    elif update.message.text == '22% 🤩':
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Абсолютно верно! 🥳\n\n22% - это максимальная объемная скидка, которую "
                                 "Компания выплачивает своему партнеру с суммы его личного товарооборота 🛒\n"
                                 "Условия для ее получения - в течение каталога (3 недели) организовать личный "
                                 "товарооборот на 7500 ББ (около 300 000 руб.)\n\nВ одиночку это могут сделать "
                                 "партнеры, у которых большая семья и широкий круг знакомых, или кто просто любит "
                                 "и хорошо умеет продавать 🛍️\nНо таких людей единицы 🤷‍♀️\n\nОтсюда вытекает "
                                 "следующий вопрос ⬇️")
        keyboard = [['Личные продажи на 300 000 руб. за 3 недели 💪'],
                    ['Построение структуры партнеров-потребителей из знакомых и незнакомых людей 👩‍💼🙎‍♂️🙎🏻'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Какой способ достижения максимальной объемной скидки 22% "
                                 "(7500 ББ, 300 000 руб.) ты выберешь для себя? 👀", 
                                 reply_markup=markup)


# In[21]:


max_turnover_discount_handler = MessageHandler(Filters.text(['10% 🙂',
                                                             '15% 😃',
                                                             '22% 🤩']),
                                               max_turnover_discount)


# In[22]:


dispatcher.add_handler(max_turnover_discount_handler)


# ### Max_discount_methods

# In[23]:


def max_discount_method(update, context):
    if update.message.text == 'Личные продажи на 300 000 руб. за 3 недели 💪':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Поздравляю, ты настоящий счастливчик! ✨\n\nСуперпродавцов, способных "
                                 "построить Директорскую структуру на личных продажах единицы.\n\nЭто "
                                 "замечательный навык, которому ты можешь научить своих партнеров по Бизнесу "
                                 "и если они смогут тебя продублировать, твой рост по карьерной лестнице "
                                 "будет очень стремительным 🚀")
        keyboard = [['Построение структуры партнеров-потребителей из знакомых и незнакомых людей 👩‍💼🙎‍♂️🙎🏻'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Давай также рассмотрим второй вариант достижения максимальной "
                                 "объемной скидки ⬇️",
                                 reply_markup=markup)

    elif update.message.text == 'Построение структуры партнеров-потребителей из знакомых и незнакомых людей 👩‍💼🙎‍♂️🙎🏻':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Здорово 👍\n\nЭто наиболее легкий и доступный способ роста в компании "
                                 "Oriflame\nОдному человек крайне сложно продать столько же, скольк могут купить "
                                 "для себя 100 и даже 1000 партнеров ☝️")
        keyboard = [['Давай 🙂'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Давай на примере разберемся как можно заработать на построении "
                                 "структуры партнеров ⬇️",
                                 reply_markup=markup)


# In[24]:


max_discount_method_handler = MessageHandler(Filters.text(['Личные продажи на 300 000 руб. за 3 недели 💪',
                                                           'Построение структуры партнеров-потребителей из '
                                                           'знакомых и незнакомых людей 👩‍💼🙎‍♂️🙎🏻']),
                                     max_discount_method)


# In[25]:


dispatcher.add_handler(max_discount_method_handler)


# ### Example_1

# In[26]:


def example_1(update, context):
    if update.message.text == 'Давай 🙂':
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Все мы с вами ежедневно умываемся, чистим зубы и принимаем душ 🛀\n\n"
                                 "Представим, что семья в месяц тратит примерно 1000 рублей на средства личной "
                                 "гигиены.\n\nПростой расчет ⬇️\nВ твой интернет-магазин с нашей помощью "
                                 "зарегистрировано 10 партнеров. Эти партнеры, делая покупки на 1000 рублей в "
                                 "месяц, создают товарооборот твоему интернет-магазину на 10 000 рублей, а "
                                 "Oriflame выплачивает тебе процент с этих покупок 💰\n\nЗатем эти партнеры "
                                 "с нашей помощью привели в свой интернет-магазин еще по 10 новых партнеров. "
                                 "В твоем интернет магазине уже 100 новых партнеров + 10 старых + Ты = 111 "
                                 "партнеров, и все, конечно же, моются ☺️\nТоварооборот твоего магазина - 111 "
                                 "партнеров * 1000 руб. = 111 000 рублей, и ты продолжаешь получать с него "
                                 "процент! 🤩\n\nНеплохо, правда? Ничего не продавая, товарооборот твоего "
                                 "магазина раскрутился до 111 000 руб. в месяц, а ты со всего этого получаешь "
                                 "свой процент 💪\n\nВажный момент❗\n\n"
                                 "Ты получаешь свои процент не только от покупок людей, которых зарегистрирует "
                                 "тебе твой Спонсор и ты лично, но и от тех, кого зарегистрируют в дальнейшем твои "
                                 "новички, новички твоих новичков и так в глубину до бесконечности 💰💰💰")
        keyboard = [['Копаем дальше 👌'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="С общей картиной мы познакомились, давай теперь разберемся детальнее 😎",
                                 reply_markup=markup)


# In[27]:


example_1_handler = MessageHandler(Filters.text(['Давай 🙂']),
                                   example_1)


# In[28]:


dispatcher.add_handler(example_1_handler)


# ### Dig_in

# In[29]:


def dig_in(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Раскрутив товарооборот своего магазина до 300 000 руб. за каталог, ты "
                             "достигнешь уровня Директора, а это уже пол пути к получению пассивного дохода - "
                             "дохода, который ты будешь получать независимо от того, продолжаешь ты работать "
                             "или ушел на заслуженный отдых 🏖️\n\nСуществует множество способов достигнуть уровня "
                             "Директор, и ты вправе выбрать тот, который тебе по душе.\n\nУ нас есть партнеры, "
                             "которые работают в расслабленном режиме и не стремятся в трехмесячный срок открыть "
                             "звание Директора. Они готовы потратить на это 8-10 месяцев и работают без четких "
                             "планов и последовательных действий 😌\n\nНо есть мотивированные партнеры, готовые "
                             "максимально быстро достигнуть звания Директор с гарантированным заработком от "
                             "30 000 руб. в месяц 💪")         
    keyboard = [['Посмотреть видео 🎥🎥'],
                ['К началу обучения']]
    markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="В следующем видео подробно описано как за 3 месяца открыть звание Директор.\n\n"
                             "Даже если ты не ставишь себе цель быстро достигнуть результата, и готов потратить "
                             "на это больше времени, обязательно посмотри это видео, чтобы понимать какие "
                             "возможности дает компания Oriflame своим партнерам ✅",
                             reply_markup=markup)


# In[30]:


dig_in_handler = MessageHandler(Filters.text(['Копаем дальше 👌']),
                                dig_in)


# In[31]:


dispatcher.add_handler(dig_in_handler)


# ### Second_video

# In[42]:


def second_video(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="https://youtu.be/_HjZ3C8yB5M",disable_web_page_preview=False)
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} начал смотреть второе видео")
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="А теперь давай освежим в памяти какие уровни дохода доступны для "
                                 "партнеров компании Oriflame 💎💎💎")
        link_1 = 'AgACAgIAAxkBAAO6XtO8lyax-pqMEvZHYOAixj6eWj4AAlSuMRvlkNhJZM9nND84fztCIsEOAAQBAAMCAANtAANW-gUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_1)
        link_2 = 'AgACAgIAAxkBAAO7XtO9FeCtIIFnlcbLHuT5uqkKr70AAg2vMRuVaaBKzsMzULdNthxYTcsOAAQBAAMCAAN4AANF2wUAARkE'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=link_2)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Бизнес План Oriflame признан одним из лучших в мире! ✨\n\n"
                                 "По онлайн продажам, интернет-магазин Oriflame занимает третье место в России. "
                                 "В других странах, показатель тоже очень высокий 👍\nВозможности "
                                 "для карьерного и личностного роста в Oriflame практически безграничны!\n\n"
                                 "Немного статистики 🤓\n22% покупаемой в России декоративной косметики, "
                                 "приобретается именно в Oriflame!\nПарфюмерии - 18%!\nСредств по уходу за "
                                 "лицом - 15%!\nКатегория здорового питания Wellness также стремительно набирает "
                                 "обороты 🚀\n\nНа самом деле, работать с продуктами, которые предлагает "
                                 "шведская компания Oriflame, очень легко, их даже рекламировать не нужно - люди "
                                 "сами с удовольствием их покупают 😍")
        keyboard = [['Три простых, но важных шага 💎'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Давай еще раз повторим три шага, которые тебе необходимо сделать, чтобы "
                                  "твой интернет-магазин начал прнносить стабильных доход 💰⬇️",
                             reply_markup=markup)


# In[33]:


second_video_handler = MessageHandler(Filters.text(['Посмотреть видео 🎥🎥']),
                                      second_video)


# In[34]:


dispatcher.add_handler(second_video_handler)


# ### Three_basic_steps

# In[35]:


def three_basic_steps(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="1️⃣ Сменить привычный магазин на свой личный интернет-магазин "
                                 "Oriflame - раньше мы делали покупки в Летуаль, Ашане и других магазинах, "
                                 "сейчас мы покупаем в своем интернет-магазине Oriflame, "
                                 "где есть товары без которых не обходится ни одна семья.\n\n2️⃣ Пройти "
                                 "обучение и включиться в работу, при этом не сбивая свой привычный график. "
                                 "Эта работа будет занимать столько времени, сколько ты на нее выделишь 👌\n\n"
                                 "3️⃣ Конечно же приглашать новых людей. Как их находить? Все просто! Примерно "
                                 "также, как мы нашли тебя 😉 Как думаешь, твоему Спонсору было сложно тебя "
                                 "найти? Конечно нет, в интернете очень много людей. У нас нет привязки к "
                                 "какому-то определенному месту или городу. Мы можем строить свой бизнес в "
                                 "62 странах мира 🌍\nПосле обучения ты получишь готовую систему развития "
                                 "своего интернет-магазина, тебе просто нужно будет настроить ее под себя и "
                                 "начать применять. И новые идеи мы тоже всегда приветствуем 🤙\n\nИ не забывай, "
                                 "твой наставник и большая дружная команда всегда рядом 🙂 Они готовы помочь "
                                 "тебе в любой непонятной ситуации 💪")
        keyboard = [['Что такое сетевой маркетинг 🤷‍♀️'],
                    ['К началу обучения']]
        markup = telegram.replykeyboardmarkup.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="А еще многих новичков пугает словосочетание \"Сетевой маркетинг\" 👻 давай в "
                                 "заключение чуть подбробнее разберемся что за ним скрывается 🤓 ⬇️",
                             reply_markup=markup)


# In[36]:


three_basic_steps_handler = MessageHandler(Filters.text(['Три простых, но важных шага 💎']),
                                           three_basic_steps)


# In[37]:


dispatcher.add_handler(three_basic_steps_handler)


# ### Multilevel_marketing

# In[38]:


def multilevel_marketing(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="https://youtu.be/NQuwUAfvLT0", disable_web_page_preview=False)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Если во всём разобраться и увидеть перспективы и возможности, "
                                 "то можно понять, что сетевой маркетинг как раз для тех людей, у кого "
                                 "нет богатых родителей, влиятельных покровителей или наследства. Здесь можно "
                                 "расти и развивать свой бизнес с нуля, получать пассивный доход, премии и "
                                 "бонусы от Компании, ездить отдыхать за счёт Компании и реализовать себя "
                                 "целиком и полностью! 🤩")
        markup = telegram.ReplyKeyboardRemove()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Поздравляю, ты прошел второй день вводного обучения 🎉🎊🎉\n\nНадеюсь он "
                                 "помог тебе чуть больше вникнуть в суть нашего бизнеса. Если еще не все понятно, "
                                 "не спеши, дай себе немного времени переварить информацию 👌 и, конечно же, попроси "
                                 "своего Спонсора объяснить поподробнее, он обязательно поможет.\n\nИ помни, глуп "
                                 "тот вопрос, который не был задан, удачи! 😉",
                                 reply_markup=markup)
        context.bot.send_message(chat_id=256137122, 
                                 text=f"@{update.effective_chat['username']} прошел второй день обучения 💪")


# In[39]:


multilevel_marketing_handler = MessageHandler(Filters.text(['Что такое сетевой маркетинг 🤷‍♀️']),
                                              multilevel_marketing)


# In[40]:


dispatcher.add_handler(multilevel_marketing_handler)


# ### Start polling

# In[41]:


updater.start_polling()

