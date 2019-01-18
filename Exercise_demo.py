import sys
try:
    A = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        A.append(list(map(int,line.split())))
except:
    pass
print(A)

# try:
#     input_martix = []
#     while True:
#         line = sys.stdin.readline().strip()
#         if line == '':
#             break
#         input_matrix.append(list(map(int, line.split())))
# except:
#     pass
# print(input_martix)