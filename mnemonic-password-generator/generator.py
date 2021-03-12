import random
import pyperclip
import time

dictionary = open("seed-phrase-words-dictionary.txt")
# numberOfLines = len(dictionary.readlines())
linesOfFile = dictionary.readlines()
password = ''

for x in range(12):
  # print(linesOfFile[random.randint(0,2047)].strip(), end=' ')
  # time.sleep(1)
  password += linesOfFile[random.randint(0,2047)].strip() + ' '

pyperclip.copy(password[0:-1])
