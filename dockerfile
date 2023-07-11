# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy the requirements files
COPY requirements.txt /app
COPY packages.txt /app

# Install required packages
RUN apt-get update
RUN apt-get install libsndfile1-dev libtesseract-dev libtesseract4 tesseract-ocr -y 
RUN apt-get install libgl1-mesa-glx freeglut3-dev freeglut3-dev libgtk2.0-dev ffmpeg libsm6 libxext6 -y

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]