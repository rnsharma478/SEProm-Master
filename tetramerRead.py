from src import readSequenceFile, getParameterDetails, pcaRegressionAlgorithm, motifsAlgorithm, processResults, writeFile,pca_training,reg_training,dataframe_woraround, cross_correlation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tetramer = '/Users/palakaggarwal/Desktop/Palak/SEProm/SEProm/train_data/TSS_Seq/Escherichia_coli'
paramVals = '/Users/palakaggarwal/Desktop/Palak/SEProm/SEProm/train_data/Tetramer.xlsx'
tetramer_cds = '/Users/palakaggarwal/Desktop/Palak/SEProm/SEProm/train_data/CDS_Seq/Escherichia_coli_CDS'

strInc = []
strDec = []

def dataCleaning(df):
    # df = df.drop(['Tetramer'], axis =1)
    duplicates = df.duplicated(subset = ['l','m','n','o','p','q'], keep = False)
    df2 = df[~duplicates]
    df1 = df[duplicates]
    df1 = (df1.groupby(df1.columns.tolist())
           .apply(lambda x: tuple(x.index))
           .reset_index(name='Tetramer'))
    df1=df1.set_index('Tetramer')
    df = pd.concat([df1,df2])
    df = df.T
    return df

paramValues = pd.read_excel(paramVals, sheet_name='Sheet2', index_col=0)
paramValues = dataCleaning(paramValues)
# print(paramValues.loc[[('TAAC','GTTA')]])
paramValues.to_csv('Tetramer_cleaned.csv')

def calculateParameters(sequence_map_per_seq,paramValues):
    param_map = {'l':[],'m':[],	'n':[],	'o':[],	'p':[],	'q':[]}
    # shift = slide= rise = tilt = roll = twist =0
    sequence_map_per_seq = sequence_map_per_seq[2:-1]
    no_of_bases = len(sequence_map_per_seq)
    list_motifs = []
    for m in range(no_of_bases-3):
        list_motifs.append(sequence_map_per_seq[m:m+4])

    for motif in list_motifs:
        if motif in paramValues.columns:
            # print("found")
            param_map['l'].append(paramValues[motif]['l'])
            param_map['m'].append(paramValues[motif]['m'])
            param_map['n'].append(paramValues[motif]['n'])
            param_map['o'].append(paramValues[motif]['o'])
            param_map['p'].append(paramValues[motif]['p'])
            param_map['q'].append(paramValues[motif]['q'])
        else:
            for j in range(len(paramValues.columns)):
                if motif in paramValues.columns[j]:
                    # print(("found inside"))
                    param_map['l'].append(paramValues[paramValues.columns[j]]['l'])
                    param_map['m'].append(paramValues[paramValues.columns[j]]['m'])
                    param_map['n'].append(paramValues[paramValues.columns[j]]['n'])
                    param_map['o'].append(paramValues[paramValues.columns[j]]['o'])
                    param_map['p'].append(paramValues[paramValues.columns[j]]['p'])
                    param_map['q'].append(paramValues[paramValues.columns[j]]['q'])
    return calculateMovingAverages(param_map)

def calculateMovingAverages(param_map):
    moving_win_size = 25
    moving_param_map = {}
    for k, v in param_map.items():
        arr = v
        moving_param_map[k] = []
        for i in range(0, len(arr) - moving_win_size + 1):
            sum = 0
            for j in range(i, i + moving_win_size):
                sum += arr[j]
            avg = sum / moving_win_size
            moving_param_map[k].append(avg)
    return normalizeMovingAverages(moving_param_map)

def normalizeMovingAverages(moving_param_map):
    normalized_map = {}
    for k in moving_param_map.keys():
        arr = moving_param_map[k]
        # maxArr = max(arr)
        # minArr = min(arr)
        rang = max(arr)-min(arr)
        normalized_map[k] = []
        for i in arr:
            norm_val = (i-min(arr))/rang
            normalized_map[k].append(norm_val)
    return normalized_map

