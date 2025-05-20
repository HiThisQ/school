n = [[1, 2], [2, 3], [0, 1], [1]]
navstiven = [False] * len(n)
def travers_dfs(v, n):
    navstiven[v] = True
    print("v: ", v, "u: ", n[v])
    for u in n[v]:
        if not navstiven[u]:
            travers_dfs(v,n)
travers_dfs(0, n)


