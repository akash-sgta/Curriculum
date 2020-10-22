import sys
INF = sys.maxsize

def chainMultiplication(vec, size):
    
    cost_matrix = [[0 for _ in range(size)] for __ in range(size)]
    k_matrix = [[0 for _ in range(size)] for __ in range(size)]

    for i in range(1, size):
        cost_matrix[i][i] = 0
    
    for L in range(2, size):
        for i in range(1, size-L+1):

            j = i+L-1
            
            cost_matrix[i][j] = INF
            minimum = (cost_matrix[i][j], i)
            
            for k in range(i, j):
                cost = (cost_matrix[i][k]
                       +cost_matrix[k+1][j]
                       +vec[i-1]*vec[k]*vec[j])
                if cost < minimum[0]:
                    minimum = (cost, k)
            
            cost_matrix[i][j] = minimum[0]
            k_matrix[i][j] = minimum[1]
    
    ans = f'cost : [{cost_matrix[1][-1]}]\n'
    for i in range(1, size):
        for j in range(1, size):
            ans += f'{k_matrix[i][j]}\t'
        ans += '\n'

    return ans

def main():
    vector = (1,2,3,4,3)
    print(chainMultiplication(tuple(vector), len(vector)))

main()
