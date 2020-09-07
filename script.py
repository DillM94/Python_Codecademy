import random

money = 100

#Write your game of chance functions here
def coin(choice, bet):
  c = random.randint(0,1) # 0 - heads, 1 - tails
  if choice == 'heads' and c == 0:
    out = bet
    return out
  elif choice == 'tails' and c == 1:
    out = bet
    return out
  else: 
    out = (-1)*bet
    return out

def cho(choice, bet):
  d1 = random.randint(1,6)
  d2 = random.randint(1,6)
  d = d1+d2
  
  if d%2 == 0:
    res = 'even'
  else:
    res = 'odd'
  if choice == res:
    out = bet
    return out 
  else:
    out = (-1)*bet
    return out

## Cards
def card(bet):
  p1 = random.randint(1,13)
  p2 = random.randint(1,13)
  if p1 > p2:
    out = bet
    return out
  elif p1 < p2:
    out = (-1)*bet
    return out
  else:
    print('It\'s a draw. Try again')
    return 0

## Roulette
def roulette(bet, number = 'none', colour = 'none'):
  col = random.randint(0,1) # Red 0, Black 1
  num = random.randint(0,37) # 37 00
  if (number == 'none') and (colour == 'none'): # No number or colour bet
    print('Try again.')
    return 0
  if num == 0 or num == 00: # 0 or 00 Loss
    if colour == 'none':
      return (-1)*bet
    elif number == 'none':
      return (-1)*bet
    else:
      print('Make a bet')
      return 0
  elif colour == 'none': # Bet just number
    if number == num:
      return (2)*bet
    else:
      return (-2)*bet
  elif number == 'none': # Bet just colour
    if colour == col:
      return bet
    else:
      return (-1)*bet
  elif (number == num) and (colour == col): # Bet number and colour
    return (5)*bet
  else: 
    return (-5)*bet

#Call your game of chance functions here
print(money)
money += coin('heads',10)
print(money)
money += cho('even', 20)
print(money)
money += card(30)
print(money)
money += roulette(5,10,'black')
print(money)
