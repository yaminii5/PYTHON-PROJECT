
import random
import time
print('Hello World! Welcome to the game')

n = random.randint(1, 50)
print('Number has been generated!!\nYou have 5 chances to guess the number between 1 to 50')

count = 5

for i in range(count-1):

    a = int(input('Guess the number: '))

    if a == n:
        print("Yay! That's right. You won!")
        break
    elif a > n:
        print('The number is less than ', a)
        
    else:
        print('The number is greater than ', a)
    print("You lost the game.")    
    



