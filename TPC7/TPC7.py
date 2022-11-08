import csv
import matplotlib.pyplot as plt 

def readataset():
    file = open("alunos.csv", encoding = "UTF8")
    alunos = []
    file.readline()
    csv_file = csv.reader(file, delimiter = ",")
    for linha in csv_file :
        dic = { 
        "id" : linha[0],
        "nome" : linha[1],
        "curso" : linha [2],
        "tpc1" : linha[3],
        "tpc2" : linha[4],
        "tpc3" : linha [5],
        "tpc4" : linha [6],
        }
        alunos.append(dic)
    file.close()
    return alunos



def distrCurso (lista):
    dic0 = {}
    for aluno in lista:
        if aluno ["curso"] in dic0.keys():
            dic0 [aluno["curso"]] = dic0 [aluno["curso"]] + 1
        else:
            dic0 [aluno["curso"]] = 1
    return dic0

def media(lista):
    for aluno in lista:
        media = (int(aluno["tpc1"]) + int(aluno["tpc2"]) + int(aluno ["tpc3"]) + int(aluno ["tpc4"])) / 4
        dic1 = {"media" : media}
        aluno.update(dic1)
    return lista
    

##Considere os seguintes escalões de notas: E [1-4], D [5-8], C [9-12], B [13-16], A [17-20], acrescente uma coluna ao dataset com o escalão correspondente a cada aluno;


def escaloesNotas(lista):
    for aluno in lista:
        media = float(aluno["media"])
        if media >=1 and media < 5:
            nota = "E"
            dicNotas = {"escalão": nota}
            aluno.update(dicNotas)
        elif media >= 5 and media < 9:
            nota = "D"
            dicNotas = {"escalão" : nota}
            aluno.update(dicNotas)
        elif media >= 9 and media < 13:
            nota = "C"
            dicNotas = {"escalão" : nota}
            aluno.update (dicNotas)
        elif media >= 13 and media <17:
            nota = "B"
            dicNotas = {"escalão" : nota}
            aluno.update (dicNotas)
        elif media >=17 and media <21:
            nota = "A"
            dicNotas = {"escalão" : nota}
            aluno.update (dicNotas)
    return lista


## Crie uma distribuição dos alunos por escalão;

def distriEscalao (lista):
    dic1 = {}
    for aluno in lista:
        if aluno ["escalão"] in dic1.keys():
            dic1[aluno ["escalão"]] = dic1[aluno ["escalão"]] + 1
        else:
            dic1[aluno ["escalão"]] = 1
    return dic1


def graficoBarras(distrib):
    fig1 = plt.figure(figsize = (20, 10))
    plt.bar(distrib.keys(), distrib.values(), color= "blue", width= 0.3)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.title("Gráfico da distribuição")
    plt.ylabel("Nº de Alunos")
    plt.show()
    return

def graficoLinha(distrib):
    fig1 = plt.figure(figsize = (20, 10))
    plt.plot(distrib.keys(), distrib.values(), color= "blue")
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Gráfico da distribuição")
    plt.ylabel("Nº de Alunos")
    plt.show()
    return

def distribTabela (distrib):
    for aluno in distrib.keys():
        print(f"{aluno:<7} => {distrib[aluno]:<10}")

def menu():
    print('''\nMenu:
(1) Ver menu
(2) Ver alunos por curso
(3) Média das notas dos alunos
(4) Escalão dos alunos
(5) Ver distribuição dos alunos por cursos
(6) Ver distribuição dos escalões de notas
(7) Ver gráficos da distribuição dos alunos por cursos
(8) Ver gráficos da distribuição de escalões
(0) Sair''')
    return




