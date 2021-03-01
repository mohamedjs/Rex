import re

def searchInPattern(pattern, string):
    search = re.compile(pattern).search(string)
    if not search:
        return "not match"
    return "found Pattern: " + search.group()

print(searchInPattern("hel(p|pes)", "can you help me"))  #(hel) that end with (p) or() Pes)
print(searchInPattern("can|can't", "can you help me"))   # search about can or can't
print(searchInPattern("can?", "can you help me"))        # search about can that have (n) or not
print(searchInPattern("can+", "can you help me"))        # search about can that have one (n) or more
print(searchInPattern("can*", "can you help me"))        # search about can that have zero (n) or more
print(searchInPattern("can{1,3}", "cann you help me"))   # search about can that have 1|2|3 (n)
print(searchInPattern("can{1}", "cann you help me"))     # search about can that have at least one (n)
print(searchInPattern("can{,3}", "cann you help me"))    # search about can that have at most one (n) == {1,3}
print(searchInPattern("[A-Z]", "cann you Help me"))      # search about capital char
print(searchInPattern("[^A-Z]", "cann you Help me"))     # search about Not capital char
print(searchInPattern("^c", "cann you Help me"))         # search about sentence start with (c)
print(searchInPattern("e$", "cann you Help me"))         # search about sentence end with (e)
print(searchInPattern("[A-Za-z]", "cann you Help me"))   # search about capital or smal char
print(searchInPattern("\w", "cann you Help me"))         # search about [A-Za-z0-9] all char or number
print(searchInPattern("\d", "cann you Help me 123?"))    # search about [0-9]  number
print(searchInPattern("\s", "cann you Help me 123?"))    # any white space [\t\n\r]
print(searchInPattern("\W", "cann you Help me"))         # search about not [A-Za-z0-9] all char or number
print(searchInPattern("\D", "cann you Help me 123?"))    # search about not [0-9]  number
print(searchInPattern("\S", "cann you Help me 123?"))    # any not white space [\t\n\r]
print(searchInPattern("\?", "cann you Help me?"))        # when search about spcial char like (^,?,$,{) you shoud use (\)
print(searchInPattern("\{.+\}", "{cann you Help me?}"))  # search about any word in {any}
print(searchInPattern("\[.+\]", "[cann you Help me?]"))  # search about any word in [any] 

# search about any word  start with (<) aFter that have word and aFter that close with (>) aFter that have word with space
# aFter that close with (</) aFter that any word atet that (>) 
# <html> <head> </head> <body> </body> <\html>
print(searchInPattern("\<.+\>(.|\t)*\<\/.+\>", "<div> <h1> Hello </h1> </div>"))
