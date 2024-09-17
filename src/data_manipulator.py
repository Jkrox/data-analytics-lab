from typing import Dict

import pandas as pd


def clean_data(file_path: str) -> pd.DataFrame:
    """Clean the data from the CSV file

    Args:
        file_path (str): path to the CSV file

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    df = pd.read_csv(file_path)
    df["precio_unitario"] = df["precio_unitario"].round(2)
    df["coste_unitario"] = df["coste_unitario"].round(2)

    df.dropna()
    df.drop_duplicates()
    return df


def get_sales_last_quarter(df: pd.DataFrame) -> pd.DataFrame:
    """Sales ordered by countries, products and product categories

    Args:
        df (pd.Dataframe): cleaned dataframe with the data

    Returns:
        pd.Dataframe: dataframe with the sales ordered by countries, products and product categories
    """
    # Convert the date column to datetime
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
    
    # Get the last quarter date range
    last_quarter = df["fecha_venta"].max() - pd.DateOffset(months=3)
    
    # Filter the data for the last quarter
    last_quarter_data = df[df["fecha_venta"] >= last_quarter]
    
    # Calculate the sales for each row
    last_quarter_data["ventas"] = last_quarter_data["cantidad_vendida"] * last_quarter_data["precio_unitario"]
    
    # Group by date and country and sum the sales
    sales_last_quarter = last_quarter_data.groupby(["fecha_venta", "pais"]).agg({
        "ventas": "sum"
    }).reset_index()
    
    return sales_last_quarter


def get_total_sales_by_product_and_customer(
    df: pd.DataFrame,
) -> Dict[str, pd.DataFrame]:
    """Calculate total sales by product and total sales by customer

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        pd.DataFrame: dataframe with total sales by product and customer
    """
    # Calculate the sales for each row
    df["ventas"] = df["cantidad_vendida"] * df["precio_unitario"]

    # Group by product and sum the sales
    total_sales_by_product = df.groupby("producto")["ventas"].sum().reset_index()
    total_sales_by_product.columns = ["producto", "total_ventas_producto"]

    # Group by customer and sum the sales
    total_sales_by_customer = df.groupby("cliente_id")["ventas"].sum().reset_index()
    total_sales_by_customer.columns = ["cliente_id", "total_ventas_cliente"]

    # Merge the two dataframes
    total_sales = pd.concat([total_sales_by_product, total_sales_by_customer], axis=1)

    return {
        "total_ventas_producto": total_sales_by_product,
        "total_ventas_cliente": total_sales_by_customer,
        "total_ventas": total_sales,  # this is not the best to use as it will have repeated columns
    }


def get_customers_with_multiple_categories(df: pd.DataFrame) -> float:
    """Detect customers who have made purchases in more than two product categories and calculate the percentage they represent.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        float: percentage of customers who have purchased in more than two categories
    """
    # Group by customer and category, then count distinct categories per customer
    category_counts = df.groupby("cliente_id")["categoria_producto"].nunique()
    # Filter customers with more than two categories
    customers_with_multiple_categories = category_counts[category_counts > 2]
    # Calculate the percentage
    percentage = (
        len(customers_with_multiple_categories) / df["cliente_id"].nunique()
    ) * 100

    return percentage


def classify_customers_by_total_purchases(df: pd.DataFrame) -> pd.DataFrame:
    """Classify customers based on their total purchases into 'Low', 'Medium', and 'High' using percentiles.

    Args:
        df (pd.DataFrame): cleaned dataframe with the data

    Returns:
        pd.DataFrame: dataframe with a new column classifying customers
    """
    # Calculate the total purchases per customer
    df["ventas"] = df["cantidad_vendida"] * df["precio_unitario"]

    # Calculate the total purchases per customer
    total_purchases = df.groupby("cliente_id")["ventas"].sum()

    # Calculate the 33rd and 66th percentiles
    percentile_33 = total_purchases.quantile(0.33)
    percentile_66 = total_purchases.quantile(0.66)

    # Define a function to classify customers
    def classify(purchase):
        if purchase < percentile_33:
            return "Bajo"
        elif purchase < percentile_66:
            return "Medio"
        else:
            return "Alto"

    # Apply the classification function to the total purchases
    df["clasificacion_cliente"] = df["cliente_id"].map(total_purchases).apply(classify)

    return df


if __name__ == "__main__":
    data_cleaned = clean_data("./ventas_dataset_grande_corregido_con_paises.csv")
    # print("Columns in the DataFrame:", data_cleaned.columns)

    # sales_last_quarter = get_sales_last_quarter(data_cleaned)
    # sales_by_product_and_costumer = get_total_sales_by_product_and_customer(data_cleaned)

    # percentage_customers_multiple_categories = get_customers_with_multiple_categories(data_cleaned)
    # print(f"Percentage of customers with purchases in more than two categories: {percentage_customers_multiple_categories:.2f}%")

    # print(sales_last_quarter)
    # print(sales_by_product_and_costumer.get("total_ventas_producto"))

    # Classify customers by total purchases
    data_classified = classify_customers_by_total_purchases(data_cleaned)
    print(data_classified.head(20))
