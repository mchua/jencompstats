# Create an Excel workbook.
book = xlwt.Workbook(encoding="utf-8")

# Add a sheet to that workbook called "2012."
sheet2012 = book.add_sheet("2012") 

# Add another sheet to that workbook called "2008."
sheet2008 = book.add_sheet("2008") 

# Put the data in the cells.
# Let's start with headers for 2012 first.
sheet2012.write(0, 0, "Gender")
sheet2012.write(0, 1, "Age")
sheet2012.write(0, 2, "Region")

# These will be the same headers as for 2008.
sheet2008.write(0, 0, "Gender")
sheet2008.write(0, 1, "Age")
sheet2008.write(0, 2, "Region")

# Hey, this looks repetitive!
# Just for kicks, let's define a function for later use.
# This will let us simply call the function to write all the headers we need.
# For instance: write_headers(sheet2008)
def write_headers(sheet):
    sheet.write(0, 0, "Gender")
    sheet.write(0, 1, "Age")
    sheet.write(0, 2, "Region")

# Now let's put the data in...
# Here's the first person in the 2012 sheet.
# Notice how the numbers are written as strings here.
# We could also not convert them to strings --
# sheet2012.write(1, 0, 1)
# would be as valid as the line of code below.
sheet2012.write(1, 0, "1")
sheet2012.write(1, 1, "3")
sheet2012.write(1, 2, "Kassel")

# And here's the second person in the 2012 sheet.
# Here we see an example of the function that converts an int to a string.
sheet2012.write(2, 0, str(2))
sheet2012.write(2, 1, str(4))
sheet2012.write(2, 2, "Stuttgart")

# Here's the first person in the 2008 sheet.
# We're going to have this person's data stored in variables...
person1_2008_gender = 1
person1_2008_age = 2
person1_2008_region = "Wien"
sheet2008.write(1, 0, person1_2008_gender)
sheet2008.write(1, 1, person1_2008_age)
sheet2008.write(1, 2, person1_2008_region)

# By the way -- we can write equations, too!
sheet2008.write(1, 3, "=A2+A3")

# Finally, we'll use info from a simple data structure (a list)
# Imagine that we already have this information from somewhere.
person2_2008 = [1, 2, "Freiburg"]
# Now write it in as the second person in the 2008 worksheet.
sheet2008.write(2, 0, person2_2008[0])
sheet2008.write(2, 1, person2_2008[1])
sheet2008.write(2, 2, person2_2008[2])

# And save the worksheet...
# TODO: Change the path (file save location) here to the appropriate one.
book.save("pronouns-spreadsheet.xls")
