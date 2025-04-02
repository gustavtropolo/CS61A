(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false) ;condition is already a list
)

(define expr (if-program '(= 0 0) '2 '3))

(define (square n) (* n n))

(define (pow-expr base exp)
  (if (= exp 0) 1
    (if (= (modulo exp 2) 0)
      `(square ,(pow-expr base (/ exp 2)))
      `(* ,base ,(pow-expr base (- exp 1)))
    )
  )
)
(pow-expr 2 1)

; (define-macro (repeat n expr)
;   `(repeated-call ,n ___))

; (repeat (+ 2 3) (print 1))
; (begin (print 1) (print 1) (print 1))

(define-macro (repeat n expr) ;takes an expression as it is
  `(repeated-call ,n (lambda () ,expr))) ;even though its a quote, since its a macro, we eval when we're done
;expr is treated as the global symbol expr instead if we don't use quotes

(define (repeated-call n f)
  (if (= n 1)
    (f) ;this should be quoted so we eval all at once
    (begin (f)  (repeated-call (- n 1) f))))
(repeat (+ 3) (print 1))
; (begin (print 1) (print 1) (print 1))