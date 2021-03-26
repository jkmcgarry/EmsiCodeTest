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

If I were to make more adjustments to it in the future, I would probably add a means to display the
lines that were within a specified degree of accuracy. For example, if 5 words were input and all but 1 word was
on a line, then the program would display that line because it was very close to matching 100%.

Examples of output from a single run:
Enter the words you remember: his head a flag
Found words on:  1  lines.
Holding his head up for a flag of all the free. at line:  32

Example using cases:
Enter the words you remember: Don John
Found words on:  20  line(s).
Don John of Austria is going to the war, at line:  25
Don John laughing in the brave beard curled, at line:  30
Don John of Austria at line:  35
(Don John of Austria is going to the war.) at line:  39
(Don John of Austria is going to the war.) at line:  72
Don John of Austria at line:  75
(Don John of Austria is girt and going forth.) at line:  79
But Don John of Austria is riding to the sea. at line:  89
Don John calling through the blast and the eclipse at line:  90
Don John of Austria at line:  94
(Don John of Austria is armed upon the deck.) at line:  98
But Don John of Austria has fired upon the Turk. at line:  106
Don John’s hunting, and his hounds have bayed— at line:  107
Don John of Austria at line:  111
(Don John of Austria is hidden in the smoke.) at line:  115
(But Don John of Austria has burst the battle-line!) at line:  133
Don John pounding from the slaughter-painted poop, at line:  134
Don John of Austria at line:  142
(Don John of Austria rides homeward with a wreath.) at line:  146
(But Don John of Austria rides home from the Crusade.) at line:  150
