def HanoiTower(n,A,B,help):
    if n == 1:
        print('1' + A + '->' + B)
        return
    else:
        HanoiTower(n-1, A, help, B)
        print(str(n) + A + '->' + B)
        HanoiTower(n-1, help, B, A)
#HanoiTower(3,'A','B','HELP')