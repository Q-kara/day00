import os
import random
name=input("What file would you like to open? Please add file extension(filename.ext)")
exist=os.path.exists(name)
if exist:
    txt_file=open(name)
    file_content=txt_file.readlines()
else:
    txt_file=open("shortwords.txt")
    file_content=txt_file.readlines()
word=random.choice((file_content))
word_length = len(word)-1
random_num = random.randint(0,word_length)
random_char = word[random_num]
hidden_word = word.replace(random_char,"_")
changed_word = "Guess the word {0}".format(hidden_word)
print(changed_word)
letter=input("Guess the missing letter:")
if random_char ==letter:
    print("The word was {0}.Well Done! You are awesome".format(word))
else:
    print("Wrong! Do better next time")
