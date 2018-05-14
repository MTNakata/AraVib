# AraVib

## 0. Topics

1. About AraVib and AraVibS
1. Developmental environment
1. How to transfer the slow-motion video from iPhone/iPad to PC
1. Reference

## 1. About AraVib & AraVibS

<img src="https://github.com/MTNakata/Image_folder/blob/master/AraVib_logo.png" width="200">

AraVib is a command-line software implemented by Python to automatically analyze the movies of free vibration of Arabidopsis stems. 
Please refer to our article (see Reference) on shooting method to analyze by AraVib. 
In AraVib, the red marker on the black background is tracked, the one-dimensional vibration waveform is drawn from the coordinates of the marker, 
and damped natural frequency ωd is calculated by Fast Fourier Transform. The output is the csv file of the ωd list 
and three graphs including the raw vibration waveform. AraVibS is an extended version of AraVib for efficient detection of 
mutants using data of ωd, which was calculated by AraVib, and growth traits. In addition, the AraVib_model_control program that 
assists to create a model for mutant detection by AraVibS is also included.

AraVib and AraVibS will be released in this page soon.

How to use AraVib and AraVibS will be released on the wiki soon.

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

For MacOS users, Homebrew, a useful package manager, was installed according to the instruction of the web page. 

URL: https://brew.sh/

Homebrew works as a command brew in Terminal on MacOS. 

`pyenv`, a Python version manager, was installed by the following Terminal command.

```
$ brew install pyenv
```

You can find how to install `pyenv` in the GitHub page. 

URL: https://github.com/pyenv/pyenv

`ffmpeg` was installed by the brew command.

```
$ brew install ffmpeg
```

For easy installation of Python 3 and its data-science packages, we used the open source Anaconda Distribution. 

URL: https://www.anaconda.com/

We installed Anaconda by `pyenv` command in Terminal.

```
$ pyenv install anaconda3-4.4.0
```

Conda, Jupyter notebook, Matplotlib, Numpy, Pandas, Scipy, Sqlite and Scikit-learn are packaged in Anaconda.

To put the Python package installed by the `pip` command directly under Anaconda, the next command was executed.

```
$ conda install -c anaconda pip
```

After that we installed OpenCV-Python with `pip` command.

```
$ pip install opencv-python
```

URL: https://docs.opencv.org/3.0-beta/index.html

## 3. How to transfer the slow-motion video from iPhone/iPad to PC

Slow-motion mode can be used with iPhone6 or later, iPad Pro 2017 or later.

**!Caution!  
There are many situations when Slow-motion-movie files (240 fps) are automatically converted to temporally distorted-video files (30 fps). Such video files cannot be analyzed correctly no longer. The files should keep in the Photos App and take a backup in iCloud or iTunes. It is difficult to restore the data if they have been converted and deleted.**

The following shows how to transfer the files successfully, failed cases and how to check the authenticity.

**iPhone/iPad settings**

1. Settings → Camera → Format → Select "Most Compatible"
1. Settings → Photos → Select "Keep Originals" in Transfer to Mac or PC

**Most reliable method**

The most reliable method is the USB transfer method. Connect your iPhone/iPad and Mac with USB and transfer the movie files with the Photo app in Mac. The transferred pictures or movies will be stored at the following path. Confirm that from Terminal.

`Pictures/Photos Library.photoslibrary/Masters/[YYYY]/[MM]/[DD]/`

Reference: http://www.idownloadblog.com/2017/11/22/how-to-shoot-slo-mo-video-1080p-at-240fps-iphone/

**Successful (in the case of iPhone6 only)**

Each file was transfered from the "Photo" folder using Airdrop by the "Share" function or the Wifi by the "Upload" function of the iPhone App "Documents by Readdle".

Readdle's Documents: https://readdle.com/documents

**Failed**

File were transfered from the iPhone/iPad's Photo App using Airdrop.

**Checking the authenticity**

Please check with the information of the movie file in the message when executing the `ffmpeg` command.

The messege of a correct file. (You can confirm ~240 fps in `Stream #0:1(und)`)
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/AraVib/mov/movie_tmp/2018-04-26 10.04.37.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2018-04-26T04:17:18.000000Z
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 6
    com.apple.quicktime.software: 11.3
    com.apple.quicktime.creationdate: 2018-04-26T10:04:37+0900
  Duration: 00:00:04.17, start: 0.000000, bitrate: 38418 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, mono, fltp, 94 kb/s (default)
    Metadata:
      creation_time   : 2018-04-26T04:17:18.000000Z
      handler_name    : Core Media Data Handler
    Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720, 38306 kb/s, 239.86 fps, 240 tbr, 2400 tbn, 4800 tbc (default)
    Metadata:
      rotate          : 90
      creation_time   : 2018-04-26T04:17:18.000000Z
      handler_name    : Core Media Data Handler
      encoder         : H.264
    Side data:
      displaymatrix: rotation of -90.00 degrees
