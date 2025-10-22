age = [10,20,30,50,90]
age2 = [55,44,22,86,89,47,65,21]

age.append(80)
print(f"{age}")
age.pop(2)
print(f"{age}")
age.insert(2,89)
print(f"{age}")
age.remove(90)
print(f"{age}")
age.reverse()
print(f"{age}")
age.sort()
print(f"{age}")
print(f"{age.index(80)}")
age.extend(age2)
print(f"{age}")
print(f"{age2}")
age2.extend([80,56,21,49,52,16])
print(f"{age2}")
print(f"{max(age2)}")


# method overriding

name1 = "kalpesh"
name2 = "rathod"
fullName = name1 + name2
print(f"full name is: {fullName}")


names = ["k","l"] * 3
print(names)

print(len(age2))

listName = name1.split(",")
print(f"listName: {listName}")

num = 10;
for i in (10,50,90):
    print(i)




s = []

xyz = ()
print(type(xyz))

c = {}
print(type(c))



a = {66,50,50,50,90,20,20}
b = {99,88,33,20}
c = a | b
print(c)


