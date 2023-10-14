"""
В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и
связь между ними. Одному продукту может соответствовать много
категорий, в одной категории может быть много продуктов.
Напишите метод с помощью PySpark, который вернет все продукты с их
категориями (датафрейм с набором всех пар
«Имя продукта – Имя категории»).
В результирующем датафрейме должны также присутствовать продукты,
у которых нет категорий.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

products_df = spark.createDataFrame([
    (1, 'Продукт 1'),
    (2, 'Продукт 2'),
    (3, 'Продукт 3'),
    (4, 'Продукт 4')
], ['product_id', 'product_name'])

categories_df = spark.createDataFrame([
    (1, 'Категория 1'),
    (2, 'Категория 2'),
    (3, 'Категория 3')
], ['category_id', 'category_name'])

product_category_df = spark.createDataFrame([
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3)
], ['product_id', 'category_id'])

result_df = products_df.join(product_category_df, 'product_id', 'left') \
    .join(categories_df, 'category_id', 'left') \
    .select(products_df.product_name, categories_df.category_name)

result_df.show()
