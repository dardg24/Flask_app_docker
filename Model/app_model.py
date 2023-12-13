from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd
import sqlite3

# Leo el DF
df = pd.read_csv('data/Advertising.csv', index_col=0)

# Hago cambios en el DF
df['newpaper'] = df['newpaper'].str.replace('s', '')
df['newpaper'] = df['newpaper'].astype(float)


conn = sqlite3.connect('data/Db_av.db')
df.to_sql('tabla', conn, if_exists='replace', index=False)
conn.close()

model = pickle.load(open('data/advertising_model','rb'))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Hola Soy Daniel, Bienvenido a mi API del modelo advertising"

# 1. Endpoint que devuelva la predicción de los nuevos datos enviados mediante argumentos en la llamada
@app.route('/predict', methods=['GET'])
def predict():
    data = request.get_json()
    
    # Comprueba si los datos están bajo la clave 'data' y si es una lista
    if 'data' in data and isinstance(data['data'], list):
        # Extrae el primer conjunto de valores de la lista
        tv, radio, newpaper = data['data'][0]

        # Realiza la predicción
        prediction = model.predict([[float(tv), float(radio), float(newpaper)]])
        
        # Devuelve la predicción en el formato esperado por el test
        return jsonify({'prediction': str(round(prediction[0], 2)) + 'k €'})

    return jsonify({'error': 'Formato de datos incorrecto'}), 400



# 2. Ingesta de datos nuevos
@app.route('/ingest', methods=['POST'])
def ingest_data():
    data = request.get_json()

    # Comprueba si los datos están bajo la clave 'data' y si es una lista de listas
    if 'data' in data and all(isinstance(item, list) and len(item) == 4 for item in data['data']):
        conn = sqlite3.connect('data/Db_av.db')
        cur = conn.cursor()

        for item in data['data']:
            # Asume que la estructura es [tv, radio, newpaper, sales]
            tv, radio, newpaper, sales = item
            cur.execute('INSERT INTO tabla (TV, radio, newpaper, sales) VALUES (?, ?, ?, ?)', 
                        (tv, radio, newpaper, sales))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Datos ingresados correctamente'}), 200
    else:
        return jsonify({'error': 'Formato de datos incorrecto'}), 400


#3. Reentrenar
@app.route('/retrain', methods=['POST'])
def retrain():
    # Conectar a la base de datos y extraer los datos
    conn = sqlite3.connect('data/Db_av.db')   
    df = pd.read_sql('SELECT * FROM tabla', conn)
    conn.close()

    X = df[['TV', 'radio', 'newpaper']]  
    y = df['sales']

    # Reentrenar el modelo
    model.fit(X, y)

    # Guardar el modelo reentrenado
    with open('data/advertising_model_retrained', 'wb') as f:
        pickle.dump(model, f)

    return jsonify({'message': 'Modelo reentrenado correctamente.'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)