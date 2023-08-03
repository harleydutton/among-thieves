from pathlib import Path

def findFile(projectRoot,name):
    for path in Path(projectRoot).rglob("*/"+name+".md"):
        return path
    
def cat(absName):
    with open(absName) as myFile:
        return myFile.read()
    
def githubLink(text, heading):
    return "[{}](#{})".format(text, heading.replace(" ","-").lower())