---
title: Core Concepts in BCI Literature
date: 2022-11-29 14:59:20
categories: [BCI]
tags: [EEG, BCI, neuroscience]
thumbnail: 
excerpt: In my way to a Brain-Computer Interface project, I did an extensive research on this field. This post then enumerates sets of key terms which formed my basis of understanding to BCI literature.
banner: 
sticky: 
---
# BCI background

If you ever wondered the world of Brain-Computer Interface, we are in the same place. So interested I was in it, that I decided to prepare a year project related to BCI.  
In order to accomplish the proposed project, I had to do an extensive research on BCI. It was undoubtedly a time-consuming task,but also rewarding at the same time. The knowledge a I gained supported to build my own draft of an integral **framework of the BCI world**.  
I would really want to develop each of the points into proper paragraphs linking each logically. However, I decided to not disclose them fully until the full research is finished. So for now, I am presenting a series of words which are **concepts** that can help you to constitute **your own BCI mind map**. In case you need a further reading, I have also attached some further reading which were most helpful for me.

## Non-invasive vs Invasive
EEG preferred, 83% of BCI are EEG.

## Paradigms
Setups and target of study.

### First generation
- Sensorimotor rhythms
- P300
- Visual Evoked Potential
- Slow Cortical Potential
- Activity of Neural Cell


### Second expansion
Added:
- Response to mental task
- Hybrid

### The most studied paradigms now
- Motor Imagery
  - **Sensorimotor rhythms SMR**
  - Imagined Body Kinematics IBK
- External Stimulation
  - **P300**
  - **Steady State Visual Evoked Potential SSVEP**
- Error-potential
- Hybrid/others

## Mechanisms of Motor Imagery
- Mu rhythm and beta rhythms
- Normally brain in ERSynchronisation
- When trying to execute an action -> ERDesynchronisation
- Mainly in frontal and medial lobe
  - C3, C4 most relevant
- Capture these changes, identify patterns, predict actions

## Methodology in Motor Imagery
- Pipeline:
    1. Collect amplitude
    2. BCI Transducer
       1. Artifact Processor
       2. Feature Generator
          1. Signal enhancement / Feature pre-processing
          2. Feature extraction (paradigm dependent)
          3. Feature selection / Dimension reduction
       3. Feature Translator
          1. Feature classification
          2. Post-processing 
    3. Control Interface
    4. Device Controller
- A catalogue of methods (till 2007, review 1)
  - See Table 1 in Appendices
- A review 2 on methods till 2007
  - Feature filtering methods
    - Time domain
    - Spatial domain
  - Feature extraction methods
    - Band-power features
    - Time point features
    - Connective features
  - Feature selection
    - Filter
    - Wrapper
    - Embedded methods
  - Performance measurer
    - Classification accuracy
    - Confusion Matrix or Kappa metric
    - Receiver Operating Characteristics or Area Under the Curve
  - Classifiers: 5 families
    - Linear classifier
    - Neural Networks
    - Non-linear Bayesian classifiers
    - Nearest Neighbour classifiers
    - Combinations
- A review 3 up to 2018
  - Most frequent methods
    - Band-pass filtering
    - Common Spatial Patterns
    - Linear Discriminant Analysis
- Review 2's update till 2017, future expectations, second generation methods
  - Adaptive classifiers
    - Preferred, outperforms, regardless supervised or not
  - Matrix and tensor classifiers
    - Promising, requires more research
    - Riemannian geometry classifier is at the state-of-art
  - Transfer learning methods
    - Useful when few data
    - Performance highly variable
  - Deep learning
    - Not convincing results
    - May due to limitation of data
    - Shallow CNN may work better
  - Miscellaneous but surprisingly good simple models when little data
    - Shrinkage LDA (always over LDA)
    - Random Forest classifiers



