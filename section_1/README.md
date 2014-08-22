Section 1: Preparation!
------------------------


Our goals for this section is to:

1. Read in our data from the "sample_data.json.gz" file.
2. Unpack the file's json into python dictionaries.

3. Implement the "clean_text" function
	a. Remove words we don't care about (and, but, etc.)
	b. Clean up text artifacts (we don't care about "\n"!)


All code can be found in this directory. Look at the starter methods in
`clean_data.py`. The comments should point you in the right direction, but if
you get stuck feel free to ask me or a neighbor for help.

If you're already done with this and waiting for the next section, try
modifying clean_data.py to uses Python's argparse library to make a command
line script that can accept any data file instead of hardcoding one. We want to
invoke it like `clean_data.py --file sample_data.json.gz`.
