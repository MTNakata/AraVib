from AraVib_modules.AraVib_video_convert import generate_code, video_converter
from AraVib_modules.AraVib_img_to_vibwave import img_bulk_read_cv2, red_trace_generate, red_trace
from AraVib_modules.AraVib_img_to_vibwave import img_to_center, nan_processing, center_to_displacement
from AraVib_modules.AraVib_FFT import displacement_to_difference, transform_hanning, displacement_to_major_freq

import os, sys, shlex, subprocess, time
import sqlite3

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from collections import Counter


def freqs_power_graph(freqs, power, col="k"):
    fig = plt.figure(figsize=(13,10))
    ax = fig.add_subplot(111)
    ax.plot(freqs,power,color=col,marker=".",markersize=12,linewidth=3)
    
def plot_graph(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data)
    
def main(i, date_fname, path_list0, df, h, s, v, record = False, db="test"):
    start = time.time()
    
    path_frame, path_bin, path_db, path_mov, path_crop, path_trace, path_file = path_list0
    
    date = date_fname
    sample_name = "{:03d}".format(i)

    args1,mov_name = generate_code(i, df, path_mov, path_frame)
    video_converter(args1) 

    fnames, img_files = img_bulk_read_cv2(path_frame)
    
    #For crop image recording: 切り出し画像記録用
    if record:
        os.chdir(path_crop)
        for n,img in enumerate(img_files):
            cv2.imwrite("{}_{:05d}.jpg".format(i,n),img[:600,:,:])
    
    print("******************************")
    bin_imgs = red_trace(fnames, img_files, h, s, v)
    
    if record:
        os.chdir(path_bin)
        for n,img in enumerate(bin_imgs):
            cv2.imwrite("{}_{:05d}.jpg".format(i,n),img)
    
    print("h: {}, s: {}, v: {}".format(h,s,v))

    center_list_raw, cl_array1 = img_to_center(bin_imgs)
    c = Counter(cl_array1)
    print(c)

    center_list1 = nan_processing(center_list_raw)

    displacement_list1 = center_to_displacement(center_list1)
    
    dif_array1, start_point1 = displacement_to_difference(displacement_list1)
    hanning_array1 = transform_hanning(displacement_list1, start_point1)
    freqs1, power1, major_freq1 = displacement_to_major_freq(hanning_array1)
    
    print("ωd of {} = {:.4f} Hz".format(sample_name,*major_freq1))

    os.chdir(path_file)
    plt.scatter(np.array(center_list_raw)[:,0],np.array(center_list_raw)[:,1],cmap="plasma")
    plt.savefig("{}_{}_coordinates.png".format(date,sample_name),dpi=250)
    plot_graph(displacement_list1)
    plt.savefig("{}_{}_displacement_vibration.png".format(date,sample_name),dpi=250)
    plot_graph(hanning_array1)
    plt.savefig("{}_{}_hanning_vibration.png".format(date,sample_name),dpi=250)
    freqs_power_graph(freqs1, power1, col="k")
    plt.savefig("{}_{}_fft_power_spectrum.png".format(date,sample_name),dpi=250)

    os.chdir(path_db)
    conn = sqlite3.connect('vibration.db')
    columns=["date","sample_no","mov_name", "Freq_Hz"]
    df = pd.DataFrame(np.array([[date],["{:03d}".format(i)],[mov_name],[*major_freq1]]).T, columns=columns)
    df.to_sql("vibration{}".format(db), conn, if_exists="append")
    df2 = pd.io.sql.read_sql("select * from vibration{}".format(db), conn)
    conn.close()
    
    #For detection site recording: 検出部位記録用
    if record:
        os.chdir(path_trace)
        for n,img in enumerate(img_files):
            try:
                cv2.circle(img,tuple(center_list_raw[n]), 40, (0,0,255), 3)
                cv2.imwrite("{}_{:05d}.jpg".format(i, n),img[:600,:,:])
            except:
                cv2.imwrite("{}_{:05d}.jpg".format(i,n),img[:600,:,:])
    
    print(df2)
    print("Runtime = {:.4f}s".format(time.time() - start))