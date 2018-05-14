#!/Users/local/.pyenv/versions/anaconda3-4.0.0/bin python3
# coding: utf-8
import os, sqlite3

import numpy as np
import pandas as pd

from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

from AraVib_modules.AraVibS_def import growth_trait_selection, freq_file_selection

def model_create(df_growth_trait, freq_data):
    
    local_path = os.getcwd()
    model_path = local_path + "/model/"
    
    lr_model = LinearRegression()
    lr_model.fit(df_growth_trait,freq_data)
    
    model_fname0 = input("model file name?: ")
    model_fname = str(model_fname0)
    
    from sklearn.externals import joblib
    joblib.dump(lr_model, model_path+model_fname, compress=True)

    pred_freq = lr_model.predict(df_growth_trait)
    dif = freq_data - pred_freq
    
    return model_fname,dif

def create():
    
    print("************ Step 1: Please select growth-trait data ************")
    local_path = os.getcwd()
    summery_path = local_path + "/mov/summary/"
    
    growth_trait_path =  growth_trait_selection()
    df_gt = pd.read_csv(growth_trait_path)
    
    print("************ Step 2: Please select ωd data ************")
    freq_path, freq_fname = freq_file_selection()

    df_freq = pd.read_csv(freq_path)
    freq_data = df_freq["Freq_Hz"]
    
    print("************ Step 3: Please name your new model ************")
    local_path = os.getcwd()

    model_fname,dif = model_create(df_gt, freq_data)
    local_param,scale_param = stats.norm.fit(dif)
    
    db_path = local_path + "/mov/db_tmp/"
    
    columns=["model_file","local_param","scale_param"]

    df_model = pd.DataFrame(np.array([[model_fname,local_param,scale_param]]),
                            columns=columns)
    
    print(df_model)
    
    conn = sqlite3.connect(db_path + 'vibration.db')
    df_model.to_sql("model", conn, if_exists="append")
    conn.close()
    
def view():
    local_path = os.getcwd()
    db_path = local_path + "/mov/db_tmp/"
    
    conn = sqlite3.connect(db_path+'vibration.db')
    df_model = pd.io.sql.read_sql("select * from model", conn)
    conn.close()
    print(df_model)
    
def delete():
    local_path = os.getcwd()
    model_path = local_path + "/model/"
    db_path = local_path + "/mov/db_tmp/"
    
    conn = sqlite3.connect(db_path+'vibration.db')
    df_model = pd.io.sql.read_sql("select * from model", conn)
    conn.close()
    print(df_model)
    
    model_name_ = input("Which model do you want to delete? (input name):")
    model_name = str(model_name_)
    
    confirm_ = input("Do you really want to delete {}? (y/n):".format(model_name))
    confirm = str(confirm_)
    
    if confirm.lower() == "y":
        df_model_2 = df_model[df_model["model_file"]!=model_name]
        print(df_model_2)

        conn = sqlite3.connect(db_path+'vibration.db')
        df_model_2.to_sql("model", conn, if_exists="replace",index=False)
        conn.close()

        os.remove(model_path+model_name)
    
    else:
        pass

if __name__ == '__main__':
    
    loop = True
    
    while loop:
        mode_ = input("Create a new model (1), view(2), or delete a model (3):")
        mode_no = int(mode_)
        if mode_no < 4:
            loop = False
        else:
            pass
    
    print("*"*50)
    if mode_no == 1:
        create()
    elif mode_no == 2:
        view()
    else:
        delete()
    print("*"*50)