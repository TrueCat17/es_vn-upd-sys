init python:
	day2_map_necessary_done = 0
	day2_cards_with_sl = 0
	day2_dv_bet = 0
	day2_un = 0
	d2_gave_keys = False

label day2_main1:
	$ new_chapter(2, "day2", "days")
	$ day_time()
	
	scene bg black
	
	$ renpy.pause(2)
	
	window show
	"Мне снился сон…"
	"Казалось, я нахожусь в каком-то вакууме, а вокруг – пустота."
	"Но не только {i}вокруг{/i} – Я единственное существо во Вселенной."
	"Как будто она вернулась в некое сингулярное состояние перед самым Большим Взрывом."
	"И вот-вот что-то должно было произойти."
	"Вдруг я начал слышать голос."
	"Слов не разобрать, но он показался мне знакомым."
	"Голос что-то нежно нашёптывал, как будто убаюкивая."
	"И тут я понял...{w} Это был голос той Незнакомки из автобуса.{w} Той девушки из сна."
	th "Но что она хочет мне сказать? Кто она?.."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg int_house_of_mt_day
	with fade2
	
	window show
	"Я проснулся."
	window hide
	
	play music music_list["my_daily_life"] fadein 5
	
	with flash
	
	window show
	"Яркие лучи солнца били в глаза."
	"Время приближалось к полудню."
	"Лениво потянувшись и зевнув, я начал вспоминать вчерашний день."
	"За несколько секунд все его события пронеслись перед глазами: автобус, лагерь, местные обитатели."
	th "Но ведь всё не так, неправильно!"
	"Не эта ситуация, не моё положение – они неправильны априори, – а моё отношение к ним."
	th "Ведь я вчера запросто заснул здесь, а до этого мило беседовал с местными пионерами, даже умудрялся шутить!"
	th "Но как можно себя так вести в подобной ситуации?!"
	th "Я же должен бояться, шарахаться от каждого шороха, избегать любого контакта с потенциально враждебными существами."
	"Все события прошедшего дня словно заволокло похмельной дымкой."
	th "Это очень похоже на утро после хорошей пьянки: вчерашнее естественное, непредосудительное, в высшей степени нормальное поведение утром становится кошмаром, гротескной гравюрой из иллюстраций к «Божественной комедии»."
	th "Да, всё именно так, однако прошлого уже не вернуть."
	"Хотя, возможно, оценив обстановку, я действовал по ситуации."
	"Я огляделся по сторонам, пытаясь понять, не забросило ли меня куда-нибудь ещё, но домик Ольги Дмитриевны выглядел так же, как и вчера."
	"Всё было как будто на своих местах, разве что на спинке кровати висела пионерская форма."
	"Я с недоверием покрутил её в руках, примерил и оделся."
	th "Всё равно это лучше, чем ходить в зимней одежде."
	th "Посмотреть бы теперь на себя – наверняка выгляжу как клоун!"
	"А для этого нужно зеркало.{w} Хотя бы самое маленькое."
	"Нашлось оно на дверце шкафа."
	
	play sound sfx_open_cabinet_2
	
	window hide
	
	scene cg d2_mirror:
		pause 0.5
		block:
			linear 0.05 pos (-5, -5)
			linear 0.05 pos ( 0,  0)
			linear 0.05 pos ( 5,  5)
			linear 0.05 pos ( 0,  5)
			linear 0.05 pos ( 5,  0)
			linear 0.05 pos ( 0,  0)
			repeat 3
	with dissolve
	
	window show
	me "Твою!.."
	"Я взглянул на новоиспечённого пионера и аж отпрыгнул в сторону от неожиданности!"
	"На другой стороне зеркала стоял какой-то подросток!"
	"Похожий на меня, но не я!"
	"Куда пропали недельная небритость, мешки под глазами, сутулость и смертельно уставшее выражение лица?!"
	"Похоже, меня не закинули назад во времени или в параллельную реальность, а просто поменяли с кем-то телами."
	th "Действительно просто!{w} Такое же на каждом шагу встречается!"
	"Я пригляделся к незнакомцу повнимательнее и только тогда понял, что это я сам!"
	"Только образца конца школы – начала института."
	th "Ладно, хотя бы так."
	th "Да уж, {i}человек в стрессовой ситуации{/i} слона и не приметил!"
	th "А вот вожатая обратила внимание и вчера ночью меня отчитала за неподобающее обращение к ней…"
	th "К чёрту!"
	window hide
	
	play sound sfx_close_cabinet
	
	$ pause(1)
	
	$ persistent.sprite_time = "day"
	scene bg int_house_of_mt_day
	with dissolve
	
	window show
	th "Вряд ли мой внешний вид влияет на что-то ещё."
	"Если верить часам, завтрак уже давно позади."
	th "Ну ладно, попробую всё же в столовой что-нибудь найти."
	th "Вчера же со Славей получилось."
	"От этих воспоминаний я невольно улыбнулся."
	window hide
	
	stop music fadeout 3
	
	$ persistent.sprite_time = "day"
	scene bg ext_house_of_mt_day
	with dissolve
	
	play ambience ambience_camp_center_day fadein 3
	
	window show
	"На улице ярко светило солнце, дул лёгкий ветерок."
	th "Прекрасный летний день."
	"Я уже несколько лет не чувствовал себя по утрам так хорошо."
	"Все проблемы на секунду улетели куда-то далеко, растворились в редких, цвета первого снега облаках."
	"Вдруг передо мной словно из ниоткуда появилась Ольга Дмитриевна."
	show mt normal panama pioneer at center with dissolve
	mt "Доброе утро, Семён!"
	me "Доброе!"
	"Я улыбнулся, пытаясь всем своим видом показать, что несмотря ни на что утро моё было действительно добрым."
	mt "Ты только вчера приехал, так что будить я тебя не стала, но завтрак-то…"
	show mt smile panama pioneer at center with dspr
	mt "Хотя ладно! Вот, держи!"
	
	play sound sfx_paper_bag
	
	"Она протянула мне бумажный свёрток."
	"Судя по масляным пятнам, внутри, скорее всего, бутерброды."
	me "Ой, спасибо!"
	show mt normal panama pioneer at center with dspr
	mt "А теперь марш умываться!"
	"Я уже собирался уходить."
	mt "Сейчас, подожди."
	hide mt with dissolve
	window hide
	
	$ pause(1)
	
	window show
	show mt normal panama pioneer at center with dissolve
	"Ольга Дмитриевна забежала в домик и, вернувшись, сунула мне небольшой пакетик."
	"Внутри оказались зубная щётка, мыло, небольшое полотенце и что-то ещё – я особо не всматривался."
	show mt smile panama pioneer at center with dspr
	mt "Пионер должен быть всегда чист и опрятен!"
	mt "Дай я тебе галстук правильно завяжу на первый раз, а то он болтается.{w} Потом научишься, сам будешь!"
	me "А может, не надо? Я сейчас умываться иду."
	th "Ну да, вдруг зацеплюсь за кран и удавлюсь..."
	show mt normal panama pioneer at center with dspr
	mt "Ладно, тогда потом.{w} И не забудь про линейку."
	th "Карандаши, ручки, линейки…{w} Такие вещи не забываются!"
	me "Какую линейку?"
	show mt angry panama pioneer at center with dspr
	mt "В смысле – какую линейку?!"
	"Она нахмурилась."
	mt "Сегодня же понедельник!"
	th "Странно, а по моим подсчётам – воскресенье…"
	th "Впрочем, смена дня недели – это ещё не самое страшное."
	show mt normal panama pioneer at center with dspr
	mt "Обычно у нас линейки рано утром, до завтрака, но сегодня понедельник, поэтому она будет в 12 часов."
	mt "Не опаздывай!"
	me "Хорошо. А где?"
	mt "На площади, где же ещё!"
	"Спорить было бессмысленно."
	
	stop ambience fadeout 2
	
	"Я направился в сторону «помывочной»."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_washstand_day
	with dissolve
	
	play music music_list["everyday_theme"] fadein 5
	
	window show
	"На отдельный душ и туалет рассчитывать не приходилось, но при виде этого выкидыша загнивающего социализма – причудливой черепашки с панцирем из жести, множеством ног-кранов и кафельным брюшком – мне стало несколько не по себе."
	"Я не был брезгливым человеком, но тем не менее, стоя тут, понял, что всё же есть какой-то минимальный уровень привычного комфорта, без которого жить мне довольно проблематично."
	"Вот ведь как бывает – когда теряешь вещи, которые всегда казались совершенно обыденными и естественными, понимаешь, что на самом деле они были незаменимы."
	th "А, да и чёрт с ним! Выбирать всё равно не из чего."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_washstand2_day
	with dissolve
	
	play sound sfx_open_water_sink
	
	$ renpy.pause(1)
	
	play sound_loop sfx_water_sink_stream
	
	window show
	"Вода оказалась просто ледяной."
	"Если помыть руки не составило особого труда, то вот умыться или прополоскать рот ей – уже большая проблема."
	"В пакетике, который мне дала Ольга Дмитриевна, не нашлось зубной пасты."
	"Можно, конечно, было почистить зубы и так, но в полотенце была завернута какая-то кругленькая коробочка."
	"«Зубной порошок»."
	th "Прелестно! +1 за то, что я где-то в прошлом."
	"Умылся я довольно быстро, в том числе и из-за ледяной воды."
	window hide
	
	stop sound_loop
	play sound sfx_close_water_sink
	
	$ persistent.sprite_time = "day"
	scene bg ext_washstand_day
	with dissolve
	
	window show
	"Кто-то быстро шёл, даже бежал в мою сторону."
	"Я обернулся."
	show sl normal sport at center with dissolve
	"Передо мной стояла Славя в спортивном костюме."
	"Похоже, эта девочка будет хорошо выглядеть абсолютно во всём – и в пионерской форме, и в купальнике, и, наверное, даже в космическом скафандре."
	show sl smile sport at center with dspr
	sl "Физкульт-привет!"
	me "Охай… То есть, бобр… Доброе утро! Вот…"
	"Приветствие мне удалось выбрать не сразу."
	show sl normal sport at center with dspr
	sl "Почему на завтрак не пришёл?"
	me "Проспал."
	"Я сказал это так, словно гордился своим достижением."
	me "Но мне Ольга Дмитриевна бутерброды принесла."
	show sl smile sport at center with dspr
	sl "А, ну отлично тогда! Не забудь про линейку!"
	me "Да, конечно."
	th "Забудешь тут."
	sl "Ладно, я побежала, не скучай!"
	hide sl with dissolve
	"Она помахала мне на прощание и скрылась за поворотом тропинки."
	th "Судя по всему, линейка начнётся через пару минут."
	
	stop music fadeout 3
	
	"Стоило быстренько забежать «домой», закинуть пакетик с умывальными принадлежностями, съесть бутерброды и только уже потом идти на площадь."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_house_of_mt_day
	with dissolve
	
	play sound sfx_open_door_strong
	
	window show
	"Я распахнул дверь домика вожатой и вбежал внутрь так, как будто запрыгивал в последний вагон уходящего поезда."
	window hide
	
	scene black
	with dissolve
	
	play music music_list["awakening_power"] fadein 0
	
	window show
	"Но, кажется, это было не лучшим решением – посреди комнаты стояла Ольга Дмитриевна…"
	"И переодевалась!"
	"Я застыл как вкопанный, стараясь даже не дышать."
	"Наконец вожатая заметила меня."
	mt "Семён!"
	"Я тут же отвернулся."
	mt "Стучаться надо! А теперь вон!"
	window hide
	
	stop music fadeout 2
	
	$ persistent.sprite_time = "day"
	scene bg ext_house_of_mt_day
	with dissolve
	
	play ambience ambience_camp_center_day fadein 3
	
	window show
	th "Да, неудобно получилось."
	"Хотя зрелище мне пришлось по нраву."
	"Через минуту вышла и Ольга Дмитриевна."
	show mt normal panama pioneer at center with dissolve
	mt "Вот, держи.{w} Теперь это и твой дом тоже."
	window hide
	
	play sound sfx_keys_rattle
	
	$ renpy.pause(1)
	
	window show
	"Она протянула мне ключ.{w} Я положил его в карман."
	th "Дом…"
	th "Конечно, если опустить всю фантасмагоричность происходящего, этот лагерь был далеко не самым плохим местом на Земле, но назвать его домом…"
	th "Всего за день, проведённый здесь!"
	th "Вряд ли я смогу это сделать даже спустя год."
	mt "Ладно, пойдём, опаздываем."
	me "А как же бутерброды?.."
	mt "По дороге съешь!"
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_houses_day
	with dissolve
	
	window show
	"Мы шли вдоль домиков пионеров, я уплетал бутерброды с колбасой, а Ольга Дмитриевна трещала без умолку.{w} Ву-ву-ву – как трансформатор!"
	"Но меня не волновало ничего кроме еды."
	show mt normal panama pioneer at center with dissolve
	mt "Понял?"
	me "А?"
	show mt angry panama pioneer at center with dspr
	mt "Ты не слушаешь!"
	me "Простите…"
	show mt normal panama pioneer at center with dspr
	mt "Сегодня начинается твоя новая пионерская жизнь!"
	mt "И ты должен приложить все усилия, чтобы она стала счастливой!"
	me "А, да, конечно…"
	show mt surprise panama pioneer at center with dspr
	mt "Я серьёзно! У пионера много обязанностей, на него возложена большая ответственность – участвовать в общественной работе, помогать младшим, учиться, учиться и ещё раз учиться!"
	mt "Мы все тут как одна большая семья.{w} И тебе предстоит стать её частью."
	th "Да, частью…{w} Я готов даже расписаться в партбилете, лишь бы не слушать этот бред."
	show mt smile panama pioneer at center with dspr
	mt "Надеюсь, по окончании смены у тебя останутся самые лучшие воспоминания о нашем лагере."
	mt "Воспоминания на всю жизнь!"
	me "А когда смена заканчивается?"
	show mt normal panama pioneer at center with dspr
	mt "Что ты постоянно всякие глупости спрашиваешь?"
	th "Похоже, ответов от неё мне не добиться ."
	"А жаль.{w} Этот мир кажется дружелюбным, но вот представиться {i}он{/i} так и не соизволил."
	th "Возможно, сейчас я отношусь к этому несколько спокойнее, чем вчера?"
	"Как будто у нас с {i}ним{/i} негласное перемирие – он не трогает меня, но и мне запрещено задавать какие-либо вопросы."
	"Конечно, ситуация не из приятных, но что мне остаётся?{w} Плохой мир лучше доброй ссоры."
	mt "Самое главное для тебя – использовать время, которое ты проведёшь здесь, с пользой."
	me "Я постараюсь."
	"Честно говоря, этот разговор меня сильно утомил."
	
	stop ambience fadeout 2
	
	"Узнать хотя бы, где это «здесь» находится!{w} Но…"
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_square_day
	with dissolve
	
	play music music_list["get_to_know_me_better"] fadein 5
	
	window show
	"Мы пришли на площадь."
	"Пионеры уже выстроились в шеренгу."
	show mt normal panama pioneer at center with dissolve
	me "А что, ещё не все пришли?"
	mt "Да вроде все."
	"Она окинула взглядом свой бравый пионеротряд."
	mt "Ладно, иди становись."
	th "Странно.{w} Почему тогда она мне сказала, что больше спальных мест нет?"
	hide mt with dissolve
	window hide
	
	scene cg d2_lineup
	with dissolve
	
	window show
	"Пока вожатая рассказывала о плане мероприятий на неделю, я осматривал присутствующих."
	"В паре человек от меня стоял Электроник, чуть дальше – Лена и Славя, а в самом конце – Ульянка и Алиса."
	th "Все знакомые здесь."
	"Ольга Дмитриевна говорила про какие-то спортивные соревнования, а я уставился на памятник."
	th "«Генда»..."
	"Не удавалось вспомнить ни одного революционера с похожей фамилией."
	"Да и поза у него какая-то странная – как будто смотрит на происходящее с недоверием, может быть, пренебрежением или даже надменностью."
	th "Наверное, какой-то местный деятель…"
	sl "О чём мечтаешь?"
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_square_day
	show sl normal pioneer at cright
	show mt normal panama pioneer at cleft
	with dissolve
	
	window show
	"Славя вывела меня из раздумий."
	"Рядом стояла Ольга Дмитриевна."
	mt "Ты запомнил план на неделю?"
	me "План?{w} План я никогда не забуду!"
	show mt smile panama pioneer at cleft with dspr
	mt "Вот и отлично!"
	"Она посмотрела на Славю."
	show mt normal panama pioneer at cleft with dspr
	mt "Принесла?"
	sl "Да."
	"Славя протянула мне какой-то листок."
	mt "Это обходной лист. Тут четыре позиции. За сегодня тебе нужно везде отметиться."
	mt "Во-первых, записаться в клуб, они у нас в здании кружков и отдельно – музыкальный."
	mt "Во-вторых, в медпункт зайти."
	mt "Ну, и в-третьих – в библиотеку."
	mt "Всё понял?"
	me "Да."
	"Обходной оказался неплохой возможностью что-нибудь выяснить, так как в этих локациях я ещё не бывал."
	mt "Тогда давай, начинай прямо сейчас."
	me "А как же обед?"
	mt "Ничего страшного! Я тебе ещё бутербродов принесу. Обходной лист важнее!"
	sl "Удачи тебе."
	hide sl
	hide mt
	with dissolve
	"Они ушли так быстро, что я и слова сказать не успел."
	th "Пропустил завтрак, теперь и обед придётся."
	th "Да что же это такое?"
	th "Впрочем, может, успею как-нибудь?"
	th "Обед в час.{w} Хотя если я пойду есть, то могу не попасть в какое-нибудь место из списка."
	
	stop music fadeout 3
	
	th "Ладно, пока всё равно в столовую идти рано!"
	window hide
	
	$ disable_all_zones()
	
	$ set_zone("music_club", "day2_musclub")
	$ set_zone("clubs", "day2_clubs")
	$ set_zone("library", "day2_library")
	$ set_zone("medic_house", "day2_aidpost")
	$ set_zone("dining_hall", "day2_dinner")
	
	jump day2_map

