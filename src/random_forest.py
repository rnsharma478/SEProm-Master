from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

def random_forest(combined_df):
    print("Random Forest")
    clf = RandomForestClassifier(n_estimators=100)
    #CREATING DATAFRAME:
    tss_df = pd.DataFrame(combined_df[:12879])
    nt_df = pd.DataFrame(combined_df[12879:])
    tss_df['TSS'] = 1
    nt_df['TSS'] = 0
    # print(tss_df.tail)
    # print(nt_df.head)
    combined_df = pd.concat([tss_df, nt_df], ignore_index=True)
    print(combined_df)
    # combined_df = combined_df.drop(['o','s','u'], axis =1)

    x = combined_df.drop("TSS", axis=1)
    y = combined_df["TSS"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)
    clf = clf.fit(x_train,y_train)
    pred = clf.predict(x_test)
    print(pred)
    print(y_test)
    print(confusion_matrix(y_test, pred))
    print(accuracy_score(y_test, pred))
    print(classification_report(y_test, pred))