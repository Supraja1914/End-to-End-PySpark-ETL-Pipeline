from operator import countOf

from pyspark.sql import SparkSession


from ETL_Project.Scripts.Extract  import extract_data
from ETL_Project.Scripts.transform import transform_data
from ETL_Project.Scripts.Load import load_data

# Initialize Spark
spark = SparkSession.builder \
    .appName("ETL_Pipeline_Supraja") \
    .config("spark.jars", "/Users/suprajabhogineni/SparkJars/mysql-connector-j-8.0.33.jar") \
    .getOrCreate()

# Paths
input_path = "data/input/CallcenterInsight.csv"

df_raw = extract_data(spark, input_path)
df_clean = transform_data(df_raw)

# Write cleaned data to MySQL
df_clean.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/etl_demo") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "cleaned_callcenter_data") \
    .option("user", "root") \
    .option("password", "Supraja@123") \
    .mode("overwrite") \
    .save()

print("✅ Data successfully loaded into MySQL!")
spark.stop()








