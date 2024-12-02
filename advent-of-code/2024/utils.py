# Creates a list of the text of each line of the file
def readFile(filename):
    lines = []
    data = open(filename, 'r')
    
    while(1):
        line = data.readline()
        if line: lines.append(line.strip())
        else: return lines