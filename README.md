# ME 701 - Homework 6

For this homework, you will work individually to complete the GUI developed
in class.  Your job is to create a *function evaluator* that has the
following features:

  - Three editable text boxes.   The first is for input of `x` values,
    the second is for the input of a function (e.g., `np.sin` and
    `lambda x: x**3`).  The final box, when return is pressed, is updated
    to show the numerical value of the function given the values of `x`.
 -  Ensure that `x` can be a single number, a sequence of numbers,
    or a NumPy expression.  In other words, the following should all be
    valid values in your first box:
      * `1.23`
      * `0, 1, 2, 3`
      * `np.linspace(0, 1, 4)`
  - Add a `save as` feature that
    saves the `x` and `f(x)` data to file as two columns.
  - (BONUS) use Matplotlib to embed a plot in your GUI that plots
    $f(x)$ versus $x$ every time the output is calculated.


An example (including the embedded plot) is shown below:

<img src="screenshot.png" alt="example gui"
    	title="Example GUI" width="400" height="400" />
