import findspark
import os

findspark.init()

from pyspark.sql import SparkSession


def get_spark_session(app_name="NYC Taxi Pipeline"):
    """
    Create and return a Spark session with predefined configurations.
    """
    # Set HADOOP_HOME and update PATH
    hadoop_home = "C:\\vs_code_projects\\python\\hadoop-3.2.1"
    os.environ['HADOOP_HOME'] = str(hadoop_home)
    os.environ['PATH'] += os.pathsep + str(hadoop_home + '\\bin')
    
    # Create Spark session
    spark = SparkSession. \
        builder. \
        appName(app_name). \
        config("spark.executor.cores", 1). \
        config("spark.executor.instances", 1). \
        config("spark.executor.memory", "1g"). \
        config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"). \
        config("spark.hadoop.io.native.lib.available", "false"). \
        master("local[*]"). \
        getOrCreate()
    
    return spark
