anwser = int(input("Van welk getal wilt u de tafel zien? "))

def showTafel(getal: int):
    for x in range(1,11):
        uitkomst = x * getal
        print(uitkomst)

showTafel(anwser)