import keyboard
from PIL import ImageGrab
import time
from aip import AipOcr

app_id = ''
api_key = ''
secret_key = ''

client = AipOcr(app_id, api_key, secret_key)

while True:

    keyboard.wait(hotkey='alt+a')
    keyboard.wait(hotkey='ctrl+s')
    time.sleep(0.1)

    image = ImageGrab.grabclipboard()
    image.save('image_001.jpg')

    with open('image_001.jpg', 'rb') as file:
        image = file.read()
        result = client.basicAccurate(image)
        result = result['words_result']
        for i in result:
            print(i['words'])
            with open('word.txt', 'a+', encoding='UTF-8') as text:
                text.writelines('%s\n' % i['words'])

    hotkey = keyboard.read_hotkey()
    if hotkey == 'q':
        break
