# import numpy as np
# # yArch = np.load('./data/data_3d_h36m.npz')
# # print(yArch)

# test = np.array([1, 2, 3])
# print(test)

########################
####  讀取CDF 檔!!!  ####
########################

# reference: https://www.cxybb.com/article/weixin_38828673/117912498
# 1. pip install cdflib

# 2. 讀取cdf信息
# import cdflib as cdf
# cdf_file = cdflib.CDF('path')
# cdf_file.cdf_info()

# 3. 獲得變量信息
# cdf_file.varattsget(variable=0...n)
# n指的是变量，有多少个变量，则n可以是多少

# 4. 獲得數據信息
# cdf_file.varget(variable=0...n)

import cdflib
path = './data/h36m/S1/MyPoseFeatures/D3_Positions/Directions 1.cdf'
cdf_file = cdflib.CDF(path)

x = cdf_file.cdf_info()
print('print xdf_info:\n', x)

y = cdf_file.varattsget(variable=0)
print('\n获得变量信息: \n', y)

z = cdf_file.varget(variable=0)
print('\nget the variables in the cdf file:\n', z)
