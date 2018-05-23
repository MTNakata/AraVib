#!/Users/local/.pyenv/versions/anaconda3-4.0.0/bin python3
# coding: utf-8
from AraVib_modules.AraVib_video_convert import create_df, create_db
from AraVib_modules import  AraVib_body

import os
import sqlite3

import numpy as np
import pandas as pd
        
def main():
    #threshold of H, S, V
    hue = [5, 165]
    saturation = 75
    value = 90
    
    #get paths of current directory
    local_path = os.getcwd()
    
    path_list = [local_path + "/mov/" + i for i in ["frames_tmp","bin_tmp",
                                      "db_tmp","movie_tmp","mov_crop_tmp","trace_tmp",
                                                    "summary"]]  
    
    #Input information    
    date_raw = input("Input date of image files (YYYY-MM-DD): ")
    date_fname = str(date_raw)
    db_name = "".join(date_fname.split("-"))
    
    loop = True
    
    while loop:
        record_raw = input("Record images in process? (y/n): ")
        record_ = str(record_raw)
        if  record_.lower() == "y":
            record = True
            loop = False
        elif  record_.lower() == "n":
            record = False
            loop = False
        else:
            pass
    
    #create database for run and output
    df001 = create_df(path_list[3],fformat=".mov",date_fname = date_fname)
    print(df001)
    df002 = create_db(df001,path_list[2], db_name=db_name)
    print(df002)
    
    os.chdir(path_list[2])
    conn = sqlite3.connect('vibration.db')
    columns=["date","sample_no","mov_name", "Freq_Hz"]
    df = pd.DataFrame(np.array([[np.nan],[np.nan],[np.nan],[np.nan]]).T, columns=columns)
    df.to_sql("vibration{}".format(db_name), conn, if_exists="replace")
    conn.close()
    
    #run AraVib main script
    for i in range(len(df002)):
        try:
            AraVib_body.main(i, date_fname, path_list, df002, 
                  h =hue, s = saturation, v = value, record = record, db=db_name)
        except ValueError:
            os.chdir(path_list[2])
            conn = sqlite3.connect('vibration.db')
            columns=["date","sample_no","mov_name", "Freq_Hz"]
            df = pd.DataFrame(np.array([[date_fname],["{:03d}".format(i)],[df002["mov_name"][i]],[np.nan]]).T, columns=columns)
            df.to_sql("vibration{}".format(db_name), conn, if_exists="append")
            conn.close()
            
    #For test: テスト用
    #AraVib_body.main(11, date_fname, path_list, df002, h =[5, 165], s = 60, v = 90, db=db_name)
    
    os.chdir(path_list[2])
    conn = sqlite3.connect('vibration.db')
    df_final = pd.io.sql.read_sql("select * from vibration{}".format(db_name), conn)
    conn.close()
    
    os.chdir(path_list[-1])
    csv_fname = "{}.csv".format(date_fname)
    df_final.iloc[1:,1:].to_csv(csv_fname,index = False)
    
    return path_list[-1]+"/"+csv_fname, csv_fname

if __name__ == '__main__':
    main()
    