# telescope

This program was built using Jupyter Notebook and Python 3.6 to create
software that controls the navigation of a telescope.  It gives
the user constantly updated information about where the telescope is
instantaneously pointing, the user's input coordinates, and target
information.  It is still largely a work in progress, but with
some more work can be used to navigate a telescope.

The coordinates used in the program are hard-coded in on lines 10-11. 

To engage target tracking, set "go" to 1 on line 487.  This will prompt
the user for target coordinates in RA and Dec, which the telescope
will automatically track and print Hour Angle.

