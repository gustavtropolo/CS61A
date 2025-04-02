;(define (over-or-under num1 num2) (if (< num1 num2) -1 (if (= num1 num2) 0 1)))
(define (over-or-under num1 num2) (cond ((< num1 num2) -1) ((= num1 num2) 0) (else 1)))


;(define (make-adder num) (lambda (x) (+ num x)))
(define (make-adder num) 
  (define (helper x) (+ num x))
  helper) ; returns the last expression in the body

;(define (composed f g) (lambda (x) (f (g x))))
(define (composed f g) (define (helper x) (f (g x))) helper)

(define (repeat f n) ; CANT RETURN A DEFINITION STATEMENT, MUST RETURN THE NAME
  (define (helper x) 
    (define (helper2 x k)
      (if (= k n) 
        x ; be careful to not put too many parenthesis or else it thinks its evaluating something
        (helper2 (f x) (+ k 1)))) ; be sure to apply f to x and not two arguments
    (helper2 x 0) ) ; call helper2 on x and 0
  helper) ; return helper

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))


(define (gcd a b)
  (define (helper x y)
    (if (= y 0)
      x
      (helper y (modulo x y))
    )
  )
  (helper (max a b) (min a b))
)
