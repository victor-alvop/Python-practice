# if function

'''
# 01 
# --- Stock validation ----
stock = int(input('How many items do you have? '))
if stock >= 100 and stock <= 1000:
  print('Stock updated')
else:
  print('The stock have to be between 100 and 1,000 items')
'''

'''
# 02
# --- The greatest between three numbers ---  
a = float(input('Enter a number: '))
b = float(input('Enter b number: '))
c = float(input('Enter c number: '))

if a > b: 
  number = a
  print(a)
elif b > c:
  number = b
  print(b)
else:
  number = c
  print(c)
'''

'''
# 03
# --- Even and odd number ---
number = int(input('Enter a number: '))
if number%2 == 0:
  print('Even')
else:
    print('Odd')
'''

'''
# 04
# --- Number clasification --- 
  number = float(input('Enter a number: '))
  if number == 0:
    print('The number is 0')
  elif number >= 1:
    print('Positive')
  elif number <= -1:
    print('Negative')
'''

'''
#05
# --- Guess a random number ---
import random
secret_number = random.randint(1, 100)
correct = False

while correct == False:
  print('\nGuess the number')
  user_number = int(input('Enter a number: '))
  if secret_number == user_number:
    correct = True
    print('You guessed it!\n')
  elif secret_number > user_number:
    print('The number is higher\n')
  elif secret_number < user_number:
    print('The number is lower\n')

'''

'''
#06
# --- IMC calculator ---
print('IMC Calculator\n')
weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))
imc = weight / (height * height)

if imc <= 18.5:
  print('Under weight')
elif 18.5 <= imc < 25:
  print('Healthy weight')
elif 25 <= imc < 30:
  print('Over weight')
elif imc >= 30:
  print('Obesity')
  '''