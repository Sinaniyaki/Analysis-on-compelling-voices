# Analysis into what makes voices more compelling/engaging
The goal of this project was finding our what makes people voices to sound more compelling through comutation algorithms. Our general approach is gathering as much data abuout the voices we have, and generating sample voices using Amazon Polly and Google Cloud Text to Speach (TTS). Then, doing a survey to find interesting results about the generated voices.

## Dataset:
Our raw original data are in a directory called "ccdata", and in that directory. There are more directories inside "ccdada". and in each directory there are voices. The dataset was given to us by Paige Tuttosi [Linkedin](https://pages.github.com/).
We made a dataset from the files we had called "final_classification_features.csv" that we use to make other datasets and compare more details are below.

## Approach
### visualization_regression.ipynb:
This notebook processes audio files (.wav) and uses PyAudioAnalysis library to extract features.
The notebook handles...
* Processing the directories with .wav files to create data set of audio features
* Principal Component Analysis for dimension reduction and scatter plots for data analysis
* Neural network created using the Keras library, trained/validated/tested on the ccdata dataset from nowwithfeeling.com
* Predicts "agreeableness" and "compelling" from some of the generated audio files within the project in the directory "generated_audio_wav"

### Audio_processing_and_voice_generation.ipynb:
This notebook process audiofiles, use gradientclassifybooster, generate voices using Google cloud tts and Amazon Polly. In order to use Google cloud tts and Amazon Polly. I needed to use my personal key, so it might be difficult to run
the code. However, there are markdowns in this juputer notebook so it should not be difficult to know what it is doing. I have tried my best to explain everything through comments and markdown. I ran the code locally in my Ubuntu VMware. I have disabled my key for security reasons, so you might need to plug in your personal key.
The generated voices are saved in "audio_files" directory.


### audio_survey.py:
Collecting survey data for the report.


## special dependencies:
Need to make google cloud credentials to run Google Cloud TTS
Same for Amazon Polly need to set up a key to run Amazon Polly as well. 
Need to be able to import all these as well. Depending on the system the codes are being run you might need to install some of them.
```
import os
import ast  
import pandas as pd
from pathlib import Path
import librosa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from google.cloud import texttospeech
import boto3
```
Install PyAudioAnalysis following the guide on the official github repository (https://github.com/tyiannak/pyAudioAnalysis/tree/master/pyAudioAnalysis) .
Install dependencies using
```
pip install -r requirements.txt
```