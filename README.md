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

How-to-use-AraVib: https://github.com/MTNakata/AraVib/wiki/How-to-use-AraVib

How-to-use-AraVibS: https://github.com/MTNakata/AraVib/wiki/How-to-use-AraVibS.

How-to-transfer-movies: https://github.com/MTNakata/AraVib/wiki/How-to-transfer-movies-from-iPhone-iPad

## 2. Developmental environment

<details><summary>Our developmental environment is shown in the following</summary><div>

- ffmpeg (3.3.4)
- homebrew (1.3.7)
- pyenv (1.1.3)
- Python 3 (3.6.1)
- Conda (4.3.30)
- Matplotlib (2.0.2)
- Numpy (1.13.1)
- OpenCV-Python (3.3.0.10)
- Pandas (0.20.3)
- Scipy (0.19.1)
- Sqlite (3.13.0)
- Scikit-learn (0.19.1)

The details on the Mac: https://github.com/MTNakata/AraVib/wiki

</div></details>

<details><summary>Easier installation of packages (Update:2018/10/02)</summary><div>

For MacOSX Sierra or High Sierra, install-packages.sh was added to install packages more easily.

```
$ git clone https://github.com/MTNakata/AraVib.git
$ cd AraVib
$ sh install-packages.sh
```

Then, installing packages will start. This shellscript includes installation of homebrew, pyenv, Anaconda and ffmpeg.

Please confirm completion of installation by `python` code.

```
$ python
Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If installation is failed, you see something like the next.

```
$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

</div></details>

## 3. Reference

"High-throughput Analysis of Arabidopsis Stem Vibrations to Identify Mutants with Altered Mechanical Properties"  
Miyuki T Nakata, Masahiro Takahara, Shingo Sakamoto, Kouki Yoshida, Nobutaka Mitsuda  
doi: https://doi.org/10.1101/315838  
