import argparse


# 定义一个函数，检查给定的文件是否正确
def check_answers(exercise_file, generated_answer_file, reference_answer_file):
    # 读取题目文件和生成的答案文件
    with open(exercise_file, 'r') as ex_file, open(generated_answer_file, 'r') as gen_ans_file:
        exercises = ex_file.readlines()
        generated_answers = gen_ans_file.readlines()

    # 读取参考答案文件
    with open(reference_answer_file, 'r') as ref_ans_file:
        reference_answers = ref_ans_file.readlines()

    correct_indices = []  # 存储正确答案的索引
    wrong_indices = []  # 存储错误答案的索引

    # 遍历题目文件和生成的答案文件，检查是否正确
    for i, (exercise, generated_answer) in enumerate(zip(exercises, generated_answers), start=1):
        exercise = exercise.strip()
        generated_answer = generated_answer.strip()

        # 如果参考答案文件的长度小于题目文件，则将参考答案设置为N/A
        if i <= len(reference_answers):
            reference_answer = reference_answers[i - 1].strip()
        else:
            reference_answer = "N/A"

        # 如果生成的答案和参考答案相同，则将该题的索引添加到正确索引中
        if generated_answer == reference_answer:
            correct_indices.append(i)
        else:
            # 如果生成的答案和参考答案不同，则将该题的索引添加到错误索引中
            wrong_indices.append(i)

    # 返回正确索引和错误索引
    return correct_indices, wrong_indices

def main():
    parser = argparse.ArgumentParser(description='Check elementary math exercise answers.')
    parser.add_argument('-e', required=True, help='Exercise file')
    parser.add_argument('-g', required=True, help='Generated answer file')
    parser.add_argument('-r', required=True, help='Reference answer file')

    args = parser.parse_args()
    exercise_file = args.e
    generated_answer_file = args.g
    reference_answer_file = args.r

    correct_indices, wrong_indices = check_answers(exercise_file, generated_answer_file, reference_answer_file)

    with open('Grade.txt', 'w') as grade_file:
        grade_file.write(f'Correct: {len(correct_indices)} ({", ".join(map(str, correct_indices))})\n')
        grade_file.write(f'Wrong: {len(wrong_indices)} ({", ".join(map(str, wrong_indices))})\n')


if __name__ == '__main__':
    main()
