import pandas as pd
from src.data_manipulator import (
    get_total_sales_by_product_and_customer,
)

def get_most_sold_category_last_year(df: pd.DataFrame) -> str:
    """Identify the most sold product category in the last year.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        str: the most sold product category
    """
    # Convert the date column to datetime
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
    # Get the last date in the dataframe
    last_date = df['fecha_venta'].max()
    # Calculate the start date of the last year
    start_date_last_year = last_date - pd.DateOffset(years=1)
    # Filter the dataframe for the last year
    last_year_df = df[(df["fecha_venta"] >= start_date_last_year)]
    # Group by product category and sum the sales
    category_sales = last_year_df.groupby("categoria_producto")["cantidad_vendida"].sum()
    # Identify the most sold category
    most_sold_category = category_sales.idxmax()
    
    return most_sold_category

def get_top_customer_by_volume(df: pd.DataFrame) -> str:
    """Calculate the customer with the highest purchase volume.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        str: the customer ID with the highest purchase volume
    """
    # Calculate the sales for each row
    df["ventas"] = df["cantidad_vendida"] * df["precio_unitario"]
    
    # Group by customer and sum the sales
    total_sales_by_customer = df.groupby("cliente_id")["ventas"].sum()
    
    # Identify the customer with the highest purchase volume
    top_customer = total_sales_by_customer.idxmax()
    
    return top_customer

def get_average_sales_per_customer(df: pd.DataFrame) -> float:
    """Calculate the average sales per customer.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        float: the average sales per customer
    """
    # Get total sales by customer using the existing function
    sales_data = get_total_sales_by_product_and_customer(df)
    total_sales_by_customer = sales_data["total_ventas_cliente"]
    
    # Calculate the total sales
    total_sales = total_sales_by_customer["total_ventas_cliente"].sum()
    
    # Calculate the number of unique customers
    num_customers = total_sales_by_customer["cliente_id"].nunique()
    
    # Calculate the average sales per customer
    average_sales_per_customer = total_sales / num_customers
    
    return average_sales_per_customer

def get_products_with_highest_profit_margin(df: pd.DataFrame) -> pd.DataFrame:
    """Identify the products that generate the highest profit margin.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        pd.DataFrame: dataframe with products and their profit margins
    """
    # Calculate the sales for each row
    df["ventas"] = df["cantidad_vendida"] * df["precio_unitario"]
    
    # Calculate the cost for each row
    df["coste"] = df["cantidad_vendida"] * df["coste_unitario"]
    
    # Calculate the profit for each row
    df["beneficio"] = df["ventas"] - df["coste"]
    
    # Group by product and sum the sales and profit
    total_sales_and_profit_by_product = df.groupby("producto").agg({
        "ventas": "sum",
        "beneficio": "sum"
    }).reset_index()
    
    # Calculate the profit margin for each product
    total_sales_and_profit_by_product["margen_beneficio"] = (
        total_sales_and_profit_by_product["beneficio"] / total_sales_and_profit_by_product["ventas"]
    )
    
    # Sort the products by profit margin in descending order
    products_with_highest_profit_margin = total_sales_and_profit_by_product.sort_values(
        by="margen_beneficio", ascending=False
    )
    
    return products_with_highest_profit_margin

def detect_seasonal_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Detect seasonal patterns in sales.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        pd.DataFrame: dataframe with total sales by month
    """
    # Convert the date column to datetime
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
    
    # Extract the month from the date
    df["mes"] = df["fecha_venta"].dt.month
    
    # Calculate the sales for each row
    df["ventas"] = df["cantidad_vendida"] * df["precio_unitario"]
    
    # Group by month and sum the sales
    sales_by_month = df.groupby("mes")["ventas"].sum().reset_index()
    
    # Sort the sales by month
    sales_by_month = sales_by_month.sort_values(by="mes")
    
    return sales_by_month