import sys, re, methods
from pathlib import Path

ep = sys.argv[1]
projectRoot = Path(ep).parent.resolve()

contents = ""
with open(ep) as my_file:
    contents = my_file.read()

embedRE = r"\!\[\[(?P<file>.*)\]\]"
#linkRE = r"\[\[(?P<file>.*)(?P<heading>#.*){0,1}(?P<text>\|.*){0,1}\]\]"

#while '[[' in contents:
m = re.search(embedRE,contents)
print(m.groupdict())

print(methods.findFile(projectRoot,m.groupdict()['file']))
myFile = methods.findFile(projectRoot,m.groupdict()['file'])
myText = methods.embed(myFile)
print(myText)



def link(token):
    return "link placeholder"