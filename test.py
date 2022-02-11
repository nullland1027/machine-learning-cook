import numpy as np

file_path = './data/adult.csv'
X, y = [], []
count_lessthan50k = 0
count_morethan50k = 0
num_images_threshould = 10000

with open(file_path, 'r') as f:
    for line in f.readlines():
        if '?' in line:
            continue
        data = line[:-1].split(', ')  # 相当于读取了一条X, 索引为[:-1]是避免了读取到\n
        if data[-1] == '<=50k' and count_lessthan50k < num_images_threshould:
            X.append(data)
            count_lessthan50k += 1
        elif data[-1] == '>50k' and count_morethan50k < num_images_threshould:
            X.append(data)
            count_morethan50k += 1
        if count_lessthan50k >= num_images_threshould and count_morethan50k >= num_images_threshould:
            break
X = np.array(X)
print(X)