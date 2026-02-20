V = int(input())
v = input()
A = v.count("A")
B = v.count("B")
if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B:
    print("Tie")