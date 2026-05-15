"""
Utility functions for reading and writing Parquet files using PySpark.
"""


def read_parquet(spark, file_path):
    """
    Read a Parquet file using PySpark.
    """
    return spark.read.parquet(file_path)


def write_parquet(df, file_path, mode="overwrite"):
    """
    Write a DataFrame to a Parquet file.
    """
    df.write.mode(mode).parquet(file_path)


def read_multiple_parquets(spark, file_paths):
    """
    Read multiple Parquet files and return a list of DataFrames.
    """
    return [spark.read.parquet(path) for path in file_paths]


def write_partitioned_parquet(df, file_path, partition_cols, mode="overwrite"):
    """
    Write a DataFrame to Parquet files partitioned by specified columns.
    """
    df.write.mode(mode).partitionBy(partition_cols).parquet(file_path)
