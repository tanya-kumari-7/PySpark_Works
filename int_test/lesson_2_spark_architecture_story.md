# Lesson 2: Spark Architecture (Storytelling Edition)

## 🎯 Lesson Goal
Understand Spark architecture **from smallest to largest unit** using a real-life factory story.

By the end of this lesson, you will clearly understand:
- Partitions, Tasks, Executors, Cores
- Stages and Jobs
- Driver, DAG, Cluster Manager
- How everything connects together

---

## 🏭 The Big Picture: A Factory Story

Imagine Spark as a **huge factory** that processes **100 GB of data**.

Processing everything by one worker is impossible, so Spark intelligently **divides work and runs it in parallel**.

---

## 🧠 Characters in the Story

| Spark Component | Story Role |
|-----------------|------------|
| Driver | Factory Manager 🧠 |
| Cluster Manager | HR Department |
| Executor | Worker Group |
| Core | Individual Worker |
| Partition | Box of raw material 📦 |
| Task | Job given to one worker |
| Stage | Phase of factory work |
| Job | Complete order |
| DAG | Work plan |

---

## 🧾 Example We Will Use

```python
df = spark.read.csv("sales.csv")
df2 = df.filter(df.amount > 1000)
df3 = df2.groupBy("city").sum("amount")
df3.show()
```

File size: **100 GB**

---

## 📦 Step 1: Partitions (Smallest Data Unit)

Spark breaks large data into smaller chunks called **partitions**.

- 100 GB file
- Default block size ≈ 128 MB
- ~800 partitions

📌 Each partition is a **box of data** that can be processed independently.

---

## 🛠 Step 2: Tasks (Smallest Execution Unit)

> **Rule:** 1 partition = 1 task

- 800 partitions
- 800 tasks created

Each task processes exactly **one partition**.

---

## 👷 Step 3: Executors (Worker Groups)

Executors are **JVM processes** that run tasks.

Important:
- ❌ Executor is NOT a machine
- ❌ Executor is NOT code
- ✅ Executor is a **process** running on a machine

Responsibilities:
- Execute tasks
- Cache data
- Send results back to the driver

---

## ⚙️ Step 4: Cores (Parallelism)

A **core** represents one parallel task slot.

Example:
- Executor with 4 cores
- Can run 4 tasks simultaneously

```
Executor
 ├── Task 1
 ├── Task 2
 ├── Task 3
 └── Task 4
```

---

## 🧠 Step 5: Driver (The Brain)

The **driver**:
- Runs your PySpark code
- Creates execution plans (DAG)
- Splits work into stages
- Creates and schedules tasks

📌 Your Python code runs **only on the driver**, never on executors.

---

## 🗺 Step 6: DAG (Execution Plan)

DAG = **Directed Acyclic Graph**

It represents:
- Transformations as nodes
- Data flow as edges

Example DAG:
```
Read → Filter → GroupBy → Show
```

---

## 🧱 Step 7: Stages (Phases of Work)

A **stage** is a set of tasks that can run **without shuffling data**.

### Rule:
> Every **shuffle** creates a new stage

---

## 🚚 Step 8: Shuffle (Why It’s Expensive)

Shuffle happens when data must move across machines.

Operations that cause shuffle:
- groupBy
- join
- distinct
- orderBy

Shuffle is expensive because:
- Network I/O
- Disk usage
- Data redistribution

---

## ▶️ Step 9: Job (Triggered by Action)

A **job** starts when an **action** is called:

```python
df3.show()
```

Each action triggers **one Spark job**.

---

## 🔁 End-to-End Execution Flow

```
PySpark Code
   ↓
Driver creates DAG
   ↓
DAG split into stages
   ↓
Stages split into tasks
   ↓
Tasks sent to executors
   ↓
Executors process partitions
   ↓
Results returned to driver
```

---

## ❓ Common Confusions (Cleared)

- Executor ≠ machine
- Task ≠ code
- Partition ≠ executor

One partition → one task → one executor core

---

## 🧠 Memory Trick (Interview Gold)

> **Partition → Task → Executor Core → Stage → Job**

---

## 📝 Checkpoint Questions

1. What decides the number of tasks?
2. What causes a new stage to be created?
3. Who creates tasks: driver or executor?
4. Can one executor run multiple tasks at once? Why?

---

📌 **Next Lesson:** Chapter 3 – Partitions & Parallelism Tuning (Performance Deep Dive)
________

--------------------