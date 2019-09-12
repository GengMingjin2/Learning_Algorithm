#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: A simple experiment for Kalman Filter.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 21:06:09
"""

import numpy as np
from tqdm import trange

def ekf_experiment():
    """
    A simple experiment for Extended Kalman Filter.
    """
    z = [(i**0.5 / 10) for i in range(100)]
    label = [i for i in range(100)]
    z_observation = np.mat(z)

    noise = np.round(np.random.normal(0, 0.1, 100), 4)
    noise_mat = np.mat(noise)

    z_mat = z_observation + noise_mat

if __name__ == "__main__":
    ekf_experiment()
