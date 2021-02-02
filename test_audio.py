# #--------------------------VER-1.0--------------------------------------------
# import pyttsx3
# import speech_recognition as sr
# import time
# import os, sys
# import datetime
# from fuzzywuzzy import fuzz  #можно использовать для настройки нечёткого распознавания речи
# #device_index =1
#
# opts = {
#     "assist_name" : ('аня', 'анька', 'анюта', 'антроцит', 'ань', 'анечка'),
#     "call" : ('скажи', 'покажи', 'расскажи', 'поясни', 'произнеси', 'сколько'),
#     "commands" : {
#         "ctime": ('текущее время', 'сейчас времени', 'который час'),
#         "battle_net" : ('включи battle.net', 'запусти battle.net', 'battle.net'),
#         "stop" : ('стоп', 'выключись', 'отключись')
#     }
# }
# # functions
# def speak(what):
#     print(what)
#     speak_engine.say(what)
#     speak_engine.runAndWait()
#     speak_engine.stop()
#
# def callback(recognizer, audio):  #
#     try:
#         voice = recognizer.recognize_google(audio, language='ru-RU').lower()
#         print("[log] Распознано: " + voice)
#
#         if voice.startswith(opts["assist_name"]):
#             # обращение к assist_name
#             cmd = voice
#
#             for x in opts['assist_name']:
#                 cmd = cmd.replace(x, "").strip()
#
#             for x in opts['call']:
#                 cmd = cmd.replace(x, "").strip()
#
#             # распознать комманду
#             cmd = recognizer_cmd(cmd)
#             execute_cmd(cmd['cmd'])
#
#
#     except sr.UnknownValueError:
#         print("[log] Не распознано!")
#     except sr.RequestError as er:
#         print("[log] Неизвестная ошибка!")
#
# def recognizer_cmd(cmd):  # нечеткий поиск
#     RC = {'cmd': '', 'percent': 0}
#     for c,v in opts['commands'].items():
#
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > RC['percent']:
#                 RC['cmd'] = c
#                 RC['percent'] = vrt
#
#     return RC
#
# def execute_cmd(cmd):  # command ----> do something
#     if cmd == 'stop':
#         speak('выключаюсь хозяин')
#         sys.exit()
#
#     elif cmd == 'battle_net':
#         # включить батлнет
#         os.system("G:\\Hearthstone\\Hearthstone Beta Launcher.exe")
#
#     elif cmd == 'ctime':
#         now = datetime.datetime.now()
#         speak('сейчас' + str(now.hour) + ":" + str(now.minute))
#
#     else:
#         speak("комманда не распознана")
#
# # start
#
# r = sr.Recognizer()
# micro = sr.Microphone(device_index=1)
#
# with micro as source:
#     r.adjust_for_ambient_noise(source)
#
#
# speak_engine = pyttsx3.init()
# # синтезатор речи
# # voices = speak_engine.getProperty('voices')
# # speak_engine.setProperty('voice', voices[4].id)
# # синтезатор речи
#
# speak("Доброе утро!")
# speak("Я тут")
#
# stop_listening = r.listen_in_background(micro, callback)
# while True : time.sleep(0.1) # бесконечная прослушка
#
# #--------------------------VER-1.0--------------------------------------------


#--------------------------VER-2.0--------------------------------------------
import speech_recognition as sr # импортируем библиотеки
import os, sys
import pyttsx3
import datetime
import webbrowser

speak_engine = pyttsx3.init() #  инициализация  голоса


def speak(what): #  функция которая слушает что мы говорим
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def command(): #  функция которая записывает наши комманды
    r = sr.Recognizer() #  инициализация ркогнайзера

    with sr.Microphone() as source: #  открываем запись с микрофона
        print("Говорите")
        r.pause_threshold = 0.5 #  пауза после которой нужно говорить
        r.adjust_for_ambient_noise(source, duration=1) #  штука которая улавливает шум и чистит его
        audio = r.listen(source)  # запись которую мы получили из микрофона

    try: #  используем трай эксепт для обработки исключений
        cmd = r.recognize_google(audio, language='ru-RU').lower() #  вызываем комманду как рекогнайзер гугла и инициализируем русский язык(англ по умолчанию)
        print('u said - ' + cmd) #  принтуем ,то что мы сказали , чтобы понять работает или нет
    except sr.UnknownValueError:  # исключение если текст полученный с микрофона непонятен
        print("Unknown func") #  принтуем что ничего не понятно
        cmd = command() #  запускаем считывание с микрофона снова до тех пор, пока не словим трай

    return cmd #  возвращаем то что мы сказали


def do(command):  #  функция которая обрабатывает текст и делает

    if 'открой battle.net' in command:
        speak('открываю')
        os.system("G:\\Hearthstone\\Hearthstone Beta Launcher.exe")

    elif 'youtube открой' in command:
        speak('открываю')
        url = 'https://www.youtube.com'
        webbrowser.open(url)

    # elif 'апекс открой ' or 'apex открой ' in command:
    #     speak('открываю апекс')
    #     os.system("D:\\Games\\Apex\\r5apex.exe")

    elif 'выключись' in command:
        speak("выключаюсь хозяин")
        sys.exit()

    return command

speak("Приветствую хозяин, что желаете?")

while True:
    do(command())


#--------------------------VER-2.0--------------------------------------------