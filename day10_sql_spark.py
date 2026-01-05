from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

def main():
    # Initialize Spark
    spark = SparkSession.builder \
        .appName("Day10SQLMindset") \
        .getOrCreate()

    # 1. Load Data
    df = spark.read.csv("obesity_prediction.csv", header=True, inferSchema=True)

    # 2. Feature Engineering (The Python Way)
    df_transformed = df.withColumn("BMI", round(col("Weight") / (col("Height")**2), 2))

    # 3. REGISTER AS A VIEW (The "Step-wise" Bridge to SQL)
    # This is the core of Day 10
    df_transformed.createOrReplaceTempView("obesity_table")

    # 4. DATA ANALYSIS (The SQL Way)
    # Interviewers love to see that you can write complex SQL strings
    sql_query = """
        SELECT 
            Obesity, 
            COUNT(*) as People_Count, 
            ROUND(AVG(BMI), 2) as Average_BMI
        FROM obesity_table
        GROUP BY Obesity
        ORDER BY Average_BMI DESC
    """
    
    sql_results = spark.sql(sql_query)

    print("--- Final SQL Results ---")
    sql_results.show()

if __name__ == "__main__":
    main()