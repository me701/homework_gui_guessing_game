# ME 701 - Homework 6

For this homework, you will work individually to build 
a GUI application for the guess-a-number game.  This
game proceeds as follows:

  1. The computer generates a random integer from zero up to 
     but not including 10000, i.e., a four-digit integer.
     Initially, the number is shown to the user as four X's, 
     i.e., `XXXX`.  Here, `X` means the digit is not yet known.

  2. At each turn, the user selects (a) which digit to guess and 
     (b) the value of that digit.  If the guess is right, 
    the appropriate `X` is changed to the number.  For example, 
    if the second digit was guessed correctly to be 3, the 
    displayed number should become `X3XX`.

  3. The user gets 10 (or some possibly definable) turns.  The user
     should be told how many turns remain.  

  4.  If all four digits are guessed in 10 or fewer turns,
     the user wins.


## Deliverables

  - Digitize your GUI layout add to this repository as `layout.png`.

  - Using any tools at your disposal, implement the interface to be as close 
    to your planned layout as possible.

  - Your GUI should be playable by executing `python guess_the_number.py`.

## Bonus

  - +1 if you add in a helper "hint" after each wrong turn.   One
    possibility is to randomly select an unknown digit and same something
    about it.  For example, if the number is 3412 and the user guesses wrong
    and sees 3XX2, you could select the 4 and tell the user the digit is
    even or it's less than 5, etc. 

  - +1 if you can determine what number of turns leads to a user winning
    50% of the time on the average.  This is not a GUI question, but it's 
    an interesting one.  Confirm your result through simulation!
