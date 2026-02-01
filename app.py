from flask import Flask, render_template, request
import json
from data_engine import data_manager
from model_engine import ia_model
from ia_agent import agente

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1. PROCESAMIENTO DE MEDICIONES
    # Agrupamos para obtener el promedio por sede
    df_resumen = data_manager.df.groupby('sede').agg({
        'energia_total_kwh': 'mean',
        'agua_m3': 'mean',
        'pct_eficiencia': 'mean'
    }).reset_index()

    # Convertimos a diccionario para la tabla del HTML
    resumen_tabla = df_resumen.to_dict(orient='records')

    # 2. DATOS PARA GRÁFICAS (JSON)
    graph_data = {
        'sedes': df_resumen['sede'].tolist(),
        'eficiencia': [round(x, 2) for x in df_resumen['pct_eficiencia'].tolist()],
        'energia': [round(x, 2) for x in df_resumen['energia_total_kwh'].tolist()]
    }

    # 3. RECOMENDACIONES DEL AGENTE
    recomendaciones = agente.get_recommendations()

    # 4. PREDICCIÓN FUTURA
    pred_resultado = None
    if request.method == 'POST':
        try:
            ultima_fecha = data_manager.df['timestamp'].max()
            # Tu modelo predice basándose en la última fecha real
            df_futuro = ia_model.predict_future(ultima_fecha)
            
            pred_resultado = {
                'energia': round(df_futuro['energia_total_kwh'].sum(), 2),
                'agua': round(df_futuro['agua_m3'].sum(), 4)
            }
        except Exception as e:
            print(f"Error en predicción: {e}")
            pred_resultado = {"error": "Error al procesar predicción"}

    return render_template(
        'index.html', 
        mediciones=resumen_tabla, 
        recs=recomendaciones, 
        pred=pred_resultado,
        graph_data=graph_data
    )

if __name__ == '__main__':
    app.run(debug=True)