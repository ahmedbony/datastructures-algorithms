def activityselectionproblem(s, f):
    n = len(f)
    print("Selected Activity are: ")
    i = 0
    print(i)
    for j in range(n):
        if s[j] >= f[i]:
            print(j)
            i=j


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
activityselectionproblem(s, f)