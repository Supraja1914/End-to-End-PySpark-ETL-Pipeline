from pyspark.sql import SparkSession
from ETL_Project.Scripts.Extract import extract_data

# 1️⃣ Initialize Spark session
spark = SparkSession.builder \
    .appName("CrosscheckOutputFile") \
    .getOrCreate()

# 2️⃣ Define paths directly
input_path = "Data/Input/CallcenterInsight.csv"
output_path = "Data/Output/cleaned_data.csv"

# 3️⃣ Read the cleaned output
out = spark.read.option("header", True).csv(output_path)

print("\n✅ Sample of Cleaned Output Data:")
out.show(5, truncate=False)

print("\n📘 Schema of Cleaned Output:")
out.printSchema()

# 4️⃣ Compare record counts
df_raw = extract_data(spark, input_path)
print(f"✅ Raw Data Loaded: {df_raw.count()} records")
print(f"✅ Cleaned Output Records: {out.count()} records")

# 5️⃣ Optional: check for duplicates or missing values
print("\n🔍 Checking for nulls in each column:")
for col in out.columns:
    null_count = out.filter(out[col].isNull()).count()
    if null_count > 0:
        print(f"Column '{col}' has {null_count} nulls")

spark.stop()
print("\n🚀 Crosscheck Completed Successfully!")
