import os, sys, shlex, subprocess, time
import sqlite3
import pandas as pd
import numpy as np

def create_df(path, fformat=".mov",date_fname = "2017-12-18"):
    os.chdir(path)
    ls0 = shlex.split("ls")
    ls =  subprocess.run(ls0,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ls.stdout
    output = str(output)[2:].split("\\n")[:-1]
    mov_name_list = [i for i in output if i.lower().endswith(fformat)]
    date0 = "".join(date_fname.split("-"))
    
    sample_no = len(mov_name_list)
    
    date = [date0 for i in range(sample_no)]
    time = ["00.00" for i in range(sample_no)]
    index = [str(i) for i in range(sample_no)]
    
    columns=["index","date","mov_name","start_time"]
    text_parts = [index,date,mov_name_list,time]
    df = pd.DataFrame(np.array(text_parts).T, columns=columns)
    
    return df
    
def create_db(df,path,db_name="test"):
    os.chdir(path)
    print("db_name: ", db_name)
    conn = sqlite3.connect('vibration.db')
    df.to_sql("vibration_mov{}".format(db_name), conn, if_exists="replace")
    df2 = pd.io.sql.read_sql("select * from vibration_mov{}".format(db_name), conn)
    return df2

def generate_code(i, df2, path, path0):
    date = df2.loc[i,"date"]
    mov_name = df2.loc[i,"mov_name"]
    print(mov_name)
    start_time = df2.loc[i,"start_time"]
    str1 = "ffmpeg -i {}/\"{}\"".format(path, mov_name)
    str2 = "-ss 00:00:{} -t 00:00:03.00 -vcodec png {}/image_%03d.png".format(start_time,path0)
    args = str1+" "+str2
    return shlex.split(args), mov_name

def video_converter(args0):
    try:
        subprocess.check_call(args0)
    except:
        print("failed")
        sys.exit()