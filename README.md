
# Aplicación Flask para Predicciones y Reentrenamiento de Modelo

Esta aplicación Flask proporciona una interfaz sencilla para realizar predicciones, ingresar datos nuevos y reentrenar un modelo de machine learning con los datos actuales.

## Características

- **Predicciones**: Realiza predicciones basadas en datos ingresados por el usuario.
- **Ingesta de Datos**: Permite la inserción de nuevos datos para el entrenamiento del modelo.
- **Reentrenamiento del Modelo**: Facilita el reentrenamiento del modelo con los datos actuales.

## Cómo Empezar

Sigue estos pasos para poner en marcha el proyecto:

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/dardg24/Flask_app_docker
   ```
2. **Instalar Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar la Aplicación**:
   ```bash
   python app.py
   ```

## Uso

### Predicciones:

Envía los datos para realizar una predicción.
```bash
POST /predict
```

### Ingesta de Datos:

Inserta nuevos datos para el entrenamiento del modelo.
```bash
POST /ingest
```

### Reentrenamiento del Modelo:

Inicia el proceso de reentrenamiento del modelo con los datos actuales.
```bash
POST /retrain
```

## Tecnologías Utilizadas

- Flask
- Pandas
- Scikit-learn

## Contribuir

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será muy apreciada.

## Licencia

Distribuido bajo la Licencia MIT. Ver LICENSE para más información.

## Contacto

Daniel Rodríguez - danielrdegouveia@gmail.com

URL del Proyecto: https://github.com/dardg24/Flask_app_docker
