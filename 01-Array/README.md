# Week 1: Python Basics & Lists (Array)

## I. Python Basic Concepts

### 1. Variables and Data Types

#### Variables

- In Python, you can use variables **without declaring the type**.
- The type is automatically assigned based on the value.

```python
x = 10             # int
pi = 3.14          # float
greeting = "Hello" # str
is_active = True   # bool
```

- Choose meaningful variable names.
- You can reassign a variable with a different type, but it is not recommended.

#### Basic Data Types and Operators

- **int**: Integer (e.g., 0, 10, -5)
- **float**: Floating point (e.g., 3.14, -2.7)
- **str**: String (e.g., "Hello", "123")
- **bool**: Boolean (`True` / `False`)

```python
a = 5
b = 2
print(a + b)    # 7
print(a - b)    # 3
print(a * b)    # 10
print(a / b)    # 2.5 (float result)
print(a // b)   # 2 (integer division)
print(a % b)    # 1 (remainder)
print(a ** b)   # 25 (power)
```

---

### 2. Conditionals (if / elif / else)

```python
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C or lower")
```

- You can use multiple `elif`.
- `else` is optional.

---

### 3. Loops

Python mainly uses **for loops** and **while loops**.

#### 3-1. Using `for` and `range()`

```python
for i in range(5):
    print(i)  # 0 to 4
```

```python
for i in range(1, 5):
    print(i)  # 1 to 4
```

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

#### 3-2. Loop through a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### With index (using `enumerate`)

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

#### Reverse loop

```python
for fruit in reversed(fruits):
    print(fruit)
```

#### Nested loop (2D list)

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

---

### 4. Functions

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 5)  # 7
```

---

## II. Python Lists

### 1. What is a List?

- A dynamic array that can grow or shrink.
- Unlike arrays in other languages (C, Java), Python lists can automatically expand.

---

### 2. Creating and Using Lists

```python
my_list = []  # Empty list
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "cherry"]

print(numbers[0])   # 10
print(fruits[1])    # "banana"

numbers[1] = 50     # [10, 50, 30, 40]
```

---

### 3. List Slicing

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[3:])     # [3, 4, 5]
print(nums[::2])    # [0, 2, 4]
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] (reverse)
```

---

### 4. Common List Methods

```python
numbers = [1, 2, 3]
numbers.append(4)      # [1, 2, 3, 4]
numbers.insert(0, 0)   # [0, 1, 2, 3, 4]

last_item = numbers.pop()     # 4
first_item = numbers.pop(0)   # 0
print(numbers)                # [1, 2, 3]

numbers.remove(2)  # [1, 3] (removes the first occurrence of value)

numbers = [3, 1, 4, 2]
numbers.sort()     # [1, 2, 3, 4]

numbers2 = [5, 3, 2]
sorted_list = sorted(numbers2)  # [2, 3, 5]
print(numbers2)                 # [5, 3, 2] (original remains)

letters = ['a', 'b', 'c']
letters.reverse()  # ['c', 'b', 'a']
```

---

### 5. List Comprehension

```python
squares = [x*x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

even_squares = [x*x for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # [4, 16]
```

---

### 6. Useful Built-in Functions

```python
nums = [5, 2, 7, 1]
print(len(nums))   # 4
print(sum(nums))   # 15
print(min(nums))   # 1
print(max(nums))   # 7
```

---

✅ **Tip:** `list()` can convert other iterables (like tuples or strings) into lists.
