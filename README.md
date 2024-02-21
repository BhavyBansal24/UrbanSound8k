# UrbanSound8k

![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/cover.jpeg?raw=true)

#### Project is live at : [UrbanSound8k](https://urbansound8k.streamlit.app/)

## Dockerized installation in local machine

- paste below code in cmd

  ```
  git clone https://github.com/BhavyBansal24/UrbanSound8k.git
  docker build -t ultra_sound8k .
  docker run -dp 8501:8501 --name SoundDetect ultra_sund8k
  timeout 2 /nobreak && start http://localhost:8501

  ```

## How to use UrbanSound8k web-app:

- Click [here](https://urbansound8k.streamlit.app/)
- Click on Browse Files
  ![alt text](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/browse.jpeg?raw=true)
- Upload a (.wav) audio file, Model will classify your uploaded sound from the classes.
- classes are : ['dog_bark' , 'children_playing' , 'car_horn' , 'air_conditioner' , 'street_music' , 'gun_shot' , 'siren' , 'engine_idling' , 'jackhammer' , 'drilling']
  ![.wav image](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/open.jpeg?raw=true)
- After uploading completes, you can see the prediction on right side as shown below
  ![prediction](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/prediction.jpeg?raw=true)
- Below that you can also view other analysis such as spectrogram, Harmonic Percussive Separation, Mel-Frequency Cepstral Coefficients (MFCC), Zero Crossing Rate and many more.

---

## Model Details :

- Sequential model
  ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/model.jpeg?raw=true)
- Training of 15 Epoch
  ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/training.jpeg?raw=true)

---

## Model Results :

- Model Accuracy
  - ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/ModelAccuracy.png?raw=true)
- Model Loss
  - ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/ModelLoss.png?raw=true)

---

## Model Evaluation

- Classification Report
  - ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/ClassificationReport.jpeg?raw=true)
- Confusion Matrix
  - ![](https://github.com/BhavyBansal24/UrbanSound8k/blob/master/extras/ConfusionMatrix.png?raw=true)

---

## Dataset used for Training model:

- Dataset is taken from kaggle and link for dataset is [here](https://www.kaggle.com/datasets/chrisfilo/urbansound8k)
- This dataset contains 8732 labeled sound of urban sounds from 10 classes: air_conditioner, car_horn, children_playing, dog_bark, drilling, enginge_idling, gun_shot, jackhammer, siren, and street_music

---

## Libraries and framework used in project :

- [Pandas](https://pandas.pydata.org/)
- [Librosa](https://librosa.org/doc/latest/index.html)
- [Numpy](https://numpy.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Ipython](https://ipython.org/)
- [OpenCV](https://opencv.org/)

---

## Do check my Kaggle (ipynb)Notebook:

- Link to my kaggle notebook is [here](https://www.kaggle.com/code/bhavybansal/urbansound8k-cnn-classifier)
- Do upvote notebook, Hope you like it.
- and do Not forgot to check my other notebooks on kaggle as well

---

### Do 🌟 this Github Repository, Hope you have loved my work

---

## Moreover don't forget to follow me on :

- [github](https://github.com/BhavyBansal24)
- [Kaggle](https://www.kaggle.com/bhavybansal)
- [Linkedin](https://www.linkedin.com/in/bhavybansal24/)
- [Twitter](https://twitter.com/BhavyBansal_24)
- [Instagram](https://www.instagram.com/bhavybansal_24/)

---

## Portfolio Website :

- Hope you love to know more about me, check my Portfolio Website [here](https://bhavybansal24.github.io/Neural-Programmer/)
