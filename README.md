# EmsiCodeTest
Code project for Interview process at EMSI

The program was written in Python version 3.9 on Windows 10.
No other libraries not already built into python were used.
I lacked the means to run it in Debian Buster and I was unable to use Docker because
it required owning or upgrading to Windows 10 Pro, and I only have the Home edition.
Therefore, I decided that I would code the program in the envirnoment that I would be able to finish it in
and ensure that it runs properly.

The program can be run by opening a powershell window in the location of the files using the command
py -i EmsiTestFinal.py.

The prompt: "Enter the words you remember: " will appear and simply type any words separated with a space,
no quotes are required. Using the example from the prompt: the input would look like: his head a flag
The program will then attempt to find a line within the poem that contains all the words typed.
If a match is found, the results will be displayed for each line that all the words were found on a line
If not all words were found, then no results will be displayed. The program must be run again in order
to input a new set of words.

When searching the poem, both files must be within the same directory in order to work.
The search for words is able to identify the word regardless of case either within the poem,
or from the input of the user, and can also distinguish a word if punctuation is attached to it.
In order to account for the potential of words from other lines mixing together, the program has
an added functionality to also display near matches if 75% or more of the words entered were found on a line.
