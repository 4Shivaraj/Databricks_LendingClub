# Databricks notebook source
# MAGIC %md
# MAGIC ### Pre-Prod Environment Vairables

# COMMAND ----------

rawFiles_file_path="abfss://raw-data@formula1datalake98.dfs.core.windows.net/lending_loan/"

# COMMAND ----------

processed_file_path="abfss://processed-data@formula1datalake98.dfs.core.windows.net/pre-prod/lending_loan/"

# COMMAND ----------

cleanedScript_folder_path="/LendingClub/Data-Cleaning/"

# COMMAND ----------

cleanedFiles_file_path="abfss://cleaned-data@formula1datalake98.dfs.core.windows.net/lending_loan/"

# COMMAND ----------

dbfs_file_path="/FileStore/tables/"

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

# COMMAND ----------


def ingestDate(input_df):
    date_df=input_df.withColumn("ingest_date",current_timestamp())
    return date_df
