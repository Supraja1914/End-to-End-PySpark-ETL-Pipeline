def transform_data(df):
    df_transformed = df.dropna()
    print("✅ Data transformed (nulls removed)")
    return df_transformed
