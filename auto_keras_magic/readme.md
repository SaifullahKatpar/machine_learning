# Machine Learning Using AutoKeras

## Installation

One way to install all the required dependencies, is to use virtual environment. The steps are as follows: <br>
* run the following commands (enjoy):

<pre><code>&#955; pip install virtualenv <br />
&#955; virtualenv venv<br />
&#955; venv\Scripts\activate.bat <br />
&#955; pip install -r requirements.txt<br />
</code></pre>

* Alternatively you can simply run the following command:
<pre><code>&#955; run_exec.bat </code></pre>

The script sets up set virtualenv, activates it and installs all the required dependencies. <br>
Windows 10 OS was used for the evaluation of the library with "Cmder" as the console emulator <br>

## Description
Use of an open source library [AutoKeras](https://autokeras.com/) for automated machine learning.
AutoKeras provides the functions to automatically search for architecture
and parameters for deep learning models. <br> [Nvidia GeForce 940MX GPU](https://www.geforce.com/hardware/notebook-gpus/geforce-940mx) was used for training purposes. <br>
Different datasets were used for evaluation of library

## Pre-processing strategy
In the case of Olivetti Faces dataset, because data was sampled from 40 individuals and each class only had 10 samples, the size of the dataset was increased by 4x by artificially synthesizing data, this was achived by rotating each image 90, 180 and 270 degrees counter clockwise <br>

## Results

| Dataset | No. of Samples | Data Augmentation | Normalized features | Train Accuracy (%) | Test Accuracy (%) | Average Precision (%) | Average Recall (%) | Average F1 Score (%) | Total Support | Epochs | Time Taken (s) | Batch Size |
| :-: | :-: | :-: | :-: | :-: | :-: | :-:| :-: | :-: | :-: | :-: | :-: | :-: |
| [Olivetti Faces Dataset](http://scikit-learn.org/stable/datasets/olivetti_faces.html) | 1600 | Y | Y | 96.449 | 97.500 | 97 | 98 | 97 | 320 | 53 | 110.767 | 128 |
| [Cifar-10 Dataset](https://en.wikipedia.org/wiki/CIFAR-10) | 60000 | N | Y | 69.580 | 68.870 | 68 | 69 | 68 | 10000 | 66 | 1876.29 | 128 |
| [Cifar-100 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html) | 60000 | N | Y | 40.1440 | 39.66 | 39 | 41 | 40 | 10000 | 54 | 1370.663991 | 128
| [MNIST](https://en.wikipedia.org/wiki/MNIST_database) | 60000 | N | Y | 98.248 | 98.180 | 98 | 98 | 98 | 10000 | 41 | 98.350 | 128 |
| [Sign Language Classification](https://github.com/aa18514/machine_learning/tree/master/sign%20language%20classification) | 1080 | N | Y | 98.000 | 95.000 |  95 | 95 | 95 | 120 | 69 | 132.53 | 128 |
| [Fashion MNIST](https://arxiv.org/abs/1708.07747) | 60000 | N | Y | 89.304 | 88.550 | 88 | 89 | 89 | 10000 | 57 | 1398 | 128

The classification report containing average precision, recall, f1-score and total support along with the precision, recall, f1-score and support for each class is given in the direcotry 'classification_reports\\classification_report_[dataset].csv' <br>

## Limitations
* It seems like AutoKeras does not support architectures such as ResNet. At the minute only it seems like only [Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) are supported and there is no support for [Recurrent Neural Networks](https://en.wikipedia.org/wiki/Recurrent_neural_network).
* Cifar-100 suffers from very low test and train performance as compared to the baseline model
* There is limited support in Keras for things like plotting the [ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) for multiple classes
* Things such as [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning) become more difficult to achieve

## Issues
[Common Troubleshooting Issues](docs/troubleshooting_issues.md)
