(define (flatten expr)
  (cond 
    ((null? expr)
      '()
    )
    ((list? (car expr)) ;we want just the elements form expr
      (append (flatten (car expr)) (flatten (cdr expr))) ;append since both are lists
    ) ;flatten will eventually give a num, need to put the second in a list to put together
    (else ;the curr elem is not a list
      (cons (car expr) (flatten (cdr expr)))
    )
  )
)


(define x '(1 (2) 3 ((4))))
(expect (flatten x) (1 2 3 4) )

;cons removes nesting from second term
;append merges lists
;list makes a list out of the items
;quote also makes a list



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
(expect (flatten-nested-* '(* 1 (- 3 (* 4 (- 5 6) (* 7 8))))) (* 1 (- 3 (* 4 (- 5 6) 7 8))) )


; (expect (flatten-nested-* '(* 1 2 (* 3) (* 4) (- 5 0) (* 6 (* 7 8)))) (* 1 2 3 4 (- 5 0) 6 7 8) )
; (expect (flatten-nested-* '(* 1(+ 5 (* 6 (* 7 8)))))   (* 1(+ 5 (* 6 7 8))))
; (expect (flatten-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))))   (* 1 2 3 4 (+ 5 (* 6 7 8))))

(define (remove-nested-* exp parent-is-*)
  (if (null? exp) ;if its not nil, its a list
    '()
    (if (not (list? (car exp))) ;the first element is not a list
      (cons (car exp) (remove-nested-* (cdr exp) parent-is-*))
      (if (is-mul? (car exp)) ; the first item is a list
        (if parent-is-* ;if the parent wasn't star, it now is
          (append (remove-nested-* (cdr (car exp)) parent-is-*) (remove-nested-* (cdr exp) parent-is-*))
          (append (list (remove-nested-* (car exp) #t)) (remove-nested-* (cdr exp) parent-is-*)) ;car exp is a list, but not mul      
        )
        (append (list (remove-nested-* (car exp) #f)) (remove-nested-* (cdr exp) parent-is-*)) ;car exp is a list, but not mul      
      )
    )
  )
)
(expect (flatten-nested-* '(* 1 (- 3 (* 4 (- 5 6) (* 7 8))))) (* 1 (- 3 (* 4 (- 5 6) 7 8))) )
;Expected:
;    (* 1 2 3 4 (+ 5 (* 6 7 8)))  could add logic to ask if the parent was mul
; Received:
;     (* 1 2 3 4 (+ 5 6 7 8))
;(expect (remove-nested-* '(* 1 2 (* 3) (* 4) (- 5 0) (* 6 (* 7 8))) #t) (* 1 2 3 4 (- 5 0) 6 7 8) )
; (* 1 2 3 4 (- 5 0) 6 7 8)
;(expect (remove-nested-* '(* 1(+ 5 (* 6 (* 7 8)))) #t)   (* 1(+ 5 (* 6 7 8))))
;(expect (remove-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))) #t)   (* 1 2 3 4 (+ 5 (* 6 7 8))))
; (* 1 2 3 4 (+ 5 (* 6 7 8)))

(apply append '((1) (2) (3)))
(append '(1) '(2) '(3)) ; <- same as above
;(1 2 3)
;apply append forgets about the outer parenthesis, just calls on all inner