```

The messege of a converted file. (You can see "30 fps"in `Stream #0:1(und)`)
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/AraVib/mov/movie_tmp/2018-04-26 14.50.54.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2018-04-26T08:07:43.000000Z
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 6
    com.apple.quicktime.software: 11.3
    com.apple.quicktime.creationdate: 2018-04-26T14:50:54+0900
  Duration: 00:00:21.70, start: 0.000000, bitrate: 10824 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, mono, fltp, 176 kb/s (default)
    Metadata:
      creation_time   : 2018-04-26T08:07:44.000000Z
      handler_name    : Core Media Data Handler
    Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720, 10644 kb/s, 30 fps, 30 tbr, 600 tbn, 1200 tbc (default)
    Metadata:
      rotate          : 90
      creation_time   : 2018-04-26T08:07:44.000000Z
      handler_name    : Core Media Data Handler
      encoder         : H.264
    Side data:
      displaymatrix: rotation of -90.00 degrees
```

## 4. Reference

"High-throughput Analysis of Arabidopsis Stem Vibrations to Identify Mutants with Altered Mechanical Properties"  
Miyuki T Nakata, Masahiro Takahara, Shingo Sakamoto, Kouki Yoshida, Nobutaka Mitsuda  
doi: https://doi.org/10.1101/315838  

# AraVib (in Japanese)

## 0. 目次

1. AraVibとAraVibSとは
1. 実行環境
1. iPhone / iPadからスローモーションビデオをPCに転送する方法

## 1. AraVib・AraVibSとは

これらはPythonで実装されたシロイヌナズナの解析用のソフトウェアです。

## 2. 実行環境

準備中。

## 3. iPhone / iPadからスローモーションビデオをPCに転送する方法

iPhone6以降かiPad Proの2017モデル以降でスローモーションビデオを撮影可能です。

**！注意！  
スローモーションムービーファイル（240fps）が時間軸方向に歪んだビデオファイル（30fps）に自動変換される状況が多く存在します。そのようなビデオファイルに変換されてしまった場合、正しく解析されません。動画ファイルを写真アプリに保管し、iCloudまたはiTunesでバックアップを取っておくことをお勧めします。一度変換されてしまうと、元のデータを復元することは困難です。**

以下に、成功したケースと失敗したケースを示し、最後に、転送されたデータが正しいものであるかをチェックする方法を示します。

**もっとも安全な方法**

iPhoneまたはiPadとMacをライトニングUSBで接続し、Macの写真Appで動画ファイルを転送します。転送されたファイルは以下のパスに保存されます。

`Pictures/Photos Library.photoslibrary/Masters/[YYYY]/[MM]/[DD]/`

Finderから確認する場合は「ピクチャ」フォルダ内の「写真 Library」で右クリックし「パッケージの内容を表示」を選択します。

Reference: http://www.idownloadblog.com/2017/11/22/how-to-shoot-slo-mo-video-1080p-at-240fps-iphone/

**成功したケース (ただしiPhone6のみ)**

ファイルごとにiPhoneアプリ「Documents by Readdle」内の写真フォルダからAirDropやWifiで転送を行なった場合。

Readdle's Documents: https://readdle.com/documents

**失敗したケース**

iPhoneまたはiPadの写真アプリからAirdropでPCに転送された場合。

**正しく転送されたかチェックする方法**

ターミナルで`ffmpeg -i`コマンドを実行したあとに表示されるメッセージ内の、ムービーファイルの情報を確認してください。

正しい場合のメッセージ (`Stream #0:1(und)`の項目が約240 fpsになっています)
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/AraVib/mov/movie_tmp/2018-04-26 10.04.37.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2018-04-26T04:17:18.000000Z
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 6
    com.apple.quicktime.software: 11.3
    com.apple.quicktime.creationdate: 2018-04-26T10:04:37+0900
  Duration: 00:00:04.17, start: 0.000000, bitrate: 38418 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, mono, fltp, 94 kb/s (default)
    Metadata:
      creation_time   : 2018-04-26T04:17:18.000000Z
      handler_name    : Core Media Data Handler
    Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720, 38306 kb/s, 239.86 fps, 240 tbr, 2400 tbn, 4800 tbc (default)
    Metadata:
      rotate          : 90
      creation_time   : 2018-04-26T04:17:18.000000Z
      handler_name    : Core Media Data Handler
      encoder         : H.264
    Side data:
      displaymatrix: rotation of -90.00 degrees
```

失敗した場合のメッセージ (`Stream #0:1(und)`の項目が30 fpsになっています)
```
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/AraVib/mov/movie_tmp/2018-04-26 14.50.54.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2018-04-26T08:07:43.000000Z
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 6
    com.apple.quicktime.software: 11.3
    com.apple.quicktime.creationdate: 2018-04-26T14:50:54+0900
  Duration: 00:00:21.70, start: 0.000000, bitrate: 10824 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, mono, fltp, 176 kb/s (default)
    Metadata:
      creation_time   : 2018-04-26T08:07:44.000000Z
      handler_name    : Core Media Data Handler
    Stream #0:1(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720, 10644 kb/s, 30 fps, 30 tbr, 600 tbn, 1200 tbc (default)
    Metadata:
      rotate          : 90
      creation_time   : 2018-04-26T08:07:44.000000Z
      handler_name    : Core Media Data Handler
      encoder         : H.264
    Side data:
      displaymatrix: rotation of -90.00 degrees
```

## 6. 参考文献

準備中。
