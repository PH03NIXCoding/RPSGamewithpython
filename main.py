from random import randint
import sys,time, os
t = ["r", "p", "s"]
Alexmessage="Hi I'm Alex.\nI like playing Rock Paper Scissors. We can play. But first..."
for char in Alexmessage:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

Alex = t[randint(0,2)]
player = False
name = input("\nWhat's your name?\n")

AlexMessage="Nice to meet you."
AlexMessage="Whenever you want to reset the score just say 'reset' and now... Let's play!!!"
for char in AlexMessage:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

You = 0
PC = 0

def win():
  global You
  You+=1
  print(message)
  print('Alex =', PC, '\n',name, '=',You)
def lose():
  global PC
  PC+=1
  print (message)
  print('Alex =', PC,'\n',name, '=',You)

while player == False:
    player = input("\nRock, Paper, Scissors?(r,p,s)\n")

    if player == Alex:
        print("It's a tie! No points!")
        print('Alex =',PC)
        print(name,'=',You)


    elif player == "r":
        if Alex == "p":
            message = "Ha! Paper covers Rock, you lose! I really am good at this game"
            lose()
        else:
            message ="You win!, Rock crushes Scissors"
            win()


    elif player == "rock":
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
            message ="You win!, Paper covers Rock"
            win()

    elif player == "paper":
            if Alex == "s":
                message = "Ha! Scissors cuts Paper, you lose! One more point for me"
                lose()
            else:
                message ="You win!, Paper covers Rock"
                win()

    elif player == "s":
        if Alex == "r":
            message = "Ha! Rock smashes scissors!"
            lose()
        else:
            message ="You win!, Scissors cuts Paper"
            win()
    elif player == "scissors":
        if Alex == "r":
            message = "Ha! Rock smashes scissors!"
            lose()
        else:
            message ="You win!, Scissors cuts Paper"
            win()

    elif player == "reset":
      You=1*0
      PC=1*0
      print("\nOkay let's start again")
    else:
        message = "That's not allowed. Who doesn't know how to play Rock Paper Scissors? Children are taught to play this game. I'm not that smart. I'm just a computer. I'm going to type out this long message as punishment for doing something dumb. Now go play the right way! :("
        

    player = False
    Alex = t[randint(0,2)]