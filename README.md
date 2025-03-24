## Descripción
`web_scraperF5` es un proyecto de scraping web diseñado para extraer datos de diversas fuentes en línea y almacenarlos en una base de datos MySQL. Este proyecto utiliza Python y varias bibliotecas para realizar el scraping y la gestión de la base de datos.

## Requisitos
- Python 3.8 o superior
- MySQL Server
- Docker (opcional, para despliegue en contenedores)

## Instalación
1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/web_scraperF5.git
    cd web_scraperF5
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno:
    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
    ```env
    SPOTIPY_CLIENT_ID="tu_client_id"
    SPOTIPY_CLIENT_SECRET="tu_client_secret"
    SPOTIPY_REDIRECT_URI="https://127.0.0.1:8888/callback"
<<<<<<< HEAD
    SPOTIPY_ACCESS_TOKEN="tu_token_de_acceso"
=======
>>>>>>> e6f76fab07eef5fecc064b0f7c8d875b95b7c448

    mysql_username='root'
    mysql_password='root1'
    mysql_host='127.0.0.1'
    mysql_port=3306
    bbdd_name='spotify'
    ```

## Uso
1. Ejecuta el script para crear la base de datos y las tablas:
    ```sh
    python bbdd/db_table_creation.py
    ```

2. Ejecuta el scraper:
    ```sh
    python scraper.py
    ```

## Despliegue con Docker
1. Construye la imagen de Docker:
    ```sh
    docker build -t web_scraperF5 .
    ```

2. Ejecuta el contenedor:
    ```sh
    docker run --env-file .env web_scraperF5
    ```

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
=======
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
>>>>>>> e6f76fab07eef5fecc064b0f7c8d875b95b7c448
