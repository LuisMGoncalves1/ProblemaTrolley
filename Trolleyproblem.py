# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:55:50 2022

@author: Asus
"""

def converter(l):
    lista_final = []
    for i in l:
        if i == "1":
            lista_final.append("Homem adulto")
        elif i == "2":
            lista_final.append("Mulher adulta")
        elif i == "3":
            lista_final.append("Homem idoso")
        elif i == "4":
            lista_final.append("Mulher idosa")
        elif i == "5":
            lista_final.append("Criança")
        elif i == "6":
            lista_final.append("Bebé")
        elif i == "7":
            lista_final.append("Cão")
        elif i == "8":
            lista_final.append("Gato")
    return(lista_final)
            
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
    print(" moralmente pensando, se puxarmos a alavanca, a morte de uma pessoa")
    print(" seria à nossa custa. Fica a questão, seriamos nós os assassinos? ")
elif a == "2":
    print("\n")
    print(" Logicamente salvamos 5 pessoas à custa de uma.")
    print(" Infelizmente, mudamos o rumo dos acontecimentos.")
    print(" Estamos diretamente relacionados com a morte de uma pessoa")
    print(" Somos nós os assassinos? ")
    print(" Conseguimos viver com esse peso na consciencia?")
    print(" Mas será que conseguiriamos viver com o peso de não salvar 5 pessoas?")

while True:
    print("\n")
    print("| Este é o problema dos carris mais famoso de todos. |")
    print("| Felizmente, tudo evolui. |")
    print("| Se em vez de 5 pessoas, estavam 5 crianças, a decisão mudaria? |")
    print("\n")
    
    print("---Para mais facil compreenção, aqui vai a lista de pessoas---")
    print("\n")
    print("--- Primeira Linha do comboio ---")
    print("1 - Homem adulto")
    print("2 - Mulher adulta")
    print("3 - Homem idoso")
    print("4 - Mulher idosa")
    print("5 - Criança")
    print("6 - Bebé")
    print("7 - Cão")
    print("8 - Gato")
    print("0 - Não adicionar mais")
    l1 = []
    l2 = []
    while True:
        n = input("Escreva o número que quer adicionar à primeira linha de comboio: ")
        if n != "0":
            l1.append(n)
        else:
            break

    print("\n")
    print("--- Segunda Linha do comboio ---")
    print("1 - Homem adulto")
    print("2 - Mulher adulta")
    print("3 - Homem idoso")
    print("4 - Mulher idosa")
    print("5 - Criança")
    print("6 - Bebé")
    print("7 - Cão")
    print("8 - Gato")
    print("0 - Não adicionar mais")
    while True:
        n1 = input("Escreva o número que quer adicionar à segunda linha de comboio: ")
        if n1 != "0":
            l2.append(n1)
        else:
            break
    print("\n")
    l1nomes = converter(l1)  
    print("| A primeira linha de comboio é formada por:" )
    if l1 == []:
        print("Ninguém")
    else:
        for i in l1nomes:
            print(" " +i)        
    l2nomes = converter(l2)
    print("\n")    
    print("| A segunda linha de comboio é formada por:" )
    if l2 == []:
        print("Ninguém") 
    else:
        for i in l2nomes:
            print(" " +i)
    
    #Preciso adicionar contadores às várias listas e desenvolver o algoritmo consoante os contadores, por exemplo um bebé
    # é 70 anos e uma criança 60, logo bebé < criança
    
    def converte_pontos (l):
        c = 0
        for i in l:
            if i == "1":
                c = c + 40
            elif i == "2":
                c = c + 45
            elif i == "3":
                c = c + 5
            elif i == "4":
                c = c + 10
            elif i == "5":
                c = c + 60
            elif i == "6":
                c = c + 75
            elif i == "7":
                c = c + 0
            elif i == "8":
                c = c + 0
        return(c)
    
    if converte_pontos(l1) > converte_pontos(l2):
        print("\n")
        print("| Neste caso o computador escolheria salvar as pessoas na PRIMEIRA ")
        print("| linha de comboio")
    elif converte_pontos(l1) < converte_pontos(l2):
        print("\n")
        print("| Neste caso o computador escolheria salvar as pessoas na SEGUNDA ")
        print("| linha de comboio")
    else:
        print("\n")    
        print("| Neste caso o computador considera indiferente")

    while True:
        op = str(input('| Quer repetir? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
    if op == 'N':
        break        
                 