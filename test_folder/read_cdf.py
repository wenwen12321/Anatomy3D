# human3.6m dataset cdf file format explain: 
#  

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

# run script:
# python ./test_folder/read_cdf.py

import cdflib
path = './data/h36m/S1/MyPoseFeatures/D3_Positions/Directions 1.cdf'
# path = './data/h36m/S1/MyPoseFeatures/D3_Positions/Discussion.cdf'

# cdflib.CDF('xxx.cdf') 讀取一個 cdf 文件
# load the cdf file
cdf_file = cdflib.CDF(path)

# 查看此cdf.文件信息: cdf_info()
#View the Information about the cdf file
info = cdf_file.cdf_info()
print('print xdf_info:\n', info)
# 返回一個顯示基本CDF信息的字典。這些信息包括: 
# cdfCDF的名稱 
# version CDF的版本 
# encoding CDF的字節順序 
# Majority 行/列多數 
# zVariables 一個zVariables名稱的列表。 
# rVariables 一個rVariables名稱的列表。 
# Attributes 一個包含屬性名及其作用域的字典對象列表，例如 - {attribute_name : scope}。 
# Checksum 驗算符
#
# Num_rdim 维度数，仅适用于 rVariables。
# rDim_sizes 维度大小，仅适用于 rVariables。
# Compressed CDF压缩到此文件级
# LeapSecondUpdated 最后更新的闰年表(如适用)


# 提取此cdf文件中的變量：varget ()
#Get the variables in the cdf file
x = cdf_file.varget("Pose")
print("\nget x's pose: \n", x)


y = cdf_file.varattsget(variable=0)
print('\n获得变量信息: \n', y)

# 提取此cdf文件中的變量：varget ()
z = cdf_file.varget(variable=0)
print('\nget the variables in the cdf file:\n', z)
# 返回變量數據。可以輸入變量名或變量號。默認情況下，它會根據數據類型返回帶有變量data及其規範的numpy.ndarray or或list()class對象。



print('shape of z: ', z.shape) # output: (1, 1383, 96) # 有 1383 個 frames, 32*3 的 3D 關鍵點座標
print('shape of z[0]: ', z[0][0].shape) # output: (1, 1383, 96)
print('shape of z[0]: ', z[0][0]) # output: (1, 1383, 96)

##################################################################
# 看 score.pkl 跟 cdf檔 的維度 一不一樣 => case pf S11 Directions.cdf
path = './data/h36m/S11/MyPoseFeatures/D3_Positions/Directions.cdf'

cdf_file = cdflib.CDF(path)

x = cdf_file.varget("Pose")
print("\nget x's pose: \n", x)

