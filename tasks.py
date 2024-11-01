from matplotlib import pyplot as plt
import pandas as pd
from time import time
from dataset_utils import ensure_dataset_loaded


# Задание 1: Первые 10 строк и количество строк/столбцов
@ensure_dataset_loaded()
def task_1(df):
    print("task_1")
    print("\n")

    print("Первые 10 строк датасета:")
    print(df.head(10))
    print(f"\nВсего строк: {df.shape[0]}, Всего столбцов: {df.shape[1]}")

    print("\n\n\n")


# Задание 2: Уникальные города
@ensure_dataset_loaded(required_columns=["City"])
def task_2(df):
    print("task_2")
    print("\n")

    unique_cities = df["City"].dropna().unique()
    print("Уникальные города:")
    print(unique_cities)

    print("\n\n\n")


# Задание 3: Количество товаров в каждой категории
@ensure_dataset_loaded(required_columns=["Category", "ProductID"])
def task_3(df):
    print("task_3")
    print("\n")

    product_count_per_category = df.groupby("Category")["ProductID"].count()
    print("Количество товаров в каждой категории:")
    print(product_count_per_category)

    print("\n\n\n")


# Задание 4: Среднее количество единиц товара на складе по категориям
@ensure_dataset_loaded(required_columns=["Category", "UnitsInStock"])
def task_4(df):
    print("task_4")
    print("\n")

    average_units_in_stock = df.groupby("Category")["UnitsInStock"].mean()
    print("Среднее количество единиц товара на складе по категориям:")
    print(average_units_in_stock)

    print("\n\n\n")


# Задание 5: Самый дорогой товар
@ensure_dataset_loaded(required_columns=["UnitPrice (Products)", "Product", "Category"])
def task_5(df):
    print("task_5")
    print("\n")

    max_price_row = df.loc[df["UnitPrice (Products)"].idxmax()]
    product_name = max_price_row["Product"]
    product_category = max_price_row["Category"]
    max_price = max_price_row["UnitPrice (Products)"]
    print(
        f"Самый дорогой товар: {product_name}, Категория: {product_category}, Цена: {max_price}"
    )

    print("\n\n\n")


# Задание 6: Суммарная прибыль по странам
@ensure_dataset_loaded(required_columns=["Country", "Profit"])
def task_6(df):
    print("task_6")
    print("\n")

    country_profit = df.groupby("Country")["Profit"].sum()
    print("Суммарная прибыль для каждой страны:")
    print(country_profit)

    print("\n\n\n")


# Задание 7: График продаж по странам и страна с наибольшими продажами
@ensure_dataset_loaded(required_columns=["Country", "Sales"])
def task_7(df):
    print("task_7")
    print("\n")

    country_sales = df.groupby("Country")["Sales"].sum()
    country_sales.plot(kind="bar")
    plt.title("Продажи по странам")
    plt.ylabel("Продажи")
    plt.xlabel("Страна")
    plt.show()

    max_sales_country = country_sales.idxmax()
    max_sales_value = country_sales.max()
    print(f"Страна с наибольшими продажами: {max_sales_country} {max_sales_value}")

    print("\n\n\n")


# Задание 8: Уникальные комбинации города и страны
@ensure_dataset_loaded(required_columns=["City and Counry"])
def task_8(df):
    print("task_8")
    print("\n")

    unique_city_country = df["City and Counry"].drop_duplicates()
    print("Уникальные комбинации города и страны:")
    print(unique_city_country)

    print("\n\n\n")


# Задание 9: Средняя стоимость продукта на единицу по категориям
@ensure_dataset_loaded(required_columns=["Category", "UnitCost"])
def task_9(df):
    print("task_9")
    print("\n")

    avg_cost_per_category = df.groupby("Category")["UnitCost"].mean()
    print("Средняя стоимость продукта на единицу по категориям:")
    print(avg_cost_per_category)

    print("\n\n\n")


# Задание 10: Топ-3 компании по наибольшей прибыли
@ensure_dataset_loaded(required_columns=["Customer Company", "Profit"])
def task_10(df):
    print("task_10")
    print("\n")

    top_companies = df.groupby("Customer Company")["Profit"].sum().nlargest(3)
    print("Топ-3 компании по наибольшей прибыли:")
    print(top_companies)

    print("\n\n\n")


# Задание 11: Фильтрация данных по количеству проданных товаров > 30
@ensure_dataset_loaded(required_columns=["Quantity"])
def task_11(df):
    print("task_11")
    print("\n")

    filtered_data = df.query("Quantity > 30")
    print("Записи с количеством проданных товаров больше 30:")
    print(filtered_data)

    print("\n\n\n")


# Задание 12: Топ-5 товаров по количеству заказанных единиц
@ensure_dataset_loaded(required_columns=["Product", "UnitsOnOrder"])
def task_12(df):
    print("task_12")
    print("\n")

    top_products = df.groupby("Product")["UnitsOnOrder"].sum().nlargest(5)
    print("Топ-5 товаров с наибольшим количеством заказанных единиц:")
    print(top_products)

    print("\n\n\n")


# Задание 13: Общее количество проданных товаров по каждому клиенту
@ensure_dataset_loaded(required_columns=["Customer", "Quantity"])
def task_13(df):
    print("task_13")
    print("\n")

    total_quantity_per_customer = df.groupby("Customer")["Quantity"].sum()
    print("Общее количество проданных товаров по каждому клиенту:")
    print(total_quantity_per_customer)

    print("\n\n\n")


# Задание 14: Количество уникальных категорий продуктов в каждом городе
@ensure_dataset_loaded(required_columns=["City", "Category"])
def task_14(df):
    print("task_14")
    print("\n")

    unique_categories_per_city = df.groupby("City")["Category"].nunique()
    print("Количество уникальных категорий продуктов в каждом городе:")
    print(unique_categories_per_city)
