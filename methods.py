from pathlib import Path

def findFile(projectRoot,name):
    for path in Path(projectRoot).rglob("*/"+name+".md"):
        return path
    
def cat(absName):
    with open(absName) as myFile:
        return myFile.read()
    
def githubLink(text, heading):
    return "[{}](#{})".format(text, heading.replace(" ","-").lower())

def imageEmbed(projectRoot,name,size):
    absName = None
    for path in Path(projectRoot).rglob("*/"+name):
        absName = path
    template = "<img src={} width={}>"
    return template.format(absName,size if size is not None else -1)