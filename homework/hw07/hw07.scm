(define (square n) (* n n))

(define (pow base exp)
  (define (helper exp soFar)
    (cond 
      ((= exp 0)
        soFar
      )
      ((= (modulo exp 2) 0)
        (helper (quotient exp 2) (* soFar soFar)) ;square so far
      )
      (else
        (helper (- exp 1) (* soFar base))
      )
    )
  )
  (helper exp 1)
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x ;double parenthesis around the let assignment part
      (let ((y (repeatedly-cube (- n 1) x))) ;let y be the result of the recursion, then we cube it
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (do-a-function-x-times f)
  (define (counter s n) ;s will be the list we are calling cdr on
    (if (= n 0)
      s
      (counter (f s) (- n 1)) ;otherwise we apply the function again
    )
  )
  counter ;return counter
)

(define (cadr s) 
  (car ((do-a-function-x-times cdr) s 1))
)

(define (caddr s) 
  (car ((do-a-function-x-times cdr) s 2))
)
