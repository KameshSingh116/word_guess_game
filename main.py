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

#word => rainbow
q=['A natural phenomenon caused by light refraction and dispersion.',
   'Often appears in the sky after rain.',
   'Contains seven colors: red, orange, yellow, green, blue, indigo, violet.']

#word=>computer
w=['An electronic device for processing data.',
   'Can perform calculations and run programs.',
   'Has components like CPU, RAM, and storage.']

#word=>water
e=['A transparent, tasteless liquid essential for life.',
   'Composed of hydrogen and oxygen (H₂O).',
   'Found in oceans, rivers, and rain.']

#word=>programming
r=['The process of writing instructions for computers.',
   'Involves languages like Java, Python, and C++.',
   'Used to develop software, apps, and websites.']

#word=>python
t=['A high-level programming language known for simplicity.',
   'Named after a British comedy group, not the snake.',
   'Used in web development, data science, and AI.']

if word=='rainbow':
        print(random.choice(q)) 

elif word=='computer':
        print(random.choice(w))

elif word=='water':
        print(random.choice(e))

elif word=='programming':
        print(random.choice(r))  

elif word=='python':
        print(random.choice(t))

choice='y'
while(choice=='y'):
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
      
        choice=input("Do you want to continue:(y/n):")
        if(choice=='y'):
          continue
        else:
          break