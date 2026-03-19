import random
words=["python","cake","george washington","house","blanket","pancakes","france","birthday","javascript","simple"]
chooseword=random.choice(words)
guessword=["_"]*len(chooseword)
maxattempt=10
attempts=0
guessedletters=[]
print("Welcome to my hangman game! You will get a word and you will get 10 attempts to try and guess it. Good luck!")
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