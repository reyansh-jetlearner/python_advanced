import random
print("Welcome to my 2 player hangman game! Player 1 will enter a word and Player 2 will get 10 attempts to try and guess it!")
word=input(" Now this is for player one only. What should the word be?: ")
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \nPlayer 2 your turn!")
guessword=["_"]*len(word)
maxattempt=10
attempts=0
guessedletters=[]
print("word: "+" ".join(guessword))
while attempts<maxattempt and "_" in guessword:
    guess=input("What should the leter be?")
    if len(guess)!= 1:
        print("That was more than one letter!")
        continue
    if guess in guessedletters:
        print("You already used this letter!")
        continue
    guessedletters.append(guess)