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
    for i in range(1, rounds+1):
        word=random.choice(words)
        jumbledword=wordjumble(word)
        print("Round {}: {}".format(i, jumbledword))
        hint=input("Do you want a hint? Type yes or no").lower()
        if hint =="yes":
            print(givehint(word))
        guess=input("What is the word?").lower()
        while not guess.isalpha():
            print("That is not a word. Please try again.")
            guess=input("What is the word?").lower()
        if guess == word:
            print("Correct!")
            score+=1
        else:
            print("Wrong. The word was {}".format(word))
    print("You made it! All 7 rounds complete. Your score is {} out of 7".format(score))
playgame()