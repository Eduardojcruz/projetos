import fundamentus
import pandas as pd
import matplotlib.pyplot as plt

df = fundamentus.get_resultado()

'''df.loc[['ABCB4', 'GNDI3'],['pl']] #trazer algo de uma empresa e qual indicador'''
filtro2 = df[(df.pl > 0) & (df.dy > 0.05) & (df.mrgebit > 0.3)]
filtro2.sort_values('dy', ascending = False, inplace = True)
plt.figure(figsize = (18, 8))
plt.bar(filtro2.index, filtro2.dy)
plt.xticks(rotation = 45)
plt.title("Ações com P/L maior que 0, margem Ebit maior que 30% e DY acima de 5%, ordenadas por DY")