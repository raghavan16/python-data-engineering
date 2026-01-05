from pyspark.sql import SparkSession  # Ensure capital S and S
from pyspark.sql.functions import col, round, avg, count

def main():
    # Initialize Spark
    spark = SparkSession.builder \
        .appName("ObesityFeatureEngineering") \
        .getOrCreate()
    df = spark.read.csv("obesity_prediction.csv", header=True, inferSchema=True)
    # 3. Feature Engineering (Narrow Transformation)
    # Adding BMI: Weight(kg) / Height(m)^2
    df_transformed = df.withColumn("BMI", round(col("Weight") / (col("Height")**2), 2))

    # 4. Aggregation (Wide Transformation)
    # Target: Distribution of Obesity Levels
    ##obesity_report = df_transformed.groupBy("ObesityCategory") \
    obesity_report = df_transformed.groupBy("Obesity") \
        .agg(
            count("*").alias("Total_Count"),
            round(avg("BMI"), 2).alias("Avg_BMI")
        )
    # 5. Output/Action
    print("Obesity Category Summary:")
    obesity_report.show()

    # 6. Save (Optional - for Git evidence)
    # obesity_report.write.mode("overwrite").csv("outputs/obesity_summary.csv")

if __name__ == "__main__":
    main()  