# Lesson 1: Introduction to PySpark

## 🎯 Lesson Goal
By the end of this lesson, you will understand:
- What PySpark is
- Why Pandas is not enough for big data
- What problem Apache Spark solves
- Core concepts like distributed computing and lazy execution

---

## 1. The Core Problem

Data size keeps growing:
- Few million rows → Pandas works
- Tens of millions of rows → Pandas slows down
- Hundreds of millions / GBs of data → ❌ Pandas fails

### Why?
Pandas works on:
- A **single machine**
- A **single RAM**
- Mostly **single-threaded execution**

If data size is larger than available RAM (e.g., 50GB data on a 16GB machine), Pandas throws memory errors.

---

## 2. Why Pandas Is Not Enough

| Pandas Limitation | Explanation |
|------------------|------------|
| Single machine | Cannot scale beyond one system |
| Memory bound | Entire data must fit in RAM |
| Limited parallelism | Slow for large datasets |

Example:
```python
pd.read_csv("50GB_file.csv")  # MemoryError
```

---

## 3. What Is Apache Spark?

**Apache Spark** is a:
> Distributed, in-memory data processing engine

### Key Characteristics
- **Distributed** → Uses multiple machines
- **In-memory** → Faster than disk-based systems
- **Processing engine** → Optimizes and executes jobs efficiently

---

## 4. What Is PySpark?

**PySpark** is the Python API for Apache Spark.

- Spark is written in Scala/Java
- PySpark allows Python developers to use Spark

### Simple Analogy
- Spark = Engine
- PySpark = Steering wheel (Python control)

---

## 5. PySpark vs Pandas (High-Level)

| Feature | Pandas | PySpark |
|------|--------|--------|
| Execution | Single machine | Distributed |
| Data size | Small–Medium | Very large |
| Speed | Slower on big data | Fast |
| Lazy evaluation | ❌ No | ✅ Yes |
| SQL support | Limited | Strong |

---

## 6. Distributed Computing in Spark

Distributed means:
- Data is split into **partitions**
- Partitions are processed **in parallel**
- Executors running on multiple nodes handle computation

This parallelism makes Spark scalable and fast.

---

## 7. Lazy Execution (Very Important)

In PySpark, transformations do not execute immediately.

Example:
```python
df_filtered = df.filter(df.age > 50)
```

No computation happens yet.

Execution starts only when an **action** is called:
```python
df_filtered.count()
df_filtered.show()
```

### Benefits of Lazy Execution
- Better optimization
- Reduced computation
- Efficient execution planning

---

## 8. Real-World Use Cases of PySpark

- ETL pipelines
- User activity analytics
- Financial data processing
- Feature engineering for ML models
- Processing data from S3, HDFS, BigQuery

---

## 9. Key Takeaways

- Pandas fails when data exceeds RAM
- Spark solves this using distributed computing
- PySpark is Spark’s Python interface
- PySpark uses lazy execution for performance

---

## 10. Interview Checkpoint Questions

1. Why does Pandas fail on very large datasets?
2. What does distributed computing mean in Spark?
3. What is lazy evaluation in PySpark?

---

📌 **Next Lesson:** Spark Architecture (Driver, Executor, Tasks, Partitions)

