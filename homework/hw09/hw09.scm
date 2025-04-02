(define (curry-cook formals body)
  (if (null? formals)
    body ;return the body when we've considered all formals
    `(lambda (,(car formals))
      ,(curry-cook (cdr formals) body)
    )
  )
)

(define (curry-consume curry args)
  (if (null? args)
    curry
    (curry-consume (curry (car args)) (cdr args))
  )
)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons `(equal? ,(car (cdr switch-expr)) ,(car option)) (cdr option)))
             (car (cdr (cdr switch-expr))))))
;`(switch (+ 1 1) ((1 2) (2 4) (3 6)))
;(car (cdr (cdr switch-expr))) ;is being passed as option
;(1 2) ;is what it would be
;(equals? (cdr switch-expr) (car option))
;(cond ())

;(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))
;map gives you the output of calling the lambda on each of the expr arguments
;we are passing in the next next item 