def iterateSequences(sequence_map):
    parameters = {
        'values_map': {},
        'moving_averages_map': {},
        'normalized_params_map': {},
        'combined_params_map': {
            'structuralIncreasing_params': {},
            'structuralDecreasing_params': {}
        }
    }
    for key in sequence_map.keys():
        parameters['normalized_params_map'][key] = calculateParameters(sequence_map[key],paramValues)
        # print(parameters['normalized_params_map'][key]['l'])

    return parameters


#main
sequence_map_tss = readSequenceFile.readSequenceFile(tetramer)
sequence_map_cds = readSequenceFile.readSequenceFile(tetramer_cds)
tetra_seq_map = iterateSequences(sequence_map_tss)
tetra_cds_seq_map = iterateSequences(sequence_map_cds)

#plotting to check if at 500, there is a dip CORRESPONDING TO EACH PARAMETRE(to indicate TSS)

l = [0 for i in range(974)]
m = [0 for i in range(974)]
n = [0 for i in range(974)]
o = [0 for i in range(974)]
p = [0 for i in range(974)]
q = [0 for i in range(974)]

l_cds = [0 for i in range(974)]
m_cds = [0 for i in range(974)]
n_cds = [0 for i in range(974)]
o_cds = [0 for i in range(974)]
p_cds = [0 for i in range(974)]
q_cds = [0 for i in range(974)]


for i in range(len(sequence_map_tss)):
    l = np.add(l,tetra_seq_map['normalized_params_map'][i]['l'])

    m = np.add(m,tetra_seq_map['normalized_params_map'][i]['m'])

    n = np.add(n,tetra_seq_map['normalized_params_map'][i]['n'])

    o = np.add(o,tetra_seq_map['normalized_params_map'][i]['o'])

    p = np.add(p, tetra_seq_map['normalized_params_map'][i]['p'])

    q = np.add(q, tetra_seq_map['normalized_params_map'][i]['q'])

for i in range(len(sequence_map_cds)):
    l_cds = np.add(l_cds,tetra_cds_seq_map['normalized_params_map'][i]['l'])
    m_cds = np.add(m_cds,tetra_cds_seq_map['normalized_params_map'][i]['m'])
    n_cds = np.add(n_cds,tetra_cds_seq_map['normalized_params_map'][i]['n'])
    o_cds = np.add(o_cds,tetra_cds_seq_map['normalized_params_map'][i]['o'])
    p_cds = np.add(p_cds,tetra_cds_seq_map['normalized_params_map'][i]['p'])
    q_cds = np.add(q_cds,tetra_cds_seq_map['normalized_params_map'][i]['q'])

l = [i/len(sequence_map_tss) for i in l]
m = [i/len(sequence_map_tss) for i in m]
n = [i/len(sequence_map_tss) for i in n]
o = [i/len(sequence_map_tss) for i in o]
p = [i/len(sequence_map_tss) for i in p]
q = [i/len(sequence_map_tss) for i in q]

l_cds = [i/len(sequence_map_cds) for i in l_cds]
m_cds = [i/len(sequence_map_cds) for i in m_cds]
n_cds = [i/len(sequence_map_cds) for i in n_cds]
o_cds = [i/len(sequence_map_cds) for i in o_cds]
p_cds = [i/len(sequence_map_cds) for i in p_cds]
q_cds = [i/len(sequence_map_cds) for i in q_cds]

fig, axs = plt.subplots(6)

axs[0].plot(l,label = 'l')
axs[0].plot(l_cds)
axs[1].plot(m,label = 'm')
axs[1].plot(m_cds)
axs[2].plot(n,label = 'n')
axs[2].plot(n_cds)
axs[3].plot(o,label = 'o')
axs[3].plot(o_cds)
axs[4].plot(p,label = 'p')
axs[4].plot(p_cds)
axs[5].plot(q,label = 'q')
axs[5].plot(q_cds)


for i in range(0,6):
    axs[i].legend()
    # axs[i].xticks(np.arange(-500, 500, 100))
    # plt.yticks(np.arange(0, 1, 0.2))
plt.show()

import sys
sys.exit()

