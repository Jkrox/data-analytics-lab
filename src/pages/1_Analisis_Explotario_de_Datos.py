import streamlit as st
import plotly.express as px
from src.data_manipulator import clean_data
from src.eda import (
    get_most_sold_category_last_year,
    get_top_customer_by_volume,
    get_average_sales_per_customer,
    get_products_with_highest_profit_margin,
    detect_seasonal_patterns,
)

# Cargar y limpiar los datos
data_cleaned = clean_data("./ventas_dataset_grande_corregido_con_paises.csv")

# Título de la aplicación
st.title("Análisis Exploratorio de Datos de Ventas")

# Función: Categoría de productos más vendida en el último año
st.header("Categoría de productos más vendida en el último año")
most_sold_category = get_most_sold_category_last_year(data_cleaned)
st.write(f"La categoría de productos más vendida en el último año es: {most_sold_category}")

# Función: Cliente con el mayor volumen de compras
st.header("Cliente con el mayor volumen de compras")
top_customer = get_top_customer_by_volume(data_cleaned)
st.write(f"El cliente con el mayor volumen de compras es: {top_customer}")

# Función: Ventas promedio por cliente
st.header("Ventas promedio por cliente")
average_sales_per_customer = get_average_sales_per_customer(data_cleaned)
st.write(f"Las ventas promedio por cliente son: {average_sales_per_customer:.2f}")

# Función: Productos con mayor margen de beneficio
st.header("Productos con mayor margen de beneficio")
products_with_highest_profit_margin = get_products_with_highest_profit_margin(data_cleaned)
fig_profit_margin = px.bar(products_with_highest_profit_margin.head(10), x='producto', y='margen_beneficio', title='Top 10 Productos con Mayor Margen de Beneficio')
st.plotly_chart(fig_profit_margin)

# Función: Patrones estacionales en las ventas
st.header("Patrones estacionales en las ventas")
seasonal_patterns = detect_seasonal_patterns(data_cleaned)
fig_seasonal_patterns = px.line(seasonal_patterns, x='mes', y='ventas', title='Ventas Totales por Mes')
st.plotly_chart(fig_seasonal_patterns)