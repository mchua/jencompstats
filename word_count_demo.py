# allow us to use the defaultdict function.
# what defaultdict does isn't really important for our purposes now.
from collections import defaultdict

# open the text file we want to read from
inputfile = open('Social Meanings of Sie.txt', 'r')

# read the entire file into a string
words = inputfile.read()

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
