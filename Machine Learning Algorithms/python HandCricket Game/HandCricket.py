import math
import random


OE = input("odd or even :: ")

user1 = int(input("number from 1 to 6 :: "))
computercho = random.randint(1,6)

print("computer chosen : ",computercho)
print("total : ",user1+computercho)
totalnum = user1 + computercho

us = ''
co = ''

if OE =='even' and totalnum%2==0:
  us = input("what do you chose Batting/Bowling :: ")
  print("you are now ",us)
  
elif OE=='even' and totalnum%2==1:
  co = random.choice(['Batting','Bowling'])
  print("The computer chosen :",co)

elif OE =='odd' and totalnum%2==1:
  us = input("what do you chose Batting/Bowling :: ")
  print("you are now ",us)
  
elif OE=='odd' and totalnum%2==0:
  co = random.choice(['Batting','Bowling'])
  print("The computer chosen :",co)


TotalUserScore = 0
totalComputerScore = 0

if us == "Batting":
  while True:
    user = int(input("Bat the score from 1 to 9:: "))
    comp = random.randint(1,9)
    print("computer score chosen : ",comp)
    if user == comp:
      print("You are out")
      
      while True:
        user = int(input("Bowl the ball for comp : "))
        comp = random.randint(1,9)
        print("the computer chosen :",comp)
        
        if user == comp:
          print("\n")
          print("the computer is also out")
          break
        
        totalComputerScore += comp
        print("the comp score is :",totalComputerScore)
             
      break
    TotalUserScore += user
    print("the total score : ",TotalUserScore)
    

elif us == 'Bowling':
  while True:
    user = int(input("bowl the ball from 1 to 9 : "))
    comp = random.randint(1,9)
    print("the computer chosen :",comp)
    
    if user == comp:
      print("\n")
      print("the Computer is outt!!!")
      
      while True:
        user = int(input("Bat the ball from 1 to 9 : "))
        comp = random.randint(1,9)
        
        if user == comp:
          print("you are out !!")
          break
        
        TotalUserScore+=user
        print("the present score:",TotalUserScore)
    
      break
    totalComputerScore +=comp
    print("the score of com : ",totalComputerScore)
    
elif co == "Batting":
  while True:
    user = int(input("bowl the ball fo computer :"))
    comp = random.randint(1,9)
    
    print("the computer chosen : ",comp)
    
    if user == comp:
      print("the computer is out")
      
      while True:
        user = int(input("Bat the ball from 1 to 9 : "))
        comp = random.randint(1,9)
        
        print('COMPUTER bOwl : ',comp)
        
        if user == comp:
          print("you are out!!!")
          break
        TotalUserScore += user
        print("the present score is : ",TotalUserScore)
      
      break
    totalComputerScore +=comp
    print("computer score is ",totalComputerScore)
    
elif co == "Bowling":
  while True:
    user = int(input("bat the score from 1 to 9 : "))
    comp = random.randint(1,9)
    
    print("the computer bowl : ",comp)
    
    if user == comp:
      print("you are out ")
      
      while True:
        
        user = int(input("Bowl for the computer: "))
        comp = random.randint(1,9)
        
        print('computer bat : ',comp)
        
        if user == comp:
          print("the computer is out!!!!")
          break
        
        totalComputerScore += comp
        print('the present computer score is : ',totalComputerScore)
    
    
      break
    TotalUserScore += user
    print("the total score ",TotalUserScore) 
    
if TotalUserScore > totalComputerScore:
  print("uses is the winner.... total score is : ",TotalUserScore)
elif TotalUserScore < totalComputerScore:
  print("the computer is the winner.. total computer score is ",totalComputerScore)
elif TotalUserScore == totalComputerScore:
  print("both are tie")