import random 

print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = random.randint(1,10)
print (secret_number)
guess = ()
total_try = 3
round = 1

#Jeito de não deixar o codigo dar erro após inserção de caracteres.

'''print ("Try ",t) 
while (total_try > 0):
  
  if guess <0 :

    try:
      guess = int(input("Enter your number: "))
      print ("You have choose", guess, sep = ' ')
      break
    except:
      print("Invalid value, please just numbers!")
      continue
'''
while (total_try > 0):

  print ("Try {} of 3".format(round))
  
  guess = int(input("Type a number: "))
  
  print("you typed: ", guess)

  
  right =  secret_number == guess  

  high  = guess > secret_number

  low   = guess < secret_number
                
  if (right):

    print ("Right Number")

  else:
        
    if(high):
      print("Wrong Number, You chosse a higher number than secret number.")
        
    elif(low):
      print("Wrong Number, you choose a lower number than secret number.")
  
  if (guess == secret_number):
    break


 
  total_try = total_try - 1
  round = round + 1

print("End Game")          
 
  




        
                  
