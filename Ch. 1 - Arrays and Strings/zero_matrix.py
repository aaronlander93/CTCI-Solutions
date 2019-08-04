def zero_matrix(matrix):
    zero_cols = []
    count = 0
    for row in matrix:
        has_zero = False
        count = 0
        
        for column in row:
            if column == 0:
                zero_cols.append(count)
                has_zero = True
                
            count += 1

        if(has_zero):
            for num in row:
                num = 0

         
    if zero_cols:
        for row in matrix:
            for index in zero_cols:
                row[index] = 0
            

matrix = [[1, 2, 1],[3,2,3],[0,1,1]]

zeroed_matrix = zero_matrix(matrix)

for row in matrix:
    print(row)
    print('\n')
