# SudokuSolver
Python3 Sudoku solver using the backtracking algorithm. Origninaly an assignment that I moddified to be contained within a class. I also added some other methods.


___
___

# H3 Creating the object
Using default parameters. This reads the unsolved puzzle from <b>input.txt</b>
```python
s = Sudoku()
```

___

Selecting the input file. This reads the unsolved puzzle from <b>~/Desktop/puzzles/0092.txt</b>
```python
s = Sudoku(input_file="~/Desktop/puzzles/0092.txt")
```

___

Turning on HTTP. This will print out a html showing the steps taken when solving the board.
```python
s = Sudoku(serverHTML=1)
```


___
___

# H3 Solving the board
Use the <b>solve()</b> attribute to solve the board. The solved board can be accessed by using the <b>solved_board </b> getter.
```python
#Create the object
s = Sudoku()

#Solve the board
s.solve()

#Access the solved board
solved = s.solved_board
```


___
___

# H3 Serving HTTP content
When creating the attribute, set the <b>serverHTML</b> parameter to 1.
```python
#Create the object
s = Sudoku(serveHTML=1)

#Solve the board
s.solve()
```
This will display a line of numbers.
The first is the row number, the second is column number, the third is the number that was valid at the time it was set.

