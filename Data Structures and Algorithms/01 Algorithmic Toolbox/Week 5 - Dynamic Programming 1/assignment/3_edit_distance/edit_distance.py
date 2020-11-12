
def edit_distance(s, t, del_cost=1, ins_cost=1, mismatch_cost=1):
    # First row and first col will be correct with this initialization; rest will be revisited:
    mx = [[i + j for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):

            dist_if_del = mx[i-1][j] + del_cost
            dist_if_ins = mx[i][j-1] + ins_cost
            diag_cost = 1 if s[i-1] != t[j-1] else 0
            dist_if_diag = mx[i-1][j-1] + diag_cost

            mx[i][j] = min(dist_if_del, dist_if_ins, dist_if_diag)

    return mx[len(s)][len(t)]  # return the edit distance, not an alignment


if __name__ == "__main__":
    print(edit_distance(input(), input()))
