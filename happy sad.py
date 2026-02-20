a = input()
happy = a.count(":-)")
sad = a.count(":-(")
if happy > sad:
    print("happy")

if happy < sad:
    print("sad")
if happy == sad:
    if happy == 0:
        print("none")
    if happy != 0:
        print("unsure")
