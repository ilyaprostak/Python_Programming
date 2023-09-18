# импортируем необходимые библиотеки
import requests, json
import pyttsx3, pyaudio, vosk

# инициализируем библиотеку для синтеза речи
tts = pyttsx3.init('sapi5')

# устанавливаем язык для синтеза речи
voices = tts.getProperty('voices')
tts.setProperty('voices', 'ru')

# выбираем голос для синтеза речи
for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft Irina Desktop - Russian':
        tts.setProperty('voice', voice.id)

# загружаем модель для распознавания речи vosk
model = vosk.Model('model_small')
record = vosk.KaldiRecognizer(model, 16000)

# инициализируем библиотеку для записи и воспроизведения аудио
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=8000)
stream.start_stream()


# функция для получения речевых команд от пользователя
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if record.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(record.Result())
            if answer['text']:
                yield answer['text']


# функция для синтеза речи
def speak(say):
    tts.say(say)
    tts.runAndWait()


# начало работы программы
speak('Здравствуйте! Я готов к работе.')
print('start...')

# запрос на получение случайной картинки собаки
url = 'https://dog.ceo/api/breeds/image/random'
response = requests.get(url)

# бесконечный цикл для получения речевых команд от пользователя
for text in listen():
    if 'показать' in text:
        # выводим картинку в консоль
        print(response.content)
    elif 'сохранить' in text:
        # сохраняем картинку как файл
        with open('dog.jpg', 'wb') as f:
            f.write(response.content)
        speak('Картинка сохранена.')
    elif 'следующая' in text:
        # запрашиваем новую случайную картинку
        response = requests.get(url)
        speak('Новая картинка загружена.')
    elif 'назвать породу' in text:
        # извлекаем породу из текста ссылки
        breed = response.json()['message'].split('/')[-2]
        speak(f'Порода собаки: {breed}.')
    elif 'разрешение' in text:
        # получаем разрешение картинки
        img = response.content
        width, height = img.size
        speak(f'Разрешение картинки: {width} на {height} пикселей.')
    else:
        speak('Команда не распознана. Попробуйте еще раз.')