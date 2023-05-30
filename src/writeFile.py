def writeResults(path, map):
    tss = ''
    notss = ''
    headers = 'Seq,'
    for i in range(0,1000):
        headers+=str(i)
        headers+=','
    headers +='/n'
    isArr = 0
    tss += headers
    for seq in map.keys():
        tss += str(seq) + ','
        for start in (map[seq]).keys():
            # print(type(map[seq][start]))
            if isinstance(map[seq][start], list):
                isArr = 1
                if (map[seq][start][0] == 1 and map[seq][start][1] == 0):
                    tss+='1'
                else:
                    tss+='0'
            else:
                tss += str(map[seq][start])
                tss+=','
            # tss.join(',')
        tss += '/n'
        # print(tss)
        import sys
        sys.exit()
