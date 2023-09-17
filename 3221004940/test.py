import sys
import difflib

def read_text_file(file_path):
    '''
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在.")
        sys.exit(1)

def calculate_plagiarism_rate(original_text, copied_text):
    d = difflib.Differ()
    diff = list(d.compare(original_text.split(), copied_text.split()))
    match = [item for item in diff if item[0] == ' ']
    plagiarism_rate = (len(match) / len(original_text.split())) * 100
    return round(plagiarism_rate, 2)

def main():
    if len(sys.argv) != 4:
        print("用法: python 论文查重.py <原文文件路径> <抄袭版文件路径> <答案文件路径>")
        sys.exit(1)

    original_file_path = sys.argv[1]
    copied_file_path = sys.argv[2]
    answer_file_path = sys.argv[3]

    original_text = read_text_file(original_file_path)
    copied_text = read_text_file(copied_file_path)

    plagiarism_rate = calculate_plagiarism_rate(original_text, copied_text)

    with open(answer_file_path, 'w', encoding='utf-8') as answer_file:
        answer_file.write(f"{plagiarism_rate}%\n")

if __name__ == "__main__":
    main()
