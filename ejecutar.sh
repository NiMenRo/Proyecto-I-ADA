#!/bin/bash

# variable con el nombre de la carpeta del entorno virtual
VENV="venv"

# comprobación de la existencia del entorno virtual
if [ -d "$VENV" ]; then
    echo "El entorno virtual ya existe."
else
    echo "Creando el entorno virtual..."
    python3 -m venv $VENV
fi

echo "Activando el entorno virtual..."
source $VENV/bin/activate

# instalacion de librerias/dependencias
if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
else
    echo "No se encontró el archivo requirements.txt. Asegúrate de que esté en la carpeta del proyecto."
fi

# ejecutar el servidor
echo "Iniciando el servidor de desarrollo..."
python manage.py runserver


