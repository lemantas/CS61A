(define (cube x)
  (* x x x)
)

(define (over-or-under x y)
  (if (< x y)
    -1
    (if (= x y)
      0
      1))
)

(define (make-adder num)
  (lambda (x)
    (+ x num))
)

(define structure
    (cons (cons 1 nil) 
        (cons 2 
            (cons (cons 3 4) 
                  (cons 5 nil))))
)

(define (remove item lst)
    (cond ((null? lst) nil)
          ((equal? (car lst) item) (remove item (cdr lst)))
          (else (cons (car lst) (remove item (cdr lst)))))
)

; ant an implementation of sqrt algorithm just 4 fun :)
(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define (rooty x)
    (define (improve guess)
        (average guess (/ x guess)))
    (define (rooty-iter guess)
        (if (= (square guess) x)
            guess
            (rooty-iter (improve guess))))
    (rooty-iter 1))
