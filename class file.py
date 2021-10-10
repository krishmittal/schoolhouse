c=0
list1=[]
while True:
    print("this is the menu")
    print("1: Add a customer")
    print("2: Modify customer details")
    print("3: Delete customer details")
    print("4: sort customer list")
    print("5: display the sorted list")
    print("6: Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        print("1: Add amount deposited")
        print("2: Add a customer account")
        d=int(input("Enter your choice"))
        if d==1:
            print(list1)
            amount=int(input("how much would you like to deposit?: "))
            pos=int(input("at what position"))
            list1.insert(pos, amount)
        elif d==2:
            list2=eval(input("add a customer list"))
            list1.extend(list2)
    elif c==2:
        print(list1)
        pos=int(input("at what position"))
        e=int(input("Enter your choice"))
        list1[pos]=e
        print(list1)