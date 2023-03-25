class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):

        ''' Проверка стека на пустоту. Метод возвращает True или False. '''

        if self.size() == 0:
            return True
        else:
            return False

    def push(self, el):

        ''' Добавляет новый элемент на вершину стека. Метод ничего не возвращает. '''

        self.stack.append(el)

    def pop(self):

        ''' Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека. '''

        return self.stack.pop()

    def peek(self):

        ''' Возвращает верхний элемент стека, но не удаляет его. Стек не меняется. '''

        if not self.is_empty():
            return self.stack[-1]

    def size(self):

        ''' Возвращает количество элементов в стеке. '''

        return len(self.stack)
