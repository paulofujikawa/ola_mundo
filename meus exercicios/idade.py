# Escrever um programa que le uma idade e classifica por menor de idade, adulto e idoso 
idade = int(input())
if idade < 18:
    print("menor de idade ")
if idade >= 18 and idade < 65:
    print("adulto")
if idade >= 65:
    print("idoso")