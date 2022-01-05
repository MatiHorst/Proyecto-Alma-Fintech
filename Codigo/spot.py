"""
spot.py
Modulo para obtener el precio spot.
Se crea un objeto en el que se asigna la información del instrumento que se necesita, y luego se extrae el precio spot.
"""

import yfinance as yf

def yahoo(instrumento):
    elemento = yf.Ticker(instrumento)
    for key, value in elemento.info.items():
        if (key == 'regularMarketPrice'):
            priceElem = value
            return priceElem
