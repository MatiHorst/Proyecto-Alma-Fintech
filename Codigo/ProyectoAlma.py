"""
ProyectoAlma.py
Script de un bot con el que se busca oportunidad de arbitraje de tasas de interés.
Se utiliza conexión websocket con datos en tiempo real.
"""

import pyRofex
import controlador
from Configuracion import cuenta
from Configuracion import constantes

# Mensaje de bienvenida
print(" "*65 + "Alma fintech ")
print("Inicializando Bot...\n")

# Inicializo el ambiente
pyRofex.initialize(cuenta.user, cuenta.password, cuenta.account, pyRofex.Environment.REMARKET)

# Se inicializa la conexión Websocket en el ambiente de prueba
pyRofex.init_websocket_connection(market_data_handler = controlador.market_data_handler)

# Se realiza la subscripción
pyRofex.market_data_subscription(tickers = constantes.instruments, entries = constantes.entries)
