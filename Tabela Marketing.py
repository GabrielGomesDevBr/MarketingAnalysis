#!/usr/bin/env python
# coding: utf-8

# # Fazendo análise de dados (Marketing Analytics)
# ## Banco de Dados Fictício: Marketing Analytics)
# ### Questionamentos para Análise:
# 
# ### Perfil Demográfico:
# 
# ### Qual a faixa etária média dos clientes?
# 
# ### Qual é a distribuição de gênero entre os clientes?
# 
# ### Desempenho do Produto:
# 
# ### Qual produto tem a maior média de valor gasto?
# 
# ### Qual é o produto mais vendido?
# 
# ### Canais de Venda:
# 
# ### Qual canal de venda gera mais receita?
# 
# ### Qual canal de venda é mais popular entre diferentes faixas etárias?
# 
# ### Geografia:
# 
# ### Qual cidade contribui mais para as vendas totais?
# 
# ### Existe alguma diferença no padrão de compras entre cidades?
# 
# ### Comportamento Temporal:
# 
# ### Como as vendas variam ao longo do tempo?
# 
# ### Existe uma sazonalidade nas compras?

# In[187]:


#Criando dados utilizando o faker.
import pandas as pd
import numpy as np
from faker import Faker
import random
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')

# Configurar o Faker para gerar dados fictícios
fake = Faker()

# Criar uma lista para armazenar os dados
dados = []

# Gerar 100 linhas de dados fictícios
for _ in range(100):
    cliente_id = _ + 1
    nome_cliente = fake.name()
    idade = random.randint(18, 60)
    genero = random.choice(['Masculino', 'Feminino'])
    cidade = fake.city()
    produto = random.choice(['Camiseta', 'Tênis', 'Calça Jeans'])
    valor_gasto = round(random.uniform(20.00, 150.00), 2)
    data_compra = fake.date_between(start_date='-6M', end_date='today')
    canal_venda = random.choice(['Loja Física', 'Online'])

    dados.append([cliente_id, nome_cliente, idade, genero, cidade, produto, valor_gasto, data_compra, canal_venda])

# Criar um DataFrame com os dados
df = pd.DataFrame(dados, columns=['ID Cliente', 'Nome Cliente', 'Idade', 'Gênero', 'Cidade',
                                   'Produto Comprado', 'Valor Gasto (R$)', 'Data da Compra', 'Canal de Venda'])

# Exibir o DataFrame
print(df)


# In[188]:


#Verificando as primeiras linhas do data frame do data frame 
df.head()


# In[189]:


#Verificando as últimas linhas do data frame 
df.tail()


# In[190]:


#Verificando a quantidade de linhas nas uas respectivas colunas
df.count()


# In[191]:


#verificando valores vazios (nulos)
df.isnull().sum()


# In[192]:


#verificando as colnuas
df.columns


# In[193]:


#verificando a classe de cada coluna
df.dtypes


# In[194]:


#Verificando o data frame com um todo.
df.describe


# In[195]:


#Renomear colunas para que não existam espaços vazios, substituindo-os por underscore, oque vem a:
#Facilidade de Acesso:

# Colunas sem espaços podem ser acessadas de maneira mais fácil e intuitiva,
# sem a necessidade de uso de aspas ou de colchetes.

# Compatibilidade com Funções e Métodos:
# Algumas funções e métodos em Python podem não lidar bem com espaços nos nomes
# das colunas. Ter nomes de colunas sem espaços aumenta a compatibilidade e evita possíveis erros.

# Sintaxe Mais Limpa:
# Nomes de colunas sem espaços proporcionam uma sintaxe mais limpa e legível,
# tornando o código mais fácil de entender.

# Consistência:
# Manter uma convenção consistente, como usar underscores (_) em vez de espaços,
# ajuda a tornar o código mais uniforme e facilita a colaboração com outros desenvolvedores.


df = df.rename(columns={'ID Cliente':'ID_Cliente', 
                  'Nome Cliente':'Nome_Cliente', 
                  'Idade':'Idade', 
                  'Gênero':'Gênero', 
                  'Cidade':'Cidade',
                  'Produto Comprado':'Produto_Comprado', 
                  'Valor Gasto (R$)':'Valor_Gasto_(R$)', 
                  'Data da Compra':'Data_da_Compra', 
                  'Canal de Venda':'Canal_de_Venda'})
     


# In[196]:


#Verificando se as alterações nos nomes das colunas ficaram de acordo
df


# In[197]:


#Estatísticas Descritivas
df.describe()


# In[198]:


# Gráfico de distribuição da Idade
sns.histplot(df['Idade'], bins=10, kde=True)
plt.title('Distribuição de Idades')
plt.show()


# In[199]:


# Contagem de Gênero
sns.countplot(x='Gênero', data=df)
plt.title('Contagem por Gênero')
plt.show()


# In[200]:


# Contagem de Produtos Comprados
sns.countplot(x='Produto_Comprado', data=df)
plt.title('Contagem por Produto')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[201]:


# Boxplot do Valor Gasto por Canal de Venda
sns.boxplot(x='Canal_de_Venda', y='Valor_Gasto_(R$)', data=df)
plt.title('Boxplot do Valor Gasto por Canal de Venda')
plt.show()


# In[202]:


# Gráfico de distribuição da Idade
sns.histplot(df['Gênero'], bins=10, kde=True)
plt.title('Distribuição de Gênero') 
plt.ylabel = ('Contagem')
plt.show()


