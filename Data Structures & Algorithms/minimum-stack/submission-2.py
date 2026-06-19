class MinStack:

    def __init__(self):
        self._stack = []
        self._prefix = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._prefix:
            if self._prefix[-1] >= val:
                self._prefix.append(val)
        else:
            self._prefix.append(val)
    def pop(self) -> None:
        remove_val = self._stack.pop()
        if remove_val == self._prefix[-1]:
            self._prefix.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._prefix[-1]
