from random import randint


aciertos = 0
fallos = 0

goOn = True

#Loop goes on until goOn is false
while(goOn):
    numerador=randint(15,99)
    denominador=randint(11,numerador)
    cociente=numerador // denominador
    resto = numerador % denominador

    mensaje='Divide ' , numerador , ' entre ' , denominador , '. Si quieres acabar pon adios\n'
    
    player = input (mensaje) 
    

    if (player == 'adios'):
        goOn = False
    elif (player == str(cociente)):
        print ("Genial")

# #List of options
# game  = ["Rock", "Paper", "Scissors"]

# #Assigning a random option to computer
# computer = game[randint(0,2)]


# #Keep count for points
# playersPoint = 0
# computersPoint = 0

# goOn = True

# #Loop goes on until goOn is false
# while(goOn):
#     #Ask for user input
#     player = input("Rock, Paper or Scissors? or enter Finish to end!\n")

#     #Check for scenarios
#     if(player == 'Finish'):
#         goOn = False
#     elif(player == computer):
#         print("Tie!")
#     elif(player == "Rock"):
#         if(computer == "Paper"):
#             print("You lose!", computer, "covers", player)
#             computersPoint = computersPoint + 1 
#         else:
#             print("You win!", player, "smashes", computer)
#             playersPoint = playersPoint + 1
#     elif(player == "Paper"):
#         if(computer == "Scissors"):
#             print("You lose!", computer, "cut", player)
#             computersPoint = computersPoint + 1
#         else:
#             print("You win!", player, "covers", computer)
#             playersPoint = playersPoint + 1
#     elif(player == "Scissors"):
#         if(computer == "Rock"):
#             print("You lose...", computer, "smashes", player)
#             computersPoint = computersPoint + 1
#         else:
#             print("You win!", player, "cut", computer)
#             playersPoint = playersPoint + 1
#     else:
#         print("That's not a valid play. Check your spelling!")
#     #Assigning a random option to computer
#     computer = game[randint(0,2)]
#     print('********Next Turn********')

# #Printing final points
# print("********Final Points********")
# print("Player: ", playersPoint)
# print("Computer: ", computersPoint)