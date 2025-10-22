class A:
    label = "A: lable"

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

cup = D()
print(cup.label)