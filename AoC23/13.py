import numpy as np


def parse(puzzle):
    puzzle = puzzle.splitlines()
    mat = np.empty((len(puzzle), len(puzzle[0])), dtype=bool)
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            mat[i, j] = puzzle[i][j] == "#"
    return mat


def check_sym(mat, idx, dim):
    dist = min(idx + 1, mat.shape[dim] - idx - 1)
    ia = np.arange(idx + dist, idx, -1)
    a = np.take(mat, ia, dim)
    ib = np.arange(idx - dist + 1, idx + 1)
    b = np.take(mat, ib, dim)
    return np.all(a == b)

def check_sym_1(mat, idx, dim):
    dist = min(idx + 1, mat.shape[dim] - idx - 1)
    ia = np.arange(idx + dist, idx, -1)
    a = np.take(mat, ia, dim)
    ib = np.arange(idx - dist + 1, idx + 1)
    b = np.take(mat, ib, dim)
    return np.sum(a != b) == 1 


with open("13.input", "r") as fp:
    data = fp.read().strip("\n")

data = data.split("\n\n")
data = [parse(p) for p in data]

def find_sym(d):
    sols = [(-1, -1)]
    possible_row_sym = np.where(~np.any(np.diff(d, axis=0), axis=1))[0]
    possible_col_sym = np.where(~np.any(np.diff(d, axis=1), axis=0))[0]
    for prs in possible_row_sym:
        if check_sym(d, prs, 0):
            sols.append((99, prs))
    for pcs in possible_col_sym:
        if check_sym(d, pcs, 1):
            sols.append((0, pcs))
    return sols

def sol_part1(data):
    sol = 0
    for d in data:
        ss = find_sym(d)[-1]
        sol += (ss[0] + 1) * (ss[1] + 1)
    print(sol)

def sol_part2(data):
    sol = 0
    ssol = []
    for k, d in enumerate(data):
        print(k)
        ssol.append(set())
        for i in range(d.shape[0]):
            for j in range(d.shape[1]):
                d[i, j] = 1 - d[i, j]
                ss = find_sym(d)
                ssol[k] |= set(ss)
                d[i, j] = 1 - d[i, j]

        ssol[k].remove(find_sym(d)[-1])
        assert len(ssol[k]) == 2
        for ss in ssol[k]:
            sol += (ss[0] + 1) * (ss[1] + 1)

        ## TODO: there is a bug here, but should be faster
        # # if sum zero and check false
        # # check if sym is up to one
        # possible_row_sym = np.where(np.sum(np.diff(d, axis=0), axis=1) == 0)[0]
        # possible_col_sym = np.where(np.sum(np.diff(d, axis=1), axis=0) == 0)[0]
        # for prs in possible_row_sym:
        #     if check_sym_1(d, prs, 0):
        #         print("body, row,", prs)
        #         sol += 100 * (prs + 1)
        # for pcs in possible_col_sym:
        #     if check_sym_1(d, pcs, 1):
        #         print("body, col,", pcs)
        #         sol += (pcs + 1)
        # # if sum is one, fix it, the check sym true
        # diff_row = np.diff(d, axis=0)
        # diff_row_sum = np.sum(diff_row, axis=1) == 1
        # possible_row_sym = np.where(diff_row_sum)[0]
        # idx_to_change_row = np.where(diff_row[possible_row_sym, :] == 1)[1]

        # diff_col = np.diff(d, axis=1)
        # diff_col_sum = np.sum(diff_col, axis=0) == 1
        # possible_col_sym = np.where(diff_col_sum)[0]
        # idx_to_change_col = np.where(diff_row[:, possible_col_sym] == 1)[0]

        # print(possible_row_sym, idx_to_change_row)
        # print(possible_col_sym)
        
        # for prs in possible_row_sym:
        #     d2 = np.copy(d)
        #     d2[prs, idx_to_change_row] = 1 - d2[prs, idx_to_change_row]
        #     if check_sym(d2, prs, 0):
        #         print("line, row,", prs)
        #         sol += 100 * (prs + 1)
        # for pcs in possible_col_sym:
        #     d2 = np.copy(d)
        #     d2[idx_to_change_col, pcs] = 1 - d2[idx_to_change_col, pcs]
        #     if check_sym(d2, pcs, 1):
        #         print("line, col,", pcs)
        #         sol += (pcs + 1)

        print("-------")

    print(sol)

sol_part2(data)