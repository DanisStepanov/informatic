class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стек пуст"

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Стек:", stack.items)

print("Извлечение элемента:", stack.pop())
print("Извлечение элемента:", stack.pop())

print("Вершина стека:", stack.peek())
print("Размер стека:", stack.size())