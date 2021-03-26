# EmsiCodeTest
Code project for Interview process at EMSI

The program was written in Python version 3.9 on Windows 10
I lacked the means to run it in debian buster and I was unable to use Docker because
it required owning or upgrading to Windows 10 Pro, and I only have the Home edition.

The program can be run by opening a powershell window in the location of the files using the command
py -i EmsiTestFinal.py

The prompt: "Enter the words you remember: " will appear and simply type any words separated with a space
The program will then attempt to find a line within the poem that contains all the words typed.
If a match is found, the results will be displayed for each line that all the words were found on a line
If not all words were found, then no results will be displayed.

When searching the poem, both files must be within the same directory in order to work.
The search for words is able to identify the word regardless of case either within the poem,
or from the input of the user, and can also distinguish a word if punctuation is attached to it.
