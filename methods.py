from pathlib import Path

def findFile(projectRoot,name):
    for path in Path(projectRoot).rglob("*/"+name+".md"):
        return path
    
    
def link(args):
    return "link placeholder"

def cat(absName):
    with open(absName) as myFile:
        return myFile.read()