import re
##program takes the contents of the txt. file and
##puts it into a list of lists for each line

##user enters words they remember and the program checks each line for
##matches
##if a word matches, then it goes and checks the next word the user had put in
##for a match

linesFound = []
lineNumber = []
word_list = []
count = 0

file = open('lepanto.txt', encoding="utf8")
for line in file: ##go through line by line and make each line a list of words within the list per line
    stripped_line = line.strip()
    line_list = stripped_line.split()
    word_list.append(line_list)
file.close()

value = str(input("Enter the words you remember: "))
userList = value.split()
userList = [x.lower() for x in userList] ##used to remove cases from user input

def listtoString(s): ##function to convert a list into a string
    str1 = " "
    return str1.join(s)

for i in range(len(word_list)):
    currentLine = listtoString(word_list[i]) ##variable initialized to current line of poem being read and made into a string
    otherLine = re.sub(r'[^\w\s]', '', currentLine) ##string variable assigned to currentLine with punctuation removed
    for j in range(len(userList)):
        if(userList[j] in otherLine.lower() or userList[j] in word_list[i]): ##increments counter if a word is found in either the raw list
            count += 1                                                       ##or in the string 
        if j == len(userList)-1:##
            if count == len(userList): ##appends contents of line that has all the words the user entered to a list
                linesFound.append(word_list[i])
                lineNumber.append(i+1) ##appends the number of the line the word was found on, using +1 since the list starts at 0
            count = 0 ##reset counter when at last word to search
        else: ##continues if current word is not in list
            continue
        
print("Found words on: ", len(lineNumber), " line(s).")
for k in lineNumber: ##prints out each line all words user entered were found on
    foundLine = listtoString(word_list[k-1])
    print(foundLine, "at line: ", k)
