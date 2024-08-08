#  Summary of Lecture 9.4.pdf 
**Summary**
## Static Hashing

Static hashing is a hashing scheme where the hash function maps search-key values to a fixed set of bucket addresses. This means that the number of buckets is determined in advance and does not change as the database grows or shrinks.

### Advantages of Static Hashing

* **Simplicity:** Static hashing is relatively simple to implement and understand.
* **Deterministic:** The bucket address for a given search-key value is always the same, which makes it easy to locate records.
* **Space efficiency:** Static hashing can be space-efficient, as it only requires a fixed amount of space for the bucket address table.

### Disadvantages of Static Hashing

* **Fixed number of buckets:** The number of buckets is fixed in advance, which can lead to performance problems if the database grows or shrinks significantly.
* **Bucket overflow:** If a bucket becomes too full, it can overflow, which can lead to performance problems.
* **Reorganization:** If the database grows or shrinks significantly, the hash function may need to be recomputed and the data reorganized, which can be time-consuming.

## Dynamic Hashing

Dynamic hashing is a hashing scheme where the number of buckets can change dynamically as the database grows or shrinks. This means that the hash function can be modified to accommodate the changing number of buckets.

### Advantages of Dynamic Hashing

* **Flexibility:** Dynamic hashing is more flexible than static hashing, as it can accommodate changes in the database size.
* **Reduced overflow:** Dynamic hashing can reduce bucket overflow by increasing the number of buckets as the database grows.
* **Improved performance:** Dynamic hashing can improve performance by reducing bucket overflow and by allowing the hash function to be modified to accommodate the changing number of buckets.

### Disadvantages of Dynamic Hashing

* **Complexity:** Dynamic hashing is more complex to implement and understand than static hashing.
* **Overhead:** Dynamic hashing can incur more overhead than static hashing, as it requires additional data structures to manage the changing number of buckets.

## Comparison of Static and Dynamic Hashing

The following table compares static and dynamic hashing:

| Feature | Static Hashing | Dynamic Hashing |
|---|---|---|
| Number of buckets | Fixed | Dynamic |
| Bucket overflow | Possible | Unlikely |
| Reorganization | May be required | Not required |
| Complexity | Simple | Complex |
| Overhead | Low | High |

## Bitmap Indices

Bitmap indices are a special type of index that is designed for efficient querying on multiple keys. Bitmap indices are created by storing a bitmap for each value of an attribute. The bitmap has as many bits as records in the relation, and each bit corresponds to a record. If a record has the value v for the attribute, then the corresponding bit in the bitmap for v is set to 1. Otherwise, the bit is set to 0.

Bitmap indices can be used to answer queries on multiple attributes very efficiently. For example, to find all records where the gender is male and the income level is L1, we can perform the following operation:

```
(bitmap-gender-male) AND (bitmap-income-level-L1)
```

This operation will return a bitmap with 1s for all records that satisfy the query. We can then retrieve the records corresponding to the 1s in the bitmap.

Bitmap indices are particularly useful for queries on attributes that take on a relatively small number of distinct values. This is because the size of a bitmap is proportional to the number of distinct values.

## Applications of Hashing and Bitmap Indices

Hashing and bitmap indices are used in a variety of applications, including:

* **Database management systems:** Hashing and bitmap indices are used to improve the performance of database queries.
* **Search engines:** Hashing is used to index web pages and bitmap indices are used to filter search results.
* **Data mining:** Hashing and bitmap indices are used to identify patterns and trends in data.
* **Computer security:** Hashing is used to store passwords and other sensitive information in a secure way.
