from pyspark import SparkContext
from pyspark import SparkConf
from operator import add

conf = SparkConf().setAppName('Hello World')
sc = SparkContext(conf=conf)
while (True):
    data = sc.parallelize(list("Hello World"))
    counts = data.map(lambda x: (x, 1)).reduceByKey(add).sortBy(lambda x: x[1], ascending=False).collect()
    for (word, count) in counts:
        print("{}: {}".format(word, count))
    break
sc.stop()