@echo off

:: variable con el nombre del entorno virtual
set VENV=venv

:: comprobación de existencia de entorno virtual
if exist %VENV% (
    echo El entorno virtual ya existe.
) else (
    echo Creando el entorno virtual...
    python -m venv %VENV%
)

echo Activando el entorno virtual...
call %VENV%\Scripts\activate

:: instalación de librerias/dependencias
if exist requirements.txt (
    echo Instalando dependencias desde requirements.txt...
    pip install -r requirements.txt
) else (
    echo No se encontró el archivo requirements.txt. Asegúrate de que esté en la carpeta del proyecto.
)

:: ejecutar servidor
echo Iniciando el servidor de desarrollo...
python manage.py runserver

pause
