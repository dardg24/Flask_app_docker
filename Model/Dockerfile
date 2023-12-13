# Imagen base oficial de Python
FROM python:3.8

#Directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt /app/

# Aplicacióm Flask
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Puerto para la aplicacióm
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app_model.py"]
