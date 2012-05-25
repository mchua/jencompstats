# Demo file for doing word frequency counts on qualitative answers

# import the eXceL ReaDing library
import xlrd

# Open up the proper sheet within the proper excel file.
wb = xlrd.open_workbook('Anredepronomen-data.xls')
sh = wb.sheet_by_name(u'Anredepronomen_im_Alltag')

# grab all the responses for Q56
# note that Q56 is column 129, and Q57 is column 130.
q56_responses = sh.col_values(129)

# put all the responses for Q56 into a string called 'words'
# this code is magic; do not question it (yet).
words = ''.join([unicode(item) for item in q56_responses])

# allow us to use the defaultdict function.
# what defaultdict does isn't really important for our purposes now.
from collections import defaultdict

# count the words...
# this code is sort of magic, until you learn dictionaries.
# once you do, you'll be able to understand it.
wordcount = defaultdict(int)
for word in words.split():
    wordcount[word] += 1

# sort the words by frequency of count
# this code is magic; do not question it.
sorted_wordcount = sorted(wordcount.items(), key=lambda item: item[1])

# and print them prettily.
for item in sorted_wordcount:
    print item
