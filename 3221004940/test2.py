import jieba
import time
start = time.perf_counter()
def lcs(X, Y):
    # Get the length of the strings
    m = len(X)
    n = len(Y)
    # Create a 2D array to store the LCS
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Iterate through the 2D array
    for i in range(m + 1):
        for j in range(n + 1):
            # If the current character is same, then the LCS is current character
            if i == 0 or j == 0:
                L[i][j] = 0
            # If the current character is same, then the LCS is current character
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            # If the current character is not same, then the LCS is maximum of LCS of current character and the LCS of previous character
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Return the length of LCS
    return L[m][n]

def calculate_similarity_rate(original_text, plagiarized_text):
    X = list(jieba.cut(original_text))
    Y = list(jieba.cut(plagiarized_text))

    lcs_length = lcs(X, Y)
    avg_length = (len(X) + len(Y)) / 2.0

    return lcs_length / avg_length

with open("orig.txt", "r", encoding='utf-8') as f:  #打开文本
    original_text = f.read()   #读取文本

with open("orig_0.8_add.txt", "r", encoding='utf-8') as f:  #打开文本
    plagiarized_text = f.read()   #读取文本
#original_text = "今天是星期天，天气晴，今天晚上我要去看电影。"
#plagiarized_text = "今天是周天，天气晴朗，我晚上要去看电影。"
print(f"重复率: {calculate_similarity_rate(original_text, plagiarized_text):.2f}")

end = time.perf_counter()
print(f"程序运行时间:{end - start:0.4f}秒")