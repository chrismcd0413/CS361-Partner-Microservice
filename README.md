# CS361 Partner Microservice

To start: word_service.py needs to be running. 

main.py contains an example of how to use the service: 

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
 
Here, you'll enter whether you want a 5, 6, or 7 letter word. It will write the number into word_service.txt
and then it will randomly grab a word from one of the 3 word banks and put it back in the file. 

Sequence Diagram:

![Sequence diagram](https://github.com/chrismcd0413/CS361-Partner-Microservice/assets/40510393/2462cc4f-140f-4348-a644-6c21cefc8227)
