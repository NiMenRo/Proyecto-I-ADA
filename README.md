# Instrucciones para ejecución

## Ejecución mediante script (crea el ambiente virtual y ejecuta de forma automática)

- En Linux, ejecutar el archivo `ejecutar.sh`

    ```bash
    ./ejecutar.sh
    ```

- En Windows, ejecutar el archivo `ejecutar.bat`

    ```cmd
    ejcutar.bat
    ```

## Creación de un ambiente virtual para la ejecución de forma manual

1. Instalación de virtualenv

    ```bash
    pip install virtualenv
    ```

2. Creación de un ambiente virtual y activación

    - Creación

        ```bash
        virtualenv venv
        ```

    - Activación

        ```bash
        # en windows
        .venv\Scripts\activate

        # en linux
        source venv/bin/activate
        ```

3. Instalación de librerias en el ambiente

    ```bash
    # instalacion
    pip install -r requirements.txt

    # verificar la instalacion
    pip freeze
    pip list
    ```

4. Ejecución de la aplicación

    ```bash
    python manage.py runserver 
    ```

## Ejecución de la aplicación

Al usar el script o ejecutar de forma manual, el servidor de la aplicación corre en el puerto 8000 en el siguiente link
**<http://localhost:8000/>**

## Ejecución Mediante Docker

1. Tener Docker previamente instalado e iniciado

2. Ejecutar el siguiente comando en la raiz del proyecto

    ```bash
    docker build -t django-app .
    ```

3. Una vez creada la imagen correr el contenedor mediante el siguiente comando

    ```bash
    docker run -p 8000:8000 django-app
    ```

4. La aplicación se ejecuta en el puerto 8000, en el siguiente link **<http://localhost:8000/>**
