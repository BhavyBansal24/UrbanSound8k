import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tensorflow.keras.models as models
import tensorflow.keras.layers as layers

CSV_FILE_PATH = ".csv"
AUDIO_FILE_PATH = ".wav"

df = pd.read_csv(CSV_FILE_PATH)
