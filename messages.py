# -*- coding: utf-8 -*-
import requests
msg_hello = 'Welcome to Almaty Travel Assistant bot! 🚣 🏕️ 🏞️ \nДобро пожаловать в Almaty Travel Assistant bot 🚣 🏕️ 🏞️'
msg_language = 'Choose language... 🌐 \nВыберите язык... 🌐 '

msg_city = 'Choose city... 🌆'
rmsg_city = 'Выберите город... 🌆'

rmsg_action = 'Выберите действие 🎬'
msg_action = 'Choose action 🎬'

msg_question = 'You can ask me howto questions. \nTry to use keywords.'
rmsg_question = 'Вы можете спросить у меня любой вопрос.\nСтарайтесь исользовать ключевые слова'

#urls
url_emergency = 'http://telegra.ph/Tips-04-25'
url_currency = 'http://telegra.ph/Currency-04-25'
ru_url_emergency = 'http://telegra.ph/Tips-04-25'
ru_url_currency = 'http://telegra.ph/Currency-04-25'

# events
event1 = '⛰️ 🌄 ⛰️ 🌄 ⛰️ 🌄 ⛰️ 🌄 \nThe Charyn Canyon is a natural monument, built of sedimentary rocks, the age of which is about 12 million years.\n\n The height of the sheer mountains of the canyon reaches 150-300 m.\nThe most interesting place for tourists is the Valley of Castles.Many tourists compare this place with the American Grand Canyon.'
event2 = '🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ \nKok Zhailau is one of the most beautiful places on the territory of the Ile-Alatau National Natural Park.\n\n"Kөk Jailau" in translation from the Kazakh language means Green pasture.\n\nThus, the name of the place cannot be better described, in spring and summer on the Kok Zhaylau plateau, the abundance of greenery amazes imagination. This plateau under the peak of Kumbel with a view of Almaty.'
event3 = '🚴‍♀ 🚴‍♂️ ️🚵‍♂️ 🚵‍♀️ \nThe second сritical Mass cycling.\n\nThis time the route of the bike ride is 10 km and will cover such streets and avenues as Al-Farabi, VOAD, Tole bi, Abylai Khan. The participants finish in the territory of the Musical Theater named after G. Musrepov.'
event4 = '👪 👨‍👧 👩‍👧 👨‍👦 \nThe most cozy, sweet festival is "Sweet dreams".\n\n"Sweet Dreams" is a festival for the whole family, for those who like to discover new tastes and emotions.\n\nAt the festival will be presented the sweets of some of the best confectioners of the city: cakes, cakes, eclairs, capkakes, handmade chocolate and this is only a small part.'
event5 = '🏡 👩‍🌾 👨‍🌾 🍓 \nPlaces to run in Almaty. \n\nRunning is a useful lesson that does not require special expenses. All you need is sports shoes and a good place. \n\nLast we are ready to share in todays selection of places for running in the city.'
event6 = '🌸 🌸 🌸 🌸 🌸 🌸\nhere will be event6'

url_event1 = 'http://telegra.ph/AMAZING-CHARYN-KOLSAI-KAINDY-04-26'
url_event2 = 'http://telegra.ph/TREKKING-ON-THE-PLATEAU-KOK-ZHAILAU-18-04-26'
url_event3 = 'http://telegra.ph/3-The-second-sritical-Mass-cycling-04-26'
url_event4 = 'http://telegra.ph/4-Free-Festival-of-Sweets-04-26'
url_event5 = 'http://telegra.ph/5-Places-to-run-in-Almaty-04-27'
url_event6 = 'http://telegra.ph/6-The-Sakura-bloom-festival-on-April-29-at-1400-04-27'

en_events = {1: event1, 2: event2, 3: event3, 4: event4, 5: event5, 6: event6}
en_event_urls = {1: url_event1, 2: url_event2, 3: url_event3, 4: url_event4, 5: url_event5, 6: url_event6}


