import streamlit as st
import plotly.express as px
from src.data_manipulator import (
    clean_data,
    get_sales_last_quarter,
    get_total_sales_by_product_and_customer,
    get_customers_with_multiple_categories,
    classify_customers_by_total_purchases,
)

data_cleaned = clean_data("./ventas_dataset_grande_corregido_con_paises.csv")

st.title("Análisis de Datos de Ventas")

st.header("Ventas del Último Trimestre")
sales_last_quarter = get_sales_last_quarter(data_cleaned)
fig_sales_last_quarter = px.bar(sales_last_quarter, x='fecha_venta', y='ventas', color='pais', title='Ventas del Último Trimestre por País')
st.plotly_chart(fig_sales_last_quarter)

st.header("Ventas Totales por Producto y Cliente")
sales_by_product_and_customer = get_total_sales_by_product_and_customer(data_cleaned)

# Gráfico de ventas totales por producto
fig_sales_by_product = px.bar(sales_by_product_and_customer["total_ventas_producto"], x='producto', y='total_ventas_producto', title='Ventas Totales por Producto')
st.plotly_chart(fig_sales_by_product)


fig_sales_by_customer_pie = px.pie(sales_by_product_and_customer["total_ventas_cliente"], names='cliente_id', values='total_ventas_cliente', title='Distribución de Ventas Totales por Cliente')
st.plotly_chart(fig_sales_by_customer_pie)

st.header("Clientes con Múltiples Categorías de Productos")
percentage_customers_multiple_categories = get_customers_with_multiple_categories(data_cleaned)
st.write(f"El porcentaje de clientes que han comprado en más de dos categorías de productos es: {percentage_customers_multiple_categories:.2f}%")

st.header("Clasificación de Clientes por Compras Totales")
classified_customers = classify_customers_by_total_purchases(data_cleaned)
fig_classified_customers = px.histogram(classified_customers, x='clasificacion_cliente', title='Clasificación de Clientes por Compras Totales')
st.plotly_chart(fig_classified_customers)