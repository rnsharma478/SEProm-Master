# import src.principalComponentAnalysis as pca
from lib import pcaEquations as pca_equations
from lib import regEquations as reg_equations
import src.logisticRegression as lr
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn import preprocessing
import pandas as pd

MOVING_AVG_WINDOW_SIZE = 25
NO_TSS_WINDOW_LENGTH = 200
MOTIFS_NO_TSS_WINDOW_LENGTH = 200
ITR_WINDOW_SIZE = 100
SKIP_WINDOW = 1 #TODO 8 Previous 25
SKIP_WINDOW_SEQUENCE = 1
SKIP_WINDOW_RANGE = 40

WINDOW_40_PROB = 0.50
WINDOW_80_PROB = 0.50
WINDOW_100_PROB = 0.50
MOTIF_PROB = 0.50

RESULT_ITR_WINDOW = 5
RESULT_ITR_WINDOW_THRESH = 3
IGNORE_TSS_SEQ_THRESH = 35


def iterateSequences(param_map):
    # print("param_map_entire:", param_map.keys())
    final_result = {}
    normalized_map = param_map['normalized_params_map']
    for seq in normalized_map:
        final_result[seq] = iterate(seq,normalized_map)
    # print (final_result[0][155])
    return final_result

def iterate(seq,normalized_map):
    # print("Running PCA_Reg algo on sequence = ",seq)
    params_map = normalized_map[seq]
    params = ['a','b','c','d','e','f','g','h','i','j','k','l','ma','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad','ae']
    # print("all parameters are:",params)
    length = len(params_map[params[0]])
    i = 0
    seq_40_map = {}
    seq_80_map = {}
    seq_100_map = {}

    # arr_check = [i for i in range(0,length-ITR_WINDOW_SIZE-ITR_WINDOW_SIZE-NO_TSS_WINDOW_LENGTH, SKIP_WINDOW)]
    # print(arr_check)
    # import sys
    # sys.exit()
    for i in range(0,length-ITR_WINDOW_SIZE-ITR_WINDOW_SIZE-NO_TSS_WINDOW_LENGTH, SKIP_WINDOW):
        tss_motif_start = i
        tss_motif_stop = tss_motif_start + ITR_WINDOW_SIZE
        no_tss_motif_start = tss_motif_stop + NO_TSS_WINDOW_LENGTH
        no_tss_motif_stop = no_tss_motif_start + ITR_WINDOW_SIZE

        tss_window_40_arr = extractWindowx(tss_motif_stop, params, params_map,40)
        no_tss_window_40_arr = extractWindowx(no_tss_motif_stop, params, params_map,40)

        tss_window_80_arr = extractWindowx(tss_motif_stop, params, params_map,80)
        no_tss_window_80_arr = extractWindowx(no_tss_motif_stop, params, params_map,80)

        tss_window_100_arr = extractWindowx(tss_motif_stop, params, params_map,100)
        no_tss_window_100_arr = extractWindowx(no_tss_motif_stop, params, params_map,100)

        seq_40_map[tss_motif_start] = []
        seq_40_map[tss_motif_start].append(tss_window_40_arr)
        seq_40_map[tss_motif_start].append(no_tss_window_40_arr)

        seq_80_map[tss_motif_start] = []
        seq_80_map[tss_motif_start].append(tss_window_80_arr)
        seq_80_map[tss_motif_start].append(no_tss_window_80_arr)

        seq_100_map[tss_motif_start] = []
        seq_100_map[tss_motif_start].append(tss_window_100_arr)
        seq_100_map[tss_motif_start].append(no_tss_window_100_arr)

    return predictPCA(seq, seq_40_map, seq_80_map, seq_100_map,params)

def extractWindow(start, stop, params, params_map):
    arr = []
    for p in params:
        param_arr = params_map[p]
        sum = 0.0
        length = 0
        itr_undefined = 0
        for i in range(start, stop+1):
            try:
                param_arr[i]
                sum = sum+ param_arr[i]
                length+=1
            except:
                print("index error at", i)
                itr_undefined += 1
        number = round(sum / length,6)
        arr.append(number)
    return arr

def extractWindowx(motif_stop, params, params_map,x):
    start = motif_stop - x
    stop = motif_stop
    return extractWindow(start, stop, params, params_map)

def pca_khud(seq_map,params,ind):
    pca = PCA(5)
    seq_data=pd.DataFrame(columns=[params],index = [i for i in range(len(seq_map.keys()))])

    for bp in seq_map.keys():
        # seq_40_data.loc[bp] = [0 for i in range(31)]
        # for tss_no_tss in range(len(seq_40_map[bp])):
        seq_data.loc[bp] = seq_map[bp][ind]
    # seq_40_data = seq_40_data.div(2)

    # pca.fit(seq_data)
    # print(pca.n_components_)
    # print(pca.components_)
    # seq_pca = pca.transform(seq_data)
    seq_pca = pca.fit_transform(seq_data)


        #WE STILL HAVE TO TRANSFORM THE TEST DATA(THUS WE NEED TRAINING DATA SEPARATELY)

    # print(seq_pca[0])
    # print(seq_pca[0])
    return seq_pca
    # print(pca.explained_variance_ratio_)
    # print(type(seq_40_tss_pca))
    # import sys
    # sys.exit()


