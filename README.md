# COMP5361-propositional-logic

**COMP 5361 Discrete Structures and Formal Languages**

1. Write a Python program that takes as input a truth assignment A for propositional variables P = {P 1, P 2, . . . , P n} and a propositional sentence S involving these variables, and produces output True or False, depending on whether the given assignment A satisfies the sentence S or not. To show that your program works, run your program on the following input: ((P1∧P2)∨(P3∧True))∨((¬P1∧¬P3)∧P2).

Note that your program should work for any n ≥ 1, and other inputs also will be given as tests.

2. Write a Python program that takes input P and S as in Question 1, generates the truth table for S, and outputs Tautology, Contingency, or Contradiction, depending on which category S falls into. To show that your program works, run your program on the following inputs:

     (a) (¬P1∧(P1∨P2))→P2

     (b) P2∧(P1→¬P2)∧(¬P1→¬P2)

     (c) (P1→(P2→P3))→((P1→P2)→P3)
