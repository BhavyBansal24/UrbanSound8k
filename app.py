import streamlit as st
from pydub import AudioSegment
import numpy as np
import helper
import librosa
import librosa.display as idp
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

st.sidebar.title("UrbanSound8k Audio Classifier")

Uploaded_file = st.sidebar.file_uploader("Insert File", type=['.wav','.mp3'])
if Uploaded_file is not None:
    # st.write(Uploaded_file)
    
    # files                                                                       
    if Uploaded_file.name.endswith('.mp3'):
    # convert wav to mp3
        sound = AudioSegment.from_mp3(Uploaded_file)
        sound.export("audio.wav", format="wav")
        Uploaded_file = "audio.wav"
    raw, sample_rate = helper.preprocess(Uploaded_file)

    # Play Audio File
    st.title("Play Uploaded File & Waveplot")
    out = helper.play_audio(raw, sample_rate)
    fig, ax = plt.subplots()
    ax = idp.waveshow(raw, sr=sample_rate)
    st.pyplot(fig)
    st.audio(Uploaded_file, format='audio/wav')

    # Printing the results
    st.title("predicted Class")
    prediction = helper.audio_to_result(Uploaded_file)
    le.classes_ = np.load('classes.npy')
    pred_class = le.inverse_transform(prediction)
    class_ = "Predicted Class : "+ str(pred_class[0])
    st.success(class_)

    # STFT
    st.title('spectrogram')
    X_db = helper.Spectrogram(raw)
    fig, ax = plt.subplots()
    ax = idp.specshow(X_db, sr=sample_rate, x_axis="time", y_axis="hz")
    plt.title("Input Audio's Spectrogram")
    st.pyplot(fig)

    # Harmonic-Percussive Separation (HPS)
    st.title('Harmonic Percussive Separation')
    h, p = helper.HPS(raw, sample_rate)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Harmonics")
        fig, ax = plt.subplots()
        ax = librosa.display.specshow(
            h, y_axis='mel', x_axis='s', sr=sample_rate)
        plt.title("Harmonic Mel Spectogram")
        st.pyplot(fig)
    with col2:
        st.header("Percussion")
        fig, ax = plt.subplots()
        ax = librosa.display.specshow(
            p, y_axis='mel', x_axis='s', sr=sample_rate)
        plt.title("Percuisive Mel Spectogram")
        st.pyplot(fig)

    # MFCC
    st.title('Mel-Frequency Cepstral Coefficients (MFCC)')
    mfcc = helper.MFCC(raw, sample_rate)
    fig, ax = plt.subplots()
    ax = idp.specshow(mfcc, x_axis="s")
    plt.title("Mel-Frequency Cepstral Coefficients")
    st.pyplot(fig)

    # Zero-Crossing
    st.title('Zero Crossing Rate')
    zero_crossing = helper.ZCR(raw)
    fig, ax = plt.subplots()
    ax.plot(raw[4700:5500])
    plt.title("Zero Crossing Rate")
    st.pyplot(fig)
    st.write("Total Number of Zero Crossing is: ", str(sum(zero_crossing)))

    # Spectral Centroid & Roll-Off
    st.title('Spectral Centroid & Roll-Off')
    C, R = helper.Spectral(raw, sample_rate)
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        ax = plt.semilogy(C.T, "r")
        plt.ylabel("Hz")
        plt.title("Spectral Centroid")
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        ax = plt.semilogy(R.T, "r")
        plt.ylabel("Hz")
        plt.title("Spectral Roll-Off")
        st.pyplot(fig)

    # Chroma Feature
    st.title('Chroma Feature')
    chroma = helper.Chroma(raw, sample_rate)
    fig, ax = plt.subplots()
    ax = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
    plt.colorbar()
    plt.title("Chromagram")
    st.pyplot(fig)

    # RMSE & log power spectrogram
    st.title('RMSE & log power spectrogram')
    S, RMSEn, times = helper.RMSE(raw)
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        ax = plt.semilogy(times, RMSEn[0])
        plt.title("Root Mean Squared Energy")
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        ax = librosa.display.specshow(librosa.amplitude_to_db(
            S, ref=np.max), y_axis='log', x_axis='time')
        plt.title("log Power Spectrogram")
        st.pyplot(fig)
