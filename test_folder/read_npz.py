# run script:
# python ./test_folder/read_npz.py

# reference (save & load .npz file): https://ithelp.ithome.com.tw/articles/10196167
# https://www.796t.com/article.php?id=144889
import numpy as np

path = './data/data_2d_h36m_gt.npz'                      # 有 ['positions_2d', 'metadata'] # 【'metadata'】: {'num_joints': 17, 'keypoints_symmetry': [[4, 5, 6, 11, 12, 13], [1, 2, 3, 14, 15, 16]]}
# path = './data/data_2d_h36m_cpn_ft_h36m_dbb.npz'       # 有 ['positions_2d', 'metadata'] # 【'metadata'】: {'layout_name': 'h36m', 'num_joints': 17, 'keypoints_symmetry': [[4, 5, 6, 11, 12, 13], [1, 2, 3, 14, 15, 16]]} 
# path = './data/data_2d_h36m_hr.npz'                    # 只有 ['positions_2d'] (可能要再重做 preprocessing)
data = np.load(path, allow_pickle=True)

lst = data.files
print('lst is: \n', lst) # output: ['positions_2d', 'metadata']

for item in lst:
    print('【' + item + '】') # output: positions_2d, metadata
    tmp_item = data[item]
    print(tmp_item, '\n')

# print(data['positions_2d'].shape) # output: (), I don't know why this cannot output its shape
#################################################

# 
# path2 = './data/data_3d_h36m.npz'
# data2 = np.load(path2, allow_pickle=True)

# # lst2 = data2.files
# # print('lst2 is: \n', lst2) # output: ['positions_3d']

# for item2 in lst2:
#     tmp_item2 = data2[item2]
#     print(item2) # output: positions_3d
# print('\n', data[item])

# test = data['positions_3d']
# # print(test.itemsize) # output: 8
# print(test.size) # output: 1