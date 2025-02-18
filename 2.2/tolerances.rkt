#lang racket

(define (reportOk? report [tolerance 1] [prev null]) 
  (cond 
    [(= 1 (length report)) #t]
    [else 
      (let ([diff (apply - (take report 2))])
        (let ([diffOk (and (> diff 0) (< diff 4))])
          (cond 
            [(and (not diffOk) (> tolerance 0)) 
              (or 
                (if (null? prev)
                  ; first item in the original list, just drop it
                  (reportOk? (drop report 1) (- tolerance 1))
                  ; any other item in the list, drop it and slot the previous in
                  (reportOk? (append (list prev) (drop report 1)) (- tolerance 1)))
                ; or, try dropping the second item in the list
                (reportOk? (append (list (first report)) (drop report 2)) (- tolerance 1)))]
            [diffOk (reportOk? (drop report 1) tolerance (first report))]
            [else #f])))]))

(length 
  (filter 
    (λ (report) 
      (let ([reportList (map string->number (string-split report))])
        (or 
          (reportOk? (reverse reportList))
          (reportOk? reportList)))
      )
    (file->lines "input.txt")))