label day2_map:
	if day2_map_necessary_done == 5:
		jump day2_main2
	if day2_map_necessary_done == 2:
		$ reset_zone("dining_hall")
		$ day2_map_necessary_done += 1
	
	$ show_map()

label day2_musclub:
	play ambience ambience_camp_center_day fadein 3
	
	$ persistent.sprite_time = "day"
	scene bg ext_musclub_day
	with dissolve
	
	window show
	"Музыкальный клуб – небольшое одноэтажное здание – располагался поодаль от остальных построек лагеря."
	"Не раздумывая, я открыл дверь и вошёл."
	window hide
	
	stop ambience fadeout 2
	
	play sound sfx_open_door_2
	
	$ pause(1)
	
	$ persistent.sprite_time = "day"
	scene bg int_musclub_day
	with dissolve
	
	play ambience ambience_music_club_day fadein 3
	
	window show
	"Внутри меня встретил настоящий оркестр: барабаны, гитары и даже рояль."
	"Некоторое время я внимательно изучал музыкальные инструменты – хотелось понять, из какого они примерно временного периода, – но неожиданно под роялем послышалось копошение."
	window hide
	
	scene cg d2_miku_piano2
	with dissolve
	
	play music music_list["so_good_to_be_careless"] fadein 5
	
	window show
	th "Девочка. Кажется, что-то ищет."
	"Она стояла на четвереньках в такой пикантной позе, что я не сразу решился начать разговор."
	me "Простите…"
	window hide
	
	scene cg d2_miku_piano
	with dissolve
	
	window show
	mip "Ааа! Кто здесь?"
	window hide
	
	play sound sfx_piano_head_bump
	with vpunch
	
	$ renpy.pause(1)
	
	window show
	"Она попыталась вскочить, но днище рояля стало для неё непреодолимой преградой."
	mip "Ай!"
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg int_musclub_day
	with dissolve
	
	show mi shocked pioneer at center with dissolve
	window show
	"С трудом, но девочка всё же выбралась."
	me "Извини, что напугал…"
	show mi normal pioneer at center with dspr
	mip "Да ничего! Вижу, у тебя обходной, новенький, значит?"
	me "А? Да."
	show mi smile pioneer at center with dspr
	mip "Меня Мику зовут."
	mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
	mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
	"Она говорила с такой скоростью, что половину слов просто проглатывала."
	me "А я Семён."
	show mi happy pioneer at center with dspr
	mi "Отлично! Не хочешь к нам в клуб вступить? Правда, я тут пока одна, но с тобой нас будет двое! Ты на чём-нибудь играть умеешь?"
	"Уже в период моего «отшельничества» я купил гитару и выучил пару аккордов, но потом забросил, как и всё, на что требовалось больше нескольких часов."
	me "Знаешь, я как-то не планировал особо…"
	show mi normal pioneer at center with dspr
	mi "Да ладно тебе, я тебя научу играть! Хочешь, на трубе, например? Или на скрипке? Я на всём умею, честно-честно."
	"Спорить с девочкой-мультиинструменталистом бессмысленно, так как в ответ наверняка последует ещё одна пулемётная очередь из слов."
	me "Я подумаю, а пока не могла бы ты подписать?"
	show mi happy pioneer at center with dspr
	mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я ещё и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
	me "Обязательно… А сейчас мне пора, извини."
	show mi shy pioneer at center with dspr
	mi "Конечно, приходи непременно…"
	window hide
	
	stop ambience fadeout 2
	
	stop music fadeout 3
	
	$ renpy.pause(1)
	
	$ persistent.sprite_time = "day"
	scene bg ext_musclub_day
	with dissolve
	
	play ambience ambience_camp_center_day fadein 3
	
	window show
	"Окончание её фразы скрылось за закрытой дверью."
	"С одной стороны, неплохо вечерком посидеть побренчать на гитаре, но в такой компании…"
	show dv normal pioneer close at center with dissolve
	"Я повернулся, собираясь уходить, и столкнулся нос к носу с Алисой."
	"Она недобро посмотрела на меня."
	dv "Зачем пришёл?"
	me "Обходной…"
	dv "Подписал?"
	me "Да…"
	dv "Свободен!"
	hide dv with dissolve
	"Алиса вошла внутрь, а я поспешил покинуть это место."
	window hide
	
	stop ambience fadeout 2
	
	$ disable_current_zone()
	$ day2_map_necessary_done += 1
	jump day2_map

label day2_clubs:
	play ambience ambience_camp_center_day fadein 2
	
	$ persistent.sprite_time = "day"
	scene bg ext_clubs_day
	with dissolve
	
	window show
	"Я направился к зданию кружков."
	"По правде говоря, мне никогда особенно не нравилась общественная работа."
	"В школе я всегда под любым предлогом пропускал субботники, в институте не было ни малейшего желания вступать в студенческий совет."
	"Меня не интересовали секции бокса, авиамоделирования или кройки и шитья."
	"Так что сюда я пришёл лишь с целью отметиться."
	window hide
	
	stop ambience fadeout 2
	
	play sound sfx_open_door_clubs
	
	$ pause(1)
	
	$ persistent.sprite_time = "day"
	scene bg int_clubs_male_day
	with dissolve
	
	play ambience ambience_clubs_inside_day fadein 3
	
	window show
	"Внутри никого не оказалось."
	"Я словно оказался в берлоге юного робототехника: повсюду валялись провода, нехитрые платы, микросхемы, на столе стоял осциллограф."
	"Из соседнего помещения послышались голоса, и через секунду в комнату вошли двое пионеров."
	show el normal pioneer at cleft
	show sh normal pioneer at cright
	with dissolve
	"В одном я узнал Электроника, второй же мне был незнаком."
	el "Привет, Семён! А мы тебя ждали."
	th "Кажется, он знает всё и обо всех…"
	me "А чего вы меня ждали?"
	el "Ну как же, ты пришёл в наш клуб кибернетиков записываться, так?"
	"Он не дал мне ответить."
	show el smile pioneer at cleft with dspr
	el "Знакомься, это Шурик, он у нас главный!"
	me "А вас в клубе этом только двое, я так полагаю?"
	show el normal pioneer at cleft with dspr
	el "Ну, можешь считать, что уже трое."
	"Шурик подошёл ко мне и уверенно протянул руку."
	"Его лицо почему-то казалось знакомым."
	show sh normal_smile pioneer at cright with dspr
	sh "Добро пожаловать!"
	me "Угу…"
	show sh normal pioneer at cright with dspr
	el "Давай я тебе тут всё покажу!{w} Ты не стесняйся, располагайся."
	me "Да нет, ребята, я вообще-то…"
	show sh normal_smile pioneer at cright with dspr
	sh "Всегда рады новым членам."
	"Он сказал это так, что в голове у меня невольно заиграл гимн Советского Союза."
	"Удивительно, но я ещё помнил слова – в первом классе у меня была тетрадка с текстом гимна на обратной стороне."
	me "Да нет, мне бы просто обходной лист подписать."
	show sh normal_smile pioneer at cright with dspr
	show el grin pioneer at cleft with dspr
	el "Так ты к нам запишись, а мы тебе его подпишем."
	"Он хитро улыбнулся."
	"Я уже подготовился к длинному и нудному разговору, как вдруг в комнату кто-то вошёл."
	show el normal pioneer at left
	show sh normal pioneer at right
	show sl normal pioneer at center
	with dissolve
	"Я обернулся и увидел Славю."
	sl "А, Семён! Надеюсь, они тебя тут не достают?"
	show sl angry pioneer at center with dspr
	"Она строго посмотрела на будущих светил отечественного роботостроения."
	sl "А то я их знаю – они могут!"
	me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
	"Я решил воспользоваться ситуацией."
	show sl normal pioneer at center with dspr
	sl "Так это не проблема, давай сюда."
	"Славя взяла листок и подошла к Шурику."
	sl "Подписывай!"
	show sh upset pioneer at right with dspr
	sh "Ну подожди, мы ещё не закончили…"
	show sl angry pioneer at center with dspr
	sl "Закончили! Подписывай!"
	"Она посмотрела на него так, что возражать Шурик не решился."
	
	stop ambience fadeout 2
	
	"Он поставил свою закорючку, и я, поблагодарив Славю, с чистой совестью направился дальше."
	window hide
	
	$ disable_current_zone()
	$ day2_map_necessary_done += 1
	jump day2_map

label day2_library:
	play ambience ambience_camp_center_day fadein 3
	$ persistent.sprite_time = "day"
	scene bg ext_library_day
	with dissolve
	
	window show
	"Вообще, я, конечно, любил читать, но просиживать днями в библиотеке при нынешних обстоятельствах в мои планы не входило."
	"Так что этот чекпойнт стоило пройти побыстрее."
	window hide
	
	stop ambience fadeout 3
	
	$ persistent.sprite_time = "day"
	scene bg int_library_day
	with dissolve
	
	play ambience ambience_library_day fadein 3
	
	window show
	"Когда я зашёл внутрь, у меня в голове всплыло воспоминание из детства."
	"Оно было очень ярким."
	"Мне лет 7 или 8, мы с мамой в библиотеке."
	"Пока она выбирает какие-то книжки, которые мне понадобятся для учёбы, я сижу и разглядываю местную подборку комиксов."
	"Тогда я не знал, почему их здесь так много и почему нельзя забрать часть домой."
	"Понятия коллективной собственности в том возрасте для меня не существовало."
	"Впрочем, как и понятия собственности вообще."
	"Тем более странным показалось это воспоминание сейчас, когда я находился в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
	"Советская символика была буквально повсюду, а на полках стояли книги в основном соответствующей тематики."
	"Читать их я никак не планировал; знакомство с полным собранием сочинений Маркса – одна из последних вещей на Земле, которая могла бы прийти мне в голову."
	th "Но где же библиотекарь?"
	"Найти её оказалось не так уж и сложно."
	window hide
	
	scene cg d2_micu_lib
	with dissolve
	
	window show
	"Я пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
	"Она так мило спала, что мне совсем не хотелось её будить."
	th "Пожалуй, подожду – если через полчаса не проснётся, тогда уж что поделать…"
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg int_library_day
	with dissolve
	
	window show
	"Просто так сидеть было скучно, и я взял с полки первую попавшуюся книгу."
	"Артур Шопенгауэр, «Мир как воля и представление»."
	"Я открыл примерно на середине и начал читать:"
	window hide
	
	$ set_mode_nvl()
	
	window show
	nvl clear
	"Жизнь человека с её бесконечными трудами, нуждой и страданием следует рассматривать как объяснение и парафраз акта зачатия, т.е. решительного утверждения воли к жизни; с этим связано и то, что человек обязан природе смертью и с тоской думает об этом обязательстве."
	"Разве это не свидетельствует о том, что в нашей жизни заключена некая вина?"
	"И тем не менее, периодически расплачиваясь смертью за рождения и смерти, мы всегда существуем и испытываем все горести и радости жизни попеременно, когда ни одна из них не может нас миновать: таков результат утверждения воли к жизни."
	"При этом страх смерти, который, несмотря на все страдания жизни, удерживает нас в ней, становится, в сущности, иллюзией; но столь же иллюзорно и влечение, заманившее нас в жизнь."
	"Объективное выражение этого соблазна можно увидеть в обращённых друг на друга страстных взглядах влюблённых: они есть чистейшее выражение воли к жизни в её утверждении. Как она здесь кротка и нежна!"
	"Она хочет благополучия, спокойного наслаждения и тихой радости для себя, для других, для всех."
	window hide
	
	$ set_mode_adv()
	
	play sound sfx_knock_door2
	
	window show
	"В дверь постучали."
	"Я быстро закрыл книгу и положил её на место."
	th "Какая отличная привычка – стучать.{w} Надо и мне её взять на вооружение."
	
	play sound sfx_open_door_clubs_2
	
	"В библиотеку вошла Лена."
	show un normal pioneer at cleft with dissolve
	un "Ой…"
	show un shy pioneer at cleft with dspr
	me "Привет!"
	"Я улыбнулся."
	un "Привет, а я вот книжку пришла отдать…"
	"У неё в руках была «Унесённые ветром», которую я видел вчера."
	un "Ой, а Женя спит, тогда я попозже зайду…"
	mz "Уже не сплю."
	show mz normal glasses pioneer far at cright with dissolve
	"Я удивлённо посмотрел в сторону библиотекарши."
	"Она сидела за столом и пристально наблюдала за мной."
	show mz angry glasses pioneer far at cright with dspr
	mz "А тебе чего?"
	me "Мне бы обходной…"
	show mz normal glasses pioneer at cright with dissolve
	mz "Давай."
	"Библиотекарша быстро расписалась и протянула мне его."
	"Вид у неё был такой, что продолжать разговор не возникало никакого желания."
	"Лена подошла к ней и отдала книжку, а я поблагодарил Женю и вышел."
	window hide
	
	stop ambience fadeout 2
	
	$ disable_current_zone()
	$ day2_map_necessary_done += 1
	jump day2_map

