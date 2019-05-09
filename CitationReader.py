'''
Created on Sep 19, 2018

The program must read a citation of a book, magazine article or a journal article in the APA
style and output
- the category (book, magazine article or a journal article) of the referenced item
- a list of source components, separated by field 

@author: lufei Guan
'''

reference = input ('Please enter a reference\n').strip()

#figure out the first 3 field: authors, year, and title
#authors
authorsPartEndPos = reference.find("(")
authors = reference[0:authorsPartEndPos]

afterAuthors = reference[authorsPartEndPos:]

#year
timePartEndPos = afterAuthors.find(")")
timePart = afterAuthors[0:timePartEndPos].strip('( )')
year = timePart[0:4]

afterYear = afterAuthors[timePartEndPos:]

#title
titlePartAndRest = afterYear[3:]
questionMarkPos = titlePartAndRest.find("?")
exclamationMarkPos = titlePartAndRest.find("!")
periodMarkPos = titlePartAndRest.find(".")

if titlePartAndRest.count("?") > 0:
    title = titlePartAndRest[0:questionMarkPos+1]
elif titlePartAndRest.count("!") > 0:
    title = titlePartAndRest[0:exclamationMarkPos+1]
else:
    title = titlePartAndRest[0:periodMarkPos+1]

afterTitle = titlePartAndRest[len(title)+1:]

#determining the category and other fields
if afterTitle.count(": ") > 0:   #book
    month = ''
    publicationTitle = ''
    volume = ''
    issue = ''
    pages = ''
    publisher = afterTitle.split(": ")[1].strip(".")
    address = afterTitle.split(": ")[0]
    print("BOOK---------------------------------")
    
elif len(timePart) > 5: #magazine article
    month = timePart[6:].split()[0]
    publicationTitle = afterTitle.split(", ")[0].title()
    volumePart = afterTitle.split(", ")[1]
    if volumePart.find("(") > 0:
        volume = volumePart[:volumePart.find("(")]
        issue = volumePart[volumePart.find("(")+1:volumePart.find(")")]
    else:
        volume = volumePart
        issue = ''
    pages = afterTitle.split(", ")[2].strip(".")
    publisher = ''
    address = ''
    print("MAGAZINE ARTICLE---------------------------------")
    
else:   #journal article
    month = ''
    publicationTitle = afterTitle.split(", ")[0].title()
    volumePart = afterTitle.split(", ")[1]
    if volumePart.find("(") > 0:
        volume = volumePart[:volumePart.find("(")]
        issue = volumePart[volumePart.find("(")+1:volumePart.find(")")]
    else:
        volume = volumePart
        issue = ''
    pages = afterTitle.split(", ")[2].strip(".")
    publisher = ''
    address = ''
    print("JOURNAL ARTICLE---------------------------------")
    
print('AUTHORS:'.rjust(20), authors)
print('TITLE:'.rjust(20), title)
print('YEAR:'.rjust(20), year)
print('MONTH:'.rjust(20), month)
print('PUBLICATION TITLE:'.rjust(20), publicationTitle)
print('VOLUME:'.rjust(20), volume)
print('ISSUE:'.rjust(20), issue)
print('PAGES:'.rjust(20), pages)
print('PUBLISHER:'.rjust(20), publisher)
print('ADDRESS:'.rjust(20), address)
print('--------------------------------------------------')
