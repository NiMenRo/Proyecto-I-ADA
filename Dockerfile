# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . /app/

# Exponer el puerto en el que correrá el servidor de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]