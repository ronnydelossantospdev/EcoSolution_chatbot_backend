import pandas as pd
import re
import time
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


inicio = time.time()
i_tiempo_fDatos = time.time()


def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúñü\s]', '', texto)
    return texto


# Cargar el dataset
df = pd.read_csv('dataset/medio_ambiente_dataset.csv')


# Limpiar los datos
df['Preguntas'] = df['Preguntas'].apply(limpiar_texto)
df['Respuestas'] = df['Respuestas'].apply(limpiar_texto)


# Separar características (Preguntas) y etiquetas (Respuestas)
X = df['Preguntas']
y = df['Respuestas']


# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Vectorización del texto usando TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Crear y entrenar el modelo de regresión logística
modelo = LogisticRegression(random_state=42, max_iter=1000)
modelo.fit(X_train_tfidf, y_train)
f_tiempo_fDatos = time.time()
print(f"Tiempo de entrenamiento del modelo: {round(f_tiempo_fDatos - i_tiempo_fDatos, 3)}")

# Evaluar el modelo
y_pred = modelo.predict(X_test_tfidf)
precision = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {precision:.2%}')
print(classification_report(y_test, y_pred))

# Función para interactuar con el chatbot
# def chatbot(pregunta):
#     pregunta_limpia = limpiar_texto(pregunta)
#     pregunta_tfidf = vectorizer.transform([pregunta_limpia])
#     respuesta = modelo.predict(pregunta_tfidf)[0]
#     return respuesta

# Interactuar con el modelo
# print("\n¡El chatbot está listo para responder tus preguntas sobre medio ambiente!")
# while True:
#     pregunta_usuario = input("Haz una pregunta (o escribe 'salir' para terminar): ")
#     if pregunta_usuario.lower() == 'salir':
#         print("¡Hasta luego!")
#         break
#     respuesta_chatbot = chatbot(pregunta_usuario)
#     print(f"Respuesta: {respuesta_chatbot}")


i_tiempo_guardarM = time.time()

# Guardar el Modelo y el Vectorizador
joblib.dump(modelo, 'chatbot/modelo/modelo.pkl') # Guardar el modelo de regresión logística
joblib.dump(vectorizer, 'chatbot/modelo/vectorizer_tfidf.pkl') # Guardar el vectorizador TF-IDF
print("Modelo y vectorizador guardados exitosamente.")

f_tiempo_guardarM = time.time()
print(f"Tiempo guardando modelo: {round(f_tiempo_guardarM - i_tiempo_guardarM, 3)}")


fin = time.time()
print(f"Tiempo estimado: {round(fin - inicio, 3)}")