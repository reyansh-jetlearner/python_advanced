import random
def username_generator():
    name=input("What is your full name?")  
    fullname = name.split()
    if len(fullname)<2:
        print("Please enter the full name")  
    firstname=fullname[0].lower()
    lastname=fullname[1].lower() 

    usernames=[]
    username1=firstname+lastname
    username2=firstname[:3]+lastname[2:]
    username3=lastname[2:5]+firstname[2:]
    username4=firstname[3:5]+lastname[:3]+str(random.randint(0,9))
    username5=lastname[3:]+ firstname[:5]+str(random.randint(10,99))
    username6=lastname[-2:]+firstname+"$"

    usernames = [username1]
    usernames.append(username2)
    usernames.append(username3)
    usernames.append(username4)
    usernames.append(username5)
    usernames.append(username6)

    finalusername=random.choice(usernames)
    print("Your final username is: {}".format(finalusername))

while True:
    username_generator()