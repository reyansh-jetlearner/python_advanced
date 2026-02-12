import random
words=["tiramisu","spaghetti","cheesecake","pizza","chicken","pancakes","waffles","cupcake","brownie","macarons","crossaint"]

def wordjumble(word):
   ws=list(word)
   random.shuffle(ws)  
   return "".join(ws)

def givehint(word):
    letter=word[0].upper()
    return "The first letter of the word is {}".format(letter)

def playgame():
    score=0
    rounds=7
    print("Welcome to the Word Jumble Game!")
    print("Unscramble the letters to find the word. There are 7 rounds. Get as many correct answers as you can!") 
    