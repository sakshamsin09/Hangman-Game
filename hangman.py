from words import words
import random
import string
#print(words)

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()


def hangman():
    word=get_valid_word(words)
    print(word)
    word_letters = set(word)   # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what user guessed
    lives=len(word)
    while len(word_letters) > 0 and lives>0:
        #letters used
        print("you have ",lives,"lives and used letters : ", ' '.join(used_letters))
        #curernt word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word : ", ' '.join(word_list))
        user_letter = input("guess a letter : ").upper()
        if user_letter in alphabet-used_letters :
             used_letters.add(user_letter)
             if user_letter in word_letters:
                 word_letters.remove(user_letter)
             else:
                 lives-=1
                 print("letter is not in word")
        elif user_letter in used_letters:
            print("you have already used this letter")
        else:
            print("you entered wrong letter" , user_letter)
    if(lives==0):
        print("you lost")
    else:
        print("you win")

hangman()