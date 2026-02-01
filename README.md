# ⚡ UPTC Energy IA Engine - Proyecto INDRA

¡Bienvenidos! Somos un equipo de desarrollo que ha creado esta solución de **Inteligencia Artificial** para la optimización y gestión del consumo energético en la **UPTC**. Este repositorio contiene el núcleo del motor de análisis, predicción y el agente consultor de eficiencia.

📍 **Repositorio:** [Alexander-Renteria-DevMl/INDRA](https://github.com/Alexander-Renteria-DevMl/INDRA)

---

## 🚀 Visión del Proyecto
Como grupo, identificamos la necesidad de transformar los datos de consumo institucional en información accionable. Nuestra plataforma permite:
1.  **Analítica Descriptiva:** Entender quién, dónde y cuándo se consume más energía.
2.  **Modelado Predictivo:** Anticipar la demanda semanal mediante Machine Learning.
3.  **Gestión de Eficiencia:** Evaluar el desempeño de cada sede mediante el KPI de intensidad energética ($kWh/m^2$).

---

## 🏗️ Estructura del Software
Basándonos en la arquitectura de nuestro repositorio, el sistema se divide en:

* **`app.py`**: El orquestador principal basado en **Flask**. Conecta la lógica de backend con el Dashboard interactivo.
* **`data_engine.py`**: Motor de procesamiento de datos. Realiza la limpieza, normalización e integración de las métricas de las sedes.
* **`model_engine.py`**: Implementación del modelo de IA (Random Forest) para la generación de pronósticos de consumo.
* **`ia_agent.py`**: Nuestro **Agente de IA** que analiza patrones de desperdicio y genera recomendaciones automáticas de ahorro.
* **`templates/index.html`**: Interfaz de usuario que visualiza las métricas mediante gráficas dinámicas de Plotly.js.



---

## 🔍 Hallazgos de nuestro Análisis (EDA)
Durante el desarrollo, nuestro equipo respondió preguntas críticas que fundamentan la lógica del sistema:

### 📊 Diagnóstico por Sectores
* **Laboratorios:** Detectamos que son el sector con mayor consumo base (24/7).
* **Comedores:** Presentan picos críticos entre las **12:00 p.m. y 2:00 p.m.**
* **Consumos Fantasma:** Identificamos oportunidades de ahorro en oficinas (fines de semana) y salones (horario nocturno).

### 🔮 Factores de Predicción
Determinamos que la **hora del día**, el **día de la semana** y el **calendario académico** son las variables con mayor poder predictivo para nuestra IA.



---

## 🛠️ Instalación y Ejecución Local

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Alexander-Renteria-DevMl/INDRA.git](https://github.com/Alexander-Renteria-DevMl/INDRA.git)
    cd INDRA
    ```

2.  **Instalar dependencias necesarias:**
    ```bash
    pip install flask pandas scikit-learn numpy plotly
    ```

3.  **Iniciar el servidor:**
    ```bash
    python app.py
    ```
4.  **Visualizar el Dashboard:** Ingresa a `http://127.0.0.1:5000` en tu navegador.

---

## 📈 Impacto Institucional
Como equipo, proyectamos que la implementación de este motor de IA y el seguimiento de las recomendaciones del agente pueden generar un ahorro del **15% en la factura energética** de la UPTC, promoviendo una cultura de sostenibilidad basada en datos.

---

**Desarrollado con ❤️ por nuestro equipo de Ingeniería - UPTC 2026**
