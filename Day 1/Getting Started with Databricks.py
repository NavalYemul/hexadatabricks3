# Databricks notebook source
# MAGIC %md
# MAGIC #### Welcome to databricks

# COMMAND ----------

# MAGIC %md
# MAGIC # Getting Started with Spark
# MAGIC ## Getting Started with Databricks
# MAGIC ### Azure Databricks
# MAGIC #### Lakehouse
# MAGIC ##### Delta lake

# COMMAND ----------

print("Run Python")

# COMMAND ----------

# MAGIC %scala
# MAGIC println("run Scala")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "RUN SQL"

# COMMAND ----------

print("ehello")

# COMMAND ----------

# MAGIC %sql 
# MAGIC Create schema if not exists hexawaredev;
# MAGIC use hexawaredev

# COMMAND ----------

# MAGIC %sql
# MAGIC create table hexawaredev.sample(id int, name string, age int)

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO hexawaredev.sample VALUES(1,'a', 28),(2,'b',30)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from hexawaredev.sample

# COMMAND ----------

# MAGIC %sql
# MAGIC show schemas;
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail hexawaredev.sample

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended hexawaredev.sample

# COMMAND ----------


