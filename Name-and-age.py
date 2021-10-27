name = ""
age = ""

while name == "":
    name = input("Wat is uw naam? ")

while age == "":
    age = input("Wat is uw leeftijd? ")

def showData():
    print("Hallo " + str(name) + ", je leeftijd is " + str(age) + " jaar.")

showData()