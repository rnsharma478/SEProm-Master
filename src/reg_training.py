import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def log_reg(combined_df):
    print ("LOG REG")
    tss_df = pd.DataFrame(combined_df[:12879])
    nt_df = pd.DataFrame(combined_df[12879:])
    tss_df['TSS'] = 1
    nt_df['TSS'] = 0

    combined_df = pd.concat([tss_df,nt_df],ignore_index=True)
    # mean_data = combined_df.groupby('TSS').mean()
    # print(combined_df)

    #train data
    x= combined_df.drop("TSS",axis=1)
    y= combined_df["TSS"]
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.4, random_state=1)
    logreg = LogisticRegression()
    logreg.fit(x_train,y_train)
    pred = logreg.predict(x_test)
    print("prediction is: ",pred)
    print("testing results should be: \n",y)
    print(classification_report(y_test,pred))
    print(confusion_matrix(y_test,pred))
    print(accuracy_score(y_test,pred))
    # import sys
    # sys.exit()