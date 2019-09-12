#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: A simple experiment for Kalman Filter.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 21:06:09
"""

import numpy as np
# Add the two lines codes if there is no figure showing in your PyCharm~
#import matplotlib
#matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from tqdm import tqdm

def kf_experiment():
    """
    A simple experiment for Kalman Filter
    """
    z = [i**2 / 10 for i in range(100)]  # observations for position p
    z_observation = np.mat(z)

    noise = np.round(np.random.normal(0, 1, 100), 2) # a noise for z, N(0,1)
    noise_mat = np.mat(noise)

    z_mat = z_observation + noise_mat # the real observations z

    x_mat = np.mat([[0,], [0,]]) # initialize the state vector x ( consist of position p and velocity v)
    # 定义初始化协方差矩阵
    P_mat = np.mat([[1, 0], [0, 1]])
    # 定义初始化状态转移矩阵， 每秒采样一次，因此delta_t = 1
    F_mat = np.mat([[1, 1], [0, 1]])
    # 定义状态转移协方差矩阵，数值小表示认为状态转移矩阵准确度高
    Q_mat = np.mat([[0.0001, 0], [0, 0.0001]])
    # 定义观测矩阵
    H_mat = np.mat([0.2, 0])
    # 定义观测矩阵协方差，因为观测量仅仅为一维的，且已经被人为假设成N(0,1)
    R_mat = np.mat([1])

    for i in tqdm(range(100)): # 开始迭代~
        x_predict = F_mat * x_mat
        P_predict = F_mat * P_mat * F_mat.T + Q_mat
        K_mat = P_predict * H_mat.T / (H_mat * P_predict * H_mat.T + R_mat)
        x_mat = x_predict + K_mat * (z_mat[0, i] - H_mat * x_predict)
        P_mat = (np.eye(2) - K_mat * H_mat) * P_predict

        plt.plot(x_mat[0, 0], x_mat[1, 0], 'ro', markersize = 1)
        plt.plot(z[i], 0.2*i, 'bo', markersize = 1)

    plt.show()

if __name__ == "__main__":
    kf_experiment()