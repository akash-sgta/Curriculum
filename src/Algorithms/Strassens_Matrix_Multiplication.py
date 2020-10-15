def mat_add(mat_a, mat_b, dim):
    temp = [[0]*dim]*dim
    for i in range(dim):
        for j in range(dim):
            temp[i][j] = mat_a[i][j] + mat_b[i][j]
    return temp

def multiply(mat_a, mat_b, ini_a, ini_b, dim):
    if dim <= 2:
        temp = [[0, 0]] * 2
        temp[0][0] = mat_a[0][0]*mat_b[0][0] + mat_a[0][1]*mat_b[1][0]
        temp[0][1] = mat_a[0][0]*mat_b[0][1] + mat_a[0][1]*mat_b[1][1]
        temp[1][0] = mat_a[1][0]*mat_b[0][0] + mat_a[1][1]*mat_b[1][0]
        temp[1][1] = mat_a[1][0]*mat_b[0][1] + mat_a[1][1]*mat_b[1][1]
        return temp
    else:
        mid = dim // 2


if __name__ == "__main__":
    a_dim = int(input("A row col : "))
    a = []
    for i in range(a_dim):
        temp = tuple(input(int, input().split()))
        a.append(temp)

    b_dim = int(input("B row col : "))
    b = []
    for i in range(b_dim):
        temp = tuple(input(int, input().split()))
        b.append(temp)
