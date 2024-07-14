---
title: EEG Feeling Emotions with PyTorch
date: 2022-10-26 12:23:19
categories: [EEG]
tags: [EEG, PyTorch, Machine Learning]
thumbnail: 
excerpt: How do you feel today? Wait, don't tell me. Let me guess it. Based on? Your brain signals.
banner: 
sticky: 
---
# Goal
Today, we are building a machine learning model that accepts EEG (ElectroEncephaloGram) signals and decides whether the source of these signals is happy or sad.

## Data Source
EEG data from [Kaggle](https://www.kaggle.com/datasets/birdy654/eeg-brainwave-dataset-feeling-emotions), and full notebook can be found [here](https://colab.research.google.com/drive/1uHlS2GPhqjeEn1hAN_8pgxZpO9LQr5Nw?usp=sharing).

# EEG feeling emotions

<a href="https://colab.research.google.com/drive/1uHlS2GPhqjeEn1hAN_8pgxZpO9LQr5Nw?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 1. Environment
---
Before hands on, get the **tools** 🧰 ready!

### 1.1 Import!
To import the tools (libraries) we need, run the following command.

```py
# Import libraries
import torch, pandas, numpy, os, requests, zipfile, io, matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset
```

### 1.2 Turn on the **GPU**!
To use the GPU (which makes code run faster) in Google Colab, in the top left corner:
- Click on *Edit*
- Click on *Notebook settings*
- From the drop down menu in *Hardware accelerator*
- Select **GPU**
- Save

Ready? Check whether GPU is ready by running the following code. The output should be `Using cuda.`, via which GPU is used.

```py
# Use GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device}.")
```

### 1.3 Locate

Find a place to play around, let's create a folder called `EEG` and we build everything inside it. The result should be `/content/EEG folder`.

```sh
# Create and get to `EEG` folder
! mkdir -p /content/EEG
%cd /content/EEG/
```

## 2. Data
---
Bring up the data✨, and let's see what it is made of!

### 2.1 Download the data
The result data stored in `/content/EEG/data/emotions.csv`.

```sh
# Download the eeg data
! mkdir -p ./data
! wget -q -O ./data/emotions.csv https://github.com/UOMDSS/workshops-2022-2023/raw/main/semester-1/Week-7-EEG-Feeling-Emotions-Logistic-Regression/data/emotions.csv
! ls

```

### 2.2 Read data
Now that we have the data in a folder, we read it into our notebook environment.

```py
# Read csv file
data = pandas.read_csv("./data/emotions.csv")
data
```

We see *mean*, some omitted columns, *fft*, *label*.
This notebook shallowly explores the data, to better understand what is meant with each row and column, refer to the dataset.
For example, the "a" and "b" in the end refers to whether the source of data is from person "a" or person "b".

### 2.3 Understand data
What is inside of this dataset? Dimensions? Type? What data can be useful?

```py
# Print data about the data
print(data.shape)
print(data.columns)
# for (i, col) in enumerate(data.columns):
#   print(i, col)
print(data.describe())
```

> ***Side notes***: fft stands for Fast Fourier Transform. This data enables us to represent a kind of *wave* graphs (time domain signals i.e. time vs amplitude) to another kind of *wave* graphs (frequency vs amplitude)。
> The main point here is that **we can visualize that!**

### 2.4 Visualise data
FFT columns represents elaborated signals, therefore, let's plot that brain signal as a graph.

```py
# Extract fft data
# ranges is tweakable
start = 0 # min = 0
end = 749 # max = 749
ranges = [(f"fft_{start}_a", f"fft_{end}_a"), ("label", "label")]
fft_data = pandas.concat([data.loc[:, i:j] for i, j in ranges], axis = 1) [data["label"] != "NEUTRAL"].reset_index()
fft_data
```

Now the data size has been reduced to:
- 1416 rows
- 752 columns
Why?

```py
# Plot fft brain signals
# moment (row) is tweakable
moment = 0
fft_data.iloc[moment, 1:-1].plot(figsize=(20, 15), label="Fast Fourier Transform at interval 0s to 1s")
plt.legend()
```

```py
# Brain signals over time
fig = plt.figure(figsize=(25, 15))
for i in range(0, 6):
    plt.subplot(3, 2, i+1)
    plt.plot(fft_data.iloc[i, 1:-1])
    plt.title("Fast Fourier Transform on " + fft_data.loc[i, "label"] + " emotion")
```
By eye, how would you say the differences between positive and negative brain signals?

## 3. Create model
---
Now it is time to write the **logistic regression** model ​⚒️!

> ***Side notes***: we can if we want, write the step-by-step code of the model. But most of the times, we tend to use a *frameworks* (code), a prepared codebase that already has the skeleton of model. They are handy and easy to use.  
> This notebook uses [**PyTorch**](https://pytorch.org/), a framework like this.

### 3.1 Dataset class
Imagine the datasets as spare data which could come in any form, how can PyTorch handle each case?  
The answer is that it **doesn't** handle, we as users are the ones reponsible to moderate the data according to PyTorch **dataset interface**.  
The following code is out of scope of this workshop. Just run it and should be fine, although you can have a look if interested.

```py
# Define emotion dataset in PyTorch
class EmotionDataset(Dataset):
    def __init__(self, df, transform=None, target_transform=None):
        self.data = df
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data.iloc[index, :-1].values.astype(numpy.float64)
        y = self.data.iloc[index, -1]
        if self.transform:
            x = self.transform(x)
        if self.target_transform:
            y = self.target_transform(y)
        return x, y
```

### 3.2 Model class
We aim to predict the emotion with a **logistic regression**, don't we?  
Luckily, PyTorch is able to help you to write this model incredibly fast.

> ***Side notes***:   
>  - `torch.nn.Linear(x, y)` maps `x` to `y` in a regression line.  
>  - `torch.sigmoid(x)` computes the value of x after applying sigmoid function


```py
# Build Logistic Regression model
class EmotionLogisticRegressionModel(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(EmotionLogisticRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)
    
    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred
```

## 4. Train model
---
The most intense part (for computers) comes now! We train 🏋 the model.

### 4.1. Hyperparameters
Different from the "parameters" which is obtained after training, "hyperparameters" are values that we humans choose to affect the model globally.  
For example, choosing `cuda`, `GPU` as our hardware resource you can consider it as a kind of "hyperparameter".

```py
# Choose hyperparameters
fft_start = 0
fft_end = 20
ranges = [(f"fft_{fft_start}_a", f"fft_{fft_end}_a"), (f"fft_{fft_start}_b", f"fft_{fft_end}_b"), ("label", "label")]
train_proportion = 0.8 
batch_size = 64
learning_rate = 0.01 
epochs = 50
```

### 4.2 Create train and test cycles
One last thing before training the model, is to wrap all the train cycle and test cycle as a "function" (function is just a block of code, callable with the name of the function). This gives us more concise and readable code.  
You don't need to fully understand what is going on inside, as it has some complex concepts. But feel free to ask if you want to know it.

```py
# Create train cycle
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
```

```py
# Create test cycle
def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X,y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)

            test_loss += loss_fn(pred, y).item()
            correct += (pred == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: Accuracy: {100*(correct):>0.1f}%, Avg loss: {test_loss:>8f} \n\n")
```

### 4.3 Train
Finally! The following cell intialises the model and trains the model. Learning the data may take some time, please be patient. Same, some functions are specific to PyTorch, you don't need to fully understand them. Have a guess, what do they mean?

```py
# Initialise
# Create dataset
data = pandas.read_csv("eeg_data.csv")
data = pandas.concat([data.loc[:, i:j] for i, j in ranges], axis=1)[data["label"] != "NEUTRAL"]
input_size = data.shape[1] - 1
output_size = 1
dataset = EmotionDataset(data, transform=lambda x: torch.from_numpy(x).float(), target_transform=lambda x: torch.tensor([0]).float() if x == "POSITIVE" else torch.tensor([1]).float())
train_size = int(train_proportion * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# Create model
model = EmotionLogisticRegressionModel(input_size, output_size).to(device)

# Loss and optimizer
loss_fn = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

```

```py
# Train model!
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader, model, loss_fn, optimizer)
    test(test_loader, model, loss_fn)
print("Done!")
```

# Conclusion
Today we built a logistic regression model with PyTorch to predict the emotions based on the EEG of a person. It is a bit abstract to input made up EEG data, therefore there won't be a predicting step here.

The original format of this post is in a google colab notebook, hence the style of this post.