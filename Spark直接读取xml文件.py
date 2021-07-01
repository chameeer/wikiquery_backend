$HADOOP_HOME/sbin/stop-all.sh
$HADOOP_HOME/sbin/start-all.sh
$SPARK_HOME/bin/pyspark --packages com.databricks:spark-xml_2.11:0.12.0

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as Type
import pyspark.ml.feature as FT
from pyspark import StorageLevel
spark = SparkSession.builder.getOrCreate()

df = spark.read.format('xml').options(rowTag='page').load('file:///root/Desktop/Wiki_Query/zhwiki-latest-pages-articles.xml')
# df.printSchema()
# df.count()
df = df.filter(~df.title.like("Wiki%")).filter(~df.title.like("Help%"))
df.select([df.id, df.title, df.revision.text._VALUE]).write.format('xml').save('file:///root/Desktop/Wiki_Query/zhwiki-filter')

df = spark.read.format('xml').load('file:///root/Desktop/Wiki_Query/zhwiki-filter')