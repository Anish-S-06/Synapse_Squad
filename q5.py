#Team Name - Synapse_Squad
def calculate(expression:str)->float:
    stack = []
    num = 0
    sign = '+'

    for iter in range(len(expression)):

        if expression[iter].isdigit():
            num = num * 10 + int(expression[iter])

        if expression[iter] in '+-*/' or iter == len(expression) - 1:

            if sign == '+':
                stack.append(num)

            elif sign == '-':
                stack.append(-num)

            elif sign == '*':
                stack.append(stack.pop() * num)

            elif sign == '/':
                stack.append((stack.pop() / num))
        if expression[iter] in '+-*/':
            sign = expression[iter]
            num = 0
    val=float(sum(stack))

    return round(val, 2)
