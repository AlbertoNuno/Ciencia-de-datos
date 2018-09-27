# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc

from myLib import mylib
import string
#%%definición de funciones 
def count_values(x,parameter):
    counter=0
    size=len(x)
    for i in range (size):
        if(x[i]==parameter):
            counter =counter+1  
    return counter 

#%%importacion de datos
 '../Data/datos_proyecto1.csv'
data = pd.read_csv( '../Data/datos_proyecto1.csv', encoding ='latin1')
data = data.iloc[:,0:7]

#%%repote de calidad de los datos
dqr= mylib.dqr(data)

#%%eliminación de datos nulos
data=data.dropna()
#%%lEstadísticas de los datos

plantel_c= pd.DataFrame(data['Plantel'])
modelo_c =  pd.DataFrame(data['Modelo educativo'])
clave_c=  pd.DataFrame(data['Clave de la carrera'])
carrera =  pd.DataFrame(data['Carrera Profesional Tecnico -Bachiller'])
matricula = pd.DataFrame(data['Matricula'])
periodo =  pd.DataFrame(data['Periodo'])




                 


 #%% conteo de valores únicos de cada columa del dataframe original


#%% 
alumnos = pd.DataFrame()
alumnos = carrera.join(matricula)
#%%

n_carreras = len(matricula)
plt.bar(np.arange(n_carreras),matricula.iloc[:,0])
plt.show()
    
    




