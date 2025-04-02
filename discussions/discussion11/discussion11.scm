(define (is-mul? exp)
  (and (list? exp) (equal? (car exp) '*))
)

(define (flatten-nested-* expr)
  (if (not (list? expr)) 
    expr
    (let ((expr (map flatten-nested-* expr))) ;calls flatten children and so forth
      (if (is-mul? expr) ;if the first item is mul list
        (apply append (map (lambda (e) (if (is-mul? e) (cdr e) (list e))) expr))
        expr ;map allows us to either skip (* 2 3) (2 3) or get as list 
      ) ;when its subtract, we just return the expression we've built
    ) ;if its mul, and its sub expression is mul, we append
  )
)
;(expect (flatten-nested-* '(* 1 (- 3 (* 4 (- 5 6) (* 7 8))))) (* 1 (- 3 (* 4 (- 5 6) 7 8))) )
; (expect (flatten-nested-* '(* 1 2 (* 3) (* 4) (- 5 0) (* 6 (* 7 8)))) (* 1 2 3 4 (- 5 0) 6 7 8) )
; (expect (flatten-nested-* '(* 1(+ 5 (* 6 (* 7 8)))))   (* 1(+ 5 (* 6 7 8))))
; (expect (flatten-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))))   (* 1 2 3 4 (+ 5 (* 6 7 8))))

; NEW PROBLEM

(define (fact n)
  (if (<= n 1) 1
    (* n (fact (- n 1))))
)

(define (val n)
  (if (<= n 1) 1
    (* n (val (- n 1))))
)

(define original fact)
(define (fact n) 
  (print (list 'fact n) 'entering...)
  (let ((result (original n)))
    (print (list 'fact n) 'returns: (val n))
    result
  )
) 


(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
    (define ,sym1 ,expr1)
    (define ,sym2 ',(eval expr2))
  )
)

;(assign x y (+ 1 1) 3)  ; now x is bound to 2 and y is bound to 3
;(assign x y y x)        ; swap the values of x and y



; we want (cond 
;            ((equal? a ) print 'a)
;          )

(define-macro (switch expr cases)
  `(let ((val ,expr))
  ,(cons
    'cond 
    (map (lambda (case) (cons
            `(equal? val ,(car case))
          (cdr case)))
        cases))))


(switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b))
                      (3 (print 'c))))