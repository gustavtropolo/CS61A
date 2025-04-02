from scheme import *
from scheme_reader import *
expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors

print(read_line("((x) (+ x 2))"))
env = create_global_frame()
x = read_line('(define f (lambda (x) (+ x 2)))')
# Pair('define', Pair('f', Pair(Pair('lambda', Pair(Pair('x', nil), Pair(Pair('+', Pair('x', Pair(2, nil))), nil))), nil)))
env = create_global_frame()
# line1 = read_line("(define x 1)")
# scheme_eval(line1, env) # Type SchemeError if you think this errors
# line2 = read_line("(let ((x 5)) (+ x 3))")
# scheme_eval(line2, env)

line1 = read_line("(define x 5)")
scheme_eval(line1, env) # Type SchemeError if you think this errors
line2 = read_line("(define y 'bye)")
scheme_eval(line2, env) # Type SchemeError if you think this errors
line3 = read_line("(let ((a 1) (2 2)) a)")
scheme_eval(line3, env) # Type SchemeError if you think this errors
# (42 50)
line4 = read_line("(let ((x 'hello)) x)")
scheme_eval(line4, env) # Type SchemeError if you think this errors
