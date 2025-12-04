dictionary={}

while True:
    print("1. Add/Update")
    print("2. Retrive a definition")
    print("3. Delete a definition")
    print("4. View the dictionary")
    print("5. Stop")
    choice=int(input("Enter your choice(1-5): "))

    if choice==1:
        word=input("What is the word: ")
        def90=input("Enter the definition: ")
        dictionary[word]=def90
        print("Added")
    elif choice==2:
        which=input("What word do you want to view?")
        print("{}:{}".format(which,def90[which]))
    elif choice==3:
        which=input("Which one do you want to delete?: ")
        del dictionary[which]
        print("Deleted")
    elif choice==4:
        for conloop in dictionary:
            print("{}:{}".format(conloop,dictionary[conloop]))
    elif choice==5:
        print("Exiting...Bye!")
        break
    else:
        print("Sorry, Invalid Option")