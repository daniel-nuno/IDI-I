# %%
import pandas as pd

df_vt = pd.read_excel('C:/Users/nuno/Downloads/datosCT.xlsx', 'vt')

df_vt = df_vt.rename(columns={'Unnamed: 0': 'Mes'})
df_vt['Ingreso'] = df_vt['Ingreso'] + 1000

# %%
df_vt['Utilidad'] = df_vt['Ingreso'] - df_vt['Gasto']
# %%
avr_gasto = df_vt[df_vt['Utilidad'] <= 0]['Gasto'].mean()
# %%
ingreso_anual = df_vt['Ingreso'].sum()
# %%
meses_utilidad_positiva = df_vt[df_vt['Utilidad'] >= 0]['Mes']
# %%

df_8c = pd.read_excel('C:/Users/nuno/Downloads/datosCT.xlsx', '8c', index_col=0)
# %%
df_8c = df_8c.div(1.609)
# %%
gdl = df_8c['GDL']
from_gdl_over1000 = gdl[gdl >= 1000]