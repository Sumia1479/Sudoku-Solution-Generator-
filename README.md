# Sudoku-Solution-Generator-

Overview: 
Sudoku generator and solver using dokusan library and backtracking algorithm to solve a randomly generated Sudoku board.

Installation:
pip install dokusan

Display Format:

![image](https://user-images.githubusercontent.com/80353305/192398704-39b98eca-2f98-4cb3-9827-d2a431a4c0db.png)

Sudoku Generator:
To generate a new sudoku:

```
from dokusan import generators
sudoku = generators.random_sudoku(avg_rank=150)
```

Ranking and Sudoku difficulty:
avg_rank option roughly defines the difficulty of the sudoku. This program generates a Sudoku board of level 150 (average time to generate is 700ms).


