#Radhe Radhe
import random
name=input("What should i call you?:")
print(f"Let's Go {name}")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)

print(f"{name} start guessing")

guess=''
turns=3
