from pathlib import Path

def findFile(projectRoot,name):
    for path in Path(projectRoot).rglob("*/"+name+".md"):
        return path
    
def embed(absPath):
    with open(absPath) as myFile:
        return myFile.read()
    
def link(args):
    return "link placeholder"