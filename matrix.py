import math


def print_matrix( matrix ):
    
    for i in range(len(matrix[0])):
        s = ""
        for j in range(len(matrix)):
            s += str(matrix[j][i]) + "\t"
        print s 

def ident( matrix ):
    m = []
    cols = len(matrix)
    rows = len(matrix[0])
    for c in range( cols ):
        m.append([])
        for r in range( rows ):
            if c == r:
                m[c].append(1)
            else:
                m[c].append(0)
    return m

def scalar_mult( matrix, s ):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j] * s)
    return matrix


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = []

    for i in range(len(m2)):
        m.append([])
        for j in range(4):
            n = m1[0][j]*m2[i][0] + m1[1][j]*m2[i][1] + m1[2][j]*m2[i][2] + m1[3][j]*m2[i][3]
            m[i].append(n)
    
    return m



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
