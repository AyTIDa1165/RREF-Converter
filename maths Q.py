r = int(input("rows: "))
c = int(input("columns: "))
matrix = []
for i in range(r):
    L = input().split()
    L = [float(x) for x in L]
    matrix.append(L)

def pivot_finder(matrix):
    L = []
    for i in matrix:
        count = 0
        for j in i:
            if j == 0:
                count += 1
            else:
                break
        L.append(count)
    return L

#rearranging

def rearranged(matrix):
    pivot = pivot_finder(matrix)
    matrix2 = []
    for i in range(len(pivot)):
        for i in range(len(pivot)):
            if pivot[i] == max(pivot):
                matrix2.append(matrix[i])
                pivot[i] = -10000000
                break
    matrix2.reverse()
    return matrix2

def showstop(pivot):
    flag = True
    for i in range(len(pivot) - 1):
        if pivot[i] >= pivot[i+1]:
            if pivot[i+1] != c:
                flag = False
    
    return flag

#REF
while True:
    if showstop(pivot_finder(rearranged(matrix))) == True:
        break
    matrix = rearranged(matrix)
    pivot2 = pivot_finder(matrix)
    for i in range(len(pivot2)-1):
        if pivot2[i] == pivot2[i+1]:
            point = pivot2[i+1]
            ref1 = []
            ref2 = []
            for j in range(len(matrix[i])):
                ref1.append(matrix[i+1][j] * matrix[i][point])
                ref2.append(matrix[i][j] * matrix[i+1][point])
            for j in range(len(ref1)):
                matrix[i+1][j] = ref1[j] - ref2[j]
            break

#converting pivots to 1

pivot2 = pivot_finder(matrix)
for i in range(len(pivot2)):
    point = pivot2[i]
    if point == len(matrix[i]):
        pass
    else:
        my_pivot = matrix[i][point]
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j]/my_pivot


#RREF

for j in range(len(pivot2) - 1):
    i = len(pivot2) - 1 - j
    point = pivot2[i]
    if pivot2[i] == len(matrix[i]):
        pass
    else:
        for k in range(i):
            ref1 = []
            frac = matrix[k][point]
            for l in range(len(matrix[i])):
                ref1.append(matrix[i][l]*frac)
            for l in range(len(matrix[k])):
                matrix[k][l] = matrix[k][l] - ref1[l]

#rounding and -0.0 problem

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = round(matrix[i][j], 4)
        if -matrix[i][j] == 0.0:
            matrix[i][j] = 0.0

print("RREF:")
for i in matrix:
    print(i)

#storing free vars in list

#storing column vectors where every entry is 0
fv_list = []
for j in range(c):
    flag = True
    for i in range(r):
        if matrix[i][j] != 0:
            flag = False
    if flag == True:
        fv_list.append(j)

#storing normal free var columns
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j != pivot2[i] and matrix[i][j] != 0:
            fv_list.append(j)

fv_list = list(set(fv_list))
fv_list.sort()

#parametric form list of vectors

vector_list = []
for j in range(len(fv_list)):
    vector = []
    for i in range(c):
        if len(vector) == fv_list[j]:
            vector.append(1)
        elif i in fv_list:
            vector.append(0.0)
        else:
            try:
                for k in range(len(matrix)):
                    if i == pivot2[k]:
                        if matrix[k][fv_list[j]] == 0.0:
                            vector.append(matrix[k][fv_list[j]])
                        else:
                            vector.append(-1*matrix[k][fv_list[j]])
                        break
            except:
                vector.append(0.0)
    vector_list.append(vector)

#final paramtric form

ans = ''
for i in range(len(fv_list)):
    ans += ' + x' + str(fv_list[i]) + str(vector_list[i])
start = [0]*(c)
print("Solution in parametric form:")
print(str(start) + ans)