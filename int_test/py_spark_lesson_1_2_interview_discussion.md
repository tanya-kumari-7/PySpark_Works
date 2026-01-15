# PySpark Lessons 1 & 2 + Interview Discussion

## 📘 Lesson 1: Introduction to PySpark

### 1. Problem with Pandas
- Pandas works on a **single machine** and requires **all data in RAM**.
- For large datasets (e.g., 50GB), Pandas **fails** due to memory constraints.

### 2. Why Spark?
- Spark is a **distributed, in-memory computing engine**.
- It can process **large datasets** efficiently.
- **Data is split into partitions** and processed on multiple machines simultaneously.

### 3. Key PySpark Concepts
- **Distributed computing**: Data split into partitions, processed across nodes.
- **Lazy execution**: Transformations are not computed until an **action** is called (e.g., `count()`, `show()`).
- Comparison with Pandas:
  | Feature | Pandas | PySpark |
  |--------|--------|--------|
  | Execution | Single machine | Distributed |
  | Data size | Small-Medium | Very large |
  | Speed | Slower | Fast |
  | Lazy evaluation | ❌ | ✅ |

---

## 📘 Lesson 2: Spark Architecture (Storytelling Edition)

### Story Analogy: The Big Factory
- Factory processes **100 GB of data**.
- One worker cannot do it alone.
- Components of Spark:
  | Component | Story Role |
  |-----------|-----------|
  | Driver | Factory Manager 🧠 |
  | Cluster Manager | HR Department |
  | Executor | Worker Group |
  | Core | Individual Worker |
  | Partition | Box of raw material 📦 |
  | Task | Job given to one worker |
  | Stage | Phase of work |
  | Job | Complete order |
  | DAG | Work plan |

### Example Code
```python
df = spark.read.csv("sales.csv")
df2 = df.filter(df.amount > 1000)
df3 = df2.groupBy("city").sum("amount")
df3.show()
```
File size: 100 GB

### Spark Architecture Flow
1. **Partitions**: Large data split into smaller chunks based on size & transformation. Example: 100 GB → 800 partitions.
2. **Tasks**: Each partition gets one **task**; tasks are units of execution.
3. **Executors**: JVM processes on nodes that execute tasks; can run multiple tasks depending on **cores**.
4. **Cores**: One parallel task slot per core.
5. **Driver**: Main program; creates **DAG**, splits stages, creates tasks, schedules execution.
6. **DAG**: Directed Acyclic Graph; logical plan of transformations.
7. **Stages**: Set of tasks that can execute **without shuffle**; new stage created when shuffle is required.
8. **Shuffle**: Data movement across nodes for operations like `groupBy`, `join`, `distinct`.
9. **Jobs**: Triggered by **actions** like `show()` or `count()`; consist of one or more stages.

### Full Execution Flow
```
Driver (Primary Node) --> DAG --> Stages --> Tasks --> Executors (Worker Nodes) --> Process Partitions --> Return Results to Driver
```

---

## 🧠 Interview Discussion Notes (Q&A)

### Q1: What is Apache Spark?
> Distributed, in-memory data processing engine that splits large datasets into partitions and executes computations across multiple machines.

### Q2: What does "distributed" mean in Spark?
> Large datasets are split into partitions and processed across multiple machines; executors run computations on these partitions in memory instead of processing the entire dataset on a single system.

### Q3: Difference between Partition and Task?
> Partition = chunk of data; Task = execution unit created by driver to process one partition. 1 partition = 1 task.

### Q4: What is an Executor?
> JVM process on a worker node that executes tasks assigned by the driver and returns results. Multiple executors can run on one node depending on resources.

### Q5: What is a Stage and when is a new Stage created?
> Stage = set of tasks that can run without shuffling data. New stage is created whenever a shuffle is required, e.g., during `groupBy`, `join` (non-broadcast), or `distinct`.

### Q6: Full Execution Flow (Partitions → Tasks → Stages → Executors → Driver)
1. PySpark code runs on **Driver**
2. Driver creates **DAG**
3. DAG split into **Stages** (shuffle boundaries)
4. Stages split into **Tasks** (1 task per partition)
5. Tasks sent to **Executors** on worker nodes
6. Executors process **Partitions** in memory
7. Results returned to **Driver**
8. Actions (`show()`, `count()`) trigger **Jobs** consisting of stages

---

## ✅ Key Takeaways from Today
- Pandas fails with large datasets; Spark solves this with **distributed computing and in-memory processing**.
- PySpark executes **lazily**; transformations are executed only when an action is called.
- Spark Architecture mental model: **Partition → Task → Executor → Core → Stage → Job → DAG → Driver**.
- Executors = processes; Driver = brain; Stage = tasks without shuffle; Job = triggered by action.
- Shuffle = expensive data movement.
- Understanding these concepts is **critical for interviews**.

---

📌 Next Steps: Chapter 3 – **Partitions & Parallelism Tuning** with **real examples**.

