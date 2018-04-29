# AraVib

## 0. Topics

1. About AraVib and AraVibS
1. Developmental environment
1. How to use AraVib
1. How to use AraVibS
1. How to transfer the slow-motion video from iPhone/iPad to PC
1. Reference

## 1. About AraVib & AraVibS

These are softwares for analysis of Arabidopsis thaliana implemented by Python.   

## 2. Developmental environment

Under Construction.

## 3. How to use AraVib and AraVibS

Under Construction.

## 4. How to use AraVib and AraVibS

Under Construction.

## 5. How to transfer the slow-motion video from iPhone/iPad to PC

**!Caution!  
There are many situations when Slow-motion-movie files (240 fps) are automatically converted to temporally distorted-video files (30 fps). Such video files cannot be analyzed correctly no longer. The files should keep in the Photos App and take a backup in iCloud or iTunes. It is difficult to restore the data if they have been converted and deleted.**

The following shows how to transfer the files successfully, failed cases and how to check the authenticity.

**Successful**

- Case 1: Each file was transfered from the "Photo" folder using Airdrop by the "Share" function of the iPhone App "Documents by Readdle".

Readdle's Documents: https://readdle.com/documents

- Case 2: Files were copied to another folder in "Documents by Readdle" and the folder was transfered.  
**!Caution!  Don't "move" files to another folder. The files were incorrectly converted and the raw files were deleted.**

- Case 3: A batch of files were uploaded to a File Server through the Wifi by the "Upload" function of "Documents by Readdle". This way takes more time than using AirDrop, but it has versatility.

**Failed**

- Case 1: Each file was directly transfered from the Photo App using Airdrop or lightening-USB cable to PC.

- Case 2: Files were moved to another folder in "Documents by Readdle" and the folder was transfered to PC. The files were incorrectly converted and the raw files were deleted.

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

## 6. Reference

Under Construction.

# AraVib (in Japanese)

## 0. 目次

1. AraVibとAraVibSとは
1. 実行環境
1. AraVibの使い方
1. AraVibSの使い方
1. iPhone / iPadからスローモーションビデオをPCに転送する方法
1. 参考文献

## 1. AraVib・AraVibSとは

これらはPythonで実装されたシロイヌナズナの解析用のソフトウェアです。

## 2. 実行環境

準備中。

## 3. AraVibの使い方

準備中。

## 4. AraVibSの使い方

準備中。

## 5. iPhone / iPadからスローモーションビデオをPCに転送する方法

**！注意！  
スローモーションムービーファイル（240fps）が時間軸方向に歪んだビデオファイル（30fps）に自動変換される状況が多く存在します。そのようなビデオファイルに変換されてしまった場合、正しく解析されません。動画ファイルを写真アプリに保管し、iCloudまたはiTunesでバックアップを取っておくことをお勧めします。一度変換されてしまうと、元のデータを復元することは困難です。**

以下に、成功したケースと失敗したケースを示し、最後に、転送されたデータが正しいものであるかをチェックする方法を示します。

**成功したケース**

- ケース1：ファイルごとにiPhoneアプリ「Documents by Readdle」内の写真フォルダから共有機能を介してAirDropで転送を行なった場合。

Readdle's Documents: https://readdle.com/documents

- ケース2：「Readles by Documents」を使って、写真フォルダから別のフォルダにファイルを「コピー」し、そのフォルダをAirDropによって転送した場合。  
**！注意！  ファイルを写真フォルダから別のフォルダに「移動」しないでください。動画は不適切な形式に変換された上、元のデータも失われることがあります。**

- ケース3：「Documents by Readdle」で複数のファイルを選択し、アップロード機能によってWifiを介してファイルサーバーにアップロードした場合。このやり方は、AirDropを使用するよりも時間はかかりますが、汎用性があります。

**失敗したケース**

- ケース1：写真アプリからAirdropまたはlightening-USBケーブル経由でPCに転送された場合。このケースでは写真アプリ内のファイルは削除されないため、やり直しが可能です。

- ケース2：「Readdles by Documents」内の写真フォルダから別のフォルダにファイルを「移動」し、そのフォルダをPCにAirdropで転送したケース。動画は前述の歪んだ動画に変換された上、元のデータも失われ、修復は不可能でした。

**正しく転送されたかチェックする方法**

`ffmpeg`コマンドを実行したあとに表示されるメッセージ内の、ムービーファイルの情報を確認してください。

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
