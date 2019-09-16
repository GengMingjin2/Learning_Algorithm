## 卡尔曼滤波器算法——简单实践
[参考博客]https://blog.csdn.net/CodeSamer/article/details/81191487
场景：
小车的一维直线匀速运动，其中p表示position，v表示velocity，z表示观测的位置；
预测时引入的高斯噪声为二维高斯，维度间相互独立，每维服从N(0, 0.0001);
delta_t = 1(每秒预测和观测一次~)
观测时引入的高斯噪声为一维高斯，服从N(0, 1)。
<img src="kf_result_figure.png" width=500>

## 深层原理的推导请移步博客[科研]https://www.cnblogs.com/bupt213/p/11505280.html

[ekf]https://github.com/simondlevy/SensorFusion/blob/master/fusion.m
[kf]http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
