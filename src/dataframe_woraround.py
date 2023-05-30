from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

def workaround(tss_data,nt_data):
    # CREATING DATAFRAME:
    tss_df = pd.DataFrame(tss_data)
    nt_df = pd.DataFrame(nt_data)
    tss_df['TSS'] = 1
    nt_df['TSS'] = 0
    combined_df = pd.concat([tss_df, nt_df], ignore_index=True)
    combined_df.to_csv('training80window_no_mov_avg')
    import sys
    sys.exit()
    x = combined_df.drop("TSS", axis=1)
    y = combined_df["TSS"]
    corr_arr = []
    # CALCULATING CORRELATION BETWEEN
    for i in x:
        corr, _ = pearsonr(combined_df[i], y)
        corr1, _ = spearmanr(combined_df[i], y)
        corr_arr.append(corr1)
        # covariance = np.cov(combined_df[i],y)
    # print(corr_arr)
    params = x.columns
    plt.bar(params, corr_arr, color='maroon', width=0.4)
    plt.ylim((-1, 1))
    plt.show()
    import sys
    sys.exit()

def readingCSV():
    df = pd.read_csv('/Users/palakaggarwal/Desktop/Palak/SEProm/SEProm/out.csv')
    # df.columns.str.match('Unnamed')
    df = df.drop('Unnamed: 0', axis = 1)
    return df