#Crie um DataFrame de exemplo com dados fictícios. 'Nome' 'Idade' 'Departamento' 'Salario'
#Exiba as primeiras linhas do DataFrame usando head() para entender a estrutura dos dados.

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Nome': ['Scott', 'Scarlett', 'Ellie', 'Ana', 'Pedro'],
    'Idade': [35, 28, 42, 30, 45],
    'Departamento': ['Vendas', 'RH', 'TI', 'Financeiro', 'Produção'],
    'Salario': [5000, 4500, 6000, 5500, 4800]
}

df = pd.DataFrame(dados)

print(df.head(5))

#Utilize info() para obter informações sobre as colunas e tipos de dados.

print(df.info())

#Selecione uma ou várias colunas específicas do DataFrame.

print()
print(df['Idade'])

# Filtrando o DataFrame com base em alguma condição
filtro_salario = df['Salario'] > 5000
print(df[filtro_salario])

#Crie uma nova coluna calculada com base em valores existentes.

df['Salario_anual'] = df['Salario'] * 12
print()
print(df)

#Visualize as estatísticas usando gráficos de barra, boxplot, histograma, etc. Visualização de Dados com Matplotlib: Crie um gráfico de linhas para visualizar uma tendência ao longo do tempo.

print("Visualizando estatísticas com gráficos:")

# Gráfico de barra

plt.bar(df['Nome'], df['Salario'])
plt.title('Salário por Funcionário')
plt.xlabel('Nome')
plt.ylabel('Salário')
plt.xticks(rotation=45)
plt.show()

# Gráfico de linha

import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios para simular uma tendência ao longo do tempo

dados_tendencia = {
    'Ano': [2018, 2019, 2020, 2021, 2022],
    'Vendas': [10000, 12000, 15000, 18000, 20000]
}
df_tendencia = pd.DataFrame(dados_tendencia)

plt.plot(df_tendencia['Ano'], df_tendencia['Vendas'], marker='o')
plt.title('Tendência de Vendas ao Longo do Tempo')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()
