# Gabriel Henrique Costa Cruzeiro - SC3037851
# Pedro Candido Salvio - SC3037126
from math import sqrt

class Flor:
    sepal_length = -1
    sepal_width = -1
    petal_length = -1
    petal_width = -1
    name = ""


#CRIA FUNÇÃO QUE LÊ O ARQUIVO
def ler_arquivo(nome_arq):
    flores = []
    with open(nome_arq, "r") as arq:
        for linha in arq:
            info = linha.strip().split(',')
            f = Flor()
            f.sepal_length = float(info[0])
            f.sepal_width = float(info[1])
            f.petal_length = float(info[2])
            f.petal_width = float(info[3])
            f.name = info[4]
            flores.append(f)
    return flores


#CRIA FUNÇÃO QUE CALCULA A DISTÂNCIA EUCLIDIANA
def distancia_euclidiana(flor_d, flor_c):
    sepal_length1 = flor_d.sepal_length
    sepal_width1 = flor_d.sepal_width
    petal_length1 = flor_d.petal_length
    petal_width1 = flor_d.petal_width

    sepal_length2 = flor_c.sepal_length
    sepal_width2 = flor_c.sepal_width
    petal_length2 = flor_c.petal_length
    petal_width2 = flor_c.petal_width

    dist_euclidiana = sqrt(((sepal_length1 - sepal_length2)**2) +
                           ((sepal_width1 - sepal_width2)**2) +
                           ((petal_length1 - petal_length2)**2) +
                           ((petal_width1 - petal_width2)**2))

    return dist_euclidiana



#CRIA FUNÇÃO PARA COLOCAR A ESPÉCIE NA DISTANCIA EUCLIDIANA CERTA USANDO MATRIZES E LAMBDA
def calcular_especies(flores_desconhecidas, flores_conhecidas):
    nomes = []
    for flor_des in flores_desconhecidas:
        distancias = []
        for flor_con in flores_conhecidas:
            #CHAMA A FUNÇÃO DISTÂNCIA EUCLIDIANA NO CÓDIGO
            dist_euclidiana = distancia_euclidiana(flor_des, flor_con)
            distancias.append((flor_con.name, dist_euclidiana))
        nomes.append(distancias)
    
    ordenado = []
    for distancias in nomes:
        distancias_ordenadas = sorted(distancias, key=lambda valor: valor[1])
        ordenado.append(distancias_ordenadas)
    
    return ordenado

#VERIFICA O NOME QUE MAIS APARECE ENTRE OS "K"
def frequencia(matriz, k):
    versicolor_cont = 0
    setosa_cont = 0
    virginica_cont = 0
    
    for i in range(k):
        especie = matriz[i][0]
        if "versicolor" in especie:
            versicolor_cont += 1
        elif "setosa" in especie:
            setosa_cont += 1
        elif "virginica" in especie:
            virginica_cont += 1
    
    if versicolor_cont > setosa_cont and versicolor_cont > virginica_cont:
        return "versicolor"
    elif setosa_cont > versicolor_cont and setosa_cont > virginica_cont:
        return "setosa"
    else:
        return "virginica"

def main():
    flores_conhecidas = ler_arquivo("iris.data.csv")
    try:
        k = int(input("Valor de k (insira um valor numérico inteiro): "))
        arquivo = input("Nome do arquivo: ")
        flores_desconhecidas = ler_arquivo(arquivo)
    except:
        print("ERRO: Não foi possível realizar a operação.")
    else:
        distancias = calcular_especies(flores_desconhecidas, flores_conhecidas)
        i = 1
        for dist in distancias:
            especie = frequencia(dist, k)
            print(f"Flor {i} é {especie}")
            i += 1

main()