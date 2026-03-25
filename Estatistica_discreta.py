from math import sqrt
import pandas as pd

# Dados que serão trabalhados
lista = [1, 2, 3, 4, 5, 2, 2, 2, 3, 4, 9, 10, 17]
print(f'Dados puros: {lista}')

# Rol da lista de números (organiza em ordem crescente).
lista.sort()
print(f'Dados organizados pelo ROL: {lista}')

# Número de classes (processo para obter o número de classes dessa lista de dados).
quantidade_elementos = len(lista) # Quantidade de elementos de uma lista.
numero_de_classes = sqrt(quantidade_elementos) # Número de classes em que a lista vai ser dividida.
arredondamento_numero_classes = round(numero_de_classes) # Arredonda as raízes quadradas não exatas para números sem vírgula.
print(f'Número de classes que vai ter: {arredondamento_numero_classes}')

# Amplitude Total.
primeiro_valor = lista[0]
ultimo_valor = lista[quantidade_elementos-1]
amplitude_total = ultimo_valor - primeiro_valor # Valor da amplitude total.
print(f'Amplitude total: {amplitude_total}')

# Amplitude de cada classe.
# Fórmula para isso -> amplitude total / número de classes-1
amplitude_classe = round(amplitude_total / (arredondamento_numero_classes - 1), 2)
print(f'Amplitude de cada classe: {amplitude_classe}')


# ===== DEFINIÇÃO DOS LIMITES DAS CLASSES ======
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

colunas = ['Classe', 'LI', 'LS', 'PM']
df = pd.DataFrame(lista2, columns=colunas)
print(df)




