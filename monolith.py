import sys, re, methods
from pathlib import Path

mnlName = Path(sys.argv[1]).resolve()
projectRoot = Path(mnlName).parent.resolve()
mnlText = methods.cat(mnlName)

embedRE = r"\!\[\[(?P<file>.*?)(\|(?P<rename>.*?))?\]\]"
#linkRE = r"\[\[(?P<file>.*)(?P<heading>#.*){0,1}(?P<text>\|.*){0,1}\]\]"

# print(mnlText)
# while re.search(embedRE, mnlText):
#     match = re.search(embedRE, mnlText)
#     print(match)
#     print(match.groupdict())
#     mnlText=mnlText.replace(match.group(0),"")

print(mnlText)
counter = 0
while re.search(embedRE,mnlText):
    counter += 1
    print (counter)
    match = re.search(embedRE,mnlText)
    text = methods.cat(methods.findFile(projectRoot,match.groupdict()["file"]))
    mnlText=mnlText.replace(match.group(0),text)
print(mnlText)


# print(methods.findFile(projectRoot,m.groupdict()['file']))
# myFile = methods.findFile(projectRoot,m.groupdict()['file'])
# myText = methods.cat(myFile)
#print(myText)

#while '[[' in contents:
# print(m.groupdict())
