'''
面试题：
一个句子的所有单词的首字母大写，其余小写
--------------------------------------------
利用ord函数可以获取字符的ascii码；
利用chr函数可以将ascii码转换成对应字符。

英文字母的大小写对应ascii码差值恒定：diff=ord('a') - ord('A')
'''
def title(s):
    if s is None:
        return
    diff = ord('a') - ord('A')
    res=''    #字符串不支持元素的更新，因此引入辅助字符串变量res
    for i in range(1,len(s)):
        if s[i-1] == ' ' and ord(s[i]) <= ord('z') and ord(s[i]) >= ord('a'):
            res += chr(int(ord(s[i])-diff))
        elif s[i-1] != ' ' and ord(s[i]) <= ord('Z') and ord(s[i]) >= ord('A'):
            res += chr(int(ord(s[i])+diff))
        else:
            res += s[i]
    if ord(s[0]) <= ord('z') and ord(s[0]) >= ord('a'):
        res = chr(int(ord(s[0]) - diff)) + res
    else:
        res = s[0] + res
    return res

if __name__ == '__main__':
    s = 'I loVe pyThOn'
    s = title(s)
    print(s)