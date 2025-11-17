# 🚀 End-to-End PySpark ETL Pipeline

This project demonstrates a **complete ETL (Extract, Transform, Load)** workflow built using **Apache PySpark**.  
The pipeline performs **data ingestion from CSV**, applies **transformations and aggregations**, and generates **cleaned insights** ready for analytics and reporting.


## 📁 Project Overview

The **End-to-End PySpark ETL Pipeline** is designed to automate the process of reading raw CSV data, transforming it using PySpark, and producing high-quality structured datasets for downstream analytics.

This project showcases real-time, production-style ETL logic, and demonstrates how to work with distributed data efficiently using PySpark in a **free-tier, local environment (MacOS)**.


## 🧩 Architecture

                ┌────────────────────────────┐
                │        Raw Data (CSV)      │
                └──────────────┬─────────────┘
                               │
                               ▼
                  ┌──────────────────────┐
                  │  Extract (PySpark)   │
                  │  - Read CSV          │
                  │  - Schema Validation │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Transform (PySpark)  │
                  │ - Data Cleaning      │
                  │ - Aggregation        │
                  │ - Business Logic     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Load (PySpark)     │
                  │ - Write to Output    │
                  │ - Save as Parquet/CSV│
                  └──────────────────────┘

Tech Stack:

| Component   | Tool/Version         |
| ----------- | -------------------- |
| Language    | Python 3.11          |
| Framework   | Apache PySpark 4.0.1 |
| OS          | macOS                |
| IDE         | VS Code / PyCharm    |
| Data Source | CSV Files            |

⚙️ Features

✅ End-to-End ETL Workflow (Extract → Transform → Load)
✅ Schema validation and null handling
✅ Aggregation and transformation logic using PySpark
✅ Modular, reusable Python code structure
✅ Runs entirely on free-tier (local) environment

📊 Output

After execution, the pipeline generates cleansed and aggregated datasets, which can be easily connected to Power BI, Tableau, or any BI tool for visualization.

💡 What I Learned

Building scalable ETL pipelines using Apache PySpark

Handling schema validation, joins, and transformations

Managing file I/O operations on macOS

Structuring Python code for modular and reusable data workflows

Setting up Git and pushing a project from local machine to GitHub