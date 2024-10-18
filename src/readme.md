# Proyecto de Búsqueda de Películas con Docker

Este programa permite realizar búsquedas en un dataset de las 1000 mejores películas de IMDB utilizando embeddings de texto para encontrar coincidencias relevantes basadas en descripciones.

## Estructura del Proyecto

La estructura de archivos y directorios del proyecto es la siguiente:

Peliculas/
├── src/
│   ├── buscar_peliculas.py
│   ├── data_loader.py
│   └── semantica.py
├── tests/
│   ├── test_buscar_pelicula.py
│   ├── test_data_loader.py
│   └── test_semantica.py
Dockerfile
requirements.txt

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- [Docker](https://www.docker.com/get-started) en tu sistema.
- Asegúrese de tener instaladas las librerias de Python que se 
  encuentra en el archivo requirements.txt.

## Construcción de la Imagen Docker

Para construir la imagen Docker de este proyecto, sigue estos pasos:

1. Abre una terminal o consola en el directorio del proyecto.
2. Ejecuta el siguiente comando para construir la imagen:

   ```bash
   docker build -t pelis .

## Ejecutar la aplicación principal

   ```bash
   docker run -it --rm pelis

## Uso

El programa pedirá que ingreses un término de búsqueda.
Puedes buscar películas con una descripción.
Para salir del programa, escribe salir y presiona Enter.

Ejecutará la aplicación de búsqueda de películas, y podrás interactuar con ella desde la terminal.

## Ejecutar pruebas unitarias

   ```bash
   docker run -it --rm -e RUN_MODE=test pelis

Ejecutará todas las pruebas unitarias definidas en el directorio tests/ usando el módulo unittest de Python.

## Recolección de datos de cobertura "coverage"

   ```bash
   $env:PYTHONPATH = "src" # permite que los módulos en 'src' sean accesibles para los tests
   coverage run -m unittest discover -s tests # busca y ejecuta automáticamente todos los tests en la carpeta especificada ('tests' en este caso)
   coverage report # Genera un informe en la consola que muestra el porcentaje de cobertura de código alcanzado
   coverage html # permite una inspección visual de qué partes del código están cubiertas por los tests

Name                            Stmts   Miss  Cover
---------------------------------------------------
src\buscar_peliculas.py            24      2    92%
src\data_loader.py                 15      3    80%
src\semantica.py                   10      0   100%
tests\test_buscar_pelicula.py      11      1    91%
tests\test_data_loader.py          18      1    94%
tests\test_semantica.py            17      1    94%
---------------------------------------------------
TOTAL                              95      8    92%

## Notas
Asegurese que el archivo IMDB.csv esté en la misma carpeta que main.py para que el programa funcione correctamente.