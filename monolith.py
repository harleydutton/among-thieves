import sys, re

ep = sys.argv[1]

contents = ""
with open(ep) as my_file:
    contents = my_file.read()


embedRE = r"\!\[\[.*\]\]"
linkRE = re.compile(r"\!\[\[(?P<file>.*)(?P<heading>#.*)(?P<text>\|.*)\]\]")

#this should be replaced with "while <single match>:"
#while '[[' in contents:
print(contents)
print(re.match(embedRE,contents))
    


def findFile(name):
    return "filename placeholder"

def embed(token):
    return "embed placeholder"

def link(token):
    return "link placeholder"