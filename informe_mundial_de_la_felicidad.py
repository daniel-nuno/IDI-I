# %%
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/nuno/Downloads/2020_report.csv')
data.info()
print(data.columns)
# %%

plt.figure()
msno.bar(data)
plt.show()

data1 = data.iloc[:,1:9]
# %%
media = data1.mean()
print(media)
# %%
plt.figure()
plt.scatter(np.arange(138), data1['happiness_score'])
plt.plot(np.arange(138), media[0]*np.ones(138),c='r')
plt.xlabel("Overall Rank")
plt.ylabel("Happiness score")
plt.show()
# %%
meadiana = data1.median()
print(meadiana)
# %%
plt.figure()
plt.scatter(np.arange(138), data1['happiness_score'])
plt.plot(np.arange(138), meadiana[0]*np.ones(138),c='b')
plt.xlabel("Overall Rank")
plt.ylabel("Happiness score")
plt.show()
# %%
moda = data1.mode()
print(moda)
# %%
resumen = data1.describe()
# %%
varianza = data1.var()
print(varianza)
# %%
plt.figure()
plt.scatter(np.arange(138), data1['happiness_score'])
plt.plot(np.arange(138), media[0]*np.ones(138),c='r')
plt.plot(np.arange(138), media[0]+varianza[0]*np.ones(138),c='g')
plt.plot(np.arange(138), media[0]-varianza[0]*np.ones(138),c='g')
plt.xlabel("Overall Rank")
plt.ylabel("Happiness score")
plt.show()
# %%
desviacion_estandar = data1.std()
print(desviacion_estandar)

# %%
plt.figure()
plt.scatter(np.arange(138), data1['happiness_score'])
plt.plot(np.arange(138), media[0]*np.ones(138),c='r')
plt.plot(np.arange(138), media[0]+desviacion_estandar[0]*np.ones(138),c='g')
plt.plot(np.arange(138), media[0]-desviacion_estandar[0]*np.ones(138),c='g')
plt.xlabel("Overall Rank")
plt.ylabel("Happiness score")
plt.show()
# %%
covarianza = data1.cov()
# %%
correlacion = data1.corr()
# %%
plt.figure()
sns.pairplot(data1)
plt.show()
# %%
plt.figure()
sns.heatmap(correlacion, annot=True,
            xticklabels=correlacion.columns,
            yticklabels=correlacion.columns,
            cmap='coolwarm')
plt.show()

# %%
