import csv
import matplotlib.pyplot as plt

def lerObras():
    file = open("obras.csv", encoding = "UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter = ";")
    obras = []
    for linha in csv_file:
        obras.append(tuple(linha))
    return obras

def contaobras(lista):
    return len(lista)

def imprimeObras(lista):
    for obras in lista:
        nome, descrição, ano, periodo, compositor, duração, id = obras
        print(f"|{nome[:10]:10} |  {descrição[:25]:10}   |{ano:10}")
    
def ordenarnometuplo(lista):
    tuplos1 = []
    for obras in lista:
        nome, descrição, ano, periodo, compositor, duração, id = obras
        tuplos1.append((nome, ano))
        tuplos1.sort(key = lambda x: x[0])
    return tuplos1
    
def ordenaranotuplo(lista):
    tuplos2 = []
    for obras in lista:
        nome, descrição, ano, periodo, compositor, duração, id = obras
        tuplos2.append((nome,ano))
        tuplos2.sort(key = lambda x: x[1])
    return tuplos2

def ordenadacompositores(lista):
    compositores = []
    for obras in lista:
        nome, descrição, ano, periodo, compositor, duração, id = obras
        compositores.append(compositor)
        compositores.sort()
    return compositores


def tituloporAno (lista):
    dic = {}
    for nome, descrição, ano, periodo, compositor,duração, id in lista:
        if ano in dic.keys():
            dic[ano].append(nome)
        else:
            dic[ano] = [nome]
    return dic

def distAno (lista):
    dic0 = {}
    for nome, descrição, ano, periodo, compositor,duração, id in lista:
        if ano in dic0.keys():
            dic0[ano] = dic0[ano] + 1
        else:
            dic0[ano] = 1
    return dic0


def distPeriodo(lista):
    dic1 = {}
    for nome, descrição, ano, periodo, compositor,duração, id in lista:
        if periodo in dic1.keys():
            dic1[periodo] = dic1[periodo] + 1
        else:
            dic1[periodo] = 1
    return dic1    

def distCompositor (lista):
    dic2 = {}
    for nome, descrição, ano, periodo, compositor, duração, id in lista:
        if compositor in dic2.keys():
            dic2[compositor] = dic2[compositor] + 1
        else:
            dic2[compositor] = 1
    return dic2

def plotDistrib(distrib):
    eixoy = list(distrib.keys())
    eixox = list(distrib.values())
    plt.figure(figsize=[10,20])
    plt.barh(eixoy,eixox,color= "blue")  
    plt.xticks([x for x in range(0,len(distrib.values()))],distrib.values())
    plt.show()
    return


def composEobras(lista):
    list= []
    dic2 = {}
    for nome, descrição, ano, periodo, compositor, duração, id in lista:
        list.append((compositor,nome)) 
    for compositor, nome in list:
        if compositor in dic2.keys():
            dic2[compositor] = dic2[compositor] + [nome]
        else:
            dic2[compositor] = [nome]
    return dic2


def visualizacao(dic): 
    d = list(dic.items())
    for compositor in d:
        print(f"{compositor[0]:<28} ==>  {compositor[1]}") 
    return compositor
    






   




        

        

