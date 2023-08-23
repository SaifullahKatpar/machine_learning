I apologize for the inconvenience. Here's the raw Markdown code:

```
# Machine Learning Using AutoKeras

## Installation

To set up the required dependencies for this project, you can use a virtual environment. Follow these steps:

1. Install `virtualenv` if you haven't already:

   ```bash
   λ pip install virtualenv
   ```

2. Create a virtual environment named `venv`:

   ```bash
   λ virtualenv venv
   ```

3. Activate the virtual environment:

   ```bash
   λ venv\Scripts\activate.bat
   ```

4. Install the project's dependencies:

   ```bash
   λ pip install -r requirements.txt
   ```

Alternatively, you can run the provided script to automate this process:

```bash
λ run_exec.bat
```

This script sets up and activates the virtual environment, then installs all the required dependencies. This setup was tested on Windows 10 using "Cmder" as the console emulator.

## Description

This project explores automated machine learning using the open-source library [AutoKeras](https://autokeras.com/). AutoKeras simplifies the process of searching for optimal deep learning model architectures and hyperparameters. The training was performed on an [Nvidia GeForce 940MX GPU](https://www.geforce.com/hardware/notebook-gpus/geforce-940mx), and various datasets were used for evaluation.

## Pre-processing Strategy

For the Olivetti Faces dataset, data augmentation was applied to increase the dataset size. This was achieved by rotating each image 90, 180, and 270 degrees counterclockwise. This approach helped address the limited sample size issue.

## Results

Here are the results for different datasets:

| Dataset                                         | No. of Samples | Data Augmentation | Normalized Features | Train Accuracy (%) | Test Accuracy (%) | Average Precision (%) | Average Recall (%) | Average F1 Score (%) | Total Support | Epochs | Time Taken (s) | Batch Size |
| ----------------------------------------------- | --------------- | ------------------ | ------------------- | ------------------ | ----------------- | --------------------- | ----------------- | -------------------- | ------------- | ------ | --------------- | ---------- |
| [Olivetti Faces Dataset](link)                  | 1600            | Yes                | Yes                 | 96.449             | 97.500            | 97                    | 98                | 97                   | 320           | 53     | 110.767         | 128        |
| [Cifar-10 Dataset](link)                        | 60000           | No                 | Yes                 | 69.580             | 68.870            | 68                    | 69                | 68                   | 10000         | 66     | 1876.29         | 128        |
| [Cifar-100 Dataset](link)                       | 60000           | No                 | Yes                 | 40.1440            | 39.66             | 39                    | 41                | 40                   | 10000         | 54     | 1370.663991     | 128        |
| [MNIST](link)                                   | 60000           | No                 | Yes                 | 98.248             | 98.180            | 98                    | 98                | 98                   | 10000         | 41     | 98.350          | 128        |
| [Sign Language Classification](link)            | 1080            | No                 | Yes                 | 98.000             | 95.000            | 95                    | 95                | 95                   | 120           | 69     | 132.53          | 128        |
| [Fashion MNIST](link)                           | 60000           | No                 | Yes                 | 89.304             | 88.550            | 88                    | 89                | 89                   | 10000         | 57     | 1398            | 128        |

A classification report containing average precision, recall, f1-score, and support for each class is available in the `classification_reports` directory.

## Limitations

1. AutoKeras currently supports only Convolutional Neural Networks (CNNs) and lacks support for architectures like ResNet and Recurrent Neural Networks (RNNs).
2. The Cifar-100 dataset exhibits lower performance compared to baseline models.
3. Limited support in Keras for multi-class ROC curve plotting.
4. Challenges with implementing transfer learning.

## Issues

For common troubleshooting issues, please refer to the [Common Troubleshooting Issues](docs/troubleshooting_issues.md) documentation.
```