def getPCAs(data_arr, equation_map):
    axis_arr = []
    for key in equation_map.keys():
        sum = 0
        for i in range(len(equation_map[key])):
            sum+= data_arr[i]*equation_map[key][i]
        axis_arr.append(sum)
    temp = axis_arr.pop(0)
    axis_arr.append(temp)
    return axis_arr
