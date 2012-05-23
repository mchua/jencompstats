# I'm trying to learn something.

# import the eXceL ReaDing library
import xlrd

# Open up the proper sheet within the proper excel file.
wb = xlrd.open_workbook('Anredepronomen-data.xls')
sh = wb.sheet_by_name(u'Anredepronomen_im_Alltag')

# Store a list of all the question texts.
questions = sh.row_values(1)

# Find the column number for the question
# with the word "vermieden" in it.
# Note: this is example code, it's not meant
# to be efficient, beautiful, etc. It's meant
# to be very, very easily understandable.
counter = 0
for question in questions:
    if "vermieden" in question:
        correct_counter = counter
    else:
        counter += 1
# At the end of running this block of code,
# correct_counter holds the (single/last)
# column number of the question with the text
# "vermieden" in it.

# Find the column numbers for the questions
# with the word "individuell" in them.
# Note: this overwrites a lot of things
# that the previous code block did.
# Note: again, not meant to be elegant or
# efficient code, but rather meant to be
# easily understandable.

# make a counter and a place to store the column numbers
counter = 0
individuell_question_columns = []

# for each question...
for question in questions:
    # check if the word "individuell" is in it.
    if "individuell" in question:
        # if yes, add it to the list...
        individuell_question_columns += [counter]
        # ...and increment the counter.
        counter += 1
    # otherwise,
    else:      
        # just increment the counter.  
        counter += 1

# show us the list of column numbers for questions
# that have the word "individuell" in them.
# print individuell_question_columns
# print sh.row_values(1)[52]

# now print all the questions with the word
# "individuell" in them, to make sure we got the list
# right.
# for question in individuell_question_columns:
#    print sh.row_values(1)[question]

# which of the questions with "individuell" in them
# have at least one "ihr" response?
# (ihr = 2.0 in the excel spreadsheet)

# make a place to store the answers
individuell_questions_with_ihr = []

# for every question with "individuell" in it
for question in individuell_question_columns:
    print "now checking question #",
    print question
    # for each answer to that question
    for answer in sh.col_values(question):
        # if the answer is "ihr"
        if answer == 2.0:
            print "we have an ihr!"
            # store that question's column number
            individuell_questions_with_ihr += [question]
            # and stop looking at that question.
            break
        # otherwise,
            # we don't give a shit.

# and show us.
print "individuell_questions_with_ihr - ",
print individuell_questions_with_ihr
