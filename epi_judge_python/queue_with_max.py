import collections
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    entries = collections.deque()
    potential_max = collections.deque()

    # time: O(1) (amortized)
    def enqueue(self, x: int) -> None:
        self.entries.append(x)
        while self.potential_max and self.potential_max[-1] < x:
            self.potential_max.pop()
        self.potential_max.append(x)

    # time: O(1)
    def dequeue(self) -> int:
        value = self.entries.popleft()
        if value == self.potential_max[0]:
            self.potential_max.popleft()
        return value

    # time: O(1)
    def max(self) -> int:
        return self.potential_max[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == "QueueWithMax":
                q = QueueWithMax()
            elif op == "enqueue":
                q.enqueue(arg)
            elif op == "dequeue":
                result = q.dequeue()
                if result != arg:
                    raise TestFailure(
                        "Dequeue: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "queue_with_max.py", "queue_with_max.tsv", queue_tester
        )
    )
