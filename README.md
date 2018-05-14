# AraVib

This software is released under the MIT License, see LICENSE.txt.

## 0. Topics

1. About AraVib and AraVibS
1. Developmental environment
1. Reference

## 1. About AraVib & AraVibS

<img src="https://github.com/MTNakata/Image_folder/blob/master/AraVib_logo.png" width="200">
<img src="https://github.com/MTNakata/Image_folder/blob/master/AraVibS_logo.png" width="200">

AraVib is a command-line software implemented by Python to automatically analyze the movies of free vibration of Arabidopsis stems. 
Please refer to our article (see Reference) on shooting method to analyze by AraVib. 
In AraVib, the red marker on the black background is tracked, the one-dimensional vibration waveform is drawn from the coordinates of the marker, 
and damped natural frequency ωd is calculated by Fast Fourier Transform. The output is the csv file of the ωd list 
and three graphs including the raw vibration waveform. AraVibS is an extended version of AraVib for efficient detection of 
mutants using data of ωd, which was calculated by AraVib, and growth traits. In addition, the AraVib_model_control program that 
assists to create a model for mutant detection by AraVibS is also included.

How-to-use-AraVib is found in AraVib wiki: https://github.com/MTNakata/AraVib/wiki/How-to-use-AraVib

How-to-use-AraVibS will be released in the wiki soon.

How-to-transfer-movies is found in AraVib wiki: https://github.com/MTNakata/AraVib/wiki/How-to-transfer-movies-from-iPhone-iPad

## 2. Developmental environment

Our developmental environment is shown in the following:

- MacOS Sierra with Xcode 8.3.3
- ffmpeg (3.3.4)
- homebrew (1.3.7)
- pyenv (1.1.3)
- Python 3 (3.6.1)
- Conda (4.3.30)
- Jupyter notebook (5.0.0)
- Matplotlib (2.0.2)
- Numpy (1.13.1)
- OpenCV-Python (3.3.0.10)
- Pandas (0.20.3)
- Scipy (0.19.1)
- Sqlite (3.13.0)
- Scikit-learn (0.19.1)

Both AraVib and AraVibS can also be used on other versions and other OSs (Linux and Windows) probably.

The details are shown in AraVib wiki: https://github.com/MTNakata/AraVib/wiki

## 3. Reference

"High-throughput Analysis of Arabidopsis Stem Vibrations to Identify Mutants with Altered Mechanical Properties"  
Miyuki T Nakata, Masahiro Takahara, Shingo Sakamoto, Kouki Yoshida, Nobutaka Mitsuda  
doi: https://doi.org/10.1101/315838  