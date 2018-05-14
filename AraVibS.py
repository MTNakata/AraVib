#!/Users/local/.pyenv/versions/anaconda3-4.0.0/bin python3
# coding: utf-8
import os

import numpy as np
import pandas as pd

from sklearn.externals import joblib

import  AraVib

from AraVib_modules.AraVibS_def import growth_trait_selection, freq_file_selection
from AraVib_modules.AraVibS_def import model_selection, LR_difference
        
def main():
    
    print("************ Step 1: Please select growth-trait data ************")
    local_path = os.getcwd()
    summery_path = local_path + "/mov/summary/"
    
    growth_trait_path =  growth_trait_selection()
    df_gt = pd.read_csv(growth_trait_path)
    
    print("************ Step 2: Please select your model ************")
    
    model_fname,local_param,scale_param = model_selection()
    LR_model = joblib.load(model_fname)
    
    print("******** Step 3: Do you want to analyze ωd by AraVib? ********")
    loop = True
    
    while loop:
        print("If you want, enter y.")
        print("Or if you use the existing ωd-data file, enter n.")
        aravib_raw = input("(y/n):")
        aravib_ = str(aravib_raw)
        if  aravib_.lower() == "y":
            aravib = True
            loop = False
        elif  aravib_.lower() == "n":
            aravib = False
            loop = False
        else:
            pass
    
    loop = True
    
    while loop:

        if aravib:
            freq_path, freq_fname = AraVib.main()
        else:
            freq_path, freq_fname = freq_file_selection()

        try:
            df_freq = pd.read_csv(freq_path)
            freq_data = df_freq["Freq_Hz"]
            loop = False
        except:
            pass
    
    if len(freq_data) == len(df_gt):
        dif, p_value = LR_difference(df_gt,freq_data,LR_model,model_fname,local_param,scale_param)
        clf = np.array(p_value)  < 0.01
        
        df_freq2 = df_freq.copy()
        df_freq2["H"] = df_gt["H"]
        df_freq2["FW"] = df_gt["FW"]
        df_freq2["Dif"] = dif
        df_freq2["p_value"] = p_value
        df_freq2["Mutant?(p_value<0.01)"] = clf
        
        result_path = "{}/mov/AraVibS_result/{}+Identify.csv".format(local_path,freq_fname)
        
        print("*"*50)
        print("Mutant?(p_value<0.01)")
        print(df_freq2["Mutant?(p_value<0.01)"])
        print("*"*50)
        print("Details")
        print(df_freq2)
        print("")
        print("File_path:{}".format(result_path))
        
        df_freq2.to_csv(result_path)
    else:
        print("Error: Growth-trait data is not corresponding to freq_data")

if __name__ == '__main__':
    main()
    