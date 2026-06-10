# Week 3: The Royal Rail Ledger

## Overview
This project implements singly and doubly linked list data structures and operations in Python.

## Functions

- **`build_sll_from_list(values)`** – Builds a singly linked list from a Python list
- **`sll_to_list(sll)`** – Converts a singly linked list back to a Python list
- **`find_first_repeat_sll(sll)`** – Returns the first repeated value in a singly linked list, or `None`
- **`remove_all_from_dll(dll, target)`** – Removes all nodes with the target value from a doubly linked list
- **`is_train_palindrome(dll)`** – Returns `True` if the doubly linked list reads the same forward and backward

## Usage

```python
from src.challenges import build_sll_from_list, sll_to_list, find_first_repeat_sll

sll = build_sll_from_list([1, 2, 3, 2, 4])
print(sll_to_list(sll))            # [1, 2, 3, 2, 4]
print(find_first_repeat_sll(sll))  # 2
```

## Running Tests

```bash
python3 -m pytest --tb=short
```