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
                
if (secret_number == guess):
        print ("Right Number")
else:

        print("Wrong Number")
  




        
                  
