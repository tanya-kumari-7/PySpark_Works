# PySpark: Complete Beginner-to-Advanced Guide

## 1. What is PySpark?
PySpark is the **Python API for Apache Spark**, a distributed computing engine designed to process **large-scale data** efficiently.

- Spark = engine (written in Scala/Java)
- PySpark = Python interface to Spark
- Used when data is **too large for Pandas** or needs **distributed processing**

👉 Think of PySpark as *Pandas on multiple machines*.

---

## 2. Why PySpark?

### Problems with Pandas
- Runs on **single machine**
- Limited by RAM
- Slow for big data

### PySpark Advantages
- Distributed (multiple machines)
- Handles **TB–PB scale data**
- Very fast (in-memory computation)
- Used in **FAANG, fintech, e-commerce**

---

## 3. Spark Ecosystem

| Component | Purpose |
|--------|--------|
| Spark Core | Execution engine |
| Spark SQL | Structured data, SQL |
| PySpark | Python API |
| Spark Streaming | Real-time data |
| MLlib | Machine Learning |
| GraphX | Graph processing |

---

## 4. Spark Architecture (Very Important)

### Key Components

1. **Driver**
   - Brain of Spark
   - Runs your PySpark code
   - Creates execution plan

2. **Cluster Manager**
   - Allocates resources
   - Examples: YARN, Kubernetes, Standalone

3. **Executors**
   - Worker processes
   - Execute tasks
   - Store data in memory

4. **Tasks**
   - Smallest unit of work
   - Runs on executors

📌 Driver sends *tasks* → Executors run them on *partitions*

---

## 5. Data Abstractions in PySpark

### 1️⃣ RDD (Resilient Distributed Dataset)
- Low-level
- Immutable
- Fault-tolerant
- Rarely used now

### 2️⃣ DataFrame (MOST IMPORTANT)
- Distributed table (rows & columns)
- Optimized
- SQL compatible

### 3️⃣ Dataset
- JVM-based (not in PySpark)

👉 **Use DataFrames 95% of the time**

---

## 6. SparkSession

Entry point of PySpark

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
```

- Creates SparkContext internally
- Required for DataFrame operations

---

## 7. Reading Data in PySpark

```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
```

Supported formats:
- CSV
- JSON
- Parquet (best)
- ORC
- Avro
- JDBC (DBs)

---

## 8. DataFrame Basics

### Show data
```python
df.show()
df.printSchema()
```

### Select columns
```python
df.select("name", "age")
```

### Filter rows
```python
df.filter(df.age > 25)
```

### Add column
```python
from pyspark.sql.functions import col

df.withColumn("age_plus_1", col("age") + 1)
```

---

## 9. Transformations vs Actions ⭐

### Transformations (Lazy)
- select
- filter
- withColumn
- groupBy

👉 Creates **logical plan**, does NOT execute

### Actions (Trigger execution)
- show
- count
- collect
- write

📌 Spark runs ONLY when an action is called

---

## 10. Lazy Evaluation

```python
df2 = df.filter(df.age > 25)
```
❌ No execution yet

```python
df2.count()
```
✅ Job runs now

---

## 11. Partitions (EXTREMELY IMPORTANT)

- DataFrame is split into **partitions**
- Each partition processed in parallel

### Check partitions
```python
df.rdd.getNumPartitions()
```

### Repartition vs Coalesce

```python
df.repartition(10)   # shuffle (increase/decrease)
df.coalesce(5)       # no shuffle (only decrease)
```

---

## 12. groupBy & Aggregations

```python
from pyspark.sql.functions import sum, avg

df.groupBy("user_id") \
  .agg(sum("amount").alias("total"), avg("amount"))
```

---

## 13. Joins in PySpark

```python
df1.join(df2, "user_id", "inner")
```

Join types:
- inner
- left
- right
- full
- left_semi
- left_anti

---

## 14. Spark SQL

```python
df.createOrReplaceTempView("users")

spark.sql("SELECT * FROM users WHERE age > 25")
```

---

## 15. Functions (VERY IMPORTANT)

```python
from pyspark.sql.functions import (
    col, when, lit, concat, upper,
    row_number, rank, dense_rank
)
```

### Window Functions

```python
from pyspark.sql.window import Window

w = Window.partitionBy("user_id").orderBy(col("amount").desc())

df.withColumn("rn", row_number().over(w))
```

---

## 16. UDFs (Avoid if Possible)

- Python code runs slower
- Breaks Spark optimization

👉 Prefer **built-in functions**

---

## 17. Caching & Persistence

```python
df.cache()
df.persist()
```

Use when:
- Data reused multiple times
- Expensive transformations

---

## 18. Writing Data

```python
df.write.mode("overwrite").parquet("output/")
```

Modes:
- overwrite
- append
- ignore
- error

---

## 19. Performance Optimization ⭐⭐⭐

- Use Parquet
- Avoid UDFs
- Filter early
- Use broadcast joins
- Control partitions
- Cache wisely

---

## 20. Common Interview Questions

- Difference between RDD & DataFrame
- What is lazy evaluation?
- repartition vs coalesce
- broadcast join
- executor vs core
- skewed data

---

## 21. Where PySpark is Used

- Data Engineering
- Data Analytics
- ETL Pipelines
- Feature Engineering
- BigQuery / S3 / HDFS processing

---

## 22. Learning Roadmap (Recommended)

1. Spark architecture
2. DataFrame basics
3. Filters, joins, groupBy
4. Window functions
5. Partitions & performance
6. Spark SQL
7. Optimization & tuning
8. Real-world projects

---

## 23. Next Steps

If you want, we can go **step-by-step like a classroom**:
- Daily lessons
- Practice questions
- Interview-level scenarios
- Real datasets

Just tell me 👍

