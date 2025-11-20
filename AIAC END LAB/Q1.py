"""
recent_search_stack.py

A simple LIFO Stack class for storing recent searches in a food-delivery app.
Includes example usage and unit tests (unittest).

How to use:
- Run the file directly to see the example usage and run unit tests:
    python recent_search_stack.py

The Stack stores the most recent search on top (index 0 if you inspect get_recent()).
"""

from typing import Generic, Iterable, List, Optional, TypeVar
import unittest

T = TypeVar("T")


class Stack(Generic[T]):
    """
    A simple Last-In-First-Out (LIFO) stack.

    Intended use: store recent searches (most recent pushed item will be popped first).

    Example:
        s = Stack[str]()
        s.push("pizza near me")
        s.push("sushi")
        latest = s.pop()            # "sushi"
        peek = s.peek()             # "pizza near me"

    Methods:
        push(item)       - add an item to the top of the stack.
        pop()            - remove and return the top item. Raises IndexError if empty.
        peek()           - return the top item without removing it; returns None if empty.
        is_empty()       - True if stack has no items.
        size()           - number of items in stack.
        clear()          - remove all items.
        get_recent(n)    - list of recent items with most recent first; if n provided
                           returns up to n items.
    """

    def __init__(self, initial: Optional[Iterable[T]] = None) -> None:
        """
        Create a new stack. Optionally initialize with an iterable of items.
        Items from the iterable are pushed in iteration order so that the last item
        from the iterable becomes the most recent (top) of the stack.

        Args:
            initial: optional iterable of initial items (older -> newer)
        """
        self._data: List[T] = []
        if initial is not None:
            for item in initial:
                self.push(item)

    def push(self, item: T) -> None:
        """
        Push an item onto the top of the stack.

        Args:
            item: the item to be added (e.g., a search string)

        Raises:
            ValueError: if item is None (disallowed for this stack)
        """
        if item is None:
            raise ValueError("None is not allowed as a stack item")
        # Use append/pop for efficient stack operations (top is end of list)
        self._data.append(item)

    def pop(self) -> T:
        """
        Pop the top (most recent) item from the stack.

        Returns:
            The popped item.

        Raises:
            IndexError: if the stack is empty.
        """
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[T]:
        """
        Return the top (most recent) item without removing it.

        Returns:
            The top item, or None if the stack is empty.
        """
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if stack has no items."""
        return len(self._data) == 0

    def size(self) -> int:
        """Return number of items in the stack."""
        return len(self._data)

    def clear(self) -> None:
        """Remove all items from the stack."""
        self._data.clear()

    def get_recent(self, n: Optional[int] = None) -> List[T]:
        """
        Return a list of recent items ordered from most recent -> older.

        Args:
            n: optional maximum number of items to return. If None returns all.

        Returns:
            List of items with the most recent first (index 0 is most recent).
        """
        # self._data stores bottom->top as index 0 -> -1. We want top->bottom.
        rev = list(reversed(self._data))
        if n is None:
            return rev
        if n < 0:
            raise ValueError("n must be non-negative or None")
        return rev[:n]

    def __repr__(self) -> str:
        """Return a concise representation showing most recent first."""
        return f"Stack(recent_first={self.get_recent()})"


# ---------------------------
# Example usage
# ---------------------------
def example_usage() -> None:
    print("=== Example usage of Stack for recent searches ===")
    searches = Stack[str]()

    # User searches
    searches.push("pizza near me")
    searches.push("vegan options")
    searches.push("sushi delivery")

    print("Most recent search (peek):", searches.peek())        # sushi delivery
    print("All recent searches (most recent first):", searches.get_recent())
    print("Stack size:", searches.size())

    # User taps top suggestion (pop)
    chosen = searches.pop()
    print("User selected:", chosen)
    print("After selecting top search, recent searches:", searches.get_recent())

    # Add another search
    searches.push("burgers open now")
    print("After new search:", searches.get_recent())

    # Clear history
    searches.clear()
    print("After clearing, is empty?", searches.is_empty())
    print("================================================\n")


# ---------------------------
# Unit tests
# ---------------------------
class TestStack(unittest.TestCase):
    def test_push_and_pop_lifo_order(self):
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.size(), 3)
        # LIFO: last pushed (3) is popped first
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())

    def test_peek_and_empty_behaviour(self):
        s = Stack[str]()
        self.assertIsNone(s.peek())
        with self.assertRaises(IndexError):
            _ = s.pop()
        s.push("a")
        self.assertEqual(s.peek(), "a")
        self.assertEqual(s.size(), 1)
        # peek shouldn't remove
        self.assertEqual(s.peek(), "a")
        self.assertEqual(s.size(), 1)

    def test_get_recent_order_and_limit(self):
        items = ["old", "mid", "latest"]
        s = Stack[str](initial=items)  # 'latest' should be on top
        self.assertEqual(s.peek(), "latest")
        self.assertEqual(s.get_recent(), ["latest", "mid", "old"])
        self.assertEqual(s.get_recent(2), ["latest", "mid"])
        self.assertEqual(s.get_recent(0), [])

    def test_clear_and_repr(self):
        s = Stack()
        s.push("x")
        s.clear()
        self.assertTrue(s.is_empty())
        self.assertIn("Stack(recent_first", repr(s))

    def test_invalid_push_none(self):
        s = Stack()
        with self.assertRaises(ValueError):
            s.push(None)

    def test_get_recent_with_negative(self):
        s = Stack([1, 2, 3])
        with self.assertRaises(ValueError):
            s.get_recent(-1)


if __name__ == "__main__":
    # Run example usage
    example_usage()

    # Run unit tests (will output test results to console).
    # exit=False so the script does not call sys.exit() after tests, useful in some environments.
    print("Running unit tests...\n")
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
