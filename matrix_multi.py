def multi(m1, m2):
    """ O(n^3) bbz """
    if len(m1[0]) != len(m2):
        return

    ncols = len(m2[0])
    nrows = len(m1)

    new_matrix = []
    for row in m1:
        new_row = []
        for col in range(ncols):
            entry = 0;
            for i,e in enumerate(row):
                entry += e*m2[i][col]
            new_row.append(entry)
        new_matrix.append(new_row)
    return new_matrix
