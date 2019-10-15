#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: A simple experiment for Kalman Filter.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 21:06:09
"""

import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from tqdm import trange

def kf_experiment2():
    """
    A simple experiment for Kalman Filter(curve).
    """
    z = [(i**2) * 0.5 for i in range(100)]
    label = [i for i in range(100)]
    z_observation = np.mat(z)

    noise = np.round(np.random.normal(0, 10, 100), 4)
    noise_mat = np.mat(noise)

    z_mat = z_observation + noise_mat

    x_mat = np.mat([[0, ], [0, ]])
    P_mat = np.mat([[1, 0], [0, 1]])
    F_mat = np.mat([[1, 1], [0, 1]])
    Q_mat = np.mat([[0.0001, 0], [0, 0.0001]])
    H_mat = np.mat([1, 0])
    R_mat = np.mat([10])

    for i in trange(100):
        x_predict = F_mat * x_mat + np.mat([[0.5, ], [1, ]])
        P_predict = F_mat * P_mat * F_mat.T + Q_mat
        K_mat = P_predict * H_mat.T / (H_mat * P_predict * H_mat.T + R_mat)
        x_mat = x_predict + K_mat * (z_mat[0, i] - H_mat * x_predict)
        P_mat = (np.eye(2) - K_mat * H_mat) * P_predict

        plt.plot(x_mat[0, 0], x_mat[1, 0], 'ro', markersize = 1)
        plt.plot(z[i], label[i], 'bo', markersize = 1)
        plt.plot(z[i], z[i] - x_mat[0, 0], 'go', markersize = 1)

    plt.show()

if __name__ == "__main__":
    kf_experiment2()
