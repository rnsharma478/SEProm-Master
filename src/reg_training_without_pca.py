import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def reg_training(tss_data,nt_data):
    tss_data['TSS'] = 1
    nt_data['TSS'] = 0

    logreg = LogisticRegression()
    combined_df = pd.concat([tss_data,nt_data],ignore_index=True)
    # print(combined_df)

    x = combined_df.drop("TSS", axis=1)
    y = combined_df["TSS"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    logreg.fit(x_train, y_train)
    pred = logreg.predict(x_test)
    print(confusion_matrix(y_test, pred))
    print(accuracy_score(y_test, pred))
