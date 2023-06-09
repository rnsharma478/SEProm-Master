from sklearn.decomposition import PCA
from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from src import reg_training_without_pca, random_forest, dataframe_woraround

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

params = ['a','b','c','d','e','f','g','h','i','j','k','l','ma','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad','ae']

def pca_train(seq_data):
    seq_data = seq_data.drop('TSS', axis=1)
    # print(seq_data)
    train, test = train_test_split(seq_data, test_size=0.2)
    pca = PCA(0.90)
    print("pca_training")
    pca.fit(train)
    # print(pca.components_)
    # print(pca.n_components_)
    indep_var_vector = pca.transform(seq_data)
    return indep_var_vector

def pca_training(normalized_map_tss):
    print("CREATING DATAFRAME")
    seq_data = pd.DataFrame(columns=params)
    print(seq_data)
    params1 = ['a','b','c','d','e','f','g','h','i','j','k','l','ma','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad','ae', 'motifs']
    # ADDING TSS DATA TO DATAFRAME
    for seq in normalized_map_tss.keys():
        m = pd.Series(avg_window(486,493,params,normalized_map_tss[seq], 'm_0_0'),index = params1)
        n = pd.Series(avg_window(462, 472, params, normalized_map_tss[seq],'m_0_1'), index=params1)
        l = pd.Series(avg_window(420, 437, params, normalized_map_tss[seq], 'm_0_2'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        m = pd.Series(avg_window(487, 494, params, normalized_map_tss[seq], 'm_1_0'), index=params1)
        n = pd.Series(avg_window(464, 471, params, normalized_map_tss[seq], 'm_1_1'), index=params1)
        l = pd.Series(avg_window(453, 462, params, normalized_map_tss[seq], 'm_1_2'), index=params1)
        k = pd.Series(avg_window(440, 452, params, normalized_map_tss[seq], 'm_1_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)
        m = pd.Series(avg_window(483, 494, params, normalized_map_tss[seq], 'm_2_0'), index=params1)
        n = pd.Series(avg_window(463, 472, params, normalized_map_tss[seq], 'm_2_1'), index=params1)
        l = pd.Series(avg_window(450, 459, params, normalized_map_tss[seq], 'm_2_2'), index=params1)
        k = pd.Series(avg_window(434, 445, params, normalized_map_tss[seq], 'm_2_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)
        m = pd.Series(avg_window(487, 498, params, normalized_map_tss[seq], 'm_3_0'), index=params1)
        n = pd.Series(avg_window(463, 472, params, normalized_map_tss[seq], 'm_3_1'), index=params1)
        l = pd.Series(avg_window(450, 459, params, normalized_map_tss[seq], 'm_3_2'), index=params1)
        k = pd.Series(avg_window(432, 445, params, normalized_map_tss[seq], 'm_3_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)
        z = len(seq_data.index)
        m = pd.Series(avg_window(786, 793, params, normalized_map_tss[seq], 'nm_0_0'), index=params1)
        n = pd.Series(avg_window(763, 772, params, normalized_map_tss[seq], 'nm_0_1'), index=params1)
        l = pd.Series(avg_window(720, 737, params, normalized_map_tss[seq], 'nm_0_2'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        m = pd.Series(avg_window(787, 794, params, normalized_map_tss[seq], 'nm_1_0'), index=params1)
        n = pd.Series(avg_window(764, 771, params, normalized_map_tss[seq], 'nm_1_1'), index=params1)
        l = pd.Series(avg_window(753, 762, params, normalized_map_tss[seq], 'nm_1_2'), index=params1)
        k = pd.Series(avg_window(740, 752, params, normalized_map_tss[seq], 'nm_1_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)
        m = pd.Series(avg_window(783, 794, params, normalized_map_tss[seq], 'nm_2_0'), index=params1)
        n = pd.Series(avg_window(763, 772, params, normalized_map_tss[seq], 'nm_2_1'), index=params1)
        l = pd.Series(avg_window(750, 759, params, normalized_map_tss[seq], 'nm_2_2'), index=params1)
        k = pd.Series(avg_window(734, 745, params, normalized_map_tss[seq], 'nm_2_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)
        m = pd.Series(avg_window(787, 798, params, normalized_map_tss[seq], 'nm_3_0'), index=params1)
        n = pd.Series(avg_window(763, 772, params, normalized_map_tss[seq], 'nm_3_1'), index=params1)
        l = pd.Series(avg_window(750, 759, params, normalized_map_tss[seq], 'nm_3_2'), index=params1)
        k = pd.Series(avg_window(732, 745, params, normalized_map_tss[seq], 'nm_3_3'), index=params1)
        seq_data = seq_data.append(m, ignore_index=True)
        seq_data = seq_data.append(n, ignore_index=True)
        seq_data = seq_data.append(l, ignore_index=True)
        seq_data = seq_data.append(k, ignore_index=True)

    seq_data.loc[:z, 'TSS'] = int(1)
    seq_data.loc[z:, 'TSS'] = int(0)

    seq_data['SI'] = seq_data['k']+seq_data['p']+seq_data['q']+seq_data['s']+seq_data['u']+seq_data['v']+seq_data['x']+seq_data['g']+seq_data['n']+seq_data['r']+seq_data['aa']+seq_data['ab']
    seq_data = seq_data.drop(['k','p','q','s','u','v','x','g','n','r','aa','ab'], axis=1)
    seq_data['SD'] = seq_data['a']+seq_data['b']+seq_data['f']+seq_data['h']+seq_data['l']+seq_data['ma']+seq_data['c']+seq_data['d']+seq_data['e']+seq_data['i']+seq_data['j']+seq_data['o']+seq_data['t']+seq_data['w']+seq_data['y']+seq_data['z']
    seq_data = seq_data.drop(['a','b','f','h','l','ma','c','d','e','i','j','o','t','w','y','z'], axis = 1)
    seq_data['EI'] = seq_data['ac']+seq_data['ad']
    seq_data = seq_data.drop(['ac','ad'], axis=1)
    seq_data['ED'] = seq_data['ae']
    seq_data = seq_data.drop('ae', axis=1)

    seq_data.to_csv('TEST_MOTIF_DATA.csv')
    import sys
    sys.exit()

    for seq in normalized_map_tss.keys():
        m = [float(i) for i in avg_window(425,505,params,normalized_map_tss[seq])]
        seq_data.loc[seq] = m

    l = len(seq_data.index)
    tss = seq_data[:l]
    # print(tss)

    for seq in normalized_map_tss.keys():
        m = [float(i) for i in avg_window(700,780,params,normalized_map_tss[seq])]
        seq_data.loc[l+seq] = m
    no_tss = seq_data.loc[l:]
    # print(tss)
    # print(no_tss)
    # import sys
    # sys.exit()
    dataframe_woraround.workaround(tss,no_tss)
    random_forest.random_forest(tss, no_tss)


    # reg_training_without_pca.reg_training(tss,no_tss)

    # corr_removal(tss,no_tss)
    #
    # import sys
    # sys.exit()
    # print(seq_data.shape)
    # print(seq_data.loc[[824]])
    # print(seq_data.loc[[1060]])

    train, test = train_test_split(seq_data, test_size=0.2)
    pca = PCA(0.90)
    print("pca_training")
    pca.fit(train)
    indep_var_vector_tss = pca.transform(seq_data[:l])
    indep_var_vector_nt = pca.transform(seq_data[l:])
    print("random_forest")
    random_forest.random_forest(indep_var_vector_tss, indep_var_vector_nt)
    import sys
    sys.exit()
    return indep_var_vector_tss, indep_var_vector_nt

def avg_window(start, stop, params, params_map, motif_name):
    arr = []
    for p in params:
        avg_p = sum(params_map[p][start:stop])/(stop-start)
        arr.append(avg_p)
    arr.append(motif_name)
    return arr

