from src.data_manipulator import clean_data
from src.eda import (
    get_most_sold_category_last_year,
    get_top_customer_by_volume,
    get_average_sales_per_customer,
    get_products_with_highest_profit_margin,
    detect_seasonal_patterns
)

if __name__ == "__main__":
    # Cargar y limpiar los datos
    data_cleaned = clean_data("./ventas_dataset_grande_corregido_con_paises.csv")
    
    # Identificar la categoría de productos más vendida en el último año
    most_sold_category = get_most_sold_category_last_year(data_cleaned)
    print(f"La categoría de productos más vendida en el último año es: {most_sold_category}")

    # Calcular el cliente con el mayor volumen de compras
    top_customer = get_top_customer_by_volume(data_cleaned)
    print(f"El cliente con el mayor volumen de compras es: {top_customer}")
    
    # Calcular las ventas promedio por cliente
    average_sales_per_customer = get_average_sales_per_customer(data_cleaned)
    print(f"Las ventas promedio por cliente son: {average_sales_per_customer:.2f}")
    
    # Identificar los productos que generan mayor margen de beneficio
    products_with_highest_profit_margin = get_products_with_highest_profit_margin(data_cleaned)
    print(products_with_highest_profit_margin.head(5))
    
    # Detectar patrones estacionales en las ventas
    seasonal_patterns = detect_seasonal_patterns(data_cleaned)
    print(seasonal_patterns)