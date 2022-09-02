from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple
from typing import List


# keep track of max value
# all methods are O(1), except pop() if the max element is removed
# additional space is O(1)
# class Stack:
#     entries = []
#     max_entry = float("-inf")

#     def empty(self) -> bool:
#         return len(self.entries) == 0

#     def max(self) -> int:
#         return self.max_entry

#     def pop(self) -> int:
#         popped = self.entries.pop()
#         if popped == self.max_entry:
#             self.max_entry = self.find_max()
#         return popped

#     def push(self, x: int) -> None:
#         if x > self.max_entry:
#             self.max_entry = x
#         self.entries.append(x)

#     def find_max(self) -> int:
#         max = float("-inf")
#         for entry in self.entries:
#             if entry > max:
#                 max = entry
#         return max


# keep track of max value to the left of each element
# all methods are O(1)
# additional space is O(n)
class Stack:
    Entry = namedtuple("Entry", ["value", "max"])
    entries: List[Entry] = []

    def empty(self) -> bool:
        return len(self.entries) == 0

    def max(self) -> int:
        return self.entries[-1].max

    def pop(self) -> int:
        return self.entries.pop().value

    def push(self, x: int) -> None:
        self.entries.append(self.Entry(x, x if self.empty() else max(x, self.max())))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
