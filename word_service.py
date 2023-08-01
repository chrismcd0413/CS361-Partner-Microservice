import time
from random import random

while True:
    time.sleep(2)
    with open('word_service.txt', 'r+') as pipe:
        contents = pipe.read()
        if contents.isdigit():
            pipe.truncate(0)
            pipe.seek(0)
            word_bank = open(f'word_bank_{contents}.txt')
            word_array = word_bank.read().splitlines()
            word_array_length = len(word_array)
            random_number = random() * word_array_length
            mod = int(random_number // 1)
            print('Random Number:', mod)

            pipe.write(word_array[mod])
            pipe.close()