ru_event1 = '⛰️ 🌄 ⛰️ 🌄 ⛰️ 🌄 ⛰️ 🌄 \nЧарынский каньон - это природный памятник, построенный из осадочных пород, возраст которого составляет около 12 миллионов лет. \n\nВысота скал каньона достигает 150-300 м. Самое интересное место для туристов - Долина замков. Многие туристы сравнивают это место с американским Гранд-Каньоном.'
ru_event2 = '🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ 🏔️ \nКок-Жайляу - одно из красивейших мест на территории национального природного Иле-Алатауского парка. \n\n“Көк-Жайлау” в переводе с казахского языка означает «Зеленое пастбище». И это самое подходящее определение для описания этого места, весной и летом на плато Кок-Жайляу обилие зелени поражает воображение. \nЭто плато под пиком Кумбеля с видом на Алматы. Тропа проходит через берёзы и сосновые рощи, оттуда открывается прекрасный вид на перевал Талгар и ближайшие вершины.'
ru_event3 = '🚴‍♀ 🚴‍♂️ ️🚵‍♂️ 🚵‍♀️ \nВсе желающие жители и гости города по традиции соберутся в 08:30 часов на территории БЦ «Нурлы Тау» и стартуют в 09:00 ч. \n\nВ этот раз маршрут велопробега составляет 10 км и охватит такие улицы и проспекты, как Аль-Фараби, ВОАД, Толе би, Абылай хана. \n\nФинишируют участники на территории ТЮЗа имени Г. Мусрепова.'
ru_event4 = '👪 👨‍👧 👩‍👧 👨‍👦 \n«Sweet Dreams» -это Фестиваль для всей семьи, для тех кто любит открывать для себя новые вкусы и эмоции. \n\nНа фестивале будут представлены- сладости одних из лучших кондитеров города: торты, пирожные, эклеры, капкейки, шоколад ручной работы и это только малая часть.'
ru_event5 = '🏡 👩‍🌾 👨‍🌾 🍓 \nБотанический сад открыт для посещений, а это значит, что пробежки на свежем воздухе станут еще доступнее. \n\nЕсли вы хотите почувствовать единение с природой во время пробежки, то такое место отлично подходит. \nСтоит отметить, что территория сада достаточно большая, поэтому рекомендуется продумать маршрут и внимательно смотреть под ноги. \nПомимо свежего воздуха, в саду можно найти различную живность — белки, фазаны и другие птицы.'
ru_event6 = '🌸 🌸 🌸 🌸 🌸 🌸 \nПраздник цветения Сакуры — ежегодное мероприятие Казахстанско-японского центра развития человеческих ресурсов.\n\nСовершенно Бесплатно вы можете поучаствовать на празднике посвященный цветению настоящей японской Сакуры, где для вас проведут небольшой концерт японской культуры'

ru_url_event1 = 'http://telegra.ph/CHARYN-KOLSAJ-KAIYNDY-04-26'
ru_url_event2 = 'http://telegra.ph/POHOD-K-PLATO-KOK-ZHAJLYAU-04-26'
ru_url_event3 = 'http://telegra.ph/Vtoroj-masssovyj-veloprobeg-04-26'
ru_url_event4 = 'http://telegra.ph/Gorodskoj-festival-sladostej-04-26'
ru_url_event5 = 'http://telegra.ph/Mesta-dlya-bega-v-Almaty-04-26'
ru_url_event6 = 'http://telegra.ph/Prazdnik-cveteniya-Sakury-29-aprelya-v-1400-04-26'

ru_events = {1: ru_event1, 2: ru_event2, 3: ru_event3, 4: ru_event4, 5: ru_event5, 6: ru_event6}
ru_event_urls = {1: ru_url_event1, 2: ru_url_event2, 3: ru_url_event3, 4: ru_url_event4, 5: ru_url_event5, 6:ru_url_event6}


def get_currency(lang):
    data = requests.get("https://post.kz/mail-app/info/remote/currencies/ops").json()
    if lang == 'en':
        result = 'Currency for today:\n'
    else:
        result = u'Курс валют на сегодня: \n'
    result += "USD: " + data['usdSell'] + '\n'
    result += "EUR: " + data['eurSell'] + '\n'
    result += "RUB: " + data['rurSell']
    return result

msq_currencies = get_currency('en')
ru_msg_currencies = get_currency('ru')

msg_shrug = """
            ¯\_(ツ)_/¯
            """