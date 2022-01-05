"""
ProyectoAlma.py
Script de un bot con el que se busca oportunidad de arbitraje de tasas de interés.
Se utiliza conexión websocket con datos en tiempo real.
"""

import pyRofex
import tasas
import spot
import re

# Mensaje de bienvenida
print(" "*65 + "Alma fintech ")
print("Inicializando Bot...\n")

# Inicializo el ambiente
pyRofex.initialize(user="xxxxxx", password="xxxxxx", account="xxxxx", environment=pyRofex.Environment.REMARKET)


# Defino como voy a manejar del mensaje recibido
def market_data_handler(message):
    print("-" * 60)
    # Se muestra por consola a que instrumento pertenecen los datos del mensaje recibido
    instrumento = message["instrumentId"]["symbol"]
    print(f'Instrumento: {instrumento}')
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
    if(precio_bid == None):
        print("No se puede calcular la tasa tomadora.")
    else:
        tasaTomadora = tasas.calculoTasa(precio_spot, precio_bid, dias)
        print(f'Tasa tomadora: {tasaTomadora}')
    if(precio_ask == None):
        print("No se puede calcular la tasa colocadora.")
    else:
        tasaColocadora = tasas.calculoTasa(precio_spot, precio_ask, dias)
        print(f'Tasa colocadora: {tasaColocadora}')
    tasas.oportunidad(tasaTomadora, tasaColocadora)


# Se inicializa la conexión Websocket en el ambiente de prueba
pyRofex.init_websocket_connection(market_data_handler=market_data_handler)

# Instrumentos a los que se suscribe
instruments = ["GGAL/FEB22", "YPFD/FEB22", "DLR/FEB22", "DLR/MAY22", "PAMP/FEB22"]
# Entradas que se desea obtener de los instrumentos subscritos
entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.OFFERS]

# Se realiza la subscripción
pyRofex.market_data_subscription(tickers=instruments, entries=entries)

