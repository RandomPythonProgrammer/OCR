from deep_translator import GoogleTranslator
from pathlib import Path
import os

translator = GoogleTranslator(source='zh-CN', target='en')

folder = 'input'

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    with open(path, 'rb') as text_file:
        text = text_file.read().decode('utf8')
        translated_text = translator.translate(text)
        with open(f'output/{Path(path).stem}_[translated].txt', 'w+') as output_file:
            output_file.write(translated_text)
