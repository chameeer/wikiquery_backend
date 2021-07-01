import findspark
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.sql.functions import udf
import pyspark.sql.functions as F
import pyspark.sql.types as typ
import pyspark.ml.feature as ft
import pyspark.ml.clustering as clus
from pyspark.ml import Pipeline


findspark.init('/usr/local/spark')

sc = SparkSession.builder \
    .appName('My Spark Application') \
    .master("local[*]").config("spark.driver.memory", "100g") \
    .config("spark.executor.memory", "100g") \
    .config("spark.executor.cores", "2") \
    .config("spark.cores.max", "5") \
    .getOrCreate()

# 数据预处理
df = sc.read.csv('file:///root/Desktop/Wiki_Query/AA/10000.txt', sep='\t')
df = df.toDF('word', 'words')
df_split = df.withColumn("words", F.split(df['words'], " "))

# LDA聚类
cv = ft.CountVectorizer(inputCol="words", outputCol="features", vocabSize=1000000, minDF=10.0)
clustering = clus.LDA(k=30, optimizer='online', featuresCol=cv.getOutputCol())
pipline = Pipeline(stages=[cv, clustering])
topics = pipline.fit(df_split).transform(df_split)

# 结果分为word,id,与topic distribution
mat = topics.select(topics.columns[0], topics.columns[3])
mat = mat.withColumn("word", F.split(mat["word"], " "))


# word
def name(string):
    return string[0:-1][0]


name_udf = udf(name, returnType=typ.StringType())
mat = mat.withColumn("name", name_udf(mat["word"]))


# id
def delete_curid(string):
    return string[-1][7:]


delete_curid_udf = udf(delete_curid, returnType=typ.StringType())
mat = mat.withColumn("id", delete_curid_udf(mat["word"]))

# 储存
res = mat.select(mat.columns[3], mat.columns[2], mat.columns[1])
data_df = res.withColumn("topicDistribution", mat.topicDistribution.cast('string'))
data_df.printSchema()
data_df.write.save(path='file:///root/Desktop/Wiki_Query/csv', format='csv', mode='overwrite', sep='\t')
