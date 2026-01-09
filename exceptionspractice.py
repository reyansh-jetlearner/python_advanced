#ZeroDivisionError
try:
    n1=10
    n2=0
    ans=n1/n2
    print(ans)
except ZeroDivisionError:
    print("You cannot divide by zero")

#multiple exceptions
try:
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    ans=n1/n2
    print(ans)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("You cannot divide by zero")

#nested try except blocks
try:
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    try:
        ans=n1/n2
        print(ans)
    except ZeroDivisionError:
        print("You cannot divide by zero")
except ValueError:
    print("Invalid value")


#concept of else
try:
    print("Inside try block")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("No exceptions occurred")

#Test of age
try:
    age=int(input("Enter your age: "))
    if age<0:
        raise ValueError("Age cannot be less than 0")
except ValueError as e:
    print("Error Found: {0}".format(e))