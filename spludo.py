import random
import time
name=input("enter your name : ")
tar=50
play=0
comp=0
def player(play,val):
  input("press enter to roll the dice")
  dice=random.randint(1,6)
  if val==1:
    print("entry value : ",dice)
    return dice
  print(dice)
  if play+dice<=tar:
     if play==tar-6 and dice==6:
       return play
     play=play+dice
  if dice==6:
    play=player(play,0)
  return play
def computer(comp,val):
    print("my turn")
    time.sleep(1)
    dice=random.randint(1,6)
    if val==1:
      print("entry value : ",dice)
      return dice
    print(dice)
    if comp+dice<=tar:
       if comp==tar-6 and dice==6:
          return comp
       comp=comp+dice
    if dice==6:
       comp=computer(comp,0)
    return comp
entry=player(play,1)
entry1=computer(comp,1)
print("="*5,"turn","="*5)
while True:
       if entry==6:
           play=player(play,0)
           if play==comp:
             print("beatdown")
             comp=0
             play=player(play,0)
           if play==tar:
             break             
       else:
          entry=player(play,1)
       if entry1==6:
             comp=computer(comp,0)
             if comp==play:
               print("beatdown")
               play=0
               comp=computer(comp,0)
             if comp==tar:
               break
       else:
           entry1=computer(comp,1) 
       print(name," = ",play)
       print("computer = ",comp)
       print("="*5,"turn","="*5)
if play==tar:
   print("you win\n","your score = ",play,"\nmy score = ",comp)
else:
   print("i win\n","your score = ",play,"\nmy score = ",comp)
