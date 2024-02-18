import random
##function for timetable

def time_table():
    looping = True
    while looping: 
        try:
         x = int(input("Enter a number : "))
         for row in range(x+1):
          for col in range(x+1):
              print(f"{row*col:2}", end = "  ")
          print("")
          looping = False
        except:
         print('Please enter a number') 
              
##function for checking if number is a prime number
def prime_number(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        return True
    
test = [2, 3, 5, 7]

##for num in test:
    ##print(f"{num} is a prime number {prime_number(num)}")
    
## Guessing game for user


def guessing_game_user():
    while True:
        try:
            number = random.randint(1,20)
            print(number)
            guess = int(input("PLease enter a number : "))
            while guess != number:
                if guess > number:
                    guess = int(input("PLease enter a smaller number : "))
                else:
                    guess = int(input("PLease enter a larger number : "))
            else: 
                print("You guessed correctly")
        
        except ValueError:
            print("Input number.")
        
        q = input("Do you want to play again ? y/n : ")
        if q == "n":
            break

## guessing game for computer

def guessing_game_computer():
    while True:
        print("Hey Computer, Guess the number from 1 to 10")
        try:
            guess = random.randint(1, 10)
            print(f"Is your number : {guess}")
            x = int(input(">>> "))
            while guess != x:
                if guess > x:
                    print("I will input a smaller number .")
                    guess = random.randint(1, 5)
                    print(f"Is your number : {guess}")
                else:
                    print("I will input a larger number .")
                    guess = random.randint(6, 10)
                    print(f"Is your number : {guess}")
            else:   
                print("YAY, i got it !!!")
        except ValueError:
            print("Input number.")
        q = input("Do you want to play again ? y/n : ")
        if q == "n":
            break