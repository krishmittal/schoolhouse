L=[2,7,1,4,9,5,1,4,3]
l2=[]
l3=[]
for i in L:
    print(i)
    if i not in l2:
        l2.append(i)
        print(l2)
    else:
        l3.append(i)
print(l2)
print(l3)
