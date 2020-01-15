#!/bin/sh
#!/bin/sh

./lis.py <<'EOF' 
(defparameter one 1)
(defparameter two 2)
(defparameter six 6)
(defparameter ten 10)
(defparameter thirty 30)
(defparameter list1 '(1 2 3 4 5 6))
(defparameter list2 '(a b c d e f g))
(let ((a 7) (b 9)) (+ 4 (+ a (+ six b))))
(let ((a (+ 4 six)) (b (+ 9 two))) (+ 4 (+ a (+ six b))))
(flet ((f (n) (+ n ten)) (g (n) (- n 3))) (g (f 5)))
(flet ((f (n) (+ n ten))) (f (+ two 3)))
(defun addr (a b) (+ a b)) (addr 3 5) (addr 27 thirty)
(+ 4 5)
(append list1 list2)
(car (reverse (append list1 list2)))
(cdr (reverse (append list1 list2)))
(last (reverse (append list1 list2)))
(cons thirty list1)
(list thirty list1)
list1
(flet ((factorial (n) (if (= n 1) 1 (* n (factorial (- n 1)))))) (factorial 6))
(flet ((fibonacci (n) (if (= n 0) 0 (if (= n 1) 1 (+ (fibonacci (- n 1)) (fibonacci (- n 2))))))) (fibonacci 10))
EOF