label day2_aidpost:
	$ persistent.sprite_time = "day"
	scene bg ext_aidpost_day
	with dissolve
	
	play ambience ambience_camp_center_day fadein 3
	
	window show
	th "И что я забыл в медпункте?"
	"Здоровье вроде не шалило, тем более местный свежий воздух явно пошёл мне на пользу – чувствовал я себя куда бодрее, чем обычно."
	th "Но раз надо так надо."
	"Я вошёл."
	window hide
	
	stop ambience fadeout 2
	
	play sound sfx_open_door_1
	
	$ renpy.pause(1)
	
	$ persistent.sprite_time = "day"
	scene bg int_aidpost_day
	with dissolve
	
	play ambience ambience_medstation_inside_day fadein 3
	
	window show
	th "Обычный медпункт, у нас в школе был примерно такой же."
	show cs normal stethoscope at center with dissolve
	
	play music music_list["eternal_longing"] fadein 5
	
	"За столом сидела женщина средних лет.{w} Очевидно, медсестра."
	"Она пристально, оценивающе посмотрела на меня, и продолжила что-то писать."
	csp "Ну, здравствуй… пионер."
	"Сказала медсестра, не отрываясь от своего занятия."
	me "Добрый день… Мне бы вот…"
	csp "Ты присаживайся."
	"Я оглядел комнату."
	csp "На кушеточку."
	"Я сел."
	csp "Раздевайся."
	"Всё это она говорила совершенно ровным тоном."
	me "Зачем?.."
	csp "Смотреть тебя будем, слушать, здоровье проверять."
	show cs smile stethoscope at center with dspr
	csp "Меня, кстати, зовут Виолетта, но ты можешь звать меня просто Виолой."
	"Она повернулась в мою сторону."
	cs "Ну, чего сидишь? Раздевайся."
	me "Да я не жалуюсь ни на что. Мне бы вот…"
	"Я аккуратно протянул ей листок."
	cs "Потом."
	show cs smile at center with dissolve
	"Она сняла с шеи стетоскоп и, кажется, намеревалась меня им препарировать."
	window hide
	
	stop music fadeout 3
	play sound sfx_knock_door7_polite
	
	$ renpy.pause(1)
	
	window show
	"Но тут в дверь постучали."
	show cs normal at center with dspr
	"Медсестра нехотя ответила:"
	cs "Входите!"
	
	play sound sfx_open_door_strong
	
	"Моментально дверь распахнулась и в комнату влетел Электроник."
	show el fingal pioneer far at left with dissolve
	show cs normal at center with dspr
	el "Здрасьте! Я тут это… на футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
	"У Электроника под глазом красовался здоровенный фингал."
	th "Что-то я сомневаюсь, что такой можно заработать на футболе."
	cs "Садись, сейчас посмотрим."
	"Сказала она ему."
	show cs normal glasses at center with dissolve
	cs "А ты давай сюда свой обходной."
	"Медсестра быстро подписала его и продолжила:"
	show cs smile glasses at center with dspr
	cs "Если что заболит – сразу ко мне… пионер."
	
	stop ambience fadeout 2
	
	"Я не стал ничего отвечать и вышел, закрыв за собой дверь."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_aidpost_day
	with dissolve
	
	window show
	th "Медсестра здесь, конечно, ещё та…"
	window hide
	
	$ disable_current_zone()
	$ day2_map_necessary_done += 1
	jump day2_map

label day2_dinner:
	$ lp_us += 1
	
	$ persistent.sprite_time = "day"
	scene bg ext_dining_hall_away_day
	with dissolve
	
	window show
	"Я решил всё же сходить пообедать."
	th "Обходной лист никуда не денется – потом быстренько подпишу, – а вот мой желудок до ужина явно ждать не намерен."
	"С этими мыслями я вошёл в столовую."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg int_dining_hall_day
	with dissolve
	
	play ambience ambience_dining_hall_empty fadein 3
	
	window show
	"Внутри почти никого не было – видимо, большинство пионеров уже пообедало."
	"Внушающая уважение своими габаритами повариха выдала мне шикарный обед из трёх блюд: суп «Ипрская похлёбка», гуляш «от Лаврентия Палыча» с гарниром из картошки, сваренной, видимо, по рецептам конца XV века, и компот «Таблица Менделеева»."
	"Такому меню позавидовали бы и лучшие рестораны мира, но мне было наплевать – голод сильнее."
	"А по сравнению с моими обычными пельменями, приправленными макаронами и дошираком, и такой обед весьма неплох."
	"Я сел за первый попавшийся стол и принялся сосредоточенно жевать."
	window hide
	
	play sound sfx_punch_medium
	with vpunch
	
	play music music_list["eat_some_trouble"] fadein 5
	
	$ renpy.pause(1)
	
	window show
	"Однако сосредоточенность моя продлилась недолго – кто-то ударил меня по спине, да так, что я подавился."
	"Передо мной стояла Ульянка и торжествующе улыбалась."
	show us laugh pioneer at center with dissolve
	me "Я тебя когда-нибудь удушу!"
	show us laugh2 pioneer at center with dspr
	us "Не догонишь!"
	"Она показала язык!"
	show us grin pioneer at center with dspr
	us "Один раз уже пытался – не догнал же."
	me "Хорошо, тогда я тебя где-нибудь подкараулю!"
	show us surp2 pioneer at center with dspr
	us "Так нечестно!"
	me "Ты на себя посмотри, честная!"
	"Я ухмыльнулся."
	show us laugh pioneer at center with dspr
	us "Ладно, подожди, сейчас обед возьму и вернусь, вместе поедим."
	hide us with dissolve
	"Не самая радужная перспектива – я постарался побыстрее закончить с обедом."
	"Однако Ульянка вернулась буквально через полминуты."
	show us smile pioneer at center with dspr
	"У неё на тарелке лежал огромный кусок жареного мяса и несколько отварных картофелин."
	"По сравнению с моей королевской трапезой…"
	me "Это ты как?.. Откуда?.."
	show us laugh2 pioneer at center with dspr
	us "Уметь надо!"
	"Она посмотрела на меня и улыбнулась во все свои 32… или сколько их у неё там было… зуба."
	th "Не потерплю такого оскорбления!"
	"Я никогда толком не умел над кем-то подшучивать, да и в школе чаще прикалывались надо мной."
	"Однако как-то ей отомстить всё же было необходимо."
	me "А если Ольга Дмитриевна узнает, что ты воруешь еду?"
	show us surp3 pioneer at center with dspr
	us "Так я не ворую!"
	"Возмутилась Ульяна."
	me "А это ты ей будешь рассказывать. Думаешь, поверит?"
	show us surp2 pioneer at center with dspr
	us "И откуда же она узнает?!"
	me "Ну… это зависит от многих обстоятельств."
	show us calml pioneer at center with dspr
	us "Например?"
	"Она внимательно посмотрела на меня."
	me "Принеси мне булочку. Сладкую."
	show us shy2 pioneer at center with dspr
	us "Откуда же я тебе её возьму?"
	me "Наверное, оттуда же, где взяла это."
	"Я показал на её тарелку."
	"Ульянка замялась."
	show us dontlike pioneer at center with dspr
	us "Ладно. Но только одну!"
	show us surp2 pioneer at center with dspr
	us "И обещай, что после этого не расскажешь Ольге Дмитриевне!"
	me "Слово пионера!"
	hide us with dissolve
	"Она убежала в сторону буфета, а я недолго думая взял перечницу, открутил крышку и высыпал всё содержимое Ульянке в компот."
	"Только я закончил, как неугомонная девочка вернулась."
	show us laugh pioneer at center with dissolve
	us "Держи, вымогатель!"
	th "Кажется, она ничего не заметила."
	me "А теперь давай кто быстрее выпьет компот!"
	show us surp2 pioneer at center with dspr
	us "Что ещё за глупости!"
	me "Почему глупости? Я выиграю, вот увидишь!"
	show us dontlike pioneer at center with dspr
	us "Не буду я с тобой в детские игры играть."
	me "Сама-то не ребёнок разве?"
	"Я ехидно улыбнулся."
	show us angry pioneer at center with dspr
	us "Ах так! Ладно! Раз, два, три!"
	"Она не дала мне времени даже взять чашку, а сама моментально, одним глотком, выпила весь свой компот."
	window hide
	
	scene bg int_dining_hall_day:
		linear 0.1 pos (-5, -5)
		linear 0.1 pos ( 0,  0)
		linear 0.1 pos ( 5,  5)
		linear 0.1 pos ( 0,  5)
		linear 0.1 pos ( 5,  0)
		linear 0.1 pos ( 0,  0)
		repeat 10
	with flash_red
	
	stop music fadeout 0
	
	show us fear pioneer at center with dspr
	
	play sound sfx_angry_ulyana
	
	$ renpy.pause(5)
	
	window show
	"Через секунду у неё на лице появилось выражение первобытного ужаса, щёки покраснели, а глаза, казалось, готовы были вылезти из орбит."
	hide us with dissolve
	"Ульяна вскочила и побежала в сторону чайников с водой, на ходу выкрикивая:"
	us "Ты! Ты! Ты…"
	
	stop ambience fadeout 2
	
	"Я решил не дожидаться, пока она придёт в себя и посмеиваясь вышел из столовой, на ходу доедая булочку."
	window hide
	
	$ disable_current_zone()
	jump day2_map

label day2_main2:
	scene black
	with dissolve2
	
	window show
	"..."
	"Итак, я собрал все подписи, следовательно, надо зайти к Ольге Дмитриевне, чтобы отдать листок."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_house_of_mt_day
	with dissolve
	
	play ambience ambience_camp_center_day fadein 3
	
	show mt normal panama pioneer far at center with dissolve
	window show
	"Вожатая сидела возле домика и читала книжку."
	"Вряд ли она сама соответствовала образу идеального пионера, которого хотела сделать из меня."
	"Видимо, все её обязанности – это произносить пламенные речи на линейке, отчитывать Ульяну и принимать деятельное участие в моём физическом и идеологическом воспитании."
	show mt normal panama pioneer at center with dissolve
	me "Вот…"
	"Я протянул ей обходной."
	"Она не читая сунула листок в карман."
	th "Отлично! Значит, можно было самому за всех расписаться и вообще никуда не ходить…"
	show mt smile panama pioneer at center with dspr
	mt "Молодец! Ну как, познакомился с нашей медсестрой?"
	me "Да…"
	"Почему-то от этого вопроса у меня мурашки побежали по коже."
	show mt normal panama pioneer at center with dspr
	mt "В какой кружок записался?"
	me "Да пока ни в какой… Нужно подумать."
	show mt surprise panama pioneer at center with dspr
	mt "Ну, что же ты так! Завтра обязательно запишись куда-нибудь!"
	th "Конечно, всенепременно!"
	show mt normal panama pioneer at center with dspr
	mt "Ладно, пора уже и на ужин идти."
	th "Ну наконец-то! Я уже проголодался."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_dining_hall_away_day
	with dissolve
	
	window show
	"Вместе с Ольгой Дмитриевной мы направились к столовой."
	"Я посмотрел на небо и отметил, что солнце уже начало садиться."
	window hide
	
	$ persistent.sprite_time = "day"
	scene bg ext_dining_hall_near_day
	with dissolve
	
	show dv normal pioneer at fright
	show el normal pioneer at fleft
	with dissolve
	window show
	"На крыльце стояло несколько человек: Алиса, Электроник..."
	show us normal pioneer at cleft
	show sl normal pioneer at cright
	with dissolve
	"Ульяна и Славя."
	show dv angry pioneer at fright with dspr
	show el surprise pioneer at fleft with dspr
	
	play music music_list["always_ready"] fadein 5
	
	"Когда мы подошли, я услышал, о чем они говорят:"
	dv "И больше не называй меня ДваЧе, а то ещё получишь!"
	el "Да не называл я тебя так! Тебе показалось!"
	show us grin pioneer at cleft with dspr
	us "Называл, называл, я всё слышала!"
	show el angry pioneer at fleft with dspr
	show sl normal pioneer behind el at cright with dspr
	el "Да тебя вообще там не было!"
	us "А вот и была! Я в кустах сидела!"
	hide us with dissolve
	show sl angry pioneer at cright with dspr
	show el angry pioneer behind sl at fleft with dspr
	sl "Хватит вам! Прекратите!"
	th "Значит, Электроник своё ранение не на футболе получил."
	th "Однако, как хорошо его медсестра подлатала – от фингала не осталось и следа!"
	show mt normal pioneer at center with dissolve
	"Ольга Дмитриевна подошла к ним и попыталась выяснить, что происходит:"
	mt "Что вы тут ругаетесь?"
	sl "Алиса Сыроежкину в глаз…"
	dv "Ничего я не делала!"
	hide dv with dissolve
	"Алиса обиженно фыркнула и зашла внутрь."
	
	stop music fadeout 3
	
	mt "Ладно, пора ужинать."
	hide mt
	hide el
	hide sl
	with dissolve
	window hide
	
	stop ambience fadeout 2
	
	$ persistent.sprite_time = "day"
	scene bg int_dining_hall_people_day
	with dissolve
	
	play ambience ambience_dining_hall_full fadein 3
	
	window show
	"Последним в столовую вошёл я."
	"Похоже, свободных мест осталось не так много."
	"Вдалеке виднелось несколько незанятых стульев рядом с Алисой, но лучше поголодать недельку, чем рискнуть сесть рядом."
	"Также свободно было рядом с Ульяной, но я не сторонник китайской традиционной кухни – «ем всё, что ползает»."
	"И, наконец, свободный стул был рядом с Мику."
	"Если выбирать из трёх зол…"
	me "Не возражаешь, если я здесь присяду?"
	show mi normal pioneer at center with dissolve
	
	play music music_list["so_good_to_be_careless"] fadein 5
	
	mi "Ой, да, конечно! То есть нет, не возражаю! То есть да, садись конечно!"
	"Я сел."
	show mi smile pioneer at center with dspr
	mi "Сегодня, смотри, гречка. Ты любишь гречку? И варёная курица! Я вообще курицу не люблю. Ну, то есть не то что не люблю..."
	mi "Но если бы меня спросили, что бы мне больше всего хотелось, то бефстроганов или рагу… Нет, может быть, просто котлета! Или ромштекс! Ты любишь ромштексы?"
	me "Я не особо привередливый."
	"И это сущая правда."
	mi "Понятно. Но вот десерты, знаешь, мне здесь не очень нравятся. Я мороженое люблю! Ты любишь мороженое? Особенно пломбир «48 копеек», но и «Ленинградское» тоже. Ой, прости, я всё о себе!"
	mi "Может, ты больше эскимо любишь?"
	"Ужин в компании этой девочки начинал превращаться в пытку."
	"А я по характеру такой человек, что не могу просто так игнорировать собеседника.{w} Даже её."
	th "Мы всё же за одним столом сидим."
	show mi upset pioneer at center with dspr
	mi "Знаешь, я однажды купила вафельный рожок, начала есть, а там внутри шуруп! Представляешь? Настоящий такой шуруп! Или болт… Я, честно говоря, в них не разбираюсь!"
	show mi normal pioneer at center with dspr
	mi "Шурупы – это которыми закручивают гайки, а болты – это такие, которые отвёрткой, да?"
	th "Думаю, если бы проводился чемпионат по скоростному поеданию пищи, одно из призовых мест точно досталось бы мне."
	me "Ладно, я пойду, а тебе приятного аппетита!"
	"Я встал и направился к выходу."
	hide mi with dissolve
	
	stop music fadeout 3
	
	stop ambience fadeout 2
	
	"Мику что-то пыталась сказать мне вслед, но её слова потерялись в шуме толпы чересчур громко ужинающих пионеров."
	window hide
	
	$ sunset_time()
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_dining_hall_near_sunset
	with dissolve2
	
	play ambience ambience_camp_center_evening fadein 3
	
	window show
	"Выйдя из столовой, я сел на ступеньки и решил подождать, пока переварится ужин."
	"Я просто сидел и смотрел, как на лагерь опускается ночь."
	"Здесь всё было таким живым днём: громкий детский смех, весёлые крики, суета и беготня, шум и гам, спортивные игры и купания на пляже."
	"Но с наступлением темноты «Совёнок» резко преображался."
	"Дневные звуки сменялись тишиной, которую лишь изредка нарушали сверчки и ночные птицы."
	"Лагерь засыпал."
	"В каждой тени можно было узнать кого угодно – привидение, лешего, просто дикое животное, – но никак не пионера."
	"Всё это я понял ещё по вчерашней ночи."
	"Местные жители строго следовали заведённому распорядку."
	"Дневной лагерь – во власти людей, ночной же – скорее сил природы."
	window hide
	
	play sound sfx_pat_shoulder_hard
	
	$ pause(1)
	
	window show
	"Кто-то легонько похлопал меня по плечу."
	
	play music music_list["lightness"] fadein 5
	
	"Я обернулся."
	show el normal pioneer at left with dissolve
	"Это был Электроник."
	el "Пойдём в карты играть."
	me "В карты?"
	el "Да! Я игру новую придумал. Интерееесную!"
	me "И какую же?"
	el "Ну, надо сначала карты найти, потом расскажу."
	me "Так ищи, в чём проблема?"
	show el upset pioneer at left with dspr
	el "Они есть только у Ольги Дмитриевны, а она мне не даст…"
	me "Почему?"
	el "Ну, в прошлый раз…"
	"На крыльцо вышли вожатая и Славя."
	show el normal pioneer at left
	show mt normal pioneer at center
	show sl normal pioneer at right
	with dissolve
	el "Ольга Дмитриевна! А Семён как раз хотел у вас карты попросить!"
	me "Я вообще-то…"
	mt "Зачем?"
	show el smile pioneer at left with dspr
	el "Мы игру новую придумали!"
	th "Не мы, а ты."
	show mt surprise pioneer at center with dspr
	mt "Что за игра?"
	el "Будут карты – я покажу."
	show mt sad pioneer at center with dspr
	mt "Ох, не нравится мне эта идея…{w} Но раз и Семён за, то, наверное, ничего страшного…"
	me "Да я вообще-то…"
	show sl smile pioneer at right with dspr
	sl "Давайте я с ним схожу принесу!"
	window hide
	
	menu:
		"Пойти за картами со Славей":
			$ day2_cards_with_sl = 1
			$ lp_sl += 1
			jump day2_cards_with_sl
		"Пойти одному":
			jump day2_cards_without_sl

