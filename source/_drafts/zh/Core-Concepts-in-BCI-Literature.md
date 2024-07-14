---
title: Core Concepts in BCI Literature
date: 2022-11-29 14:59:28
categories: [脑机接口]
tags: [EEG, 脑机接口, 神经科学]
thumbnail: 
excerpt: 在我进行脑机接口项目的过程中，我不得不对这一领域进行广泛的研究。这篇文章列举了一系列我了解到构成BCI文献基础的关键术语。
banner: 
sticky: 
---
# BCI背景

如果你曾想了解脑机接口的世界，那巧了，我们在同一起跑线。我对脑机接口的兴趣使得我决定准备一个与BCI有关的年度项目。 
为了完成拟定的项目，我必须对BCI进行广泛研究。这无疑是一项耗时的任务，然而，它是值得的。我从中获得的知识支持了我建造自己的**完整BCI框架**的雏形。 
虽然我真心希望能将每个观点做适当的张开，并将每个段落逻辑地联系起来。然而，我决定在完整的研究完成之前不完全披露它们。因此，在本文中，我提出了一系列关键词。这些词是BCI领域中重要的概念，可以帮助您构成**自己的BCI思维导图**。如果您需要进一步阅读，我还附上了一些对我帮助最大的文献。

## 非侵入性与侵入性
首选EEG，83%的BCI是EEG。

## 不同的范式
研究设置和目标。

### 第一代
- 感知运动节律
- P300
- 视觉诱发电位
- 慢速皮质电位
- 神经细胞的活动


### 第二次扩展
添加：
- 对心理任务的反应
- 混合型

### 现在研究最多的范式
- 运动意象
  - **传感器运动节律SMR**。
  - 想象的身体运动学 IBK
- 外部刺激
  - **P300**
  - **稳态视觉诱发电位 SSVEP**
- 误差-电位
- 混合/其他

## 运动意象的机制
- mu节律和β节律
- 正常情况下，大脑处于ERS同步化状态
- 当试图执行一个动作时 -> ERD异步化
- 主要是在额叶和内侧叶
  - C3、C4最相关
- 捕捉这些变化，识别模式，预测行动

## 在运动意象的方法学
- 流水线：
    1. 收集振幅
    2. BCI换能器
       1. 伪装处理器
       2. 特征生成器
          1. 信号增强/特征预处理
          2. 特征提取（取决于范式）
          3. 特征选择/降维
       3. 特征翻译器
          1. 特征分类
          2. 后处理 
    3. 控制界面
    4. 设备控制器
- 方法目录（至2007年，Review 1）。
  - 见附录中的表1
- 截至2007年的方法回顾2
  - 特征过滤方法
    - 时域
    - 空间域
  - 特征提取方法
    - 带功率特征
    - 时间点特征
    - 连接性特征
  - 特征选择
    - 滤波器
    - 包裹器
    - 嵌入式方法
  - 性能测量器
    - 分类精度
    - 混淆矩阵或Kappa指标
    - 接受者操作特征或曲线下面积
  - 分类器：5个系列
    - 线性分类器
    - 神经网络
    - 非线性贝叶斯分类器
    - 最近的邻居分类器
    - 组合
- 截至2018年的Review 3
  - 最常见的方法
    - 带通滤波
    - 常见的空间模式
    - 线性判别分析
- Review 2的更新到2017年，未来的期望，第二代方法
  - 自适应分类器
    - 首选，性能更优，无论是否有监督
  - 矩阵和张量分类器
    - 有希望，需要更多研究
- 黎曼几何分类器处于最先进水平
- 转移学习方法
    - 数据少时有用
    - 性能变化很大
- 深度学习
    - 没有令人信服的结果
- 可能是由于数据的限制
    - 浅层CNN可能效果更好
- 杂七杂八，但在数据不多的情况下，简单模型的效果出奇地好
    - 缩减LDA（总是超过LDA）
    - 随机森林分类器

## 运动意象范式的表现，Review
个人信息的重要性+心理+生理+解剖变量。
### 最多使用的设置
- 通道的数量
- 状态的数量
- 受试者的数量
- ...
### 分类精度
- 文献中总体校正的CA
- 设置变量与准确性之间的相关性
- 少数有效控制

## BCI的挑战
### BCI文盲导致性能变化
驱动ERD的文盲。有效BCI的可转移性困难。课题间BCI仍然很困难。

### 在线与离线
大多数是离线的，而在线是重要的部分。

### 先进技术仍有待探索
纳入ANN、自适应分类器、Riemmanian Geometry分类器，等等。

### 缺少总结关键特征的标准化方式
建议采用内容表的格式。

