"""
controlador.py
En este modulo se define la manera en la que se maneja el mensaje recibido a través de la conexión websocket.
"""

import tasas
import spot
import re

def market_data_handler(message):
    print("-" * 60)
    # Se muestra por consola a que instrumento pertenecen los datos del mensaje recibido
    instrumento = message["instrumentId"]["symbol"]
    print(f'\nInstrumento: {instrumento}')
    dias = tasas.calcularDias(instrumento)
    # Se acomoda el símbolo del instrumento para buscarlo en yahoo finance
    instrumento = re.split('/', instrumento)[0]
    if(instrumento != 'DLR'):
        instrumento = instrumento + '.BA'
    else:
        instrumento = 'DLR'
    # Se coloca la siguiente excepción por si el bid o el ask están vacíos
    precio_bid = None if not message["marketData"]["BI"] else message["marketData"]["BI"][0]["price"]
    precio_ask = None if not message["marketData"]["OF"] else message["marketData"]["OF"][0]["price"]
    print(f'Bid: {precio_bid}')
    print(f'Ask: {precio_ask}')
    # Se toma el valor spot de yahoo finance
    precio_spot = spot.yahoo(instrumento)
    print(f"Spot: {precio_spot}")
    # print(f'Dias: {dias}')
    # Se calculan las tasas implícitas
    if(precio_bid == None):
        print("No se puede calcular la tasa tomadora.")
    else:
        tasaTomadora = tasas.calculoTasa(precio_spot, precio_bid, dias)
        print(f'Tasa tomadora: {tasaTomadora}')
    if(precio_ask == None):
        print("No se puede calcular la tasa colocadora.\n")
    else:
        tasaColocadora = tasas.calculoTasa(precio_spot, precio_ask, dias)
        print(f'Tasa colocadora: {tasaColocadora}')
    tasas.oportunidad(tasaTomadora, tasaColocadora)