label day2_cards_with_sl:
	window show
	me "Если ты не против…"
	
	stop ambience fadeout 2
	
	sl "Конечно! Пошли."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_houses_sunset
	with dissolve
	
	window show
	"Мы направились в сторону домика вожатой."
	"Где-то на полпути Славя вдруг остановилась."
	show sl normal pioneer at center with dspr
	sl "Ой, я же совсем забыла, что карты у меня!"
	th "Очень вовремя."
	me "А где твой домик?"
	show sl smile pioneer at center with dspr
	sl "Да тут рядом, пойдём!"
	"..."
	window hide
	
	with fade
	
	window show
	"Мы подошли к домику, который на самом деле больше напоминал вагончик."
	show sl normal pioneer at center with dspr
	sl "Подожди тут минутку, я сейчас!"
	hide sl with dissolve
	"Минуты ждать не пришлось – она вернулась через пару секунд."
	show sl normal pioneer at center with dissolve
	sl "Вот!"
	"Славя показала мне довольно потрёпанную колоду карт."
	me "Краплёные небось?"
	show sl smile pioneer at center with dspr
	sl "Жульничать не спортивно!"
	"А уж жульничать, не зная правил игры..."
	sl "Пойдём?"
	me "Пойдём."
	hide sl with dissolve
	"..."
	window hide
	
	with fade
	
	window show
	"На обратном пути я решил поговорить с ней в надежде что-нибудь выяснить:"
	show sl normal pioneer at center with dissolve
	me "А ты давно приехала?"
	sl "Уже неделю здесь."
	me "Понятно… А сама откуда?"
	sl "Я с севера."
	me "А поточнее?"
	show sl smile pioneer at center with dspr
	sl "Холодного севера."
	"Она посмотрела на меня и улыбнулась."
	th "Кажется, никто в этом лагере не хочет отвечать даже на самые невинные вопросы."
	"Я решил действовать по-другому."
	me "А что тебе нравится?"
	sl "В смысле?"
	me "Ну, твои увлечения?"
	show sl smile2 pioneer at center with dspr
	sl "Ааа… Я природу люблю."
	"Странно, но сейчас она почему-то немногословна."
	me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
	sl "Скорее краеведом. Всегда интересовалась историей родной страны."
	"Это действительно похоже на неё."
	"Казалось, из всех местных обитателей она единственная, кто не скрывал в себе никаких загадок."
	th "А вдруг её тоже как-то сюда забросило, и она просто, как и я, не может никому доверять до конца?"
	"Я решил прощупать почву:"
	me "А почему ты именно в этот лагерь поехала?"
	show sl normal pioneer at center with dspr
	sl "Родителям путёвку на работе дали."
	th "Опять облом."
	me "Ну, предположим, если бы у тебя был выбор?"
	sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь кажется, что ты становишься каким-то другим человеком!"
	"Мне такого совершенно не казалось."
	me "В смысле «другим»?"
	sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
	"Сейчас она рассуждала как вожатая, и это меня насторожило."
	
	stop music fadeout 3
	
	"Я решил пока прекратить расспросы."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_dining_hall_near_sunset
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 3
	
	show sl normal pioneer at cleft
	show mt normal pioneer at cright
	with dissolve
	window show
	"Когда мы вернулись, Ольга Дмитриевна сказала Славе:"
	mt "Я же вспомнила, что карты у тебя!"
	sl "Да ничего, мы принесли."
	show mt smile pioneer at cright with dspr
	mt "Ну и отлично!"
	
	jump day2_pre_cards

label day2_cards_without_sl:
	window show
	show sl normal pioneer at right with dspr
	me "Да я и один могу сходить…"
	show mt normal pioneer at center with dspr
	mt "Ладно. Возьмёшь у меня в домике в ящике стола."
	
	stop ambience fadeout 2
	
	stop music fadeout 3
	
	"Я направился к домику Ольги Дмитриевны."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_houses_sunset
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 2
	
	window show
	th "И зачем вообще согласился?"
	th "С другой стороны, какие у меня были ещё варианты?"
	th "Ночью здесь делать особо нечего, а так хоть развлекусь немного."
	"Но в мозгу упорно крутилась мысль о том, что сейчас не самое лучшее время для развлечений."
	th "Хотя, с другой стороны, если {i}здесь{/i} есть лагерь, пионеры, то это кому-то надо?"
	th "Да даже если и не надо, то самое логичное – ответы искать именно тут, а не в лесах или полях."
	"А в данный момент {i}ответы{/i} собираются играть в карты..."
	window hide
	
	stop ambience fadeout 2
	
	$ persistent.sprite_time = "sunset"
	scene bg int_house_of_mt_sunset
	with dissolve
	
	play sound sfx_unlock_door_campus
	
	$ pause(1)
	
	play ambience ambience_int_cabin_evening fadein 2
	
	window show
	"Я открыл дверь своим ключом и зашёл."
	"К моему удивлению, карт в ящике стола не оказалось."
	"В нём нашлось всё, что угодно: ножи, вилки, чашки, тарелки, клейкая лента, ножницы, пара садовых перчаток, моток верёвки, несколько целлофановых пакетов, карандаш и пара сломанных ручек."
	"Но только не карты."
	th "Может, в шкафу?"
	"Там в основном была одежда Ольги Дмитриевны, но внимание моё привлёк маленький ящичек с замочной скважиной."
	
	play sound sfx_drawer_rattle
	
	"Я потянул, но он не открылся."
	th "Интересно, что она там прячет?"
	th "Взламывать его – явно не лучшая идея, тем более не факт, что карты там."
	
	if d1_keys:
		$ d2_gave_keys = True
		
		play sound sfx_keys_rattle
		
		"Я уже собирался уходить и даже сделал несколько шагов, как в кармане что-то зазвенело."
		"Это были ключи, которые вчера забыла Славя."
		th "А что если..."
		"Некоторое время я стоял в раздумьях, но потом уверенно подошёл к шкафу и начал прикидывать, какой ключ может подойти к замку."
		"Конечно, на успех особо рассчитывать не стоило, ведь с какой стати у Слави мог оказаться ключ от личного ящика Ольги Дмитриевны?"
		"Но к моему удивлению, замок приветливо провернулся несколько раз, и я уже собирался потянуть на себя ручку..."
		window hide
		
		play sound sfx_open_door_kick
		
		$ renpy.pause(1)
		
		window show
		"Как вдруг сзади хлопнула дверь."
		"Я подскочил на месте, резко развернулся, но в домике никого, кроме меня, не было."
		th "Наверное, ветер..."
		"Я с опаской выглянул на улицу, но и там не оказалось ни единой живой души."
		"Возможно, ничего страшного и не произошло, но мне всё равно было не по себе."
		"..."
		window hide
		
		with fade2
		
		window show
		"После тщательного осмотра соседних кустов я всё-таки решил закончить начатое и уже приготовился узнать все страшные секреты вожатой..."
		sl "Семён, что ты тут так долго?"
		show sl normal pioneer at center with dissolve
		me "А... я... да..."
		"Трясущимися руками я старался побыстрее закрыть ящик и вынуть ключ."
		"Славя подошла ближе."
		show sl smile pioneer at center with dspr
		sl "Ой, мои ключи! А я их обыскалась! Где ты..."
		me "Да вот по дороге... В кустах валялись..."
		"Слава богу, что я таки успел замести следы."
		me "Пойдём?"
		"И сейчас мне больше всего хотелось поскорее убраться отсюда и забыть о попытке бесцеремонного вторжения в чужую личную жизнь."
	
	window hide
	
	stop ambience fadeout 2
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_dining_hall_near_sunset
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 3
	
	show mt normal pioneer at right
	show sl normal pioneer at left
	with dissolve
	window show
	"Когда мы вернулись к столовой, Ольга Дмитриевна с невозмутимым видом сказала:"
	mt "Ой, извини, а карты у Слави были в домике.{w} Пока ты ходил, она сбегала."
	show sl smile2 pioneer at left with dspr
	"Я посмотрел на Славю, она виновато улыбнулась."
	th "Да ладно уж, что там, не беспокойтесь обо мне…"
	
	jump day2_pre_cards

label day2_pre_cards:
	hide mt
	hide sl
	with dissolve
	"Славя и Ольга Дмитриевна зашли внутрь."
	"Я уже собирался последовать за ними, как вдруг кто-то резко дёрнул меня за руку."
	show dv normal pioneer at center with dspr
	
	stop ambience fadeout 2
	
	play music music_list["you_won_t_let_me_down"] fadein 5
	
	"Это была Алиса."
	"Она смотрела так, что у меня мурашки побежали по спине."
	me "Тебе что-то нужно?"
	"Осторожно спросил я."
	dv "Что, тоже планируешь участвовать в этой дурацкой игре?"
	me "Ну... да, а что такого?"
	dv "Нет, ничего."
	show dv smile pioneer at center with dspr:
		linear 0.5 xalign 0.72
	"Она уже собиралась уходить, но вдруг обернулась и внимательно посмотрела на меня, улыбнувшись."
	show dv smile pioneer at right:
		linear 0.5 xalign 0.5
	dv "А в карты-то играть умеешь?"
	me "Умею немного."
	"Я никак не мог понять, что ей от меня нужно."
	dv "В дурака небось и всё?"
	th "Ты-то как будто звезда покера."
	me "Ну, в принципе, да..."
	show dv normal pioneer at center with dspr
	dv "Значит, тут у тебя шансов никаких."
	me "Почему?"
	show dv angry pioneer at center with dspr
	dv "По кочану!"
	me "То есть ты правила знаешь?"
	show dv smile pioneer at center with dspr
	dv "Конечно!"
	me "Ну, значит, у тебя будет преимущество."
	"Я не видел смысла дальше продолжать этот разговор и сделал несколько шагов по направлению к двери."
	show dv angry pioneer at center with dspr
	dv "Что ты всё уйти-то пытаешься?!"
	th "А о чём, собственно, ещё говорить?"
	show dv smile pioneer at center with dspr
	dv "Давай поспорим."
	me "Ты про что?"
	show dv normal pioneer at center with dspr
	dv "Какой же ты тупой!{w} Про карты, про что же ещё!"
	me "И каков же предмет спора?"
	show dv smile pioneer at center with dspr
	dv "Что я тебя обыграю!"
	me "Ну, это самый вероятный исход."
	"Спокойно согласился я."
	show dv normal pioneer at center with dspr
	dv "Значит, боишься?"
	me "Я не боюсь...{w} Просто не привык спорить, когда не уверен."
	dv "И рисковать ты тоже не привык."
	th "Сама наблюдательность просто-таки."
	me "Ладно, тогда я..."
	show dv angry pioneer at center with dspr
	dv "Нет уж!"
	me "Ну что ещё?"
	"Обессиленно вздохнул я."
	"Алиса начала мне надоедать своей пустой болтовнёй про какой-то бессмысленный спор."
	show dv grin pioneer at center with dspr
	dv "Если не согласишься спорить, я всем расскажу, что ты ко мне приставал!"
	me "Что?!"
	dv "Что слышал!"
	th "Да, пожалуй, она вполне может..."
	me "Но это же глупо!{w} Тебе никто не поверит – я всего неполных два дня здесь, да и к тому же..."
	show dv normal pioneer at center with dspr
	dv "Хочешь проверить?"
	me "Ну, предположим...{w} И что будет, если я выиграю?"
	show dv smile pioneer at center with dspr
	dv "Я никому ничего не скажу."
	me "А если проиграю?"
	show dv normal pioneer at center with dspr
	dv "Какой же ты тупой!{w} Расскажу, что ты ко мне приставал, говорила же уже."
	me "То есть, получается, мне нужно доказать, что я не делал того, что не делал и так?"
	dv "Считай как хочешь."
	"Передо мной встал непростой выбор."
	"С одной стороны, было глупо соглашаться – я не знал правил, да и азартные игры не были моим коньком."
	"Но с другой – она вполне могла сильно осложнить мою жизнь в лагере."
	th "Хотя можно ли ей верить?"
	th "Даже если я выиграю, не претворит ли она в жизнь свои угрозы?"
	dv "Так что решил?"
	show un normal pioneer at right with dissolve
	"Я уже было собирался ответить, как у меня из-за спины бесшумно вынырнула Лена."
	show dv angry pioneer at center with dspr
	dv "Чего тебе?"
	show un scared pioneer at right with dspr
	un "Ничего..."
	hide un with dissolve
	"Лена спешно зашла в столовую."
	show dv normal pioneer at center with dspr
	dv "Ну?"
	window hide
	
	menu:
		"Поспорить с Алисой":
			$ day2_dv_bet = 1
			$ lp_dv += 2
			$ lp_un -= 1
		"Не спорить с Алисой":
			$ day2_dv_bet = 0
			$ lp_dv -= 2
			$ lp_un += 1
	
	window show
	
	if day2_dv_bet == 1:
		th "Возможно, я ещё сто раз пожалею об этом..."
		me "Ладно, идёт!"
		show dv smile pioneer at center with dspr
		"Она улыбнулась."
		me "Только если я выиграю..."
		dv "Да-да, всё честно, без обмана!"
		"Алиса поднялась по лестнице и вошла внутрь."
		hide dv with dissolve
		th "И зачем я во всё это ввязался?"
		th "Может быть, уверился, что она в любом случае найдёт, как мне жизнь испортить?"
		th "Раз уж решила..."
	
	else:
		th "Нет, ни в какие глупые авантюры я пускаться не намерен!"
		me "Извини уж..."
		show dv angry pioneer at center with dspr
		dv "Слабак!"
		"Она фыркнула, поднялась по ступенькам и у самой двери бросила мне:"
		dv "Готовься к последствиям!"
		hide dv with dissolve
		th "Последствиям?.."
		th "Вдруг я поступил неправильно?"
		"В конце концов, она вполне может до предела осложнить мою жизнь здесь."
		"Но с другой стороны, у меня просто не было права на опрометчивые шаги."
	
	stop music fadeout 3
	
	"Я тяжело вздохнул и направился за ней в столовую."
	window hide
	
	jump day2_cards


