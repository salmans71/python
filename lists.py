"""
l1 = []
n = int(input("enter no items should be enter in lists:"))
for i in range(n):
    elements = input()
    l1.append(elements)
print(l1)
#print("after inserting the new element:", l)
"""
l = [1 , 2 , 3 , 4 , 5]
l.insert(4 , "crazy")
print(l)

"""
l1 = [1 , 2 , 3 , 4 , 5]
print(l1[2:])
print(l1.pop())
#l1.sort(reverse = True)
print(l1)
print(l + l1)
del l[2:5]
print("after deletion of elements:")
print(l)
"""