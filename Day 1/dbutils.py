# Databricks notebook source
# MAGIC %md
# MAGIC #### DBFS (Databricks File System) :Abstraction of your object storage

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs 

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/tables/

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore/tables/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore/tables/")

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/tables/hexaraw")

# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/tables/first/",True)

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/tables/hexaraw/

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/tables/hexaware/

# COMMAND ----------

dbutils.fs.mv("dbfs:/FileStore/tables/hexaware/demo.csv","dbfs:/FileStore/tables/hexaraw/")

# COMMAND ----------