def predictPCA(seq, seq_40_map, seq_80_map, seq_100_map,params):
    seq_40_map_tss=pca_khud(seq_40_map,params,0)
    seq_40_map_neg_tss = pca_khud(seq_40_map,params,1)
    ds = [seq_40_map_tss,seq_40_map_neg_tss]
    for k in seq_40_map.keys():
        seq_40_map[k] = list(d[k] for d in ds)
    # print(seq_40_map[0])
    # for start in seq_40_map:
    #     seq_40_map[start][0] = pca.getPCAs(seq_40_map[start][0], pca_equations.window_40)
    #     temp = seq_40_map[start][0].pop(0)
    #     seq_40_map[start][0].append(temp)
    #     seq_40_map[start][1] = pca.getPCAs(seq_40_map[start][1], pca_equations.window_40)
    #     temp = seq_40_map[start][1].pop(0)
    #     seq_40_map[start][1].append(temp)
    # print(seq_40_map[0][0])
    # print(seq_40_map[0][1])

    seq_80_map_tss = pca_khud(seq_80_map, params, 0)
    seq_80_map_neg_tss = pca_khud(seq_80_map, params, 1)
    # print(seq_80_map_tss[0])
    # print(seq_80_map_neg_tss[0])
    ds = [seq_80_map_tss, seq_80_map_neg_tss]
    for k in seq_80_map.keys():
        seq_80_map[k] = list(d[k] for d in ds)
    # for start in seq_80_map:
    #     seq_80_map[start][0] = pca.getPCAs(seq_80_map[start][0], pca_equations.window_80)
    #     temp = seq_80_map[start][0].pop(0)
    #     seq_80_map[start][0].append(temp)
    #     seq_80_map[start][1] = pca.getPCAs(seq_80_map[start][1], pca_equations.window_80)
    #     temp = seq_80_map[start][1].pop(0)
    #     seq_80_map[start][1].append(temp)

    seq_100_map_tss = pca_khud(seq_100_map, params, 0)
    seq_100_map_neg_tss = pca_khud(seq_100_map, params, 1)
    # print(seq_100_map_tss[0])
    # print(seq_100_map_neg_tss[0])
    ds = [seq_100_map_tss, seq_100_map_neg_tss]
    for k in seq_100_map.keys():
        seq_100_map[k] = list(d[k] for d in ds)

    # print(seq_40_map[0],seq_80_map[0],seq_100_map[0])

    # for start in seq_100_map:
    #     seq_100_map[start][0] = pca.getPCAs(seq_100_map[start][0], pca_equations.window_100)
    #     temp = seq_100_map[start][0].pop(0)
    #     seq_100_map[start][0].append(temp)
    #     seq_100_map[start][1] = pca.getPCAs(seq_100_map[start][1], pca_equations.window_100)
    #     temp = seq_100_map[start][1].pop(0)
    #     seq_100_map[start][1].append(temp)
    # logReg(seq_40_map, seq_80_map, seq_100_map)
    return predictRegression(seq, seq_40_map, seq_80_map, seq_100_map)

def logReg(seq_40_map, seq_80_map, seq_100_map):
    print(seq_40_map[0])
    import sys
    sys.exit()

def predictRegression(seq, seq_40_map, seq_80_map, seq_100_map):
    for start in seq_40_map:
        seq_40_map[start][0] = lr.predict(seq_40_map[start][0], reg_equations.window_40, WINDOW_40_PROB)
        seq_40_map[start][1] = lr.predict(seq_40_map[start][1], reg_equations.window_40, WINDOW_40_PROB)

    for start in seq_80_map:
        seq_80_map[start][0] = lr.predict(seq_80_map[start][0], reg_equations.window_80, WINDOW_80_PROB)
        seq_80_map[start][1] = lr.predict(seq_80_map[start][1], reg_equations.window_80, WINDOW_80_PROB)
        # print (seq_80_map[start])
    for start in seq_100_map:
        seq_100_map[start][0] = lr.predict(seq_100_map[start][0], reg_equations.window_100, WINDOW_100_PROB)
        seq_100_map[start][1] = lr.predict(seq_100_map[start][1], reg_equations.window_100, WINDOW_100_PROB)

    for i in range(len(seq_100_map.keys())):
        for j in range(2):
            if seq_100_map[i][j] == 0:
                print((i))

    # print(list(seq_100_map.items())[0:20])
    # import sys
    # sys.exit()

    return processResults(seq, seq_40_map, seq_80_map, seq_100_map)

def processResults(seq, seq_40_map, seq_80_map, seq_100_map):
    combined_result_map = {}
    for start in seq_40_map:
        res_40_tss = seq_40_map[start][0]
        res_40_notss = seq_40_map[start][1]
        res_80_tss = seq_80_map[start][0]
        res_80_notss = seq_80_map[start][1]
        res_100_tss = seq_100_map[start][0]
        res_100_notss = seq_100_map[start][1]
        combined_result_map[start] = []
        sum_res_tss = res_40_tss + res_80_tss \
                      + res_100_tss
        sum_res_notss = res_40_notss + res_80_notss \
                        + res_100_notss
        # if(start == 155):
        #     print (sum_res_notss)
        #     print (sum_res_tss)
        #     import sys
        #     sys.exit()
        combined_result_map[start].append(1 if sum_res_tss >= 2 else 0)
        combined_result_map[start].append(1 if sum_res_notss >= 2 else 0)
    return combined_result_map

