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
En el archivo principal llamado “ProyectoAlma.py”, se debe inicializar el entorno de pyRofex mediante las credenciales de nuestra propia cuenta test en remarkets. Esto se realiza de la siguiente manera:

```python
pyRofex.initialize(user="XXXXXX", password="xxxxxx", account="xxxxxx", environment=pyRofex.Environment.REMARKET)
```

Se debe tener en cuenta que en vez de las "xxxxx", van los valores correspondientes. Los valores de dichas credenciales estan guardados en el archivo "cuenta.py" dentro de la carpeta "Configuracion". 

Posteriormente, se realiza la conxion websocket:

```python
pyRofex.init_websocket_connection(market_data_handler = controlador.market_data_handler)
```

Donde se le pasa como parametro, la función que se encarga del manejo del mensaje recibido. La misma se encuentra definida en el archivo "controlador.py".
Lo que se hace en dicho control es tomar el simbolo del instrumento del cual se recibe el mensaje para indicar por consola de que intrumento se trata. Luego se calculan los dias del periodo entre el  instrumento actual y su futuro, mediante la funcion dias la cual es definida en el archivo "tasas.py".
Del mismo mensaje recibido se extrae el valor BID y ASK que son los que nos interesan y se acomoda el nombre del simbolo para extraer el precio SPOT por medio de la funcion yahoo(instrumento), definida en "spot.py".
Se calculan las tasas implicitas y se verifica si hay o no oportunidad de arbitraje con las correspondientes funciones también definidas en "tasas.py".


Por último, se realiza la subscripción a los instrumentos solicitados a través de la siguiente linea:

```python
pyRofex.market_data_subscription(tickers = constantes.instruments, entries = constantes.entries)
```

Para realizar esta subscripción, se le pasa como primer parametro la lista de los intrumentos que se desean analizar y como segundo parametro las entradas que nos interesan, las cuales son los precios BID y ASK.
Estos valores que se pasan como parametros se almacenan en el archivo "constantes.py" dentro de la carpeta "Configuracion". 



## Ejemplo de salida
Para el caso del instrumento YPF , se tiene una salida como la siguiente en la prueba realizada:

```python
Instrumento: YPFD/FEB22
Bid: 900.75
Ask: 905.0
Spot: 843.9
Tasa tomadora: 0.91
Tasa colocadora: 0.98
-¡Hay oportunidad de arbitraje!-
```

