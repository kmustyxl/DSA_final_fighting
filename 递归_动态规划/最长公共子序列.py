def getdp(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    dp = [[0 for i in range(len_string2)] for j in range(len_string1)]
    if string1[0] == string2[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    for i in range(1,len_string1):
        if string1[i] == string2[0]:
            temp_data = 1
        else:
            temp_data = 0
        dp[i][0] = max(dp[i-1][0], temp_data)
    for j in range(1,len_string2):
        if string2[j] == string1[0]:
            temp_data = 1
        else:
            temp_data = 0
        dp[0][j] = max(dp[0][j-1], temp_data)
    for i in range(1,len_string1):
        for j in range(1, len_string2):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if string1[i] == string2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
    return dp
def LCS(string1, string2):
    '''
    最长公共子序列
    :param string1:
    :param string2:
    :return:
    '''
    if string1 is None or string2 is None:
        return
    string1 = list(string1)
    string2 = list(string2)
    dp = getdp(string1, string2)
    m = len(string1) - 1
    n = len(string2) - 1
    res = ['0' for i in range(dp[m][n])]
    index = len(res) - 1
    while index >= 0:
        if n > 0 and dp[m][n] == dp[m][n-1]:
            n-=1
        elif m > 0 and dp[m][n] == dp[m-1][n]:
            m-=1
        else:
            res[index] = string1[m]
            index -= 1
            m -= 1
            n -= 1
    return ''.join(res) #列表转换为字符串
ans = LCS('abcd','bcer')
print(ans)