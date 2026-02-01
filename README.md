# ⚡ UPTC Energy IA Engine: Gestión Inteligente de Recursos

¡Bienvenidos a nuestro repositorio! Somos un grupo de desarrollo comprometido con la innovación tecnológica en la **Universidad Pedagógica y Tecnológica de Colombia (UPTC)**. Este proyecto aplica **Inteligencia Artificial** para transformar la gestión del consumo de energía y agua en nuestras sedes.

Nuestro sistema no solo visualiza datos; utiliza modelos predictivos y agentes inteligentes para convertir registros históricos en estrategias de sostenibilidad institucional.

---

## 🚀 Visión General
Como equipo, identificamos que el gasto energético carecía de un análisis centralizado. Nuestra solución aborda este problema mediante:
1.  **Centralización de Datos:** Integración de consumos de las sedes Tunja, Duitama, Sogamoso y Chiquinquirá.
2.  **Predicción de Demanda:** Modelos de Machine Learning que anticipan el gasto de la próxima semana.
3.  **Consultoría Automatizada:** Un Agente de IA que detecta ineficiencias y propone acciones de ahorro.

---

## 🏗️ Arquitectura del Sistema
Hemos estructurado el proyecto en módulos especializados para garantizar escalabilidad y orden:

* **`data_engine.py`**: El motor de procesamiento. Realizamos la limpieza, unión de datasets y el cálculo del KPI de **Intensidad Energética** ($kWh/m^2$).
* **`model_engine.py`**: El cerebro predictivo. Implementamos un modelo de regresión (Random Forest) para proyectar consumos.
* **`ia_agent.py`**: Nuestro consultor inteligente. Analiza desviaciones y genera recomendaciones automáticas de ahorro.
* **`app.py`**: El orquestador. Desarrollado en **Flask**, conecta nuestra lógica con un Dashboard interactivo.

---

## 🔍 Hallazgos de nuestro Análisis (EDA)
Durante la fase de Análisis Exploratorio de Datos, nuestro grupo respondió preguntas críticas para la eficiencia universitaria:

### 📊 Diagnóstico por Sectores
* **Cargas Críticas:** Identificamos que los **laboratorios** mantienen el consumo base más alto y constante (24/7), evidenciando equipos que requieren funcionamiento continuo.
* **Picos Operativos:** Validamos que los **comedores** generan picos de demanda máxima entre las **12:00 p.m. y 2:00 p.m.**
* **Oportunidades de Ahorro:** Detectamos "consumos fantasma" en oficinas durante fines de semana y consumos residuales en salones después de las 9:00 p.m.

### 🔮 Factores Predictivos
Determinamos que la **hora**, el **día de la semana** y la **ocupación** son las variables con mayor peso en nuestras predicciones. Además, logramos modelar eventos aleatorios en auditorios integrando el calendario académico.

---

## 🛠️ Instalación y Configuración

### Requisitos
* Python 3.9+
* Pip (Gestor de paquetes)

### Pasos para Ejecutar
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/uptc-energy-ia.git](https://github.com/tu-usuario/uptc-energy-ia.git)
    cd uptc-energy-ia
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install flask pandas scikit-learn numpy plotly
    ```

3.  **Lanzar la aplicación:**
    ```bash
    python app.py
    ```
4.  **Acceder al Dashboard:** Abre tu navegador en `http://127.0.0.1:5000`

---

## 📊 Metas de Eficiencia
Implementamos un estándar de **0.05 kWh/$m^2$**. A través de este KPI, nuestro sistema califica cada sede:
* **Eficiencia > 90%:** Sede optimizada.
* **Eficiencia 70% - 90%:** Requiere revisión de equipos.
* **Eficiencia < 70%:** Alerta crítica por desperdicio masivo.

---

## 📈 Impacto Esperado
Como grupo, estimamos que la aplicación de las recomendaciones generadas por nuestro **Agente de IA** puede reducir el costo de la factura energética institucional en un **15%**, promoviendo un campus inteligente y transparente.

---

**Desarrollado con ❤️ por nuestro equipo de Ingeniería - UPTC 2026.**
