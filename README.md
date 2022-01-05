# Proyecto-Alma-Fintech
Bot para buscar oportunidades de arbitraje de tasas de interés. Haciendo uso de la plataforma remarkets de rofex, utilizando conexión websocket.



## Paquetes necesarios
Para su ejecución es necesario contar con los siguientes paquetes instalados:
-	pyRofex
-	yfinance
-	re
-	datetime
-	unittest


## Uso
En el archivo principal llamado “ProyectoAlma.py”, se debe inicializar el entorno de pyRofex mediante las credenciales de nuestra propia cuenta test en remarkets. Esto se realiza de la siguiente manera:.

```python
pyRofex.initialize(user="XXXXXX", password="xxxxxx", account="xxxxxx", environment=pyRofex.Environment.REMARKET)
```

Lo que sigue es el manejo del mensaje que recibe mediante la conexión websocket:

```python
def market_data_handler(message):
	…
```

En este se muestra el instrumento del que se trata por consola, se calculan los días que nos interesan para el calculo posterior de los intereses usando el mismo string del simbolo del instrumento futuro. Luego se adapta ese símbolo al nombre correspondiente para extraer el precio spot de yahoo finance mediante el módulo “spot.py.
Se obtiene el precio bid y ask de la plataforma de remarkets y se procede a calcular la tasa de interés colocadora y tomadora, así como la oportunidad de arbitraje de tasas.
Esto último se realiza con ayuda del módulo “tasas.py”. El mismo contiene las funciones para: obtener los días del plazo a futuro del instrumento en análisis, el calculo de las tasas implícitas, y ver si hay o no oportunidad de arbitraje.
Por último, se tiene el archivo “test_tasa.py” con el cual se realiza un test unitario sobre la función que calcula las tasas implícitas del módulo “tasas.py”.


## Ejemplo de salida
Para el caso del instrumento YPF , se tiene una salida como la siguiente:

```python
Instrumento: YPFD/FEB22
Bid: 900.75
Ask: 905.0
Spot: 843.9
Tasa tomadora: 0.91
Tasa colocadora: 0.98
-¡Hay oportunidad de arbitraje!-
```

