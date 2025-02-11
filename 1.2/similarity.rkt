#lang racket

(define (parseline lines l r)
  (if (empty? lines)
      (list l r)
      (let ([line (first lines)])
        (let ([numpair (string-split line)])
          (parseline
           (drop lines 1)
           (append l (list (string->number (car numpair))))
           (append r (list (string->number (car (cdr numpair))))))))))

(define numlist (parseline (file->lines "input.txt") '() '()))

(apply +  
       (map (λ (num)
              (* num 
                 (length (filter (λ (rnum) 
                                   (equal? num rnum))
                                 (car (cdr numlist))))))
            (car numlist)))