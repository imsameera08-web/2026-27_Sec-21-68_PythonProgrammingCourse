rows=3
for row_loop_var in range(1, rows  + 1):
    for col_loop_var_space in range(1, rows - row_loop_var + 1):
        print(" ",end=" ")
    for col_loop_var_dot in range(1,2 * row_loop_var):
        print("*",end=" ")
    print()        