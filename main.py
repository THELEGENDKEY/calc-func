# def angry(func):
# 	def wrapper():
# 		func()
# 		print('he is angry')
# 	return wrapper
	
# def cutesofsmthn(func):
# 	def wrapper():
# 		func()
# 		print('he looks at something cute')
# 	return wrapper
	
# def hungry(func):
# 	def wrapper():
# 		func()
# 		print('he is hungry')
# 	return wrapper
	
# def dissapoint(func):
# 	def wrapper():
# 		func()
# 		print('he is dissapointed')
# 	return wrapper
	
# def ask(func):
#   def wrapper():
#     ans = str(input('do you want a life question? y/n : '))
#     if ans == 'y':
#       print('Why are you in your body and how do you know it?')
#     else:
#       print('( nah, who cares')
#     func()
#   return wrapper
# def sad(func):
# 	def wrapper():
# 		func()
# 		print('he is sad')
# 	return wrapper
# def minecraftismylife(func):
#   def wrapper():
#     print('Do not disturb him! He plays Minecraft bedwars rn.')
#     func()
#   return wrapper
# def studies(func):
# 	def wrapper():
# 		func()
# 		print('he is studing rn')
# 	return wrapper
# def sleep(func):
# 	def wrapper():
# 		func()
# 		print('he is sleeping')
# 	return wrapper
# def cook(func):
# 	def wrapper():
# 		func()
# 		print('he is cooking')
# 	return wrapper
def countcalcwrapper(func):
  def wrapper():
    func()
    print('Thank you for using calculator!')
    input(str('Do you like our calculator? (y/n): '))
    print('Thanks for your feedback!')
  return wrapper
  
def calcwrapper(func):
  def wrapper():
    print ("Here starts the math!")
    func()
  return wrapper
@countcalcwrapper
@calcwrapper
def calc():
  try:
  	name = input('Name:')
  	if name.isalpha() == False:
  		raise ValueError
  except ValueError:
  	name = ''
  	print('Only letters!')
  print('Hello', name)
  num1 = num2 = sign = ''
  while num1 == '' or num2 == '' or sign == '':
    uses = 0
    try:
      uses + 1
      num1 = int(input('Number1: '))
      sign = input('Sign: ')
      num2 = int(input('Number2: '))
      result = ''
      if sign == '+':
        result = num1 + num2
      if sign == '-':
        result = num1 - num2
      if sign =='/':
        result = num1 / num2
      if sign =='*':
        result = num1 * num2
      if sign =='%':
        result = num2/100 * num1
      if sign =='^':
        result = num1 ** num2
      if num2 == 0 and sign ==  '/':
        raise ZeroDivisionError
      
    except ValueError:
      print('Wrong value')
    except ZeroDivisionError:
      sign = ''
      print("You can't divide by zero")
    except:
      print('Something is wrong!')
    if sign == '+':
      print(f"{num1} + {num2} = "  + str(result))
    if sign == '-':
      print(f"{num1} - {num2} = " + str(result))
    if sign == '/':
      print(f"{num1} / {num2} = " + str(result))
    if sign == '*':
      print(f"{num1} * {num2} = " + str(result))
    if sign =='%':
      print(f"{num1} % {num2} = " + str(result))
    if sign =='^':
      print(f"{num1} ^ {num2} = " + str(result))
      
    answer = str(input('Continue? y/n '))
    if answer == 'y':
      calc()
      


# @ask
# @sad
# @cutesofsmthn
# @minecraftismylife
# @dissapoint
# @studies 
# @hungry
# @angry
# @sleep
# @cook
# @calc
calc()

