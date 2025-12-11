file=open("something.txt","w")
file.write("NeverGonnaGiveYouUp somthing yap") 
file.close()
file=open("something.txt","r")
content=file.read()
print(content)
file.close()

print("_"*30)
file=open("something.txt","r")
print(file.readline())
file.close()

file=open("something.txt","a")
file.write("\n hibyeidk")
file.close()

with open("something.txt","r") as file:
    content=file.read()
    print(content)