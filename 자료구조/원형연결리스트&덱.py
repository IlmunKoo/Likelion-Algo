class _CircularDoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

    def __str__(self):                                  # modified
      return str(self._element)                         # modified

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._header._next = self._header                   # modified
    self._header._prev = self._header                   # modified
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size # 노드 개수 리턴

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor) # 노드 생성
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element # 삭제 원소 담기
    node._prev = node._next = node._element = None # 노드 none처리
    return element                                 # return deleted element

  def __iter__(self):  # generator 정의
      v = self._header._next
      while v != self._header:
          yield v
          assert isinstance(v._next, object)
          v = v._next

  def __str__(self):  # 연결 리스트의 값을 print 출력
      return " -> ".join(str(v) for v in self)
		
class Empty(Exception):
  """Error attempting to access an element from an empty container."""
pass

class CircularLinkedDeque(_CircularDoublyLinkedBase):         # note the use of inheritance
  """Double-ended queue implementation based on a doubly linked list."""

  def first(self):
    """Return (but do not remove) the element at the front of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
        raise Empty("Deque is empty")
    return self._header._next._element # 헤더 바로 뒤 원소 리턴

  def last(self):
    """Return (but do not remove) the element at the back of the deque.
    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
        raise Empty("Deque is empty")
    tail = self._header._prev
    return tail # 원형 연결리스트는 트레일러 없으므로 헤더 앞 원소 리턴

  def insert_first(self, e):
    """Add an element to the front of the deque."""
    self._insert_between(e, self._header, self._header._next) # 헤더와 헤더 바로 뒤 원소 사이 새로운 노드 삽입

  def insert_last(self, e):
    """Add an element to the back of the deque."""
    self._insert_between(e, self._trailer._prev, self.trailer) #트레일러 직전 노드와 트레일러 사이 새로운 노드 삽입

  def delete_first(self):
    """Remove and return the element from the front of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
        raise Empty("Deque is empty")
    return self._delete_node(self._header._next) # 헤더 다음노드와 self 사이 삭제

  def delete_last(self):
    """Remove and return the element from the back of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
        raise Empty("Deque is empty")
    tail = self._header._prev
    return self._delete_node(tail) # tail노드 삭제
# 원형 연결리스트는 트레일러 존재x, 헤더로 트레일러 표현한다.