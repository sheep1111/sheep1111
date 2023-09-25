import random
import tkinter as tk
import argparse


# 生成随机的小学四则运算题目
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    question = f"{num1} {operator} {num2} = ?"
    return question, answer


# 检查用户答案是否正确
def check_answer():
    user_answer = user_input.get()
    try:
        user_answer = float(user_answer)
    except ValueError:
        result_label.config(text="请输入有效数字")
        return
    if user_answer == current_answer:
        result_label.config(text="回答正确！", fg="green")
    else:
        result_label.config(text="回答错误！", fg="red")


# 更新题目和答案
def next_question():
    global current_answer
    question, current_answer = generate_question()
    question_label.config(text=question)
    result_label.config(text="")
    user_input.delete(0, "end")


# 创建主窗口
root = tk.Tk()
root.title("小学四则运算题目")

# 创建题目标签
question_label = tk.Label(root, text="", font=("Helvetica", 20))
question_label.pack(pady=20)

# 创建用户输入框
user_input = tk.Entry(root, font=("Helvetica", 16))
user_input.pack()

# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=check_answer, font=("Helvetica", 16))
submit_button.pack(pady=10)

# 创建结果标签
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# 创建下一题按钮
next_button = tk.Button(root, text="下一题", command=next_question, font=("Helvetica", 16))
next_button.pack(pady=10)

# 初始化第一道题目
next_question()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="小学四则运算题目生成器")
    parser.add_argument("-n", type=int, default=10, help="生成题目的个数，默认为10")
    args = parser.parse_args()

    for _ in range(args.n):
        root.update()
        root.after(2000)  # 等待2秒后自动显示下一题
        next_question()

    root.mainloop()
