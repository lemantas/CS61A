(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((or (= a 0) (= b 0)) (max a b))
        ((= (remainder (max a b) (min a b)) 0) (min a b))
        (else (gcd (min a b) (remainder (max a b) (min a b)))))
)

(define (filter f lst)
    (cond ((equal? lst '()) '())
          ((f (car lst)) (cons (car lst) (filter f (cdr lst))))
          (else (filter f (cdr lst))))
)

(define (all-satisfies lst pred)
    (cond ((equal? lst '()) True)
          ((not (pred (car lst))) False)
          (else (all-satisfies (cdr lst) pred)))
)

(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (accumulate combiner start (- n 1) term)
                (term n))
      ))

