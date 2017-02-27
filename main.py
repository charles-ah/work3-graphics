from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
'''
matrix = new_matrix()

matrix[0][0] = 250
matrix[0][1] = 250
matrix[0][2] = 0
matrix[0][3] = 1

matrix[1][0] = 500
matrix[1][1] = 500
matrix[1][2] = 0
matrix[1][3] = 1
'''

m = []
add_edge(m,250,500,0,500,250,0)
add_edge(m,500,250,0,250,0,0)
add_edge(m,250,0,0,0,250,0)
add_edge(m,0,250,0,250,500,0)

print "creating matrix M: "
print_matrix(m)
print "\n"
draw_lines( m, screen, color )

m = scalar_mult( m, 1.0/10 )

print "Scalar multiplication on M by a factor of 0.1"
print_matrix(m)

print ""

draw_lines( m, screen, color )

matrix_mult(ident(m),m)

print "Identity matrix: "
print_matrix(ident(m))

print "\nMatrix multiplication on M by the identity matrix:"
print_matrix(m)

print ""

s = scalar_mult(ident(m), 4.0)
print "matrix S:"
print_matrix(s)

m = matrix_mult(s,m)
print "Matrix multiplication by matrix s on M:"
print_matrix(m)

draw_lines( m, screen, color )


display(screen)

print "final image is img.png"