label day2_cards:
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	play ambience ambience_medium_crowd_indoors_1 fadein 3
	
	window show
	"Внутри всё уже было готово."
	"Тут и там толпились пионеры, весело разговаривая о своём."
	"Столы сдвинули поближе к стенам, чтобы освободить место для игроков и зрителей."
	"Я осмотрелся."
	"В дальнем углу что-то происходило."
	"Подойдя ближе, я увидел большой лист ватмана с какой-то схемой."
	window hide
	
	show cg lvl_1 with dissolve
	
	window show
	"В списке участников обнаружилось и моё имя."
	me "Эй, и кто это всё придумал?"
	"Толкнул я Электроника, стоявшего рядом."
	el "Конечно же ваш покорный слуга!"
	"Он отвесил мне поклон, от чего меня аж передёрнуло."
	me "Ну, и зачем меня сюда включили?"
	"Спросил я разочарованно."
	
	if day2_dv_bet == 1:
		"Ещё пару секунд назад оставалась хоть какая-то надежда, что не придётся участвовать в этом турнире, и благодаря этому появится возможность легально улизнуть от спора с Алисой."
	else:
		"Ещё пару секунд назад оставалась хоть какая-то надежда, что не придётся участвовать в этом турнире, и благодаря этому у Алисы не будет повода отомстить мне за то, что не стал с ней спорить."
	
	th "Но теперь этой надежды больше нет."
	el "Так распорядился слепой жребий."
	th "Хороший жребий – со всеми участниками турнира я так или иначе уже успел познакомиться."
	th "А ведь, помимо них, тут ещё не один десяток пионеров!"
	"Меня охватила тревога."
	"То чувство, когда кажется, что за тобой кто-то наблюдает в пустой плотно закрытой комнате без окон."
	window hide
	
	hide cg with dissolve
	
	show el normal pioneer at center with dissolve
	window show
	me "А призы какие-нибудь будут?"
	"Спросил я его лениво."
	"Может быть, просто хотелось отвлечься бессмысленным разговором."
	show us grin pioneer at left with dissolve
	"Электроник только собрался ответить, как откуда ни возьмись появилась Ульянка и начала прыгать вокруг него."
	us "Призы-призы!"
	show us grin pioneer at right with dspr
	us "Я что-то слышала про призы!"
	me "Знаешь, какой главный принцип Олимпийских игр?"
	show us laugh pioneer at right with dspr
	us "Нет, какой?"
	me "Вот вырастешь – узнаешь!"
	show us dontlike pioneer at left with dspr
	"Она надула губки и ткнула Электроника в бок."
	us "Так призы будут?"
	show el surprise pioneer at center with dspr
	el "Ну... Я не знаю.{w} Не от меня это зависит."
	"Он обречённо развёл руками."
	th "А ведь действительно, раз уж затеяли эту дурацкую игру, то могли хотя бы шоколадными медалями озаботиться."
	hide us with dissolve
	"Ульянка неожиданно сорвалась с места и куда-то побежала."
	th "Мне бы чуток её оптимизма..."
	me "Ну так что, правила объяснишь?"
	show el normal pioneer at center with dspr
	el "Всему своё время!{w} Ещё не все собрались."
	"Я окинул столовую взглядом – Алиса, Славя, Лена, Мику и Шурик на месте."
	me "Вроде бы все..."
	show el surprise pioneer at center with dspr
	el "Как же! Жени нет!"
	"Мне показалось, что он сказал это несколько взволнованным тоном."
	me "Ну нет и нет, что теперь?"
	me "Поставь вместо неё кого-нибудь другого."
	el "Нельзя..."
	"Растягивая каждую букву, ответил он."
	"Я не стал уточнять, почему именно нельзя."
	me "Ну сходи тогда за ней, что ли, я не знаю."
	show el normal pioneer at center with dspr
	show mt normal pioneer at right with dissolve
	mt "Не надо ему никуда ходить – он организатор, ему не положено!"
	"Словно из-под земли рядом с нами возникла вожатая."
	show el upset pioneer at center with dspr
	el "Но Ольга Дмитриевна!"
	"Взмолился Электроник."
	show mt smile pioneer at right with dspr
	mt "Семён сходит.{w} Так, Семён?"
	"Она посмотрела на меня и улыбнулась."
	th "Конечно, всегда я..."
	me "А где она?"
	show mt normal pioneer at right with dspr
	mt "Наверное, в библиотеке."
	me "Ладно..."
	"Протянул я и направился к дверям."
	hide el
	hide mt
	with dissolve
	el "Только быстрее!"
	
	stop ambience fadeout 3
	
	"Донёсся мне вслед крик Электроника."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_dining_hall_away_sunset
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 2
	
	window show
	th "Скоро и ночь уже."
	"Я не спеша, стараясь убить как можно больше времени, шёл в сторону библиотеки."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg ext_square_sunset
	with dissolve
	
	play music music_list["your_bright_side"] fadein 5
	
	window show
	"Однако Женя нашлась раньше – она сидела на лавочке, уставившись в сторону безмолвного Генды."
	show mz normal glasses pioneer at center with dissolve
	me "Ты что тут делаешь?{w} Тебя все обыскались!"
	show mz angry glasses pioneer at center with dspr
	mz "Сижу, как видишь."
	"Она нахмурилась."
	me "Пойдём скорее!"
	show mz normal glasses pioneer at center with dspr
	mz "Не хочу."
	"Женя отвернулась."
	me "Почему?"
	mz "Не хочу и всё!"
	"Я сел рядом."
	me "Слушай, мне тоже не очень нравится вся эта затея, но нельзя же всех подводить."
	"Мои слова звучали так, словно их говорил кто-то другой."
	"Ещё пару дней назад мне бы и в голову не пришло сказать подобное."
	show mz bukal glasses pioneer at center with dspr
	"Женя удивлённо посмотрела на меня."
	mz "Так что, все только меня ждут?"
	th "А я тебе о чём?"
	me "Да."
	show mz angry glasses pioneer at center with dspr
	mz "Всё равно нет!"
	"Она нахмурилась и снова отвернулась."
	me "Но почему?"
	"Я всплеснул руками."
	show mz shy glasses pioneer at center with dspr
	mz "Не умею играть в карты..."
	me "Ну и что?{w} Я тоже не знаю правил."
	show mz normal glasses pioneer at center with dspr
	mz "Ну и как тогда играть?"
	me "А что, ты умеешь только то, о чём читала в книгах?"
	show mz bukal glasses pioneer at center with dspr
	mz "Конечно."
	"Она удививилась."
	me "А если ты попадёшь в Антарктиду и тебе придётся охотиться на белых медведей?"
	show mz smile glasses pioneer at center with dspr
	mz "Белые медведи не живут в Антарктиде."
	"Женя улыбнулась."
	me "Ладно, это просто пример!"
	me "В конце концов, не на корову же играем."
	"Она задумалась."
	show mz normal glasses pioneer at center with dspr
	mz "Просто не хочу подводить ребят."
	me "Да-да."
	"Саркастически согласился я."
	show mz angry glasses pioneer at center with dspr
	mz "И не подумай ничего такого!"
	"Я даже и не понял, что она имела в виду."
	
	stop music fadeout 3
	
	stop ambience fadeout 2
	
	"Очевидно, у любого человека есть свои слабые места."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	play ambience ambience_medium_crowd_indoors_1 fadein 3
	
	window show
	"Через минуту мы уже стояли в столовой."
	show el normal pioneer at center with dissolve
	"Все внимательно смотрели на Электроника."
	el "Итак..."
	"Прокашлялся он."
	el "Каждый тур состоит из одной игры."
	el "В случае ничьей будет переигровка."
	el "После этого проигравший выбывает, и начинается следующий тур."
	el "Поскольку добровольцев..."
	"Он посмотрел на меня."
	el "Поскольку участников – восемь, то и туров будет три."
	el "Всё понятно?"
	"Толпа пионеров весело загалдела."
	show us laugh pioneer at left with dissolve
	us "А призы какие, призы?"
	show sl angry pioneer at right with dissolve
	sl "Ульяна, хватит!"
	"Вперёд выскочила Славя, тщетно пытаясь поймать Ульянку."
	show us laugh pioneer at right
	show sl angry pioneer at left
	with dissolve
	us "Пока не выиграю приз, не успокоюсь!"
	"Кажется, одной этой девочки было достаточно для варп-прыжка к Альфе Центавра."
	show us laugh pioneer at left
	show sl angry pioneer at right
	with dissolve
	us "Призы-призы!"
	"Как заведённая кричала Ульяна."
	sl "Прекрати."
	"Уговаривала её Славя."
	show el shocked pioneer at center with dspr
	"А у Электроника, похоже, от всей этой беготни вокруг него уже закружилась голова."
	show us laugh pioneer at right
	show sl angry pioneer at left
	with dissolve
	me "Давайте начинать."
	"Спокойно сказал я и добавил, обращаясь к Ульянке:"
	me "А то никаких призов не получишь."
	"Такой аргумент, похоже, подействовал, и она вернулась на своё место."
	hide us with dissolve
	show sl smile pioneer at left with dspr
	"За ней последовала и Славя, бросив мне на прощание улыбку благодарности."
	hide sl with dissolve
	show el normal pioneer at center with dspr
	"Пионеры наконец угомонились."
	hide el with dissolve
	"Я подошёл к столу, за которым сидела Лена."
	show un normal pioneer at center with dissolve
	me "Не возражаете?"
	"Она подняла на меня глаза и покраснела."
	show un shy pioneer at center with dspr
	me "Не волнуйся, я тоже правил не знаю."
	th "И почему «тоже»?"
	"Я сел."
	me "Вот вышло так, что первый тур нам с тобой играть."
	un "Да."
	jump day2_cardgame

label day2_cardgame:
	"Наконец Электроник начал объяснять правила."
	
	if not persistent.CardsDemo:
		jump demo_play
	
	menu:
		"Пройти обучение":
			jump demo_play
		"Пропустить обучение":
			jump day_2_cards_continue

label demo_play:
	python:
		dialogs = {
			(3, "rival_select", "call"): "demo_play_intro",
			(3, "me_defend_1",  "call"): "demo_play_me_defend_1",
			(3, "me_select_1",  "call"): "demo_play_me_select_1",
			(3, "rival_defend", "call"): "demo_play_rival_defend",
			(2, "rival_select", "jump"): "demo_play_after_loop",
		}
		INVISIBLE = False
		VISIBLE = False
		generate_cards(dialogs)
		rival = CardGameRivalUn('un', 'Пробная игра')
	hide bg
	hide un
	with dissolve
	jump cards_gameloop

label demo_play_intro:
	show el normal pioneer at center with dissolve
	el "Посмотрите на карты внимательно."
	el "Перед вами их ровно шесть!"
	th "Надеюсь, считать здесь все умеют."
	el "Теперь можете их открыть."
	
	$ VISIBLE = True
	"Когда все посмотрели свои карты, Электроник продолжил."
	el "Правила такие же, как в покере."
	el "Думаю, все играть умеют?"
	"Я-то умел, но вот в остальных не был уверен."
	el "Сначала идёт самая старшая карта, потом пара, потом две пары, потом тройка...{w} Ну и так далее."
	el "Первым ходом вы выбираете карту, которую хотите забрать у противника."
	el "У него же в свою очередь есть возможность поменять карты местами два раза."
	el "Но можно и не менять, если собираются забрать ненужную карту."
	el "Но учтите – противник видит, какие карты вы меняете местами."
	el "Далее соперник забирает у вас одну карту."
	el "Ну, и так далее – думаю, всё понятно."
	"Мне было совершенно ничего не понятно."
	us "Эй, ты, Эйнштейн недоделанный!"
	"Послышался издалека голос Ульянки."
	us "Ничегошеньки не понятно!"
	el "По ходу разберёшься."
	hide el with dissolve
	"Электроник отошёл к столу со схемой, оставив Ульяну злиться в одиночестве."
	me "Ходи первая."
	"Я надеялся, что быстро смогу вникнуть в игру."
	"И Лена, смутившись ещё больше, чем обычно, потянулась к моим картам."
	window hide



