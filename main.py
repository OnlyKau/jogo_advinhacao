print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42

guess = -1

#Jeito de não deixar o codigo dar erro após inserção de caracteres.

while guess <0 :

  try:
    guess = int(input("Enter your number: "))
    print ("You have choose", guess, sep = ' ')
    break
  except:
    print("Invalid value, please just numbers!")
    continue

right =  secret_number == guess  

high  = guess > secret_number

low   = guess < secret_number
                
if (right):

  print ("Right Number")

else:
        
  if(high):
    print("Wrong Number, You chosse a higher number than secret number.")
        
  if(low):
    print("Wrong Number, you choose a lower number than secret number.")


print("End Game")          
 
  




        
                  
