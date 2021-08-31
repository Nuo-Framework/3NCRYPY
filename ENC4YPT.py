import time
import colorama
from colorama import Fore, Back, Style, init
import base64
import os

init()

def logo():
    print("<------------------------------------------------->")
    print("|                                                 |")
    print("|     _____ _   ______________  ______  ______    |")
    print("|    |__  // | / / ____/ __ \ \/ / __ \/_  __/    |")
    print("|     /_ </  |/ / /   / /_/ /\  / /_/ / / /       |")
    print("|   ___/ / /|  / /___/ _, _/ / / ____/ / /        |")
    print("|  /____/_/ |_/\____/_/ |_| /_/_/     /_/         |")
    print("|                                                 |")
    print("<------------------------------------------------->")



logo()

time.sleep(0.5)

opcion1 = input("Elige una opcion para continuar:\n\n1) Encriptar 2) Desencriptar 3) Salir\n\n>>>  ")

if opcion1 == "1":
    os.system("cls")
    no_encoded_data = (input("Inserta la frase a encriptar: "))
    time.sleep(0.5)
    print("...Encriptando...")
    time.sleep(1)
    print()
    print()
    encoded=(base64.b64encode(no_encoded_data.encode('ascii')))
    encoded_ascii=encoded.decode('ascii')
    print("Texto encriptado: ", Fore.RED + Back.WHITE + encoded_ascii + Back.RESET + Fore.RESET)
elif opcion1 == "2":   
    os.system("cls")
    si_encoded_data = (input("Inserta la frase a desencriptar: "))
    time.sleep(0.5)
    print("...Desencriptando...")
    time.sleep(1)
    print()
    print()
    decoded = base64.b64decode(si_encoded_data.encode('ascii'))
    decoded_ascii=decoded.decode('ascii')
    print("Texto desencriptado: ", Fore.RED + Back.WHITE + decoded_ascii + Back.RESET + Fore.RESET)
elif opcion1 == "3":
    SystemExit
else:
    print(Fore.RED + "¡ERROR! ", Fore.YELLOW + "Porfavor inserte la opcion en mayusculas por ejemplo 'A' y presione enter. Intentelo de nuevo" + Fore.RESET)





