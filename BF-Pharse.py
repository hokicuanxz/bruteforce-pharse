import os
import time
import sys

cls = os.system('cls')
k = "\031[31m"

name = (str(input("NAME : ")))
print('\n')
print(f"WELCOME boy {name}")
time.sleep(2)
os.system('cls')

def menu():
    print("\n", '========== MENU ==========')
    print('1. Attack Pharse')
    print('2. Exit')
    print('========== MENU ==========', '\n')

def attack_pharse():
    print('\n', 'Done', time.sleep(2))

def main():
    while True:
        menu()

        pilih = input('pilih 1 - 2 : ')
        if pilih == '1':
            attack_pharse()
        elif pilih == '2':
            print('\n', "Terimakasih,sampai jumpa kembali !")
            break
        else:
            print('pilih yang bener')
        os.system('cls')
main()
        


    