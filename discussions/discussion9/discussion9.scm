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


; New problems
(define (fit total n) ; returns whether there are n DIFFERENT positive perfect squares that add to total
  (define (f total n k)
    (if (and (= total 0) (= n 0))
      #t
      (if (< total (* k k)) ; if total is less than k * k
        #f
        (or 
          (f (- total (* k k)) (- n 1) (+ k 1)) (f total n (+ k 1)) ;include the curr or don't
        )
      )
    )
  )
  (f total n 1) ; run it starting with 1
)

;(expect (fit 10 2) #t)  ; 1*1 + 3*3
;(expect (fit 9 1)  #t)  ; 3*3
;(expect (fit 9 2)  #f)  ;
;(expect (fit 9 3)  #f)  ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
;(expect (fit 25 1)  #t) ; 5*5
;(expect (fit 25 2)  #t) ; 3*3 + 4*4

;problem 2

;(draw (cons 
;  (cons 'a (cons 'b nil))
;  (cons 'c (cons 'd (cons (cons 'e nil) nil))))
;)

;(draw (list (list 'a 'b) 'c 'd (list 'e))  )

;(draw '((a b) c d (e)))

;problem 3

(define (pair-up s)
  (if (<= (length s) 3)
    (list s) ;s itself is a list ;if we are returning a list of lists in rec case, then so too in base case
    ;(cons (list (car s) (car (cdr s))) (pair-up (cdr (cdr s))))
    ;(append (list (list (car s) (car (cdr s)))) (pair-up (cdr (cdr s))))
    ;s is a list
    (append (list (list (car s) (car (cdr s))) (pair-up (cdr (cdr s))))) ;cons will always undo the extra parenthesis
                                                ;((5 6) (7 8)) ; ((7 8)) append on ((5 6)) (7 8)
                                                ; gives (5 6) 7 8
  ) ;cons creates a list, each list call within creates the pairs
)

(expect (pair-up '(5 6 7 8)) ((5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )


(define (shrink k t)
  (lambda (s)
    (if (null? s) t
      ((if (= (car s) k)  (shrink (+ k 1) t)  (shrink k (cons (car s) t)))
        (cdr s)) )))

((shrink 3 nil) '(3 1 4 1 5 9 2 6))


(define-macro (wait expr) `(lambda () ,expr))
(define (double wait-list)
  (if (null? wait-list) nil
    (cons (* 2 (car wait-list)) (wait (double ((cdr wait-list)))))))

(define twos (cons 2 (wait (double twos))))

(car ((cdr ((cdr twos)))))

(define-macro (wait expr) `(lambda () ,expr))
(define (prefix s k) (if (zero? k) nil (cons (car s) (prefix ((cdr s)) (- k 1)))))
(define (add s t) (cons (+ (car s) (car t)) (wait (add ((cdr s)) ((cdr t))))))
(define fib (cons 0 (wait (cons 1 (wait (add fib ((cdr fib))))))))