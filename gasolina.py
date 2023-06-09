import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv('./gasolina.csv', sep=',')
with sns.axes_style('darkgrid'):
  fig, ax = plt.subplots(figsize=(15/2.54, 8/2.54))
  sns.set_context('talk', font_scale= 0.75, rc={'lines.linewidth': 3})
  graf_gas = sns.lineplot(data=df_gasolina, x='dia', y='venda', ax=ax)
  graf_gas.set(title='Gasolina no mês de Julho', xlabel='Dia', ylabel='Preço')
  plt.savefig('gasolina.png')
  