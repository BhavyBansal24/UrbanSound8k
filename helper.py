import librosa
import librosa.display
import numpy as np
import IPython.display as ipd
import tensorflow as tf
from tensorflow import keras
import keras.models as models
import cv2

def preprocess(data):
    audio_data, sample_rate = librosa.load(data, res_type='kaiser_fast')
    return audio_data, sample_rate

def play_audio(raw,sr):
    out = ipd.Audio(raw,rate=sr)
    return out
def Spectrogram(raw):
    X=librosa.stft(raw) #stft -> Short-time Fourier transform
    X_db=librosa.amplitude_to_db(abs(X)) #Translation from amplitude to desibel(db) value
    return X_db

def HPS(raw,sr):
    data_h, data_p = librosa.effects.hpss(raw)
    spec_h = librosa.feature.melspectrogram(data_h, sr=sr)
    spec_p = librosa.feature.melspectrogram(data_p, sr=sr)
    db_spec_h = librosa.power_to_db(spec_h,ref=np.max)
    db_spec_p = librosa.power_to_db(spec_p,ref=np.max)
    return db_spec_h, db_spec_p

def MFCC(raw,sr):
    mfcc=librosa.feature.mfcc(raw,sr)
    return mfcc

def ZCR(raw):
    zero_crossing=librosa.zero_crossings(raw)
    return zero_crossing

def Spectral(raw,sr):
    spec_cent=librosa.feature.spectral_centroid(raw)
    spec_roll=librosa.feature.spectral_rolloff(raw,sr=sr)
    return spec_cent, spec_roll

def Chroma(raw,sr):
    chroma=librosa.feature.chroma_stft(raw, sr)
    return chroma

def RMSE(raw):
    S = librosa.magphase(librosa.stft(raw, window=np.ones, center=False))[0]
    RMSEn= librosa.feature.rms(S=S)
    times = librosa.times_like(RMSEn)
    return S, RMSEn, times
    
def audio_to_result(filename):
    model_saved = models.load_model('Saved_Model')
    raw , sr = librosa.load(filename, res_type='kaiser_fast')
    X_image = librosa.feature.mfcc(y=raw, sr=sr, n_mfcc=40)
    up_width = 173
    up_height = 40
    up_points = (up_width, up_height)
    X_image = cv2.resize(X_image, up_points, interpolation= cv2.INTER_LINEAR)
    X_image = X_image.reshape(1,X_image.shape[0],X_image.shape[1],1)
    pred = model_saved.predict(X_image)
    prediction = np.argmax(pred, axis=-1)
    return prediction