import argparse    #处理命令行参数
import random      # 随机数
from fractions import Fraction# 处理分数

# 定义运算符
operators = ['+', '-', '*', '/']

def generate_expression(min_value, max_value, max_operators):
    # 递归生成数学表达式
    if max_operators == 0 or (min_value == 1 and max_value == 1):
        #如果不需要再添加运算符或者已经达到最小值1直接返回一个随机整数
        return str(random.randint(min_value, max_value))

    operator = random.choice(operators) #随机选择一个运算符
    if operator == '+':
        e1 = generate_expression(min_value, max_value, max_operators - 1)
        e2 = generate_expression(min_value, max_value, max_operators - 1)
    elif operator == '-':
        e1 = generate_expression(min_value, max_value, max_operators - 1)
        e2 = generate_expression(min_value, max_value, max_operators - 1)
    elif operator == '*':
        e1 = generate_expression(min_value, max_value, max_operators - 1)
        e2 = generate_expression(min_value, max_value, max_operators - 1)
    else:
        e1 = generate_expression(min_value, max_value, max_operators - 1)
        e2 = generate_expression(min_value, max_value, max_operators - 1)

    return f"({e1} {operator} {e2})"#返回拼接好的表达式

# 定义一个函数，用于评估表达式
def evaluate_expression(expression):
    try:
        # 使用eval函数计算表达式的值，并使用limit_denominator函数将其限制为最简分数
        return Fraction(eval(expression)).limit_denominator()
    except ZeroDivisionError:
        # 避免除以零的错误
        return None

def generate_exercises(num_exercises, max_value):
    exercises = []#储存生成的题目
    answers = []  #储存题目的答案

    for _ in range(num_exercises):
        min_value = 1  # 最小值始终为1
        max_operators = 2  # 最多3个运算符
        expression = generate_expression(min_value, max_value, max_operators)
        exercises.append(expression)

        # 计算表达式的值
        result = evaluate_expression(expression)
        while result is None or result.numerator < 0:
            # 重新生成表达式，确保没有负数或分母为0的情况
            expression = generate_expression(min_value, max_value, max_operators)
            exercises[-1] = expression
            result = evaluate_expression(expression)

        answers.append(result)

    return exercises, answers

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            if isinstance(item, Fraction):
                file.write(f"{item.numerator}/{item.denominator}\n")
            else:
                file.write(f"{item}\n")

def main():
    parser = argparse.ArgumentParser(description='Generate elementary math exercises.')
    parser.add_argument('-n', type=int, required=True, help='Number of exercises to generate')
    parser.add_argument('-r', type=int, required=True, help='Maximum value for numbers in exercises')

    args = parser.parse_args()
    num_exercises = args.n
    max_value = args.r

    exercises, answers = generate_exercises(num_exercises, max_value)

    save_to_file('Exercises.txt', exercises)
    save_to_file('Answers.txt', answers)

if __name__ == '__main__':
    main()
