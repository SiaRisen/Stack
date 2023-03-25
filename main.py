from Stack import Stack


def check_out(string):

    stack = Stack()

    for el in string:
        if el in ['{', '[', '(']:
            stack.push(el)
        elif stack.is_empty():
            return False
        elif stack.peek() and el in [')', ']', '}']:
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':

    result = input('Введите строку со скобками: ')
    if check_out(result) is True:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
