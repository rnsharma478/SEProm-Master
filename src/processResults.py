from lib import constants

def predictSequencewiseTss(final_map):
    # for i in range(390,400):
    #     print (final_map[0][i])
    # import sys
    # sys.exit()
    result_map = {}
    for seq in final_map.keys():
        start_arr = (final_map[seq]).keys()
        result_map[seq] = {}
        for i in start_arr:
            tss = 0
            j=i
            while((j<len(start_arr)-5) and j<i+constants.RESULT_ITR_WINDOW):
                if start_arr[j] and final_map[seq][start_arr[j]]:
                    tss += final_map[seq][start_arr[j]]
                j+=1
            if (tss >= constants.RESULT_ITR_WINDOW_THRESH):
                result_map[seq][start_arr[i]] = 1
            else:
                result_map[seq][start_arr[i]] = 0
    # for i in range(390,400):
    #     print (result_map[0][i])
    # import sys
    # sys.exit()
    return result_map

def getTssPositions(result_map):

    map_positions = {}
    for seq in result_map.keys():
        start_arr = (result_map[seq]).keys()
        start_len = len(start_arr)
        # print(start_len)
        map = result_map[seq]
        positions = []
        i = 0
        while(i<len(start_arr)):
            i+=1
            if (map[start_arr[i-1]] == 1 and map[start_arr[i]] == 1):
                start = start_arr[i - 1]
                j=i
                while(map[start_arr[j + 1]] == 1 and j < start_len - 1):
                    j+=1
                stop = start_arr[j]
                if ((stop - start) > constants.IGNORE_TSS_SEQ_THRESH):
                    positions.append(str(start) + ";" + str(stop))
                    i=j
        map_positions[seq] = positions
    # print (map_positions)
    # import sys
    # sys.exit()
    return map_positions