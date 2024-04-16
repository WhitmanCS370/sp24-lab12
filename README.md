# sp24-lab12

Materials for week 12 lab in CS-370, which includes Ch. 23 "A File Viewer" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:

- SDX-ch23: The code files for the _SDX Ch. 23_ activity (as downloaded directly from the book website, unmodified)

## Team Members for Part 1

Fabian Jacob

## Team Roles for Part 1

Who will start out as

- DRIVER: Driver's name
- NAVIGATOR: Navigator's name

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

- What were the main ideas from SDX chapter 23?
  Creating files, LOG file, Inheritance, Refactoring
- What questions did you have about the material in the chapters? What did you find confusing?
  Structure of the code was a bit confusing. The way the inheritance is implemented is also hard to follow.

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
The program crashes even when we increase the number of lines to 10 as the screen is shorter than the generated output.
Then increasing the number of lines to 50 and verify the program crashes as described.

- Why does `open_log` need the line `global LOG`? What happens if it is removed?
  Nothing changes. We are trying to edit the global version of LOG not the local.
- Why doesn’t the `log` function need this statement?
  We are not changing the LOG file.

### Section 2: Windowing

Run
python3 cursor_const.py 5 logfile
python3 cursor_const.py 50 logfile

- This version should not crash. But can you see 50 lines of text? Why or why not?
  No because we cannot scroll down to see the rest of the lines.

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
  Buffer, BufferApp
* What are the factory methods?
  \_make_window, \_make_cursor, \_make_buffer
* Why do you think the author paused here to refactor before fixing the
  bugs in the previous version of the code?
  The bugs from the previous versions are still present as we are importing classes from them.

### Section 5: Clipping

Run
python3 clip_fixed.py 10 logfile
Verify that the cursor does not move outside the bounds of the text.

- However, there is another bug. What is it? (If necessary, use `CTRL-C` to interrupt the program.)
  In total 3 bugs: q does not quit the program. If the screen is smaller than the input, you can scroll off the screen which causes it to crash. When a longer input is generated, once we enlarge the screen, the rest of the lines will never show up.
- What are all the classes defined in this version of the file viewer application?
  ClipCursorFixed, ClipAppCursor

### Section 6: Viewport

Run
python3 viewport.py 50 logfile
Verify that you can scroll vertically through the text.

- What are all the classes defined in this version of the file viewer application?
  ViewportCursor, ViewportBuffer, ViewportApp
- Taking the file viewer application as a whole, do you find the code easy or difficult to read and understand? Why or why not? You might consider Ousterhout's idea of "classitis."
  The concepts are easy to understand, but the way it uses inheritance to fix bugs overcomplicates it.

## Exercise 1: Quitting the application

In the file `dispatch_keys.py`, add a method to the `DispatchApp` class so that once again you can type `q` to quit the application.

## Exercise 2: Horizontal scrolling

Modify the application to scroll horizontally as well as vertically.

Rather than creating yet another version of the app with
yet more child classes, you can modify the code in `viewport.py`

## Exercise 3: Line numbers

Modify the file viewer to show line numbers on the left side of the text.
The line numbers should not move when scrolling horizontally.