label demo_play_me_defend_1:
	window show
	"Но на середине стола её рука застыла."
	un "Ты будешь..."
	th "Точно! Я же должен защищать свою карту!"
	th "И что там говорил Электроник..."
	"Чтобы попытаться запутать соперника, можно поменять карты местами.{w} И так два раза."
	"А можно и не менять."
	"Защищать мне эту карту или нет?"
	"К тому же я могу сразу согласиться и отдать ей карту, которую она выбрала."
	"А Лена может изменить свой выбор, взяв другую карту.{w} А может и не менять."
	window hide



label demo_play_me_select_1:
	window show
	"Понемногу всё становилось понятно!{w} Или хотя бы понятнее..."
	me "Теперь моя очередь."
	"Я могу вернуть карту, которую она забрала, или выбрать любую другую."
	window hide



label demo_play_rival_defend:
	window show
	"Лена может попробовать защитить свою карту."
	"Но если я буду внимателен, то всё равно возьму ту, что выбрал с самого начала."
	window hide



label demo_play_after_loop:
	window show
	"Получилось!"
	window hide
	jump day_2_cards_continue



label day_2_cards_continue:
	$ persistent.CardsDemo = True
	
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	window show
	"Электроник, до этого лишь молча наблюдавший за игрой, удовлетворённо кивнул."
	"Похоже, теперь мы действительно немного разобрались, что к чему."
	show el normal pioneer at center with dissolve
	el "Итак, во время игры противники три раза обмениваются картами, а потом вскрываются."
	"У меня вырвался невольный смешок от слова «вскрываются»."
	show el angry pioneer at center with dspr
	el "Что смешного?"
	me "Нет, ничего."
	"Сдерживаясь из последних сил, чтобы не прыснуть, ответил я."
	"Он пристально посмотрел на меня и продолжил."
	show el normal pioneer at center with dspr
	el "И мы смотрим, у кого лучше карты."
	hide el with dissolve
	"Электроник вернулся к своему ватману."
	window hide
	
	if persistent.CardsWon3:
		menu:
			"Играть турнир":
				jump un_play
			"Пропустить турнир (выиграть у Алисы)":
				jump dv_play_win
			"Пропустить турнир (проиграть Алисе)":
				jump dv_play_fail
			"Пропустить турнир (проиграть Ульяне)":
				jump us_play_fail
			"Пропустить турнир (проиграть Лене)":
				jump un_play_fail
	elif persistent.CardsWon2:
		menu:
			"Играть турнир":
				jump un_play
			"Пропустить турнир (проиграть Алисе)":
				jump dv_play_fail
			"Пропустить турнир (проиграть Ульяне)":
				jump us_play_fail
			"Пропустить турнир (проиграть Лене)":
				jump un_play_fail
	elif persistent.CardsWon1:
		menu:
			"Играть турнир":
				jump un_play
			"Пропустить турнир (проиграть Ульяне)":
				jump us_play_fail
			"Пропустить турнир (проиграть Лене)":
				jump un_play_fail
	elif persistent.CardsFail:
		menu:
			"Играть турнир":
				jump un_play
			"Пропустить турнир (проиграть Лене)":
				jump un_play_fail
	
	jump un_play

label un_play:
	python:
		dialogs = {
			(0, "win",  "jump"): "un_play_win",
			(0, "fail", "jump"): "un_play_fail",
			(0, "draw", "jump"): "un_play_draw",
		}
		generate_cards(dialogs)
		rival = CardGameRivalUn('un', 'Лена')
	hide bg with dissolve
	jump cards_gameloop


label un_play_fail:
	$ persistent.CardsFail = True
	$ day2_card_result = 0
	jump day2_main3

label un_play_draw:
	window show
	el "Ничья! Играйте ещё раз."
	window hide
	jump un_play

label un_play_win:
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	window show
	"Я победил!"
	"Вот уж действительно – трудно играть в игру, только что придуманную, да ещё и не тобой!"
	"Но я выиграл!"
	"Правда, радость победы немного омрачало то, что проигравшей оказалась Лена."
	"Она и без того была не особо уверена в себе."
	th "Теперь мне даже неудобно смотреть на неё."
	"Возможно, следовало всё-таки проиграть, чтобы повысить её самооценку."
	
	if day2_dv_bet == 1:
		th "Но я же поспорил с Алисой..."
	
	"Электроник тем временем с гордостью объявил, что первый тур окончен."
	window hide
	
	scene cg lvl_2_semen_win
	with dissolve
	
	window show
	"Через некоторое время на ватмане появилась схема участников второго тура."
	"Пары полуфиналистов составили: Алиса и Женя, Ульяна и..."
	"Я."
	"У меня вырвался обречённый вздох."
	window hide
	
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	show us grin pioneer at center with dissolve
	window show
	"И тут же напротив уселась Ульяна!"
	us "Хы!"
	show us laugh pioneer at center with dspr
	"С улыбкой до ушей она уставилась на меня."
	us "Как это ты Лену обыграл?"
	us "Жульничал, наверное?"
	me "Я же не ты."
	me "Просто я умею играть в карты."
	th "Пусть она хотя бы так думает."
	me "А ты как Шурика обыграла?"
	show us grin pioneer at center with dspr
	us "А..."
	"Ульянка махнула рукой, показывая, как это было просто."
	us "Пригрозила, что вступлю в его клуб."
	show us laugh pioneer at center with dspr
	"И снова широко улыбнулась."
	us "Будешь мне поддаваться?"
	me "И не надейся!"
	show us dontlike pioneer at center with dspr
	us "Ну вот..."
	show us laugh pioneer at center with dspr
	us "Тогда я сама буду выбирать, какую карту тебе отдать!"
	me "Ты правила слышала?"
	show us laugh2 pioneer at center with dspr
	us "Да плевать!"
	"Похоже, её действительно это мало волновало."
	me "Ладно, тогда и я буду отдавать тебе только те карты, что выберу сам."
	show us laugh pioneer at center with dspr
	us "Договорились!"
	"Воодушевлённый победой в первом туре, я решился на этот опасный шаг."
	"Можно было ввязаться в спор, позвать Электроника и в конце концов настоять на своём, но я почему-то был полностью уверен в исходе этой партии."
	"Да, мы нарушали правила игры, но находились с Ульянкой в равных условиях."
	"Я посмотрел на Электроника."
	el "Время начинать второй тур!"
	"Скомандовал он."
	"Я аккуратно открыл карты, стараясь не дать Ульянке заглянуть в них."
	hide us with dissolve
	window hide
	jump us_play

label us_play:
	python:
		dialogs = {
			(0, "win",  "jump"): "us_play_win",
			(0, "fail", "jump"): "us_play_fail",
			(0, "draw", "jump"): "us_play_draw",
		}
		generate_cards(dialogs)
		rival = CardGameRivalUs('us', 'Ульяна')
	hide bg with dissolve
	jump cards_gameloop

label us_play_fail:
	$ persistent.CardsWon1 = True
	$ day2_card_result = 1
	jump day2_main3

label us_play_draw:
	window show
	el "Ничья! Играйте ещё раз."
	window hide
	jump us_play

label us_play_win:
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	show us dontlike pioneer at center with dissolve
	window show
	us "Эй! Так нечестно!"
	us "Ты должен был поддаваться и проиграть!"
	"От недовольства она надула щёки и стала похожа на колобка."
	us "Давай переиграем, только ты теперь поддавайся, слышишь?!"
	"Но её слышал не только я, а весь зал."
	"И даже Электроник."
	el "Никаких переигровок!"
	"Ульяна не обратила на него ни малейшего внимания."
	show us angry pioneer at center with dspr
	us "Ты должен проиграть!"
	me "Я вообще с тобой не собираюсь играть второй раз."
	"Спокойно сказал я."
	us "Ах, так?"
	me "Да, так."
	show us grin pioneer at center with dspr
	us "Тогда я всем расскажу о том, что ты к Алисе приставал."
	"Сказала она шёпотом."
	me "Чего?!"
	"Я перегнулся через стол и грозно посмотрел на неё."
	me "Значит, подслушивала?"
	us "Не подслушивала, а просто мимо проходила."
	"В конце концов, сыграть лишний раунд – это куда лучше, чем..."
	th "А ведь она может!"
	"Я вздохнул и обратился к Электронику."
	me "Переиграем, ничего страшного."
	el "Как знаете..."
	"Он пожал плечами."
	"Итак, матч-реванш начался."
	hide us with dissolve
	window hide
	jump us2_play

label us2_play:
	python:
		dialogs = {
			(0, "win",  "jump"): "us2_play_win",
			(0, "fail", "jump"): "us2_play_fail",
			(0, "draw", "jump"): "us2_play_draw",
		}
		generate_cards(dialogs)
		rival = CardGameRivalUs('us', 'Ульяна')
	hide bg with dissolve
	jump cards_gameloop

label us2_play_fail:
	$ persistent.CardsWon1 = True
	$ day2_card_result = 1
	jump day2_main3

label us2_play_draw:
	window show
	el "Ничья! Играйте ещё раз."
	window hide
	jump us2_play

label us2_play_win:
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	show us dontlike pioneer at center with dissolve
	window show
	me "Проще простого."
	"Сказал я и вальяжно развалился на стуле."
	us "Так нечестно!"
	th "Надеюсь, она не потребует ещё одной переигровки!"
	me "Почему же нечестно?"
	"Усмехнулся я."
	us "Ладно..."
	"Обиженно сказала Ульяна и встала из-за стола."
	hide us with dissolve
	"Я внимательно посмотрел на схему турнира, пытаясь понять, кто же мне достался в соперники по финалу."
	show dv normal pioneer at center with dissolve
	"В ту же секунду ко мне за стол села Алиса."
	"Я глупо и неестественно улыбнулся."
	th "Как будто боюсь её!"
	me "Поздравляю с победой."
	if day2_dv_bet == 0:
		show dv angry pioneer at center with dspr
		dv "Ты ещё пожалеешь, что струсил."
		th "Да я уже жалею..."
		"И не о том, что струсил – не надо вообще было участвовать в этой дурацкой игре."
	else:
		dv "Рассчитываешь выиграть?"
		me "Рассчитываю, что ты сдержишь своё обещание."
	show dv smile pioneer at center with dspr
	dv "Ладно, погнали!"
	hide dv with dissolve
	window hide
	jump dv_play

label dv_play:
	python:
		dialogs = {
			(0, "win",  "jump"): "dv_play_win",
			(0, "fail", "jump"): "dv_play_fail",
			(0, "draw", "jump"): "dv_play_draw",
		}
		generate_cards(dialogs)
		rival = CardGameRivalDv('dv', 'Алиса')
	hide bg with dissolve
	jump cards_gameloop

label dv_play_draw:
	window show
	el "Ничья! Играйте ещё раз."
	window hide
	jump dv_play

label dv_play_fail:
	$ persistent.CardsWon2 = True
	$ day2_card_result = 2
	jump day2_main3

label dv_play_win:
	$ persistent.CardsWon3 = True
	$ day2_card_result = 3
	jump day2_main3




label day2_main3:
	$ persistent.sprite_time = "sunset"
	scene bg int_dining_hall_sunset
	with dissolve
	
	window show
	
	if day2_card_result == 0:
		scene cg lvl_2_lena_win with dissolve
		"Как обидно всё-таки проигрывать..."
	
	if day2_card_result == 1:
		"Хотя бы один раунд я выиграл."
	
	if day2_card_result == 2:
		"Двачевской я проиграл."
		th "И это ой как нехорошо."
		th "Можно только предполагать, что она завтра выкинет."
		th "Опозорит меня на линейке (если я её, конечно, не просплю), расскажет Ольге Дмитриевне."
		th "Просто пустит слухи по лагерю."
		th "Причём самое страшное, что поверят наверняка ей, а не мне."
		"Я даже не знал точно почему, но был в этом уверен на 100%%."
	
	if day2_card_result == 3:
		if day2_dv_bet == 1:
			$ lp_dv += 2
			jump day2_dv
		else:
			scene bg int_dining_hall_sunset
			th "И неважно, что я не стал спорить с Алисой, главное – выиграл."
			th "А то, зная её, можно только предполагать, что бы она завтра выкинула."
			th "Опозорила бы меня на линейке, рассказала бы Ольге Дмитриевне."
			th "Просто пустила бы слухи по лагерю."
			th "Причём самое страшное, что поверили бы наверняка ей, а не мне.{w} Я даже не знаю точно почему, но уверен в этом на 100%%."
	
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_dining_hall_away_night with dissolve
	
	play ambience ambience_camp_center_night fadein 2
	
	$ night_time()
	
	window show
	"Я вышел из столовой."
	"Спать ложиться было ещё рано, так что небольшая прогулка показалась отличным вариантом."
	th "Куда же направиться?"
	window hide
	
	stop ambience fadeout 3
	
	$ disable_all_zones()
	$ set_zone("medic_house",   "day2_aidpost_eve")
	$ set_zone("square",		"day2_square_eve")
	$ set_zone("beach",		 "day2_beach_eve")
	$ set_zone("boat_station",  "day2_dock_eve")
	$ set_zone("camp_entrance", "day2_busstop_eve")
	$ set_zone("estrade",	   "day2_stage_eve")
	$ set_zone("sport_area",	"day2_football_eve")
	$ show_map()

label day2_aidpost_eve:
	$ persistent.sprite_time = "night"
	scene bg ext_aidpost_night
	with dissolve
	
	window show
	"Я просто шёл вперёд, не особо разбирая направления, и оказался у медпункта."
	"Если мне и была нужна скорая помощь, то скорее психологическая, а получать её у местной медсестры в мои планы никак не входило."
	"..."
	window hide
	
	jump day2_main4

label day2_square_eve:
	$ persistent.sprite_time = "night"
	scene bg ext_square_night with dissolve
	
	window show
	"Я вышел на площадь и сел на скамейку."
	"Просто таращиться на памятник Генде казалось мне сейчас хорошим занятием."
	"..."
	window hide
	
	jump day2_main4

label day2_beach_eve:
	stop ambience fadeout 2
	
	$ persistent.sprite_time = "night"
	scene bg ext_beach_night with dissolve
	
	play ambience ambience_lake_shore_night fadein 2
	
	window show
	"Я вышел на пляж."
	"Настроение было паршивым, и купаться совсем не хотелось, однако я подошёл к воде и опустил в неё руку."
	"Вода была тёплая."
	"Видимо, за день она так нагрелась, что к вечеру ещё не успела остыть."
	th "Что же, может, приду ещё, искупаюсь…"
	"..."
	window hide
	
	stop ambience fadeout 2
	
	jump day2_main4

label day2_dock_eve:
	$ persistent.sprite_time = "night"
	scene bg ext_boathouse_night
	with dissolve
	
	window show
	"Я решил пойти на пристань."
	"Солнце ещё не полностью скрылось за горизонт, и река вдалеке красиво окрашивалась во все оттенки красного, жёлтого и оранжевого."
	"Казалось, что вода там горит ярким пламенем, но чем дольше я стоял, тем пожар становился слабее и в конце концов совсем погас."
	"..."
	window hide
	
	jump day2_main4

