from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        '''Проверка стека на пустоту. Метод возвращает True или False.'''
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.stack.append(item)

    def pop(self):
        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.'''
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element

    def size(self):
        '''Возвращает количество элементов в стеке'''
        if len(self.stack) == 0:
            return None
        else:
            return len(self.stack)


def balance_check(string):
    stack = Stack()
    balance = True
    index = 0
    while index < len(string) and balance:
        symbol = string[index]
        if symbol in '[({':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.is_empty():
        return "сбалансировано"
    else:
        return "несбалансировано"


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


# Cбалансированные последовательности скобок:
string_1 = '(((([{}]))))'
string_2 = '[([])((([[[]]])))]{()}'
string_3 = '{{[()]}}'

# Несбалансированные последовательности скобок:
string_4 = '}{}'
string_5 = '{{[(])]}}'
string_6 = '[[{())}]'


print(balance_check(string_1))
print(balance_check(string_2))
print(balance_check(string_3))
print(balance_check(string_4))
print(balance_check(string_5))
print(balance_check(string_6))
