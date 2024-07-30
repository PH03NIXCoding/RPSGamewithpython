from random import randint
import sys,time, os
t = ["r", "p", "s"]
AlexMessage="Hi I'm Alex."
message="I like playing Rock Paper Scissors. We can play. But first..."
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

Alex = t[randint(0,2)]
player = False
name = input("What's your name?")

AlexMessage="Nice to meet you."
AlexMessage="Whenever you want to reset the score just say 'reset' and now... Let's play!!!"
for char in AlexMessage:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

You = 0
PC = 0

def win():
  global You
  You+=1
  print(message)
  print('Alex =', PC, '\n', name, '=', You)
def lose():
  global PC
  PC+=1
  print (message)
  print('Alex =', PC, '\n', name, '=', You)

while player == False:
    player = input("Rock, Paper, Scissors?(r,p,s)")

    if player == Alex:
        print("It's a tie! Oh I'll get you next time.")
        print('Alex =',PC)
        print(name,'=',You)
    elif player == "r":
        if Alex == "p":
            message = "Ha! Paper covers Rock, you lose! I really am good at this game"
            lose()
        else:
            message ="You win!, Rock crushes Scissors"
            win()
    elif player == "p":
        if Alex == "s":
            message = "Ha! Scissors cuts Paper, you lose! One more point for me"
            lose()
        else:
            message ="You win!, Scissors cuts Paper"
            win()
    elif player == "s":
        if Alex == "r":
            message = "Ha! Paper covers Rock, you lose! I am UNDEFEATABLE!"
            lose()
        else:
            message ="You win!, Scissors cuts Paper"
            win()

    elif player == "reset":
      You=1*0
      PC=1*0
      print("The score was reset!")
    else:
        print("That's not a allowed. Who doesn't know how to play Rock Paper Scissors?")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    player = False
    Alex = t[randint(0,2)]