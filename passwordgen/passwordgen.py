import random
import requests

def gen_password():
    req = requests.get('https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt')
    string_words = req.text
    list_of_words = string_words.split('\n')
    password = []
    for i in range(0, 4):
        password.append(list_of_words[random.randrange(0,274926)])
    seperator = '.'
    print seperator.join(password)


if __name__ == '__main__':
    gen_password()