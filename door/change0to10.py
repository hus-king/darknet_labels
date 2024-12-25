import os

def replace_zero_with_ten():
    # 获取当前工作目录
    directory = os.getcwd()
    # 遍历当前目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # 确保是txt文件
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # 替换每一行中的第一个0为10
            with open(file_path, 'w', encoding='utf-8') as file:
                for line in lines:
                    # 找到第一个0的位置
                    zero_index = line.find('0')
                    if zero_index != -1:
                        # 替换第一个0为10
                        line = line[:zero_index] + '10' + line[zero_index+1:]
                    file.write(line)

# 调用函数
replace_zero_with_ten()