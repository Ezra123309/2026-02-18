a1 = input()
a2 = input()
a3 = input()
a4 = input()
a5 = input()
a6 = input()
a = a1+a2+a3+a4+a5+a6

num = a.count('W')
if num >= 5:
    print("1")
elif num >= 3:
    print("2")
elif num >= 1:
    print("3")
else:
    print("-1")


