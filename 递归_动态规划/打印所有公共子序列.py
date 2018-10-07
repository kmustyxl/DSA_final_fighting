def printAllSub(String, i,res):
    if i == len(String):
        print(res)
        return
    printAllSub(String, i+1, res)
    printAllSub(String, i+1, res+String[i])
printAllSub('abcd',0,'')