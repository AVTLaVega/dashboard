import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración estética de la aplicación
st.set_page_config(page_title="AVT La Vega - Investor Dashboard", layout="wide")

# Estilos personalizados para simular una App moderna
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; }
    .card { background-color: #ffffff; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1, h2, h3 { color: #1e3a8a; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("AVT La Vega")
st.sidebar.markdown("**Formando jóvenes, transformando el campo**")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Navegación", 
    ["Pitch de Inversión", "Finanzas e Indicadores", "Estructura Societaria", "Cronograma 2026"])

# --- Datos Financieros Actualizados ---
df_capex = pd.DataFrame({
    "Rubro": ["Infraestructura", "Tecnología/IA", "Energía Solar", "Capital de Trabajo"],
    "Monto (Millones)": [185, 95, 45, 164]
})

data_proyeccion = {
    "Año": [1, 2, 3, 4, 5],
    "Ingresos": [935, 1493, 1567, 1691, 1826],
    "Egresos": [884, 1301, 1340, 1425, 1510],
    "Utilidad (EBITDA)": [51, 192, 227, 266, 316]
}
df_finanzas = pd.DataFrame(data_proyeccion)

# --- Contenido de las Páginas ---

if menu == "Pitch de Inversión":
    st.title("🚀 Propuesta Estratégica: AVT La Vega")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Inversión Requerida", "$489M COP")
    col2.metric("EBITDA Estimado (Año 2)", "$192M COP")
    col3.metric("Retorno (ROI)", "2.9 Años")

    st.markdown("""
    <div class="card">
    <h3>Diferenciales Tecnológicos</h3>
    <ul>
        <li><b>IA y Visión Computacional:</b> Monitoreo remoto para reducir mortalidad del 8% al 3%.</li>
        <li><b>Sostenibilidad:</b> Paneles solares para ahorro del 60-80% en energía.</li>
        <li><b>Escalabilidad:</b> Planta de beneficio propia para exportación en el Año 3 (ProColombia).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Finanzas e Indicadores":
    st.title("📊 Análisis Financiero Interactivo")
    
    tab1, tab2 = st.tabs(["Crecimiento a 5 Años", "Distribución de Inversión"])
    
    with tab1:
        fig_ingresos = px.line(df_finanzas, x="Año", y=["Ingresos", "Utilidad (EBITDA)"], 
                               title="Proyección de Crecimiento (Millones COP)", markers=True)
        st.plotly_chart(fig_ingresos, use_container_width=True)
        st.dataframe(df_finanzas, use_container_width=True)

    with tab2:
        fig_capex = px.pie(df_capex, values="Monto (Millones)", names="Rubro", 
                           title="Inversión de Capital ($489M)", hole=0.4)
        st.plotly_chart(fig_capex, use_container_width=True)

elif menu == "Estructura de Socios":
    st.title("🤝 Gobernanza y Cap Table")
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        socios = {"Socio": ["Sergio & Andrés", "Inversionistas", "Dueñas Tierra", "CTOs"],
                  "Participación": [64, 16, 12, 8]}
        fig_socios = px.pie(pd.DataFrame(socios), values="Participación", names="Socio", hole=0.5)
        st.plotly_chart(fig_socios, use_container_width=True)
    
    with col_right:
        st.markdown(f"""
        <div class="card">
        <h4>Blindaje para Dueñas de la Tierra</h4>
        <ul>
            <li><b>Activo:</b> 3.1 Hectáreas utilizables en La Vega[cite: 468].</li>
            <li><b>Vesting:</b> 6% en Año 3 y 6% en Año 5 (Total 12%).</li>
            <li><b>Pagos:</b> Arriendo fijo + Aporte a compra obligatoria (Banda $190M-$220M).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Cronograma 2026":
    st.title("🗓️ Plan Operativo: Camino al 2027")
    st.write("Hitos críticos para asegurar la financiación y el inicio de obra.")
    
    st.markdown("""
    - **Q1 2026:** Registro Cámara de Comercio, RUT y formalización de socios[cite: 121, 122].
    - **Q2 2026:** Gestión de permisos ambientales ante la CAR y validación ICA GAB[cite: 125, 385].
    - **Q3 2026:** Postulación y adjudicación de capital semilla (Meta $489M).
    - **Q4 2026:** Adecuación física del terreno y servicios hídricos [cite: 575-578].
    - **Ene 2027:** Inicio de construcción de galpones y planta de beneficio [cite: 586-588].
    """)
