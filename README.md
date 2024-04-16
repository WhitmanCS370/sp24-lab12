# sp24-lab12
Materials for week 12 lab in CS-370, which includes Ch. 23 "A File Viewer" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:
* SDX-ch23: The code files for the _SDX Ch. 23_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Sam
* NAVIGATOR: Coden

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 23?
Extreme use of inheritance to create a text editor in the CLI, seperating into viewports, buffers, etc.

* What questions did you have about the material in the chapters? What did you find confusing?
The pattern of inheritance is extremely confusing. The tier system is confusing and which classes are necessary to build others

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
It tries to edit the global/shared version of log. Nothing changes.

* Why doesn’t the `log` function need this statement?
the log funciton doesn't need LOG because it only accesses/prints LOG and doesn't modify it. No alternative LOG that can be used


### Section 2: Windowing
Run
    python3 cursor_const.py 5 logfile
    python3 cursor_const.py 50 logfile

* This version should not crash. But can you see 50 lines of text? Why or why not?
No. The number of displayed lines depends entirely on the size of the window.

### Section 3: Moving
Run 
    python3 move_cursor.py 10 logfile

Verify that there is a cursor that moves along with the arrow keys, 
and you can move the cursor outside the bounds of the displayed text.
If you move the cursor outside the window, the viewer will crash.
Verified!

### Section 4: Refactoring
Run 
    python3 buffer_class.py 10 logfile
and verify that it behaves exactly like the previous version 
- as it should, since it is only a refactoring.

* What are all the classes defined in this version of the file viewer application?
BufferApp extends DispatchApp, which extends MainApp. BufferApp has a Buffer object as well as a Cursor object. 5 in total

* What are the factory methods?
When _setup is called, it builds Window, Buffer, and Cursor, packaging them together as a larger constructor of three objects.

* Why do you think the author paused here to refactor before fixing the 
bugs in the previous version of the code?
It simplifies the code and makes it easier to identify the source of future bugs that isn't due to spaghetti code. It creates a strucutre to easily build the new versions of buffer and viewport without bugs

### Section 5: Clipping
Run
    python3 clip_fixed.py 10 logfile
Verify that the cursor does not move outside the bounds of the text.

* However, there is another bug. What is it? (If necessary, use `CTRL-C` to interrupt the program.)
The keyboard interrupt is being read as a keypress, when we just want the program to halt execution. Instead of trying to process it directly, we could implement a try-except statement to catch an interrupt before processing

* What are all the classes defined in this version of the file viewer application?
ClipCursor (Cursor, Buffer, BufferApp, ClipBuffer) -> ClipCursorFixed
ClipApp -> ClipAppFixed

### Section 6: Viewport
Run
    python3 viewport.py 50 logfile
Verify that you can scroll vertically through the text.
* What are all the classes defined in this version of the file viewer application?
ClipCursor (Cursor, Buffer, BufferApp, ClipBuffer) -> ClipCursorFixed
ClipApp -> ClipAppFixed
(ViewportCursor, ViewportBuffer) -> ViewportApp

* Taking the file viewer application as a whole, do you find the code easy or difficult to read and understand? Why or why not? You might consider Ousterhout's idea of "classitis."
Extremely difficult. The patterns of inheritance are hard to follow. Inheritance is nested. One layer of classes might have requirements multiple layers back, and it's hard to go through each of the classes. Too manh classes!

## Exercise 1: Quitting the application

In the file `dispatch_keys.py`, add a method to the `DispatchApp` class so that once again you can type `q` to quit the application.

## Exercise 2: Horizontal scrolling

Modify the application to scroll horizontally as well as vertically.

Rather than creating yet another version of the app with 
yet more child classes, you can modify the code in `viewport.py`

## Exercise 3: Line numbers

Modify the file viewer to show line numbers on the left side of the text.
The line numbers should not move when scrolling horizontally.
