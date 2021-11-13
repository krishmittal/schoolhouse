import random
print("Can't make a choice? Then toss a coin")
x=('HEADS')
y=('TAILS')
l=[y,x]
a=int(input('how many times do you wanna toss: '))
for i in range(a):
    print('1.HEADS')
    print('2.TAILS')
    c=random.choice(l)
    b=int(input('ENTER YOUR CHOICE: '))
    if c==x and b==1:
        print(c) 
        print('you won') 
    elif c==x and b==2:
        print(c)
        print('you lost') 
    elif c==y and b==1:
        print(c)
        print('you won') 
    elif c==y and b==2:
        print(c)
        print('you lost') 
print('thank you')
