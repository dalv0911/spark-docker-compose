 #!/bin/bash
 
/spark/bin/spark-submit \
--master ${SPARK_MASTER_URL} \
--conf spark.pyspark.python=/usr/bin/python3 \
 $1 \
 $2 \