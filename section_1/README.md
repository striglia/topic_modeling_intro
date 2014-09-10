Section 1: Preparation!
------------------------


Our goal for this section is to:

1. Read in our data from the "sample_data.json.gz" file.
2. Unpack the file's json into python dictionaries.

3. Implement the "clean_biz_data" function
	a. Remove words we don't care about (and, but, etc.)
	b. Clean up text artifacts (we don't care about "\n"!)


All code can be found in this directory. You can invoke the code by running
`python main.py`. The functions you need to implement are in `load.py`. The
comments should point you in the right direction, but if you get stuck feel
free to ask me or a neighbor for help.

You can also look in `hints.txt` to see some suggestions for python modules you
may find useful.

Bonus
----------

If you're already done with this and waiting for the next section, try
modifying main.py to uses Python's argparse library to make a command
line script that can accept any data file instead of hardcoding one. We want to
invoke it like `python main.py --file other_sample_data.json.gz`.

Expert
----------

Try cleaning the input businesses using a python generator so you only clean
the data lazily instead of all at once!
