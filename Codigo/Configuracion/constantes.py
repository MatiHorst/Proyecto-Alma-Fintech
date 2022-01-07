"""
constantes.py
Dicho modulo contiene los valores constantes que se utilizan en la ejecución del bot.

"""

import pyRofex

# Instrumentos a los que se suscribe
instruments = ["GGAL/FEB22", "YPFD/FEB22", "DLR/FEB22", "DLR/MAY22", "PAMP/FEB22"]

# Entradas que se desea obtener de los instrumentos a lo que se subscribe
entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.OFFERS]

