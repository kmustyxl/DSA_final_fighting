def getdp(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    dp = [[0 for i in range(len_string2)] for j in range(len_string1)]
    for i in range(len_string1):
        if string1[i] == string2[0]:
            dp[i][0] = 1
    for j in range(len_string2):
        if string2[i] == string1[0]:
            dp[0][j] = 1
    for i in range(1, len_string1):
        for j in range(1, len_string2):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
    return dp
def lcs(string1, string2):
    '''
    最长公共子串
    :return:
    '''
    if string1 is None or string2 is None:
        return
    string1 = list(string1)
    string2 = list(string2)
    dp = getdp(string1, string2)
    end = 0
    max = 0
    for i in range(len(string1)):
        for j in range(len(string2)):
            if dp[i][j] > max:
                end = i
                max = dp[i][j]
    return ''.join(string1[end-max+1:end+1])
ans = lcs('abcde','abedc')
print(ans)