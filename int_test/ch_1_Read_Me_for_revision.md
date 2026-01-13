# What is Spark
Spark is a distributed, in-memory computing engine that processes large-scale data efficiently across 
multiple machines in parallel.

## Distributed = Work is shared across many machines
Spark does not run on one single machine.
It runs on multiple machines (nodes) connected together → called a cluster

### How it works in Spark
 
 1. Data is split into parts (partitions)

 2. Each part is processed in parallel

 3. Different machines work at the same time

### Why this is important

 1. Handles very large data (GBs, TBs, PBs)

 2. Faster processing using parallelism

 3. Fault tolerant (if one machine fails, others continue)

## IN-MEMORY = Faster execution by keeping data in RAM
Spark processes data in RAM (memory) instead of repeatedly reading from disk.

## COMPUTING = Processing & transforming data
Spark is built to perform computations on data.

### Types of computations

1. Filtering (filter)

2. Aggregations (groupBy, sum, count)

3. Joins

4. Window functions

5. Machine Learning

6. Streaming analytics