label day2_busstop_eve:
	$ persistent.sprite_time = "night"
	scene bg ext_square_night
	with dissolve
	
	play ambience ambience_camp_center_night fadein 3
	
	window show
	"События прошедшего дня всё ещё ярко мелькали у меня в голове: чёртов никому не нужный обходной, глупый турнир…"
	"Сейчас мне не хотелось ничего делать, ни с кем разговаривать.{w} И даже разбираться со своей непростой ситуацией не было никакого желания."
	"Я вышел на площадь, уселся на лавочку и уставился на памятник Генде."
	"..."
	window hide
	
	with fade2
	
	window show
	"Не знаю, сколько я так сидел, но из раздумий меня вывело назойливое стрекотание сверчков."
	
	stop ambience fadeout 2
	
	"Я встал и бездумно направился куда глаза глядят."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_no_bus_night
	with dissolve
	
	play ambience ambience_camp_entrance_night fadein 3
	
	window show
	th "Автобусная остановка..."
	"По какому-то непонятному стечению обстоятельств второй день подряд вечером я попадаю именно сюда."
	th "Может быть, подсознательно надеюсь, что здесь меня будет ждать автобус, который увезёт обратно в привычный мир?"
	th "Вряд ли."
	th "С другой стороны, чем чёрт не шутит..."
	"Уже стемнело."
	"Я просто стоял там и смотрел в ночное небо."
	"Астрономия никогда меня не привлекала настолько сильно, как астронавтика."
	"Мне было интереснее смотреть на рисунки далёких созвездий, туманностей и галактик, выполненные художниками, чем разбираться в астрономических единицах, угловых скоростях и массах небесных светил."
	"Конечно, я бы смог найти Большую Медведицу."
	"Но потеряйся я в тайге, и единственным моим спасением стало бы лишь знание того, что мох растёт с северной стороны дерева."
	"Впрочем, не уверен, что и это бы мне помогло…"
	
	if day2_cards_with_sl == 1:
		$ lp_sl += 1
		jump day2_sl
	
	stop ambience fadeout 2
	
	"Постояв ещё пару минут, я направился назад в лагерь."
	"..."
	window hide
	
	jump day2_main4

label day2_stage_eve:
	if day2_card_result == 1:
		$ lp_us += 1
		jump day2_us
	
	scene black
	with dissolve
	
	window show
	"Я решил пойти на север (по крайней мере туда, где он по моим представлениям находился)."
	window hide
	
	scene bg ext_stage_big_night
	with dissolve
	
	window show
	"Спустя пару минут вдалеке показалась концертная площадка: несколько рядов деревянных скамеек и деревянная же эстрада."
	"Я поднялся на сцену."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_stage_normal_night
	with dissolve
	
	window show
	"Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
	"Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьёт слепящий свет прожекторов."
	"Вообразив, что в руках гитара, я попытался исполнить длинное красивое соло."
	"Наверное, со стороны это смотрелось смешно – парень на сцене размахивает руками, бегает туда-сюда, корчится и кривляется, при этом строя глупые гримасы."
	th "Хорошо бы меня здесь никто не увидел!"
	"С этими мыслями я спрыгнул со сцены и поспешно зашагал прочь."
	"..."
	window hide
	
	jump day2_main4

label day2_football_eve:
	if day2_card_result == 0 and day2_dv_bet == 0:
		$ lp_un += 1
		jump day2_un
	
	$ persistent.sprite_time = "night"
	scene bg ext_playground_night
	with dissolve
	
	window hide
	"Для футбола время было позднее, поэтому ни на поле, ни на спортивной площадке никого не оказалось."
	"Я постоял там пару минут, тщетно вслушиваясь в тишину, и пошёл назад."
	"..."
	window show
	
	jump day2_main4

label day2_dv:
	scene cg lvl_4_semen_win
	with dissolve
	
	play music music_list["always_ready"] fadein 5
	
	window show
	"Ура! Я выиграл! Пусть теперь Алиса знает, что со мной лучше не связываться!"
	if day2_dv_bet == 1:
		th "Значит, не зря я всё же с ней поспорил!"
	"Теперь оставалось надеяться, что она не станет распускать ложные слухи от обиды на поражение."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_beach_night
	with dissolve
	
	$ night_time()
	
	stop ambience fadeout 2
	
	window show
	"Вдруг захотелось сделать себе подарок в честь победы и пойти искупаться."
	"По правде говоря, я и плавать-то толком не умел, но возможность окунуться в прохладную воду на пляже при луне была слишком заманчивой."
	"Тем более после вчерашнего дня, проведённого в зимней одежде, меня можно было выжимать от пота."
	"Вечером здесь никого не должно было быть, поэтому я разделся до трусов и вошёл в воду."
	th "Знал бы заранее, захватил бы из дома плавки."
	
	stop music fadeout 3
	
	play ambience ambience_lake_shore_night fadein 2
	
	"Обычно мне вполне хватало проплыть 15-20 метров, но в этот раз эйфория от победы на турнире подтолкнула меня побить свой рекорд."
	"Я плыл медленно и размеренно, следил за каждым движением рук и ног, за каждым вдохом и выдохом."
	window hide
	
	stop ambience fadeout 2
	
	play music music_list["that_s_our_madhouse"] fadein 3
	
	scene bg ext_beach_night:
		linear 0.05 pos (-5, -5)
		linear 0.05 pos ( 0,  0)
		linear 0.05 pos ( 5,  5)
		linear 0.05 pos ( 0,  5)
		linear 0.05 pos ( 5,  0)
		linear 0.05 pos ( 0,  0)
		repeat
	
	window hide
	
	play sound sfx_shoulder_dive_water
	
	show blink
	
	$ renpy.pause(1)
	
	window show
	"И тут бах!"
	"Удар по спине отправил меня под воду."
	"Я начал захлёбываться, но усилием воли взял себя в руки и вынырнул, схватившись за буёк."
	window hide
	
	scene cg d2_water_dan
	show unblink
	with dissolve
	
	play sound sfx_water_emerge
	
	$ pause(1)
	
	window show
	"Я обернулся и увидел Алису, плывущую за мной."
	me "Ты что творишь?!"
	dv "Как что? Приветствую победителя."
	me "А если бы я утонул?!"
	dv "Ну, я бы тебя спасла."
	me "Ага, как же…"
	"Находиться здесь было попросту опасно – утопит ещё, не ровен час – поэтому, вложив все силы в последний рывок, я поплыл к берегу."
	window hide
	
	stop music fadeout 3
	
	$ persistent.sprite_time = "night"
	scene bg ext_beach_night
	with dissolve
	
	play ambience ambience_lake_shore_night fadein 2
	
	window show
	"Мокрый песок покрывал меня с ног до головы, а дыхание постепенно восстанавливалось."
	show dv normal swim at center with dissolve
	"Через некоторое время из воды вышла и Алиса."
	dv "А ты неплохо плаваешь!"
	th "Не сказал бы."
	me "Ага, и ты тоже."
	show dv smile swim at center with dspr
	dv "Ну, я-то понятно!"
	"Я промолчал."
	dv "Ты сегодня у меня уже два раза выиграл.{w} Значит, тебе прощаются те два долга."
	th "Какие долги, о чём она вообще?"
	"Алиса, похоже, не совсем здраво воспринимала действительность."
	me "Радушно благодарю…"
	"Съязвил я."
	dv "Знаешь, а ты не такой уж и неудачник…"
	window hide
	
	scene cg d2_2ch_beach with dissolve:
		ypos -1920
		linear 10.0 ypos 0
		linear 2.0  ypos -250
	
	window show
	"Алиса была одета в купальник, который хорошо подчёркивал все прелести её фигуры."
	"Да, при всех минусах характера Двачевской этот плюс у неё не отнимешь."
	me "А с чего это вдруг я неудачник?"
	"Она хитро улыбнулась."
	dv "А что, разве не так?"
	me "Нет конечно!"
	dv "И чем докажешь?"
	me "Не собираюсь я тебе ничего доказывать!"
	dv "Ах, вот так, значит?"
	"Сказала она беззлобно."
	me "Да, вот так..."
	"Наступило ожидаемое молчание."
	"Тихий ночной ветерок лениво играл волнами, то накатывая их на берег, то забирая назад, чтобы собраться с силами и перегруппироваться."
	"Алиса всё так же смотрела словно сквозь меня, казалось забыв о том, что я всё ещё здесь."
	me "Эй, Земля вызывает Алису!"
	"В её взгляд вмиг вернулась осмысленность."
	dv "Ладно, бывай."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_beach_night
	with dissolve
	
	window show
	"Она забрала лежащую рядом одежду и ушла."
	"..."
	window hide
	
	with fade2
	
	window show
	"Было уже поздно, но я решил ещё некоторое время полежать и посмотреть на звёзды."
	window hide
	
	scene stars
	with dissolve
	
	window show
	"В конце концов, раньше мне редко представлялась такая возможность."
	"Или просто я сам редко себе её создавал."
	th "Ведь если подумать, свет от далёких звезд долетает до нас за миллионы лет…"
	th "Вот сейчас я вижу звезду, потому что она светила тогда, а для неё это {i}тогда{/i} – далёкое прошлое."
	th "И сейчас она, возможно, уже взорвалась…"
	
	stop ambience fadeout 0
	
	play music music_list["that_s_our_madhouse"] fadein 1
	
	th "Стоп!{w} Она же и мою одежду забрала!"
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_beach_night
	with dissolve
	
	window show
	"Я вскочил и начал осматривать пляж."
	"Действительно, Алиса унесла и мою пионерскую форму."
	th "Чёрт возьми!"
	"А ведь я только начинал думать, что она, может быть, не такая уж плохая…"
	th "Надо срочно что-то придумать."
	th "Конечно, можно пожаловаться Ольге Дмитриевне, но вернуться к ней в одних мокрых трусах…"
	"В каком домике живёт Алиса, я не знал."
	th "Стучаться во все подряд тоже не вариант!"
	th "Может быть, зайти к Славе?"
	th "Да, точно, ночью в одних трусах…{w} Только розы в зубах не хватает!"
	"С какой стороны ни посмотри, я попал, причем попал серьёзно!"
	"Но делать что-то надо было в любом случае."
	"К счастью, не так много времени прошло, и я ещё успевал её догнать..."
	
	stop music fadeout 3
	
	"... бегом!"
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_square_night
	with dissolve
	
	play ambience ambience_camp_center_night fadein 3
	
	window show
	"В мгновение ока я оказался на площади."
	show dv normal pioneer2 at center with dissolve
	"К моему огромному удивлению, Алиса сидела на лавочке и явно скучала."
	"Она уже успела переодеться."
	me "Отдай!"
	show dv guilty pioneer2 at center with dspr
	dv "Да бери…"
	"Ответила она каким-то виноватым тоном и протянула мне мою форму."
	me "…"
	show dv shy pioneer2 at center with dspr
	dv "Только не думай, что я это специально тут тебя ждала и всё такое..."
	hide dv with dissolve
	"Алиса развернулась и не спеша пошла в сторону домиков."
	"Я остался стоять как вкопанный."
	"Такой финт ушами был выше моего понимания."
	th "Возможно, у неё проснулась совесть…"
	th "Хотя какое там…"
	th "В любом случае с ней нужно быть поосторожнее, и события сегодняшнего вечера ничего не меняют."
	
	stop ambience fadeout 2
	
	"Я направился к домику Ольги Дмитриевны."
	window hide
	
	jump day2_main4

label day2_sl:
	"Я уже собирался возвращаться в лагерь, как вдруг услышал какой-то шум за воротами."
	th "И кого ещё принесло?.."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_clubs_night
	with dissolve
	
	window show
	"Возле здания кружков мне почудилось, что кто-то идёт по тропинке, уходящей в лес."
	"Было так темно, что, кроме размытого силуэта, разглядеть ничего не удалось."
	"Мне стало интересно, кто же это ночью ещё не спит."
	th "Пионер, нарушающий режим? Ай-яй-яй!"
	
	stop ambience fadeout 2
	
	"Я быстро, но по возможности осторожно направился за таинственной тенью."
	window hide
	
	play ambience ambience_forest_night fadein 3
	
	$ persistent.sprite_time = "night"
	scene bg ext_path_night
	with dissolve
	
	window show
	"Тропинки сменяли друг друга, и вскоре я оказался в чаще, окончательно потеряв из виду незнакомца."
	th "Может, стоило повернуть назад?"
	"Деревья расступились, и передо мной открылся чудесный вид на небольшое лесное озеро."
	window hide
	
	scene cg d2_slavya_forest
	with dissolve
	
	play music music_list["forest_maiden"] fadein 5
	
	"И тут я увидел Славю…{w} Она шла по берегу вприпрыжку, даже не шла – порхала, на ходу стягивая пионерский галстук и расправляя рубашку."
	"Всё это зрелище показалось даже более фантастическим, чем само моё пребывание в этом лагере."
	"Славя виделась мне каким-то духом леса, может быть, нимфой."
	"Она настолько сливалась с природой, что уже становилась не просто человеком, а чем-то вроде древнего божества."
	"Я вспомнил все теологические теории, о которых читал когда-то."
	"Эта ситуация больше всего напоминала пантеизм – растворение Бога в природе, во всём сущем."
	th "Вдруг это не какие-то инопланетяне или провал во времени, а божественное провидение закинуло меня сюда."
	th "Действительно, Славя говорила, что любит природу."
	th "Получается, и в ней скрыта какая-то загадка?"
	window hide
	
	scene bg ext_path_night
	with dissolve
	
	window show
	"Славя зашла в воду."
	"Было стыдно подглядывать, но я просто не мог отвести взгляд."
	"Яркий лунный свет отражался от её мокрой кожи, делая Славю похожей на древнегреческую статую.{w} Может быть, Венеру Милосскую?"
	"Это зрелище было настолько прекрасным, что в нём как будто не осталось места ни для чего мирского, плотского – только возвышенное восхищение истинной красотой."
	"Я любовался Славей и в тот миг забыл обо всём прочем."
	"Возможно, это совсем не ад, а рай?.."
	"Под ногой предательски хрустнула ветка, Славя обернулась, но в ночи не было никакой возможности разглядеть меня.{w} По крайней мере так казалось."
	
	$ persistent.sprite_time = "night"
	scene bg ext_path_night
	with dissolve
	
	window show
	"Она быстро вылезла из озера, наскоро оделась и скрылась в чаще."
	"Я тихо последовал за ней."
	"Славя неслышно плыла между деревьев, выбирая самые удобные тропки и изящно обходя поваленные стволы, ямки и коряги."
	"Мне составляло большого труда не отставать, к тому же я совершенно не хотел, чтобы меня обнаружили – во-первых, подглядывать просто нехорошо, во-вторых, ещё неизвестно, что именно она тут делала."
	"Хотя почему-то казалось, что ничего такого – дело даже не в моём попадании в этот мир."
	"Просто – {i}ничего такого{/i}.{w} Ничего, за чем бы стоило подглядывать."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_square_night
	with dissolve
	
	window show
	"Наконец мы вышли на площадь."
	"Славя остановилась и обернулась в мою сторону."
	show sl normal pioneer far at center with dissolve
	sl "Думаешь, я тебя не заметила?"
	"Я немного растерялся, но постарался сохранить хотя бы видимость спокойствия."
	me "И давно?"
	show sl normal pioneer at center with dissolve
	sl "Не знаю..."
	"Славя подошла ближе."
	show sl smile pioneer at center with dspr
	sl "Может быть, минут пять."
	me "То есть и там, на озере?.."
	show sl surprise pioneer at center with dspr
	sl "На каком озере?"
	me "Ну..."
	"Славя выглядела искренне удивлённой, поэтому я никак не мог понять – она просто притворяется и делает вид, что ничего не произошло, или..."
	me "Ладно, проехали."
	"Я решил поступить галантно (насколько это вообще было возможно в таких обстоятельствах) и промолчать."
	show sl happy pioneer at center with dspr
	sl "Хорошо."
	"Неожиданно легко согласилась она."
	sl "Какая сегодня ночь замечательная!"
	"Славя села на скамейку и подняла глаза на небо."
	me "Наверное, тут часто бывают такие ночи."
	show sl smile2 pioneer at center with dspr
	sl "Ну, наверное..."
	me "Почему так неуверенно?"
	sl "Нет, просто задумалась."
	me "О чём?"
	show sl normal pioneer at center with dspr
	"Она внимательно посмотрела на меня, словно что-то искала у меня на лице, но затем вновь вернулась к созерцанию звёзд."
	sl "Просто иногда по ночам такое настроение бывает...{w} Днём – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
	sl "Если бы не сверчки и ночные птицы, то кажется, как будто остался наедине с космосом."
	"Почему-то мне казалось, что Славя не та, кто будет рассуждать о подобных материях."
	me "Да для меня тут даже слишком спокойно."
	show sl serious pioneer at center with dspr
	sl "Правда?"
	me "Да, правда, а что такого?"
	show sl smile pioneer at center with dspr
	sl "Ничего..."
	show sl normal pioneer at center with dspr
	sl "Ладно!"
	"Она резким движением встала и поправила юбку."
	show sl smile pioneer at center with dspr
	sl "Уже и спать пора!"
	me "Спокойной ночи!"
	hide sl with dissolve
	"Я проводил её взглядом."
	"Возможно, наш разговор и был ни о чём, но для меня он казался наполненным каким-то особенным, таинственным смыслом, который мог родиться только {i}здесь{/i}, только вместе со Славей."
	"Получается, даже в моём положении необходимы подобные минуты тишины и покоя, почти что единения со Вселенной."
	"Просто жизненно необходимы – особенно сейчас!"
	"..."
	window hide
	
	with fade2
	
	window show
	"..."
	
	stop ambience fadeout 2
	
	stop music fadeout 3
	
	"Не знаю, сколько я так сидел, но вскоре меня начало клонить в сон."
	window hide
	
	jump day2_main4

