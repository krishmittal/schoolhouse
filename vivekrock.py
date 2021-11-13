import random
print('HELLO')
x='rock'
y='paper'
z='scissors'
l=[x,y,z]
a=int(input('how many times would you like to play: '))
for i in range(a):
    print('1-rock')
    print('2-paper')
    print('3-scissors')
    b=random.choice(l)
    c=int(input('enter your choice: '))
    if b==x and c==1:
        print(b)
        print("it's a tie")
    elif b==y and c==2:
        print(b)
        print("it's a tie")
    elif b==z and c==3:
        print(b)
        print("it's a tie")
    elif b==x and c==2:
        print(b)
        print('you win')
    elif b==y and c==3:
        print(b)
        print('you win')
    elif b==z and c==1:
        print(b)
        print('you win')
    else:
        print(b)
        print('you lose')
print('thank you,hope you enjoyed')
