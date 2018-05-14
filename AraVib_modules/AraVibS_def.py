import os, sqlite3

import numpy as np
import pandas as pd

from scipy import stats

def growth_trait_selection():
    local_path = os.getcwd()
    gt_path = local_path + "/mov/growth_trait/"
    gt_csv_list0 = [i for i in os.listdir(gt_path) if i.endswith(".csv")]
    gt_csv_dic = {i+1:j for i,j in enumerate(gt_csv_list0)}
    print("\n".join(["{}:{}".format(i,j) for i,j in zip(gt_csv_dic.keys(),gt_csv_dic.values())]))
    
    loop = True
    
    while loop:
        gt_fname_no_raw = input("Which number is the growth-trait file you want to analyze? (1-): ")
        gt_fname_no = int(gt_fname_no_raw)

        try:
            gt_fname = gt_csv_dic[gt_fname_no]
            loop = False
        except:
            pass
        
    return gt_path+gt_fname

def freq_file_selection():
    print("************ Step 4: Please select ωd data ************")
    local_path = os.getcwd()
    ff_path = local_path + "/mov/summary/"
    ff_csv_list0 = [i for i in os.listdir(ff_path) if i.endswith(".csv")]
    ff_csv_dic = {i+1:j for i,j in enumerate(ff_csv_list0)}
    print("\n".join(["{}:{}".format(i,j) for i,j in zip(ff_csv_dic.keys(),ff_csv_dic.values())]))
    
    loop = True
    
    while loop:
        ff_fname_no_raw = input("Which number is the ωd file you want to analyze? (1-): ")
        ff_fname_no = int(ff_fname_no_raw)

        try:
            ff_fname = ff_csv_dic[ff_fname_no]
            loop = False
        except:
            pass
        
    return ff_path+ff_fname, ff_fname

def model_selection():
    local_path = os.getcwd()
    model_path = local_path + "/model/"
    
    db_path = local_path + "/mov/db_tmp/"
    
    conn = sqlite3.connect(db_path+'vibration.db')
    df_model = pd.io.sql.read_sql("select * from model", conn)
    conn.close()
    
    model_csv_list0 = df_model["model_file"]
    model_csv_dic = {i+1:j for i,j in enumerate(model_csv_list0)}
    print("\n".join(["{}:{}".format(i,j) for i,j in zip(model_csv_dic.keys(),model_csv_dic.values())]))
    
    loop = True
    
    while loop:
        model_fname_no_raw = input("Which model do you use? (1-): ")
        model_fname_no = int(model_fname_no_raw)

        try:
            model_fname = model_csv_dic[model_fname_no]
            local_param = df_model["local_param"][model_fname_no-1]
            scale_param = df_model["scale_param"][model_fname_no-1]
            loop = False
        except:
            pass
        
    return model_path+model_fname,float(local_param),float(scale_param)

def LR_difference(df_gt,freq_data,LR_model,model_fname,local_param,scale_param):
    local_path = os.getcwd()
    model_path = local_path + "/model/"
    
    LR_pred = LR_model.predict(df_gt)
    
    LR_dif = freq_data - LR_pred

    cdf_value = stats.norm.cdf(LR_dif, loc = local_param, scale =  scale_param)
    
    p_value = []
    
    for n in range(len(LR_dif)):
        if LR_dif[n]<=0:
            p_value.append(cdf_value[n])
        else:
            p_value.append(1-cdf_value[n])
    
    return LR_dif, p_value
    
    

    
    