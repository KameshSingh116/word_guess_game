#Radhe Radhe
import random
name=input("What should i call you?:")
print(f"Let's Go {name}")

words = ['rainbow', 'computer', 'water', 'programming',
         'python']

word=random.choice(words)

print(f"{name} start guessing")

guess=''
turns=3
size=len(word)
print("...HINT...")
hint=print(f"The word has {size} characters!")

while(turns>0):
    guess=input("Your guess:")

    if word==guess:
        print(f"You guessed it right {name}")
        break
    
    elif(word!="guess"):
        print(f"Try again you are left  with {turns-1}")
        turns=turns-1
        if(turns==0):
            print("Awwwwww! no tries left!")

    else:
        print("Invalid input buddy!")
        turns=-1

    if(turns==0):
        print("You weren't able to guess the word!")
        print(f"The word is {word}")

