def snail(snail_map):
    output = []
    row_begin = 0
    row_end = len(snail_map)
    col_begin = 0
    col_end = len(snail_map[0])
    
    while row_begin < row_end and col_begin < col_end:
        for i in range(col_begin, col_end):
            output.append(snail_map[row_begin][i]) 
        row_begin += 1
        for j in range(row_begin, row_end):
            output.append(snail_map[j][col_end - 1])
        col_end -= 1
        for k in range(col_end - 1, col_begin - 1, -1):
            output.append(snail_map[row_end - 1][k])
        row_end -= 1
        for l in range(row_end - 1, row_begin - 1, -1):
            output.append(snail_map[l][col_begin])
        col_begin += 1
    return output




