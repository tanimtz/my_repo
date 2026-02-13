Análisis de Anuncios de Vehículos en EE.UU.

Descripción del proyecto

Esta aplicación web permite explorar datos de anuncios de venta de vehículos usados en Estados Unidos mediante visualizaciones interactivas.

El objetivo del proyecto es aplicar técnicas de análisis exploratorio de datos (EDA) y desarrollar una aplicación web utilizando Streamlit para visualizar información clave del dataset.

⸻

Funcionalidades de la aplicación

La aplicación permite:
	•	Visualizar la distribución del kilometraje de los vehículos mediante un histograma interactivo.
	•	Analizar la relación entre el precio y el kilometraje utilizando un gráfico de dispersión.
	•	Explorar los datos mediante gráficos generados dinámicamente al interactuar con la interfaz.

⸻

Preparación de datos

Antes de construir la aplicación, se realizó un proceso de limpieza de datos que incluyó:
	•	Imputación de valores faltantes en variables numéricas usando la mediana.
	•	Reemplazo de valores faltantes en variables categóricas con la categoría "unknown".
	•	Conversión de la columna date_posted a formato datetime.
	•	Validación de tipos de datos y verificación de ausencia de duplicados.

⸻

Tecnologías utilizadas
	•	Python
	•	Pandas
	•	Plotly Express
	•	Streamlit

Cómo ejecutar la aplicación localmente
	1.	Clonar el repositorio: 
git clone (https://github.com/tanimtz/my_repo)
    2.	Crear y activar entorno virtual: 
conda create -n vehicles_env python=3.10
conda activate vehicles_env
    3.	Instalar dependencias
pip install -r requirements.txt
	4.	Ejecutar la aplicación:
streamlit run app.py

Este proyecto fue desarrollado como parte de un proceso de aprendizaje como DA como parte del Sprint 7 Herramientas de Desarrollo de Software