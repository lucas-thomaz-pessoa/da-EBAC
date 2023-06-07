import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv('./gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
  fig, ax = plt.subplots(figsize=(10/2.54, 10/2.54))
  graf_gas = sns.lineplot(data=df_gasolina, x='dia', y='venda', ax=ax)
  graf_gas.set(title='Gasolina no mês de Julho', xlabel='Dia', ylabel='Preço de venda')
  plt.savefig('gasolina.png')
