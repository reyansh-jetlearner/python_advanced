from datetime import datetime
def add_entry():
    entry=input("Enter your journal entry: ")
    file=open("journal.txt","a")
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("[{}] {}\n".format(timestamp, entry))
    file.close()
    print("Entry added.")
def view_entries():
    file=open("journal.txt","r")
    print("Journal Entries:")
    index=0
    for line in file:
        print("{}: {}".format(index, line))
        index+=1
    file.close()
    
print("Welcome to your Journal App")
while True:
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Exit")
    choice=int(input("Choose an option: "))
    if choice==1:
        add_entry()
    elif choice==2:
        view_entries()
    elif choice==3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")