## Performance of Motor Imagery paradigms, a review
Importance of personal information + psychological + physiological + anatomical variables.
### Most frequent setup
- Number of channels
- Number of states
- Number of subjects
- ...
### Classification Accuracy
- Overall Corrected CA in the literature
- Correlations between setup variables and accuracy
- Few effective control

## BCI Challenges
### BCI Illiteracy is causing performance variation
Drives to ERD illiteracy. Difficult the transferability of a valid BCI. Inter-subject BCI is still difficult.

### Online vs Offline
Most of them are offline, while online is the important part.

### Advanced techniques still to be explored
Incorporate ANN, adaptive classifiers, Riemmanian Geometry Classifier, etc.

### Lack of standardised manner of summarising key features
Suggested a format of table of content.

## Resources
The following are titles of some papers that I found useful to understand the BCI world.
- A comprehensive review of EEG-based brain–computer interface paradigms
- Most Popular Signal Processing Methods in Motor-Imagery BCI: A Review and Meta-Analysis
- A survey of signal processing algorithms in brain–computer interfaces based on electrical brain signals
- A review of classification algorithms for EEG-based brain–computer interfaces: a 10 year update
- Chapter 2 - Technological Basics of EEG Recording and Operation of Apparatus
- Oscillatory gamma activity in humans and its role in object representation
- Could Anyone Use a BCI?
- Performance variation in motor imagery brain–computer interface: A brief review

## Appendices
Table 1
|Stage|Methods|Subtypes|Percentage|
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --- |
| Pre-processing methods     96    | Surface Laplacian                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                            | 32% |
|                                  | Principal Component Analysis or Independent CA                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                            | 22% | 
|                                  | Common Spatial Pattern                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                            | 14% | 
|                                  | Common Average Referencing                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                            | 11% | 
|                                  | Frequency Normalization, Common Spatial Subspace Decomposition,   Robust Kalman Filter, Singular Value Decomposition, Local Averaging Technique,   Wiener Filtering, Sparse Component Analysis, Maximum Noise Fraction, Spike   Detection Methods, Neuron Ranking methods, Common Spatio-Spatial Patterns                                                                                                                    |                                                                                                                            |     | -
| Feature Selection methods     38 | Genetic Algorithm                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                            | 26% 
|                                  | Distinctive Sensitive Learning Vector Quantization                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                            | 24% 
|                                  | PCA                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 13% 
|                                  | Sequential Forward Feature Selection, Grid Search Method,   Relief Method, Recursive Feature/channel Elimination (RFE), SVM-based RFE,   Stepwise Discriminant Procedure, Linear Discriminant Analysis (LDA), Fisher   LDA (dimensionality reduction), Fisher Discriminant-based Criterion (feature   selection), Zero-norm Optimization, Orthogonal Least Square based Radial   Basis Function                              |                                                                                                                            |     
| Post-processing methods     30   | Averaging and thresholding                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                            | 57% 
|                                  | Debounce Block to deactivate                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                            | 27% 
|                                  | Event-related Negativity                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                            | 16% 
| Feature Extraction methods       | Sensorimotor                                                                                                                                                                                                                                                                                                                                                                                                                 | Power-Spectral-Density                                                                                                     | 41% 
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
| Feature Classification methods   | Use of Threshold detector                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                            | 27% 
|                                  | Linear Discriminant, LDA or FLD                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                            | 26% 
|                                  | Neural Networks:     27% are Multi-Layer Perceptron                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 25% 
|                                  | Continues Feedback                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                            | 16% 
|                                  | SVM                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                            | 11% 
|                                  | Hidden Markov Model, Bayesian Classifier (Linear), Gaussian   Classifier, Signal Space Projection (SSP), Mahalanobis Distance based   classifier, Nonlinear Discriminant Function, Bayes Quadratic Classifier, Linear   Bayesian Decision Rule, Logistic Regression, Z-scale-based Discriminant   Analysis, Linear Dynamical System, Self-Organized Map based SSP, KNN,   Variational Kalman Filter, Random Forest Algorithm |                                                                                                                            |     |     |