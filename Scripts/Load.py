



def load_data(df, output_path):
    """
    Saves the cleaned DataFrame both as a CSV file and loads it into MySQL.
    """
    # ✅ Save to local CSV
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)
    print("✅ Data saved to local output folder.")

    # ✅ Now load into MySQL (optional free-tier data warehouse)
    try:
        df.write \
            .format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/etl_project") \
            .option("dbtable", "cleaned_data") \
            .option("user", "root") \
            .option("password", "Supraja@123") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .mode("overwrite") \
            .save()

        print("✅ Data successfully loaded into MySQL database!")

    except Exception as e:
        print(f"⚠️ Could not load to MySQL: {e}")
