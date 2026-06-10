from __future__ import annotations
"""Week 3 homework: The Royal Rail Ledger."""

class SLLNode:
    def __init__(self, value: int, next: SLLNode | None = None) -> None:
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: SLLNode | None = None

class DLLNode:
    def __init__(self, value: int, prev: DLLNode | None = None, next: DLLNode | None = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None

def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()
    if not values:
        return sll
    sll.head = SLLNode(values[0])
    current = sll.head
    for value in values[1:]:
        current.next = SLLNode(value)
        current = current.next
    return sll

def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result

def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head
    while current is not None:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next
    return None

def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head
    while current is not None:
        next_node = current.next
        if current.value == target:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                dll.head = current.next
            if current.next is not None:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev
        current = next_node

def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    if dll.head is None:
        return True
    left = dll.head
    right = dll.tail
    while left is not None and right is not None:
        if left.value != right.value:
            return False
        if left is right:
            break
        left = left.next
        if left is right:
            break
        right = right.prev
    return True