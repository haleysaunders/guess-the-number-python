import random
print("Hello, what is your name?")
userName = input()
print("Well, "+str(userName)+", I am thinking of a number between 1 and 20!")
secretNumber = random.randint(1,20)
# if I wanted to test this code to make sure it's working correctly I could do that by using a DEBUG statement.
# print("DEBUG: The secret number is "+str(secretNumber)) 
# and then guess the number in the input box to make sure it is returning an answer of you guessed it 
for guessesTaken in range(1,7):
    print("Take a guess good sir or ma'am!")
    guess = int(input())
    if guess < secretNumber:
        print("Your number is too low, you fucking idiot!")
    elif guess > secretNumber:
        print("Your number is too high, dumbass!")
    else:
        break # this condition is for a correct guess where we will move onto the next part of the program
        
if guess == secretNumber: 
    print("Good job, "+str(userName)+". You guessed my number in "+str(guessesTaken)+" guesses!")
else: 
    print("Nope, the number I was thinking of was "+str(secretNumber)+".")
