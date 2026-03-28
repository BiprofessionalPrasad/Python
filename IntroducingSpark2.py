import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
# set up spark context
sc = SparkContext()

#set up spark session
spark=SparkSession(sc)

from pyspark.sql.types import Row
from datetime import datetime

#create RDD resilient distributed dataset
simple_data=sc.parallelize([1,"abc",12])
simple_data

#no of elements
simple_data.count()
simple_data.first()