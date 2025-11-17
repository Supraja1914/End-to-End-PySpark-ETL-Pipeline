from pyspark.sql import SparkSession

def extract_data(spark, file_path):
    df = spark.read.option("header", True).csv(file_path)
    print("✅ Data extracted successfully")
    return df
