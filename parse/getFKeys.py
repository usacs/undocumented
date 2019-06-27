

tables = {}
tablesSet = {}
currKey = None
forKeys = {}
with open("primaryKeys") as f:
    content = f.readlines()
    for line in content:
        words = line.split()
        if len(words) == 0:
            continue
        if currKey != None:
            tables[words[1]] = currKey
            tablesSet[words[1].replace("_","").lower()] = words[1]
            forKeys[words[1]] = []
            currKey = None
        if words[0] == "Key:":
            currKey = words[1]
currTable = None
with open("foreignReferences") as f:
    content = f.readlines()
    for line in content:
        words = line.split()
        if len(words) == 0:
            continue
        if currTable != None:
            if len(words[3:]) != 0:
                for table in list(words[3:][0].split(",")):
                    forKeys[currTable].append(tables[tablesSet[table.replace("_","").lower()]])
            currTable = None
        if words[0] == "Table:":
            currTable = words[1]



for key, value in forKeys.items():
    print("Table: "+key+"\nForiegn Keys: "+str(value)+"\n\n")
