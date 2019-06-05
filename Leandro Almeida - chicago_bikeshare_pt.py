# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
# Modulos importado para concluir a tarefa 13 adicionada por mim
from datetime import date
from math import floor

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for pos in range(20):
    print(f'Dado {pos+1}', end=' - ')
    print(data_list[pos + 1])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for pos in range(20):
    print(data_list[pos][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Funcao que converte os valores de uma couluna de dados em uma linha (lista) de dados

    Argumentos:
        :param data: Tabela de dados que sera convertida
        :param index: Coluna que sera convetida para lista (lembrar da indexacao por zero)

    Retorna:
        :return: Lista com os valores
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for pos in range(len(data)):
        column_list.append(data[pos][index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for pos in range(len(data_list)):
    if data_list[pos][6] != '':  # Executa a contagem de genero apenas se houver dado (diferente de vazio)
        if data_list[pos][6] == 'Male':
            male += 1
        elif data_list[pos][6] == 'Female':
            female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Funcao que retorna uma lista com o numero de Homens e Mulheres do conjunto de dados originais

    Argumentos:
        :param data_list: Lista com dos dados iniciais

    Retona:
        :return: Lista com o numero de homens e mulheres nesta ordem ([Homem, Mulher])
    """
    male = 0
    female = 0
    dado = column_to_list(data_list, 6)
    for pos in range(len(dado)):
        if dado[pos] != '':  # Executa a contagem de genero apenas se houver dado
            if dado[pos] == 'Male':
                male += 1
            elif dado[pos] == 'Female':
                female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Funcao que avalia qual o genero mais popular no conjunto de dados

    Argumentos:
        :param data_list: Lista de dados originais

    Retorna;
        :return: String com o genero mais comum
    """
    genero = count_gender(
        data_list)  # A funcao retorna a quantidade de homens na posicao [0] e de mulheres na posicao [1]

    if genero[0] > genero[1]:
        answer = 'Male'
    elif genero[0] < genero[1]:
        answer = 'Female'
    else:
        answer = 'Equal'

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_type(data_list):
    """
    Funcao que retorna uma lista com a contagem dos tipos de consumidores do conjunto de dados originais

    Argumentos:
    :param data_list: Lista com dos dados iniciais

    Retona:
        :return: Lista com o numero de cada tipo de consumidor)
    """

    data = column_to_list(data_list, -3)
    subscriber = customer = dependent = 0

    for pos in range(len(data)):
        if data[pos] != '':  # Executa a contagem do tipo de usuario apenas se houver dado (diferente de vazio)
            if data[pos] == 'Subscriber':
                subscriber += 1
            elif data[pos] == 'Customer':
                customer += 1
            elif data[pos] == 'Dependent':
                dependent += 1

    return [subscriber, customer, dependent]


user_type_list = column_to_list(data_list, -3)
types = ['Subscriber', 'Customer', 'Dependent']
quantity = count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.xlabel('Tipo de Cliente')
plt.ylabel('Quantidade')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Cliente')
plt.show(block=True)
print("\nTAREFA 7: Verifique o gráfico!")

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = ("Alguns clientes nao preencheram a informacao sobre o genero e por isso temos strings sem dado.\n"
          "Para que pudessemos comparar da forma proposta pela formula, nao deveria ser permitido nao informar o genero.\n"
          "Alternativamente, e mais recomendado, poderiamos adicionar a formula a quantidade de ocorrencias do genero em branco (male+female+blanks).")
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
def median (data):
    """
    Funcao para calcular a mediana de uma lista de dados

    Mediana e o valor central de um conjunto de dados ordenados.
    Caso o numero de dados seja impar o valor e o numero central. Caso seja par, o valor e a media dos valores centrais

    Argumentos
        :param data: lista de dados

    Retorna
        :return result: valor (float) da mediana
    """
    # Mediana e o valor central de um conjunto de dados ordenados.
    # Caso o numero de dados seja impar o valor e o numero central. Caso seja par, o valor e a media dos valores centrais
    if len(data) % 2 == 0:
        posicao_inferior = (len(data) // 2) - 1
        posicao_superior = (len(data) // 2)
        result = (data[posicao_inferior] + data[posicao_superior]) / 2
    else:
        posicao_central = (len(data) // 2)
        result = data[posicao_central]

    return result

trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = [float(x) for x in trip_duration_list]  # Altera os valores da lista de string para float
trip_duration_list.sort()  # Ordena a lista
min_trip = trip_duration_list[0]  # Na lista ordenada, a menor duracao e a primeira posicao da lista
max_trip = trip_duration_list[
    len(trip_duration_list) - 1]  # Na lista ordenada, a maior duracao e a ultima posicao da lista
mean_trip = 0.
median_trip = 0.
sum_trip = 0

for pos in range(len(trip_duration_list)):
    valor = trip_duration_list[pos]
    sum_trip += valor  # Variavel para termos a soma de todos os valores para calcular a media

mean_trip = sum_trip / len(trip_duration_list)  # Media e a soma dos valores dividido pela quantidade de valores

median_trip = median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

#input("Aperte Enter para continuar...")

# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
'''
def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """
'''
input("Aperte Enter para continuar...")

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
# print("Você vai encarar o desafio? (yes ou no)")
answer = input("Você vai encarar o desafio (yes ou no)? ")


def count_items(column_list):
    """
    Funcao que analisa uma lista e retorna os valores contidos e a contagem de ocorrencia de cada um deles.

    Argumentos:
        :param column_list: Lista com dos dados que serao analisados

    Retorna:
        :return item_types, count_items: Lista com os valores contidos e outra lista com o numero de ocorrencias de
        cada um deles (respectivamente)
    """

    count_items = []
    item_types = list(set(column_list))
    for type in item_types:
        count_items.append(column_list.count(type))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -3)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

print('\nTarefa extra adicionada por Leandro Almeida - Criar um grafico que mostre a quantidade de clientes por faixa etaria')

input('Aperte Enter enter para continuar')

# TAREFA 13 - Adicionada pelo aluno
# TODO: Crie um grafico que mostre a quantidade de clientes por faixa etaria
print('\nTAREFA 13: Gerando grafico da quantidade por faixa etaria')
def count_age_interval(data: list, interval: int = 10) -> object:
    """
    Funcao para retornar as faixas etarias e a quantidade de clientes em cada faixa

    Argumentos:
        :param data: Lista com as idades dos clientes
        :param interval: Intervalo das faixas etarias (10 anos se omitido)

    Retorno:
        :return: Sao retornadas duas listas: uma com as faixas etarias, outra com as quantidades por faixa etaria, respectivamente
    """

    ages = list(set(data))  # Lista do conjunto de todas as idades
    ages.sort()  # Organizando a lista para o caso do conjunto resultar em dados desordenados

    upper_range = floor(ages[len(ages) - 1] / interval)  # O numero de faixas etarias e definido pela maior
    # idade (ultima posicao da lista) dividido pelo intervalo

    age_range = []  # Lista que retorna as faixas etarias
    counter = []  # Lista que retorna a contagem de clientes
    for age in range(upper_range + 1):
        age_low = age * interval  # Menor idade do intervalo
        age_high = age_low + (interval - 1)  # Maior idade do intervalo
        age_limits = [age_low, age_high]  # Lista com as idades limites do intervalo
        age_range.append(str(age_limits[:]))  # Lista com todos os intervalos de idade
        age_limits.clear()  # Limpa a lista com os limites para a proxima iteracao
        counter.append(
            0)  # Cria a lista que vai retornar a quantidade por faixa etaria com valor "zero" em todas as posicoes

    for age in data:  # Itera por toda a lista de idades
        define_interval = floor(age / interval)  # Define qual a posicao do intervalo da idade lida
        counter[define_interval] += 1  # Soma uma unidade a quantidade de clientes do intervalo

    return age_range, counter


birth_list = column_to_list(data_list, -1)  # Converte a coluna do ano de nascimento para uma lista
birth_list = [float(birth) for birth in birth_list if bool(birth)]  # Converte o dado para o tipo float

age_list = [date.today().year - birth for birth in birth_list if bool(birth)]  # Lista com as idades dos usuarios

x_title, quantity = count_age_interval(age_list)

print("\nTAREFA 13: Verifique o gráfico!")

# Codigo para gerar o grafico
y_pos = list(range(len(x_title)))
plt.bar(y_pos, quantity)
plt.xlabel('Faixa Etaria')
plt.ylabel('Quantidade')
plt.xticks(y_pos, x_title)
plt.title('Quantidade de Clientes por Faixa Etaria')
plt.show(block=True)
