# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:55:50 2022

@author: Asus
"""
print("\n")
print("| Bem vindo ao problema dos carris |")
print("\n")
print("| Para contexto, vamos enfrentar a seguinte situação |")
print("\n")
print(" Encontra-se numa ponte com uma alavanca. ")
print(" Esta alavanca muda a direção de um comboio.")
print(" Um comboio está a andar nos carris.")
print(" Se continuar em frente, atropela 5 pessoas.")
print(" No entanto, se você puxar a alavanca, muda a direção do comboio")
print(" atropelando apenas uma pessoa.")
print("\n")
print(" 1 - Não puxar a alavanca ")
print(" 2 - Puxar a alavanca ")
a = input("| Nesta situação, o que faria? [1/2] " )
if a == "1":
    print("\n")
    print(" É um facto que não salvamos 5 pessoas da morte certa, mas")
    print(" moralmente pensando, se puxarmos a alavanca, a morte de uma pessoa.")
    print(" seria à nossa custa. Fica a questão, seriamos nós os assassinos? ")
elif a == "2":
    print("\n")
    print(" Logicamente salvamos 5 pessoas à custa de uma.")
    print(" Infelizmente, mudamos o rumo dos acontecimentos.")
    print(" Estamos diretamente relacionados com a morte de uma pessoa")
    print(" Somos nós os assassinos? ")
    print(" Conseguimos viver com esse peso na consciencia?")
    print(" Mas será que conseguiriamos viver com o peso de não salvar 5 pessoas?")

print("\n")
print("\n")
print("| Este é o problema dos carris mais famoso de todos. |")
print("| Felizmente, tudo evolui. |")
print("| Se em vez de 5 pessoas, estavam 5 crianças, a decisão mudaria? |")
print("\n")
print("| Se tiver paciencia, vou desenvolver um programa que responda da maneira")
print("| mais lógica a estas perguntas.")

print("Para mais facil compreenção, aqui vai a lista de pessoas")
print("\n")
print("1 - Homem adulto")
print("2 - Mulher adulta")
print("3 - Homem idoso")
print("4 - Mulher idosa")
print("5 - Criança")
print("6 - Bebé")
print("7 - Cão")
print("8 - Gato")

l1 = []
l2 = []
while True:
    n = input("Escreva o número da pessoa que quer adicionar: ")
    if n != "0":
        l1.append(n)
    else:
        break
    
        
    