import random
def game():
    print("this is guessing number game: ")
    
    n= random.randint(1,100)
    guesses = 0
    while True:
        a= int(input("Guess your number: "))
        guesses +=1
        if(n<a):
            print("Smaller number please ! ")
        elif(n>a):
            print("Bigger number please!")
        else:
             print(f"you have guessed the number {n} in {guesses} guesses")
             break
game()


