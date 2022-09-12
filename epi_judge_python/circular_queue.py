from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.list = [0] * capacity
        self.head = self.tail = self.num_elements = 0

    # time: O(1) (amortized)
    def enqueue(self, x: int) -> None:
        if self.size() == len(self.list):
            self.resize()
        self.list[self.tail] = x
        self.tail = (self.tail + 1) % len(self.list)
        self.num_elements += 1

    # time: O(1)
    def dequeue(self) -> int:
        self.num_elements -= 1
        value = self.list[self.head]
        self.head = (self.head + 1) % len(self.list)
        return value

    # time: O(1)
    def size(self) -> int:
        return self.num_elements

    def resize(self) -> None:
        self.list = self.list[self.head :] + self.list[: self.head] + [0] * self.size()
        self.head = 0
        self.tail = self.size()


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure("Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
