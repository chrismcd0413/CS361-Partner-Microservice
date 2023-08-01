# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        word_length = input('Enter 5, 6, or 7 to get a random word of that length')
        with open('word_service.txt', 'r+') as word_pipe:
            word_pipe.truncate(0)
            word_pipe.seek(0)
            word_pipe.write(str(word_length))
            word_pipe.close()
            time.sleep(5)
        output = open('word_service.txt').read()
        print('Your word is:', output)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
