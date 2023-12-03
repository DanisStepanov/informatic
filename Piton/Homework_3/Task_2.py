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
print("Добавлен элемент 1. Содержимое стека:", stack.items)

stack.push(2)
print("Добавлен элемент 2. Содержимое стека:", stack.items)

stack.push(3)
print("Добавлен элемент 3. Содержимое стека:", stack.items)


popped_item = stack.pop()
print("Извлечен элемент", popped_item, ". Содержимое стека:", stack.items)

popped_item = stack.pop()
print("Извлечен элемент", popped_item, ". Содержимое стека:", stack.items)

popped_item = stack.pop()
print("Извлечен элемент", popped_item, ". Содержимое стека:", stack.items)