label day2_un:
	$ day2_un = 1
	
	$ persistent.sprite_time = "night"
	scene bg ext_playground_night
	with dissolve
	
	play ambience ambience_camp_center_night fadein 3
	
	window show
	"Мне хотелось уйти подальше ото всех."
	th "Проиграть в первом же раунде!.."
	"Нет, такого я сам себе простить не мог."
	"Тогда мне показалось, что самым подходящим местом уединения будет спортивная площадка."
	th "И правда, кому вечером взбредёт в голову играть в футбол?"
	"Я присел на лавочку рядом с полем и задумался о случившемся."
	"Вдруг со стороны волейбольной площадки донеслись звуки, похожие то ли на скрип, то ли на свист."
	
	play sound sfx_lena_plays_tennis_fail
	
	"Присмотревшись, я увидел, что кто-то отчаянно машет рукой."
	th "И кому он там семафорит?.."
	"К моему удивлению, это оказалась Лена."
	"Она подкидывала воланчик и пыталась попасть по нему ракеткой."
	"Однако выходило это у неё паршиво, откровенно говоря."
	"Я некоторое время просто смотрел, но потом всё же решился подойти."
	"Обойдя волейбольную площадку, я зашёл внутрь так, чтобы она меня видела."
	"Лена пугалась даже малейшего шороха, так что не стоило повторять прошлых ошибок."
	show un normal sport at center with dissolve
	me "Привет!"
	"Она посмотрела на меня и тут же спрятала за спину ракетку и воланчик."
	me "Бадминтон любишь?"
	un "Ну, не то чтобы…"
	me "Вижу, у тебя не очень получается.{w} Может, тебя научить?"
	"По правде говоря, я и сам толком не умел, но, как и всем детям, в своё время мне приходилось пару раз играть."
	me "Давай покажу."
	show un shy sport at center with dspr
	un "Спасибо."
	"Она покраснела."
	un "Хочу попасть в команду по бадминтону, но у меня не очень выходит…"
	un "Я бы сегодня и не пришла, но…"
	show un smile sport at center with dspr
	"Она подняла глаза на меня."
	un "Мне никогда в карты не везло, а сегодня выиграла и подумала, что, может, и с этим получится…"
	"Да уж, после таких слов я понял, что поражение от Лены – это вдвойне обидно."
	me "Никогда бы не подумал, что ты увлекаешься спортом."
	show un shy sport at center with dspr
	"Она опять покраснела."
	me "Ой, прости…{w} Давай, сейчас покажу!"
	"Я взял ракетку, подбросил воланчик и…"
	
	play sound sfx_tennis_serve_1
	
	show un surprise sport at center with dspr
	"Ударил с такой силой, что он перелетел ограду и скрылся где-то между деревьями."
	me "Ой, прости!"
	"Я не ожидал от себя такой силы."
	show un normal sport at center with dspr
	un "Ничего…{w} Правда, это был последний…"
	me "Последний? Пойдём тогда поищем его!"
	un "Нет, не стоит…{w} Там в лесу…"
	me "Кто, леший?"
	"Я засмеялся."
	un "Может быть…"
	"Я-то шутил, а вот она, похоже, нет."
	me "Да никого там нет, не бойся, пойдём!"
	un "Ну, если только с тобой…"
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_path_night
	with dissolve
	
	window show
	"Мы вышли с площадки, и я начал осматривать деревья."
	
	play sound sfx_owl_far
	
	"Вдруг тишину ночи нарушило уханье совы."
	window hide
	
	stop ambience fadeout 2
	
	scene cg d2_sovenok
	with dissolve
	
	play music music_list["confession_oboe"] fadein 5
	
	window show
	"Лена, видимо, так испугалась, что схватилась за меня, обвив руками."
	"От таких крепких объятий я смутился."
	"Настолько близко чувствовать тело девочки, её тепло!"
	"Меня обуяла нежность."
	"Хотелось защищать её, не давать в обиду никому, пусть это будет даже всего лишь сова или какая другая ночная птица."
	"Осталось лишь одно желание – чтобы она не отпускала."
	"Впрочем, хорошее имеет свойство заканчиваться."
	"Через некоторое время я понял, что ухает – совёнок, сидящий на ветке рядом с нами."
	"Он крепко держал наш воланчик."
	me "Это вот его ты боялась?"
	un "Угу…"
	me "Посмотри, он совсем не страшный."
	"Лена выглянула у меня из-за спины."
	un "Не страшный…"
	me "Сейчас, подожди."
	window hide
	
	stop music fadeout 3
	
	$ persistent.sprite_time = "night"
	scene bg ext_path_night
	with dissolve
	
	play ambience ambience_camp_center_night fadein 3
	
	show un shy sport at center with dissolve
	window show
	"Я мягко освободился от её объятий и подошёл к совёнку."
	"Сначала казалось, что он испугается и улетит, выпустив воланчик."
	"Однако совёнок, похоже, и не собирался двигаться с места."
	"Мне удалось схватить воланчик и аккуратно отобрать его у птицы."
	me "Смотри, он совсем ручной!{w} Хочешь его погладить?"
	un "Может, в другой раз?.."
	"Я протянул воланчик Лене."
	show un smile sport at center with dspr
	un "Спасибо тебе."
	"Она еле заметно улыбнулась."
	show un normal sport at center with dspr
	un "Мне пора."
	me "Успехов в бадминтоне."
	show un smile sport at center with dspr
	"Лена вновь улыбнулась и побежала в сторону лагеря."
	hide un with dissolve
	th "Какая она всё же милая!"
	
	stop ambience fadeout 2
	
	"..."
	window hide
	
	jump day2_main4

label day2_us:
	scene black
	with dissolve
	
	window show
	"События прошедшего дня всё ещё ярко мелькали у меня в голове: чёртов никому не нужный обходной, глупый турнир."
	"Сегодня мне не хотелось больше ничего делать, ни с кем разговаривать.{w} А уж разбираться со своей непростой ситуацией и подавно не было никакого желания."
	"Я пошёл на север.{w} По крайней мере в ту сторону, где он по моим прикидкам был."
	"Моя традиция с молодости – ходить на север."
	"Я больше любил эту часть своего родного города, чем южные районы."
	"Также меня никогда не прельщал отдых на черноморских курортах – бескрайние леса и поля были мне куда милее, чем пляжи и барханы."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_stage_big_night
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 2
	
	window show
	"Спустя пару минут вдалеке показалась концертная площадка: несколько рядов деревянных скамеек и деревянная же эстрада."
	"Я поднялся на сцену."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg ext_stage_normal_night
	with dissolve
	
	window show
	"Там было довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
	"Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьёт слепящий свет прожекторов."
	"Вообразив, что в руках гитара, я попытался исполнить длинное красивое соло."
	"Наверное, со стороны это смотрелось смешно – парень на сцене размахивает руками, бегает туда-сюда, корчится и кривляется, при этом строя глупые гримасы."
	th "Хорошо бы меня здесь никто не увидел!"
	
	stop ambience fadeout 2
	
	play music music_list["glimmering_coals"] fadein 5
	
	us "Ого!"
	"Послышалось откуда-то сверху."
	show us laugh pioneer with dissolve:
		xalign 0.5
		yanchor 1.0
		rotate 180
	"Я поднял глаза и увидел Ульянку, свесившуюся с балки под потолком сцены."
	us "Что это мы тут делаем?"
	me "Да я просто…"
	"Оправдываться явно бесполезно."
	me "Сама всё видела."
	"Расстроенно сказал я и отвернулся."
	show us laugh2 pioneer with dspr:
		xalign 0.5
		yanchor 1.0
		rotate 180
	us "В тебе, я погляжу, умирает талант великого гитариста."
	"Я ничего не ответил."
	show us smile pioneer with dspr:
		xalign 0.5
		yanchor 1.0
		rotate 180
	us "Ну, ладно тебе, не дуйся, смотрелось забавно!"
	"Она захихикала."
	me "Забавно, говоришь?"
	"Фыркнул я."
	us "Да."
	"Спокойно ответила Ульяна."
	show us grin pioneer with dspr:
		xalign 0.5
		yanchor 1.0
		rotate 180
	us "Подойди-ка сюда."
	me "Куда?"
	us "Ко мне!"
	me "Я туда лезть не собираюсь, не думай даже!"
	"Не то чтобы я боялся высоты, но какой смысл забираться на эту балку?"
	us "Да нет! Просто сюда."
	"Я почувствовал что-то недоброе, но всё же медленно направился в её сторону."
	"Когда я оказался точно под Ульянкой, она крикнула:"
	us "Лови!"
	window hide
	
	scene cg d2_ussr_falling
	with dissolve
	
	window show
	"И прыгнула…"
	"За мгновение у меня в голове пронеслись тысячи мыслей."
	th "Как я её поймаю? А надо ли вообще ловить? А что, если она разобьётся? А что, если она мне что-то сломает? Да и почему именно я?!"
	th "Она сама виновата – нечего дурью маяться!"
	"Удивительно, сколько мыслей приходят и уходят за долю секунды."
	"А ведь иногда, чтобы родить хотя бы одну, уходят годы."
	"В конце концов, логика и инстинкт самосохранения выиграли, и я отошёл в сторону."
	window hide
	
	stop music fadeout 3
	
	$ persistent.sprite_time = "night"
	scene bg ext_stage_normal_night
	with dissolve
	
	play ambience ambience_camp_center_evening fadein 2
	
	play sound sfx_uliana_jumps_down
	
	show us upset pioneer at center with dissolve
	
	$ renpy.pause(1)
	
	show us sad pioneer at center with dspr
	window show
	"Ульянка мягко приземлилась, перекувыркнулась, мгновенно вскочила на ноги и обиженно посмотрела на меня."
	us "Почему не поймал?"
	me "Ну ты же не разбилась..."
	"Ответил я, отведя взгляд."
	show us shy2 pioneer at center with dspr
	us "А если бы разбилась?"
	me "Не разбилась!{w} Да и что это вообще такое? Дешёвых фильмов обсмотрелась?"
	show us grin pioneer at center with dspr
	us "А что, волнуешься за меня?"
	"Она ехидно ухмыльнулась."
	me "В такой ситуации… Ну, естественно, волнуюсь."
	show us surp3 pioneer at center with dspr
	us "Я польщена."
	me "Эй, ты не думай…"
	show us laugh pioneer at center with dspr
	us "Ладно-ладно. Прощаю тебе карты."
	me "А вот я тебе это прощать не…"
	hide us with dissolve
	"Я не успел закончить – Ульянка спрыгнула со сцены и скрылась в ночи."
	th "Очередная идиотская выходка этой глупой девчонки."
	th "Да, конечно, я испугался за неё."
	th "Да и будь любой другой на её месте…"
	"В очередной раз мысленно обругав Ульяну, я направился в сторону своего домика."
	window hide
	
	stop ambience fadeout 2
	
	jump day2_main4

label day2_main4:
	$ persistent.sprite_time = "night"
	scene bg ext_house_of_mt_night_without_light
	with dissolve
	
	play music music_list["a_promise_from_distant_days"] fadein 5
	
	window show
	"Впервые за день меня накрыла дикая усталость."
	"Свет в окне не горел, значит, Ольга Дмитриевна уже спала."
	th "Странно, вчера она меня дождалась."
	window hide
	
	$ persistent.sprite_time = "night"
	scene bg int_house_of_mt_night2
	with dissolve
	
	window show
	"Я зашёл, тихо разделся и лёг на кровать."
	th "Если поразмыслить, моя ситуация за сегодня совершенно не прояснилась."
	th "В сущности, я весь день занимался бесполезными вещами; в реальном мире мне бы и в голову не пришло тратить своё время на что-то подобное."
	th "Хотя как раз там у меня этого времени было хоть отбавляй."
	th "А сколько его тут – совершенно неизвестно."
	th "Может быть, целая вечность, а может, всего несколько минут."
	"Мне не хотелось больше думать о прошлом, о том, как я попал в этот лагерь."
	"Впервые за очень долгое время я по-настоящему устал – не только эмоционально, но и физически, психологически и бог знает как ещё..."
	"Я хотел лишь, чтобы от меня все отстали – в первую очередь мои мысли.{w} Хотел, чтобы всё разрешилось как-нибудь само собой."
	"Ну, или по крайней мере без моего деятельного участия."
	th "А вдруг я тут навсегда?"
	th "Тогда придётся привыкать..."
	th "Вот так просто?.. Я... я не готов...{w} Эх..."
	"Сознание улетало всё дальше, и всё сложнее становилось концентрироваться на чём-то конкретном."
	th "Наверное, лучше отложить на завтра..."
	"Я перевернулся на другой бок и заснул."
	window hide
	
	stop music fadeout 3
	
	scene bg black
	with fade3
	
	$ renpy.pause(3)
	
	jump day3_main1
