from math import sqrt
import pandas as pd

# Dados que serão trabalhados
lista = [1, 2, 6, 4, 5, 2, 2, 2, 3, 4, 11, 9, 12,  17, 18, 19, 18]
print(f'Dados puros: {lista}')

# Rol da lista de números (organiza em ordem crescente).
lista.sort()
print(f'Dados organizados pelo ROL: {lista}')

# Número de classes (processo para obter o número de classes dessa lista de dados).
quantidade_elementos = len(lista) # Quantidade de elementos na lista.
numero_de_classes = sqrt(quantidade_elementos) # Número de classes em que a lista vai ser dividida.
arredondamento_numero_classes = round(numero_de_classes) # Arredonda as raízes quadradas não exatas para números sem vírgula.
print(f'Número de classes que vai ter: {arredondamento_numero_classes}')

#definir uma lista como números ordinais das classes.
lista_ordinal_classe = list(range(arredondamento_numero_classes, 0, -1))
lista_ordinal_classe = lista_ordinal_classe[::-1]

# Amplitude Total.
primeiro_valor = lista[0]
ultimo_valor = lista[quantidade_elementos-1]
amplitude_total = ultimo_valor - primeiro_valor # Valor da amplitude total.
print(f'Amplitude total: {amplitude_total}')

# Amplitude de cada classe.
# Fórmula para isso -> amplitude total / número de classes-1
amplitude_classe = round(amplitude_total / (arredondamento_numero_classes - 1), 2)
print(f'Amplitude de cada classe: {amplitude_classe}')
print('')


#=============Distribuição de Frequência por Classes=============

# Limite Inferior (LI)
LI = round((primeiro_valor - (amplitude_classe/2)), 2)

# Limite Superior (LS)
LS = round((LI + amplitude_classe), 2)

# Ponto médio (PM)
PM = round((LI + LS) / 2, 2)

lista2 = []
contador = 1
while contador < arredondamento_numero_classes + 1:

    lista1 = []
    lista1.extend([contador, LI, LS, PM])
    lista2.append(lista1)

    LI += amplitude_classe
    LS += amplitude_classe
    PM += amplitude_classe


    contador += 1

print('========Distribuição de Frequência por Classes==========')
colunas = ['Classe', 'LI', 'LS', 'PM']
df = pd.DataFrame(lista2, columns=colunas)
print(df)


# =============Distribuição das Classes=============

#Resetar valores.
# Limite Inferior (LI)
LI = round((primeiro_valor - (amplitude_classe/2)), 2)
# Limite Superior (LS)
LS = round((LI + amplitude_classe), 2)

lista_classe = []
contador = 1
while contador < arredondamento_numero_classes + 1:
    lista_classe_atual = []

    for i in lista:
        if LI < i <= LS:
            lista_classe_atual.append(i)

    lista_classe.append(lista_classe_atual)

    contador += 1
    LI += amplitude_classe
    LS += amplitude_classe

print('')
print("============Distribuição das Classes==========")

#Tranformando a lista em um dicionario para usar o pandas.
dados_formatados = [
    {"Classe": i + 1, "Valores": x}
    for i, x in enumerate(lista_classe)
]

df = pd.DataFrame(dados_formatados)
print(df)


#=============Frequência dos dados==========

fi = 0 #Frequência Absoluta
lista_frequencia_absoluta = [] # Iniciando a lista onde vai ficar os valores da Frequência Absoluta.
fr = 0 #Frequência Relativa
lista_frequencia_relativa = [] #Iniciando a lista onde vai ficar os valores da Frequência Relativa

#Frequência Absoluta
for sublista in lista_classe:
    fi = len(sublista)
    lista_frequencia_absoluta.append(fi)

#Frequência Relativa
for numero in lista_frequencia_absoluta:
    fr = numero/quantidade_elementos
    lista_frequencia_relativa.append(fr)

#Tabela da LI e LS
print('')
print('============Tabela da Frequência============')
dados_formatados = {
     'Classe': lista_ordinal_classe,
     'FI': lista_frequencia_absoluta,
     'FS': lista_frequencia_relativa,
}

df = pd.DataFrame(dados_formatados)
print(df)

# Verificação
PFS = df["FS"].sum() # Prova real da Frequência relativa
print(f'Se a soma de todos os valores de FS (Frequẽncia Relativa) for menor que 1, algo deu errado: Resultado da soma: {PFS}')
