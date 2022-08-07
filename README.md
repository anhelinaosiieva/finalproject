# FinalProject

# Not a Lizard? Classification App
This app was created using CNN algorithm for image classification/recognition on Streamlit.

#### Video Demo: <>
#### Description:

Found a small, brown, cold-blooded animal and not sure what it might be? You are not alone!
There are people that can't distinguish lizards from newts(tritons). Because these groups of reptiles and amphibians have similar bodytypes with long tails and shorts legs. Newts or other amphibians are associated with water, have soft, slimmy skin and four toes on each front foot. Common lizards are more likely to be found on sunny spots, they are protected by scales all over their body and have five toes, tipped with tiny claws.

You can upload an image of newt or lizard and receive prediction.

#### Creating virtual environment and installing dependencies
I am working on Macbook Pro M1 chip. Here some tips on preparations if you are interested:

1. Download and install Homebrew from https://brew.sh. Follow the steps it prompts you to go through after installation.
2. Download Miniforge3 (Conda installer) for macOS arm64 chips (M1, M1 Pro, M1 Max).
3. Install Miniforge3 into home directory.
```
chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh sh ~/Downloads/Miniforge3-MacOSX-arm64.sh 
source ~/miniforge3/bin/activate
```
4. Restart terminal.
5. Create a directory to setup TensorFlow environment.
```
mkdir tensorflow-test cd tensorflow-test
```
6. Make and activate Conda environment. Note: Python 3.8 is the most stable for using the following setup.
```
conda create --prefix ./env python=3.8 conda activate ./env
```
7. Install TensorFlow dependencies from Apple Conda channel.
```
conda install -c apple tensorflow-deps
```
8. Install base TensorFlow (Apple's fork of TensorFlow is called tensorflow-macos).
```
python -m pip install tensorflow-macos
```
9. Install Apple's tensorflow-metal to leverage Apple Metal (Apple's GPU framework) for M1, M1 Pro, M1 Max GPU acceleration.
```
python -m pip install tensorflow-metal
```
10. (Optional) Install TensorFlow Datasets.
```
python -m pip install tensorflow-datasets
```
11. Install common data science packages.
```
conda install jupyter pandas numpy matplotlib scikit-learn opencv
```
12. Install Streamlit (an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.)
```
python -m pip install streamlit
```
13. Start Jupyter Notebook.
```
mkdir tensorflow-test cd tensorflow-test
```
###### Precheck after installing dependencies
```
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import matplotlib.pyplot as plt

# Check for TensorFlow GPU access
print(f"TensorFlow has access to the following devices:\n{tf.config.list_physical_devices()}")

# See TensorFlow version
print(f"TensorFlow version: {tf.__version__}")
```

#### Structure
`main.py`
Includes the runcode for Streamlit webpage. Use `streamlit run main.py` to start.

`finalproject.ipynb`
Jupyter notebook file with our model.

`data`
Folder with images used for training.

`models`
Our saved model in `.h5` format.

`logs`
Training logs.
