def gen(source, target):
    yield from source
    target.close()

def toList(target):
    result = []
    try:
        while True:
            item = yield
            result.append(item)
    except GeneratorExit:
        target.send(result)
        target.close()

def rpn(target):
    stack = []
    try:
        while True:
            item = yield
            if isinstance(item, (int, float)):
                stack.append(item)
            elif item == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif item == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif item == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif item == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a / b)
            elif item == 'end':
                result = stack.pop()
                target.send(result)
                stack.clear()
    except GeneratorExit:
        target.close()

src = [5, 7, '+', 2, '*', 20, '-', 'end',
       7, 2, '-', 2, 1, '+', '/', 3, '*', 5, '+', 'end',
       5, 2, '-', 2.5, 2, '*', '*', 13.5, '-', 'end']

lst = []
g = gen(iter(src), toList(rpn(toList(lst))))
next(g)
g.close()

print('Results:', lst)