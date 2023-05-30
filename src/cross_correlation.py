from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

def corr_with_output(combined_df):
    # CREATING DATAFRAME:
    # tss_df = pd.DataFrame(tss_data)
    # nt_df = pd.DataFrame(nt_data)
    # tss_df['TSS'] = 1
    # nt_df['TSS'] = 0
    # combined_df = pd.concat([tss_df, nt_df], ignore_index=True)
    x = combined_df.drop("TSS", axis=1)
    y = combined_df["TSS"]
    corr_arr = []
    # CALCULATING CORRELATION BETWEEN
    for i in x:
        # corr, _ = pearsonr(combined_df[i], y)
        corr1, _ = spearmanr(combined_df[i], y)
        corr_arr.append(corr1)
    print(corr_arr)
    params = x.columns
    plt.bar(params, corr_arr, color='maroon', width=0.4)
    plt.ylim((-1, 1))
    plt.show()
    import sys
    sys.exit()

def corr_removal(df):
    df_corr = df.drop("TSS", axis=1)
    cor_matrix = df_corr.corr().abs()
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    sorted_mat = upper_tri.unstack().sort_values()
    reversed_sorted = sorted_mat.iloc[::-1]
    reversed_sorted.dropna(inplace =True)
    print(type(reversed_sorted))
    for index, row in reversed_sorted.items():
        print(index, row)
    # print(reversed_sorted.loc[[1]])
    # for i in reversed_sorted:
    #     print(i)

    import sys
    sys.exit()
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.6)]
    print(to_drop)
    df1 = df.drop(to_drop, axis=1)
    print(df1.head())

    x = df1.drop("TSS", axis=1)
    y = df1["TSS"]
    logreg = LogisticRegression()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    logreg.fit(x_train, y_train)
    pred = logreg.predict(x_test)
    print(confusion_matrix(y_test, pred))
    print(accuracy_score(y_test, pred))
    # reg_training_without_pca.reg_training(tss,no_tss)

    return