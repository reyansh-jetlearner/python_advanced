d1={"apple":"fruit","soda machine":"maker", "hello":"word"}
d1["orange"]="a fruit"
#for word in d1:
#    print("{}:{}".format(word,d1[word]))
del d1["apple"]

d1["laptop"]="an electronic device"

for word in d1:
    print("{}:{}".format(word,d1[word]))

d1["laptop"]="a device"