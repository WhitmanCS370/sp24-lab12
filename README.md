# sp24-lab12
Materials for week 12 lab in CS-370, which includes Ch. 23 "A File Viewer" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:
* SDX-ch23: The code files for the _SDX Ch. 23_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Aidan VB, Steven L and Grant D

## Team Roles for Part 1
Who will start out as
* DRIVER: Grant
* NAVIGATOR: Aidan, Steven

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 23?

Using the curses module, logging info such as keystrokes and how logging works on different levels, delayed construction and why that can be helpful (could be costly to initialize something that isn't used and is helpful to know how it will be used before initializing)

Lastly, how to combine the concepts to make a robust file viewer


* What questions did you have about the material in the chapters? What did you find confusing?

We were confused at first about delayed construction but read more about it and understand its merits now._ 

## Exercise 0: Run the code

Let's start by running the 6 final versions of the code from 
the conclusions of sections 1, 2, 3, 4, 5, and 6.

As you go along, review the code you are running and address the questions 
in the exercises.

### Section 1: Curses
Run
    python3 show_lines.py 5 logfile

Verify that you see white text on a black screen. 
Typing `q` should quit the program.

Try increasing the number of lines to 10 and verify you see ten lines of text.

Then increasing the number of lines to 50 and verify the program crashes as described.

* Why does `open_log` need the line `global LOG`? What happens if it is removed?
To ensure it is accessible outside of the open_log function. And each time the function is called we're using the global variable, not creating more local variables
* Why doesn’t the `log` function need this statement?
When the log function is called there should already be a log opened and accessible in the global variable log.

### Section 2: Windowing
Run
    python3 cursor_const.py 5 logfile
    q

* This version should not crash. But can you see 50 lines of text? Why or why not?
We can not move down in the window to see the rest.

### Section 3: Moving
Run 
    python3 move_cursor.py 10 logfile

Verify that there is a cursor that moves along with the arrow keys, 
and you can move the cursor outside the bounds of the displayed text.
If you move the cursor outside the window, the viewer will crash.

### Section 4: Refactoring
Run 
    python3 buffer_class.py 10 logfile
and verify that it behaves exactly like the previous version 
- as it should, since it is only a refactoring. 

* What are all the classes defined in this version of the file viewer application?
* What are the factory methods?
* Why do you think the author paused here to refactor before fixing the 
bugs in the previous version of the code?

### Section 5: Clipping
Run
    python3 clip_fixed.py 10 logfile
Verify that the cursor does not move outside the bounds of the text.

* However, there is another bug. What is it? (If necessary, use `CTRL-C` to interrupt the program.)
* What are all the classes defined in this version of the file viewer application?

### Section 6: Viewport
Run
    python3 viewport.py 50 logfile
Verify that you can scroll vertically through the text.q
* What are all the classes defined in this version of the file viewer application?
* Taking the file viewer application as a whole, do you find the code easy or difficult to read and understand? Why or why not? You might consider Ousterhout's idea of "classitis."

## Exercise 1: Quitting the application

In the file `dispatch_keys.py`, add a method to the `DispatchApp` class so that once again you can type `q` to quit the application.

## Exercise 2: Horizontal scrolling

Modify the application to scroll horizontally as well as vertically.

Program seems to crash when reaching right limit of screen.
Possible solution: make extra variable for keeping track of screen and cursor's horizontal position,
make the text exceeding screen size not display, and dynamically shift display based on scrolling and screen size

Rather than creating yet another version of the app with 
yet more child classes, you can modify the code in `viewport.py`

## Exercise 3: Line numbers

Modify the file viewer to show line numbers on the left side of the text.
The line numbers should not move when scrolling horizontally.
