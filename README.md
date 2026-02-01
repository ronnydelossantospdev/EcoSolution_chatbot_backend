
# 🌱 EcoSolution_chatbot_backend – API de Entrenamiento y Consumo de Modelo ML

<br>

## Indice

- [📌 Descripción del Proyecto](#-descripción-del-proyecto)

    - [🧠 ¿Cómo funciona el sistema?](#-cómo-funciona-el-sistema)

    - [📊 Dataset utilizado?](#-dataset-utilizado)

    - [#🤖 Modelo de Machine Learning](#-modelo-de-machine-learning)

    - [📦 Archivos generados durante el entrenamiento](#-archivos-generados-durante-el-entrenamiento)

    - [⚡ Entrenamiento](#-entrenamiento)

    - [🌐 API del Proyecto](#-api-del-proyecto)

    - [📚 Documentación de Endpoints](#-documentación-de-endpoints)

        - [✅ Endpoint de Bienvenida](#-endpoint-de-bienvenida)

        - [✅ Endpoint para Consultas](#-endpoint-para-consultas)



- [Configuración y ejecución del proyecto](#configuración-y-ejecución-del-proyecto)

    - [✅ 1. Crear entorno virtual](#-1-crear-entorno-virtual)
    
    - [✅ 2. Activar entorno virtual](#-2-activar-entorno-virtual)

    - [✅ 3. Instalar dependencias](#-3-instalar-dependencias)

    - [✅ 4. Ejecutar el proyecto](#-4-ejecutar-el-proyecto)

    - [🛑 5. Detener el proyecto](#-5-detener-el-proyecto)

    - [🔒 6. Salir del entorno virtual](#-6-salir-del-entorno-virtual)



<br><br>

# 📌 Descripción del Proyecto

El **EcoSolution_chatbot_backend** es una API desarrollada en **Python** cuyo objetivo principal es entrenar y ejecutar un modelo de Machine Learning.

Este sistema permite:

- Entrenar un modelo de clasificación de texto
- Generar archivos de modelo entrenado
- Consumir el modelo mediante una API REST
- Procesar preguntas y generar respuestas automáticas

<br>

---

### 🧠 ¿Cómo funciona el sistema?

El proyecto utiliza técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning** para interpretar preguntas escritas por el usuario y generar respuestas automáticas.

El flujo general es:

1. Se recibe un dataset con preguntas y respuestas.
2. El sistema entrena un modelo usando regresión logística.
3. Se genera un modelo entrenado.
4. La API utiliza ese modelo para responder preguntas.

<br>

---

### 📊 Dataset utilizado

El modelo se entrena utilizando el siguiente archivo:

```bash
dataset/medio_ambiente_dataset.csv
```

Este dataset contiene información relacionada con temas medioambientales, que sirve como base para que el modelo aprenda patrones y respuestas.

<br>

---

### 🤖 Modelo de Machine Learning

El modelo fue construido utilizando:

- Algoritmo: Regresión Logística
- Vectorización: TF-IDF (Term Frequency - Inverse Document Frequency)

<br>

🔹 **Regresión Logística**

Es un algoritmo de Machine Learning que aprende patrones matemáticos y estadísticos a partir de datos para clasificar texto.

🔹 **TF-IDF**

Se utiliza para convertir texto en valores numéricos que el modelo puede interpretar.


<br>

---

### 📦 Archivos generados durante el entrenamiento

Cuando el modelo es entrenado, se generan los siguientes archivos:

| **Archivo** |	**Descripción** |
|--|--|
| `modelo.pkl`  |	Contiene el modelo entrenado |
| `vectorizer_tfidf.pkl`	| Convierte texto en datos numéricos

<br>

---

### ⚡ Entrenamiento

El proyecto incluye un scripts para entrenar el modelo.

```bash
algoritmo_modelo.py
```
<br>

---

### 🌐 API del Proyecto

El archivo principal de la API es:

```bash
api.py
```

Esta API permite consumir el modelo previamente entrenado.


<br>

---

### 📚 Documentación de Endpoints

---

### ✅ Endpoint de Bienvenida

GET /
🔹 **Descripción**

Retorna un mensaje inicial del sistema.

🔹 **Response**
```json
{
    "mensaje": [
        "¡Hola!",
        "¿Cómo puedo ayudarte?"
    ]
}
```

---

### ✅ Endpoint para Consultas

POST /datos

🔹 **Descripción**

Recibe una pregunta del usuario, la procesa mediante el modelo entrenado y retorna una respuesta.


🔹 **Payload**
```json
{
    "pregunta": "hola"
}
```

🔹 **Response**
```json
{
    "mensaje": "muy bien espero que tú también te encuentres bien"
}
```

<br><br><br><br><br>

# 🚀Configuración y ejecución del proyecto
<br>

Este documento explica cómo configurar y ejecutar el proyecto paso a paso.

## ✅ 1. Crear entorno virtual

El entorno virtual permite instalar dependencias solo para este proyecto.

Ejecutar en la raíz del proyecto:
```bash
python -m venv venv
```
<br>

## ✅ 2. Activar entorno virtual
🔹 **En Windows (PowerShell)**

```bash
.\venv\Scripts\activate
```

Si se activó correctamente, verás algo así:

```bash
(venv) PS C:\ruta\proyecto>
```
<br>

## ✅ 3. Instalar dependencias

Instalar todas las librerías necesarias usando el archivo requirements.txt.

```bash
pip install -r requirements.txt
```

<br>

## ✅ 4. Ejecutar el proyecto
```bash
python api_flask.py
```

El servidor Flask iniciará en modo desarrollo.

<br>

## 🛑 5. Detener el proyecto

Para detener el servidor Flask:
```bash
Ctrl + C
```
<br>

## 🔒 6. Salir del entorno virtual

Cuando termines de trabajar:

```bash
deactivate
```