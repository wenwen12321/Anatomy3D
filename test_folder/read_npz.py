import numpy as np

path = './data/data_2d_h36m_gt.npz'
data = np.load(path, allow_pickle=True)

lst = data.files
print('lst is: \n', lst)

for item in lst:
    print(item)
print('\n', data[item])
