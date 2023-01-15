import random
option = ("piedra", "papel", "tijera")

win_user = 0
win_computer = 0
rounds = 1

while True:
  
  print("*" * 10)
  print("ROUND ", rounds)
  print("*" * 10)

  print("Puntos Usuarios: ", win_user)
  print("Puntos Computer: ", win_computer)
  

  user_option = input("Esoge entre piedra, papel o tijera => ").lower()
  if not user_option in option:
    print("Esta opción no es válida")
    continue
  
  computer_opt =  random.choice(option)
  
  print("User option => ", user_option)
  print("Computer option => ", computer_opt)
  
  if(user_option == computer_opt):
    print("Empate")
  elif (user_option == "piedra"):
    if(computer_opt == "tijera"):
      print("Piedra gana a tijera")
      print("Usuario ganó!")
      win_user +=1
    else:
      print("Papel gana a piedra")
      print("Computer gana")
      win_computer+=1
  elif (user_option == "papel"):
    if(computer_opt == "piedra"):
      print("Papel gana a piedra")
      print("Usuario ganó")
      win_user +=1
    else:
      print("Tijera le gana al papel")
      print("Computer gana")
      win_computer+=1
  elif (user_option == "tijera"):
    if(computer_opt == "papel"):
      print("Tijera le gana a papel")
      print("Usuario gana")
      win_user +=1
    else:
      print("Piedra le gana a tijera")
      print("Computer gana")
      win_computer+=1
  if win_computer == 2:
    print("La computadora te ganó")
    break
  if win_user == 2:
    print("Excelente, Ganaste")
    break
  rounds+=1
    
  
    
  

