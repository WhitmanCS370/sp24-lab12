# sp24-lab12
Materials for week 12 lab in CS-370, which includes Ch. 23 "A File Viewer" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:
* SDX-ch23: The code files for the _SDX Ch. 23_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Terence and Rhys

## Team Roles for Part 1
Who will start out as
* DRIVER: Terence 
* NAVIGATOR: Rhys

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 23?
- Building a Filer viewer. Testing functionality using synthetic data and complications of presentation of data and screen. 
* What questions did you have about the material in the chapters? What did you find confusing?
- We found the use of classes in this chapter confusing. There were too many classes and some were unnecessary. It was hard to follow because there was no visualization of the actual program and how it would look like. 

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
- running python3 show_lines.py 5 logfile does not change when using global LOG or not, but if we run it with python3 logging_curses.py logfile does change. show_lines will not long anything, but logging_curses logs keystrokes if we have global LOG. Without it, the window records keystrokes in the window (and diagonally) because the global LOG is referencing the global variabkle (defined above) and overriding it. Without this, LOG will lose the local instance and will not record the keystrokes. We think because file=None by default, this might just print to the window. 

However, we do not know why this prints at an angle though. main calls log(repr(key)), which is a printable representation of the keystroke. Our best guess is; each keystroke is being written as if it was on the same line, but print() is printing a new line after every input. However, if this was true, adding end='' in the print statement should put it on one line, but it does not. It does print in the terminal (on one line), but not the window.

* Why doesn’t the `log` function need this statement?
Because LOG is a global variable, and log is not changing it. It can access it, but does not need to save any changes.s

### Section 2: Windowing
Run
    python3 cursor_const.py 5 logfile
    python3 cursor_const.py 50 logfile

* This version should not crash. But can you see 50 lines of text? Why or why not?
This will not crash, but it will not show all of the lines because we cannot scroll.

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
You scroll up/down/left/right but if you scroll to the bottom, it will crash. This is not the case for scrolling paast the top.
* What are all the classes defined in this version of the file viewer application?

### Section 6: Viewport
Run
    python3 viewport.py 50 logfile
Verify that you can scroll vertically through the text.
* What are all the classes defined in this version of the file viewer application?
* Taking the file viewer application as a whole, do you find the code easy or difficult to read and understand? Why or why not? You might consider Ousterhout's idea of "classitis."

## Exercise 1: Quitting the application

In the file `dispatch_keys.py`, add a method to the `DispatchApp` class so that once again you can type `q` to quit the application.

we added q to:

TRANSLATE = {
    "\x18": "CONTROL_X",
    "q": "CONTROL_X"
}

This records the q keystroke and quits the program.

## Exercise 2: Horizontal scrolling

Modify the application to scroll horizontally as well as vertically.

Rather than creating yet another version of the app with 
yet more child classes, you can modify the code in `viewport.py`

## Exercise 3: Line numbers

Modify the file viewer to show line numbers on the left side of the text.
The line numbers should not move when scrolling horizontally.
