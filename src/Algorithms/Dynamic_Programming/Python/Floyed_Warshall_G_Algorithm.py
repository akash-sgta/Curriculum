import sys
MAXINT = sys.maxsize

def floydWarshal(graph):

    vertex = len(graph)
    distance = graph

    for k in range(vertex):
        for i in range(vertex):
            for j in range(vertex):
                distance[i][j] = min(distance[i][j],
                                distance[i][k]+distance[k][j]) 
    
    ans = ''
    for i in range(vertex):
        for j in range(vertex):
            if distance[i][j] == MAXINT:
                ans += '[INF]\t'
            else:
                ans += f'[{distance[i][j]}]\t'
            if j == vertex - 1:
                ans += '\n'
    
    return ans

def main():
    graph = ([0, 5, MAXINT, 10],
              [MAXINT, 0, 3, MAXINT],
              [MAXINT, MAXINT, 0, 1],
              [MAXINT, MAXINT, MAXINT, 0])
    
    print(floydWarshal(graph))

main()