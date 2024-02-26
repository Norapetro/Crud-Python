## Instalación con Docker

es el modo fácil de levantar el proyecto

```bash
docker compose --profile web  build
docker compose --profile web  up
```

## Instalación con pyenv y poetry

es el modo difícil de levantar el proyecto pero nos sirve para habilitar las opciones de debug mas fácil. recuerde instalar un motor de mongo para la bd.

```bash
pyenv versions #opcional: sirve para comprobar si la version de python que necesitamos ya se encuentra descargada
pyenv install --list #opcional: sirve para listar los versiones disponible por pyenv
pyenv install 3.10.12
```

```bash
poetry --version
poetry env info
poetry env use $(pyenv which python)
poetry env info # la version de python debe coincidir
poetry shell
poetry install
poetry show # dependencias instaladas == pip list
poetry add [dependecias]
```

🚫 :sos: Si al realizar la instalación de las dependencia se presenta un error. Elimanar el archivo poetry.lock y ejecutar el siguiente comando

```bash
poetry lock --no-update
```

finalmente correr el server con:

```bash
uvicorn app.main:app --reload
```

generar requirements:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

.\ENV-env\Scripts\activate

uvicorn sql_app.main:app --reload

pytest .\sql_app\main.py

Render