# In[203]:


# Calcular a faixa etária média dos clientes
faixa_etaria_media = df['Idade'].mean()

# Imprimir o resultado
print(f'A faixa etária média dos clientes é: {faixa_etaria_media:.2f} anos')


# In[204]:


# Calcular a faixa etária média dos clientes
faixa_etaria_media = df['Idade'].mean()

# Gráfico de Barra
plt.figure(figsize=(8, 6))
sns.barplot(x=['Faixa Etária Média'], y=[faixa_etaria_media], palette='pastel')
plt.title('Faixa Etária Média dos Clientes')
plt.show()


# In[205]:


#Qual produto tem a maior média de valor gasto?

# Agrupar por produto e calcular a média de valor gasto
media_valor_por_produto = df.groupby('Produto_Comprado')['Valor_Gasto_(R$)'].mean().reset_index()

# Encontrar o produto com a maior média de valor gasto
produto_maior_media = media_valor_por_produto.loc[media_valor_por_produto['Valor_Gasto_(R$)'].idxmax()]

# Gráfico de Barra
plt.figure(figsize=(10, 6))
sns.barplot(x='Produto_Comprado', y='Valor_Gasto_(R$)', data=media_valor_por_produto, palette='pastel')
plt.title('Média de Valor Gasto por Produto')


# Destacar o produto com maior média
plt.annotate(f'Maior Média: {produto_maior_media["Produto_Comprado"]}', 
             xy=(produto_maior_media.name, produto_maior_media['Valor_Gasto_(R$)']),
             xytext=(10, 10),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.show()


# In[ ]:





# In[207]:


# Agrupar por cidade e calcular as vendas totais
vendas_por_cidade = df.groupby('Cidade')['Valor_Gasto_(R$)'].sum().reset_index()

# Encontrar a cidade com maior contribuição para as vendas
cidade_maior_contribuicao = vendas_por_cidade.loc[vendas_por_cidade['Valor_Gasto_(R$)'].idxmax()]

# Gráfico de Barra
plt.figure(figsize=(18, 9))
sns.barplot(x='Cidade', y='Valor_Gasto_(R$)', data=vendas_por_cidade, palette='pastel')
plt.title('Vendas por Cidade')


# Destacar a cidade com maior contribuição
plt.annotate(f'Maior Contribuição: {cidade_maior_contribuicao["Cidade"]}', 
             xy=(cidade_maior_contribuicao.name, cidade_maior_contribuicao['Valor_Gasto_(R$)']),
             xytext=(10, 10),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.xticks(rotation=45, ha='right')
plt.show()



# In[209]:


# Calcular a média de valor gasto por cidade
media_valor_por_cidade = df.groupby('Cidade')['Valor_Gasto_(R$)'].mean().reset_index()

# Gráfico de Barra para comparar padrões de compras entre cidades
plt.figure(figsize=(24, 12))
sns.barplot(x='Cidade', y='Valor_Gasto_(R$)', data=media_valor_por_cidade, palette='pastel')
plt.title('Média de Valor Gasto por Cidade')

plt.xticks(rotation=45, ha='right')
plt.show()


# In[211]:


# Converter a coluna 'Data_da_Compra' para o formato de data
df['Data_da_Compra'] = pd.to_datetime(df['Data_da_Compra'])

# Agrupar por data e calcular as vendas totais
vendas_por_data = df.groupby('Data_da_Compra')['Valor_Gasto_(R$)'].sum().reset_index()

# Gráfico de Linha
plt.figure(figsize=(12, 6))
sns.lineplot(x='Data_da_Compra', y='Valor_Gasto_(R$)', data=vendas_por_data, marker='o', color='b')
plt.title('Variação das Vendas ao Longo do Tempo')
plt.xlabel('Data da Compra')

plt.xticks(rotation=45, ha='right')
plt.show()


# In[212]:


import statsmodels.api as sm

# Converter a coluna 'Data_da_Compra' para o formato de data
df['Data_da_Compra'] = pd.to_datetime(df['Data_da_Compra'])

# Agrupar por data e calcular as vendas totais
vendas_por_data = df.groupby('Data_da_Compra')['Valor_Gasto_(R$)'].sum().reset_index()

# Configurar a coluna 'Data_da_Compra' como índice
vendas_por_data = vendas_por_data.set_index('Data_da_Compra')

# Decomposição da série temporal com período diário
decomposicao = sm.tsa.seasonal_decompose(vendas_por_data, model='additive', period=1)

# Gráficos da decomposição
plt.figure(figsize=(12, 8))

# Série Temporal Original
plt.subplot(411)
plt.plot(vendas_por_data, label='Original')
plt.legend(loc='upper left')
plt.title('Série Temporal Original')

# Tendência
plt.subplot(412)
plt.plot(decomposicao.trend, label='Tendência')
plt.legend(loc='upper left')
plt.title('Tendência')

# Sazonalidade
plt.subplot(413)
plt.plot(decomposicao.seasonal, label='Sazonalidade')
plt.legend(loc='upper left')
plt.title('Sazonalidade')

# Resíduos
plt.subplot(414)
plt.plot(decomposicao.resid, label='Resíduos')
plt.legend(loc='upper left')
plt.title('Resíduos')

plt.tight_layout()
plt.show()


# In[ ]:




