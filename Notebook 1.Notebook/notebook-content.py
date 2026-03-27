# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0434ed91-8c6e-4d2a-b4ab-ee1127dc9b6d",
# META       "default_lakehouse_name": "lh_FAIAD",
# META       "default_lakehouse_workspace_id": "95c6b3e4-e916-4fc6-aa76-29951df56f24",
# META       "known_lakehouses": [
# META         {
# META           "id": "0434ed91-8c6e-4d2a-b4ab-ee1127dc9b6d"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "f26e674a-088a-4526-8516-312ad0ccfd1e",
# META       "known_warehouses": [
# META         {
# META           "id": "f26e674a-088a-4526-8516-312ad0ccfd1e",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from pyspark.sql import Row

# Create a single-row dataframe
new_row = spark.createDataFrame([
    Row(PersonId=21, FullName="Test User", PreferredName="Test", IsSalesperson=0, EmailAddress="test_user@fabrikam.com")
])

# Append to warehouse table
new_row.write.format("delta").mode("append").saveAsTable("lh_FAIAD.dbo.People")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM lh_FAIAD.dbo.People LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Create a single-row dataframe
new_row = spark.createDataFrame([
    Row(PersonId=21, FullName="Test User", PreferredName="Test", IsSalesperson=False, EmailAddress="test_user@fabrikam.com")
])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Append to warehouse table
new_row.write.format("delta").mode("append").saveAsTable("lh_FAIAD.dbo.People")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Step 4: Verify insertion (optional)
spark.sql("SELECT * FROM dbo.People WHERE PersonId = 21").show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
