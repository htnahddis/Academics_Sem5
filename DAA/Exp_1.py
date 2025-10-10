def amortized_analysis_table(n):
    size = 1  
    used = 0  

    i_row = []
    size_row = []
    cost_row = []

    for i in range(1, n + 1):
        i_row.append(i)
        if used == size:
            size *= 2
            cost = used + 1  
        else:
            cost = 1 
        used += 1
        size_row.append(size)
        cost_row.append(cost)

    print("i      :", ' '.join(f"{i:4}" for i in i_row))
    print("size   :", ' '.join(f"{s:4}" for s in size_row))
    print("cost   :", ' '.join(f"{c:4}" for c in cost_row))

amortized_analysis_table(20)