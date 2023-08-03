import sys, re, methods
from pathlib import Path

mnlName = Path(sys.argv[1]).resolve()
projectRoot = Path(mnlName).parent.resolve()
mnlText = methods.cat(mnlName)

embedRE = r"\!\[\[(?P<file>.*?)(\\?\|(?P<rename>.*?))?\]\]"
linkRE = r"[^!](?P<car>\[\[(?P<file>.*?)(#(?P<subsection>.*?))?(\\?\|(?P<rename>.*?))?\]\])"

maxDepth = int(sys.argv[2])
for attempt in range(maxDepth):
    for match in re.finditer(embedRE,mnlText):
        filename = methods.findFile(projectRoot,match.groupdict()["file"])
        if filename is None:
            continue
        text = methods.cat(filename)
        mnlText = mnlText.replace(match.group(0),text)

for match in re.finditer(linkRE,mnlText):
    if match.groupdict()["subsection"] is not None and match.groupdict()["rename"] is not None:
        link = methods.githubLink(match.groupdict()["rename"],match.groupdict()["subsection"])
        mnlText = mnlText.replace(match.group("car"),link)

for match in re.finditer(embedRE,mnlText):
    img = methods.imageEmbed(projectRoot,match.groupdict()["file"],match.groupdict()["rename"])
    mnlText = mnlText.replace(match.group(0),img)

outName = str(mnlName).replace(".md",".mnl.md")
outFile = open(outName, "w")
outFile.write(mnlText)
outFile.close()

# print(mnlText)
# counter = 0
# while re.search(embedRE,mnlText):
#     counter += 1
#     print (counter)
#     match = re.search(embedRE,mnlText)
#     print(match.groupdict()["file"])
#     filename = methods.findFile(projectRoot,match.groupdict()["file"])
#     if ".md" not in str(filename):
#         continue
#     text = methods.cat(filename)
#     mnlText=mnlText.replace(match.group(0),text)
# print(mnlText)

# print(mnlText)
# while re.search(embedRE, mnlText):
#     match = re.search(embedRE, mnlText)
#     print(match)
#     print(match.groupdict())
#     mnlText=mnlText.replace(match.group(0),"")


# print(methods.findFile(projectRoot,m.groupdict()['file']))
# myFile = methods.findFile(projectRoot,m.groupdict()['file'])
# myText = methods.cat(myFile)
#print(myText)

#while '[[' in contents:
# print(m.groupdict())
