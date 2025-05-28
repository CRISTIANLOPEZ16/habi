# Habi Backend Challenge

## Tecnologías Utilizadas

- **Python 3.11**
- **mysql-connector-python** (para conexión a MYSQL sin ORM)
- **pytest** (para pruebas unitarias)

## Enfoque

- **Sin frameworks ni ORMs:** Para poder solucionar la primera parte del ejercicio utilice HTTPServer para correr un servicio REST con un endpoint POST /propiedades el cual me recibe en un JSON city, year para el filtro de inmuebles. Como buena practica realice una separacion de capas, creando un modulo para la logica (model) y otro para la parte de la API (http o controller).
- **SQL puro:** Realicé una subconsulta en query_repository.py para obtener el identificador maximo de cada registro en el historico y asi poder extraer el ultimo estado de cada inmueble.
- **Pruebas unitarias:** Realicé algunas pruebas unitarias validando que no extrajera inmuebles que no cumplan con los criterios de búsqueda y que no contaran con estados diferentes a lo esperado asi mismo una prueba de integracion usando request.

## Realización
Utilice una herramienta de linea de comandos llamada uv con la cual hice la implementacion de mypy con el fin de tener un tipado estatico y algunas ayudas a la hora de escribir codigo, sin embargo tambien esta el archivo requirements.txt con las dependencias necesarias para correr el proyecto.

### ejecución
Crear un entorno virtual:
```
python -m venv venv
```

Instala las dependencias:
```
pip install -r requirements.txt
```
Ejecuta el main.py para iniciar el servidor:
```
python query/main.py
```

Ejecuta las pruebas:
```
pytest
```

## Estructura

- `/query/`: Servicio REST de consulta de inmuebles.
- `/like/`: Propuesta de modelo de datos para “Me gusta”.
- `/number/`: Solución al ejercicio de bloques numéricos.

---

## Diagrama ER y modelo SQL para “Me gusta”

Ver `/like/habi_db.png` y `/like/event.sql`.

### Explicación del modelo
Tome la desicion de optar por una tabla multifuncional donde se pudiera registrar diferentes tipo de eventos, con el fin de poder tener una tabla de rastreo y estadisticas o mejoras posibles para la herramienta, yo imagine esta tabla como una especie de log para identificar interes del usuario sobre la propiedad, donde se pudiera registrar, comentarios, vistas, clicks, mapas de calor y por supuesto los "me gusta" que es lo que se pide en el ejercicio. Esta rastreabilidad mantendria un log inmutable en json_event_data, registrando timestamp del evento, tipo, etc. por cada una de las propiedades que visualiza el usuario, esto tambien se podria hacer muchas otras maneras, pero esta es una propuesta inicial para caso del ejercicio.

---

## Notas

- Las credenciales de la base de datos deben configurarse en `query/.env`. ya que utilizo python-dotenv para cargar las variables de entorno.


## Proponer un modelo de base de datos diferente para el ejercicio

Para este ejercicio, de inmuebles, el historico no lo manejaria como una relacion muchos a muchos, solo almacenaria un atributo estado en la tabla de property y el historico lo manejaria en una tabla independiente con un json para almacenar la mayor cantidad de informacion posible algo similar a lo que hice con la tabla event, sin embargo tambien se podria tener un sistema de logs en tablas NoSQL para almacenar dicho historico, ya que al cliente final no es necesario mostrarle el historico de cambio de estado, del inmueble, solo el ultimo estado.