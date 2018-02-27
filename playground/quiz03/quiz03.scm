; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  ; List the result of applying f to each element in s.
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  ; List the elements of s for which f returns a true value.
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (no-repeats s)
  (cond ((equal? s nil) nil)
        ;((equal? (filter (lambda (x) (not (equal? (car s))) (cdr s))) nil) nil)
        (else (cons (car s) 
                (no-repeats 
                    (filter 
                        (lambda (x) (not (equal? (car s) x))) 
                        (cdr s)))
                     )
                 )
               )
         )
  )
)

(define (how-many-dots s)
  (cond ((null? s) 0)
        ((and (pair? (car s)) (number? (cdr s)))
            (+ 1 (how-many-dots (car s)))
         )
        ((pair? (car s)) (+ (how-many-dots (car s)) 
                            (how-many-dots (cdr s))
                             ))
        ((number? (cdr s)) 1)
        (else (+ (how-many-dots (cdr s))))
   
   )  
)
