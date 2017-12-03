def DP_MinimumEditDistance(string1, string2):
    D = [[1 for x in range(len(string2))] for y in range(len(string1))]
    D[0][0]=0
    for i in range(1, len(string1)):
        for j in range(1,len(string2)):
            if string1[i]==string2[j]:
                D[i][j]= D[i-1][j-1]
            else:
                D[i][j]= min(D[i-1][j-1], min(D[i-1][j], D[i][j-1]))+1

    for i in range(len(string2)):
        print(D[i])
