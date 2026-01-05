from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Obesity Spark Intro") \
    .getOrCreate()

print("Spark version:", spark.version)
# Read CSV using Spark
spark_df = spark.read.csv(
    "obesity_prediction.csv",
    header=True,
    inferSchema=True
)

print("Spark DataFrame schema:")
spark_df.printSchema()

print("Row count:", spark_df.count())
