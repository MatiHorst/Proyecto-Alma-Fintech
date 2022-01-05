"""
tasas.py
Modulo para calcular los dias del periodo al plazo futuro. Las tasas implícitas, es decir, tasa tomadora y colocadora. Y
también para verificar si existe oportunidad de arbitraje partiendo de un criterio de diseño.
"""

from datetime import date
import re

# Función para obtener los dias del periodo del interés
def calcularDias(instrumento):
    mes = re.search('/(.+?)22',instrumento).group(1)
    meses = {'ENE':1, 'FEB':2, 'MAR':3, 'ABR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AGO':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DIC':12}
    dia_fin = date(2022, meses.get(mes), 1)
    return (dia_fin - date.today()).days


# Función para calcular la tasa nominal anual según el precio spot y futuro
def calculoTasa(spot, futuro, dias=1):
    TNA = ((futuro/spot)-1)*(365/dias)
    return round(TNA,2)


# Función para indicar si hay o no oportunidad de arbitraje de tasas
def oportunidad(tasaTomadora, tasaColocadora):
    if(tasaColocadora > 0 and tasaTomadora > 0 and (tasaColocadora-tasaTomadora) > 0.05):
        print('-¡Hay oportunidad de arbitraje!-\n')
    else:
        print('-¡No hay oportunidad de arbitraje!-\n')