## 资源
以下是我认为对了解BCI世界有用的一些论文的标题。
- A comprehensive review of EEG-based brain–computer interface paradigms
- Most Popular Signal Processing Methods in Motor-Imagery BCI: A Review and Meta-Analysis
- A survey of signal processing algorithms in brain–computer interfaces based on electrical brain signals
- A review of classification algorithms for EEG-based brain–computer interfaces: a 10 year update
- Chapter 2 - Technological Basics of EEG Recording and Operation of Apparatus
- Oscillatory gamma activity in humans and its role in object representation
- Could Anyone Use a BCI?
- Performance variation in motor imagery brain–computer interface: A brief review

## 附录
表1
|阶段|方法|子类型|百分比|
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --- |
| 信号增强/特征预处理     96    | Surface Laplacian                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                            | 32% |
|                                  | Principal Component Analysis or Independent CA                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                            | 22% | 
|                                  | Common Spatial Pattern                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                            | 14% | 
|                                  | Common Average Referencing                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                            | 11% | 
|                                  | Frequency Normalization, Common Spatial Subspace Decomposition,   Robust Kalman Filter, Singular Value Decomposition, Local Averaging Technique,   Wiener Filtering, Sparse Component Analysis, Maximum Noise Fraction, Spike   Detection Methods, Neuron Ranking methods, Common Spatio-Spatial Patterns                                                                                                                    |                                                                                                                            |     | -
| 特征选择/降维     38 | Genetic Algorithm                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                            | 26% 
|                                  | Distinctive Sensitive Learning Vector Quantization                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                            | 24% 
|                                  | PCA                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 13% 
|                                  | Sequential Forward Feature Selection, Grid Search Method,   Relief Method, Recursive Feature/channel Elimination (RFE), SVM-based RFE,   Stepwise Discriminant Procedure, Linear Discriminant Analysis (LDA), Fisher   LDA (dimensionality reduction), Fisher Discriminant-based Criterion (feature   selection), Zero-norm Optimization, Orthogonal Least Square based Radial   Basis Function                              |                                                                                                                            |     
| 后处理     30   | Averaging and thresholding                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                            | 57% 
|                                  | Debounce Block to deactivate                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                            | 27% 
|                                  | Event-related Negativity                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                            | 16% 
| 特征提取       | Sensorimotor                                                                                                                                                                                                                                                                                                                                                                                                                 | Power-Spectral-Density                                                                                                     | 41% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Parametric modelling (Autoregressive)                                                                                      | 16% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Time-Frequency Representation                                                                                              | 13% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | CCTM, Signal Envelope, Hjorth Parameters, Signal Complexity,   Lateralized Readiness Potential features, others            |     
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Amplitude (None)                                                                                                           | 6%  
|                                  | VEP                                                                                                                                                                                                                                                                                                                                                                                                                          | Power-spectral features                                                                                                    | 64% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Lock-in Amplifier, Asymmetry Ration of Different Band   Powers, Cross-correlation, Amplitude between N2 and P2 peaks, none |     
|                                  | P300                                                                                                                                                                                                                                                                                                                                                                                                                         | Peaks of specific time window                                                                                              | 26% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | TFR-based methods                                                                                                          | 22% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Cross-correlation                                                                                                          | 15% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Stepwise Discriminant Analysis, Matched Filtering, Piecewise   Prony Method, Area Calculation, None                        |     
|                                  | Mental task                                                                                                                                                                                                                                                                                                                                                                                                                  | Power-Spectral features                                                                                                    | 41% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Parametric modelling (Autoregressive)                                                                                      | 37% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Signal Complexity, Eigenvalues Correlation Matrix, Linear   Predictive Coding using Burg’s Method                          |     
|                                  | SCP                                                                                                                                                                                                                                                                                                                                                                                                                          | Low-pass filtering and amplitude                                                                                           | 74% 
|                                  |                                                                                                                                                                                                                                                                                                                                                                                                                              | Time Frequency Representation (TFR) method, Mixed Filter,   None                                                           |     
| 特征分类   | Use of Threshold detector                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                            | 27% 
|                                  | Linear Discriminant, LDA or FLD                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                            | 26% 
|                                  | Neural Networks:     27% are Multi-Layer Perceptron                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 25% 
|                                  | Continues Feedback                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                            | 16% 
|                                  | SVM                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 11% 
|                                  | Hidden Markov Model, Bayesian Classifier (Linear), Gaussian   Classifier, Signal Space Projection (SSP), Mahalanobis Distance based   classifier, Nonlinear Discriminant Function, Bayes Quadratic Classifier, Linear   Bayesian Decision Rule, Logistic Regression, Z-scale-based Discriminant   Analysis, Linear Dynamical System, Self-Organized Map based SSP, KNN,   Variational Kalman Filter, Random Forest Algorithm |                                                                                                                            |     |     |
