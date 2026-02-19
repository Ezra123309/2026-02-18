V = int(input())
v = input()
A = v.count("A")
B = v.count("B")
if A > B:
    print("A")
if B > A:
    print("B")
if A == B:
    print("tie")