(define (ascending? s) 
    (if (<= (length s) 1)
        #t
        (and (<= (car s) (car (cdr s))) (ascending? (cdr s)))
    )
)
 
(define (my-filter pred s) 
    (cond 
        ((null? s) 
            s ;stop when we read null
        )
        ((pred (car s)) 
            (cons (car s) (my-filter pred (cdr s))) ;include curr elem
        )
        (else
            (my-filter pred (cdr s)) ;don't include curr elem
        )
    )
)

(define (interleave lst1 lst2)
    (define (helper l1 l2 0or1)
        (cond
            ((null? l1)
                l2
            )
            ((null? l2)
                l1
            )
            (else
                (if (= 0or1 0)
                    (cons (car l1) (helper (cdr l1) l2 (- 1 0or1))) ;put l1 in front
                    (cons (car l2) (helper l1 (cdr l2) (- 1 0or1))) ;put l2 in front
                )
            )
        )
    )
    (helper lst1 lst2 0)
)

(define (notInS s x)
    (if (null? s)
        #t
        (if (= (car s) x)
            #f ;check the current element
            (notInS (cdr s) x) ;check all of the next elements
        )
    )
)

(define (no-repeats s) 
    (define (helper s soFar) 
        (cond
            ((null? s)
                s ;once we are out of elems, return soFar
            )
            ((notInS soFar (car s))
                (cons (car s) (helper (cdr s) (cons (car s) soFar))) ;if the num hasn't been used, include it
            )
            (else
                (helper (cdr s) soFar) ;don't add anything to soFar
            )
        )
    )
    (helper s nil)
)
