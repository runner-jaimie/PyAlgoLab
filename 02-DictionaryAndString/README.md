
# 📚 Week 2 - Python Dictionary & String

## I. Hash Table

### What is a Hash Table?

A **Hash Table** stores data in **Key-Value** pairs for fast retrieval.

- **Key**: string, integer, tuple, etc.
- **Value**: the actual data associated with the key

🔎 **Average time complexity:** O(1) for insert, search, delete (with good hash function and enough space)

### Hash Function

- Converts a key into a hash value (integer) for indexing
- Example:
```python
hash("apple") = 4
hash(123) = 123 % TABLE_SIZE
```

### Collision Handling

- **Chaining**: Store multiple items in a bucket using a linked list
- **Open Addressing**: Find another empty slot by probing

Python's `dict` uses optimized forms of **chaining** and **open addressing**.

---

## II. Python Dictionary

### Basic Usage
```python
# Create
person = {"name": "Alice", "age": 25}

# Insert / Update
person["city"] = "New York"

# Access
print(person.get("name", "Unknown"))

# Delete
del person["age"]

# Iterate
for key, value in person.items():
    print(key, value)
```

- Keys must be **hashable (immutable)**
- Python 3.7+ preserves **insertion order**

### Example
```python
scores = {"Alice": 90, "Bob": 75}
scores["Charlie"] = 85
print(scores.get("Alice"))  # 90
print(scores.get("Eve", 0)) # 0
del scores["Bob"]

for name, score in scores.items():
    print(f"{name}: {score}")
```

---

## 📝 III. String Basics

### String Features

- **Immutable** in Python
- Supports Unicode
- Easy slicing and built-in methods

### Example
```python
s = "Hello Python"
print(s[0])         # 'H'
print(s[-1])        # 'n'
print(s[0:5])       # 'Hello'
print(s[::-1])      # 'nohtyP olleH'

print(s.lower())    # 'hello python'
print(s.upper())    # 'HELLO PYTHON'
print("_".join(["A", "B", "C"]))  # 'A_B_C'
```

### Useful Methods
- `strip()`: Remove spaces
- `replace(old, new)`: Replace text
- `startswith()`, `endswith()`
- `isalpha()`, `isdigit()`, `isalnum()`

---

## 🔗 IV. Hash Table Collision Handling

### Chaining
- Each bucket stores a linked list of items
- Example:
```
Index 1 -> (Key1, Value1) -> (Key7, Value7) -> (Key10, Value10)
```

### Open Addressing
- Probes the next slot when a collision occurs
- Linear probing example:
```
Index 0: (Key1, Value1)
Index 1: (Key2, Value2)
Index 2: (Key3, Value3)
```

---

## ⚖️ V. Chaining vs Open Addressing Comparison

| Feature            | Chaining                   | Open Addressing                |
| ------------------ | -------------------------- | ------------------------------ |
| Collision Handling | Linked List                | Probing within the array       |
| Memory Usage       | Extra memory for chains    | Better cache performance       |
| Insert/Delete      | Simple                     | More complex (may need rehash) |
| Worst Case         | O(n) if many in one bucket | O(n) if many probes            |
| Used in Python     | Hybrid (optimized mix)     | Hybrid (optimized mix)         |

---

## ✅ Conclusion

- **Chaining**: Easy to implement, extra memory required
- **Open Addressing**: Space-efficient but complex and sensitive to load factor
- Python `dict` uses **a hybrid approach** for performance and memory efficiency.

---

> 💡 **Tip:** Mastering dictionaries and strings is essential for coding interviews (Anagrams, Palindromes, etc.)!
