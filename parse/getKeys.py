


i = 0
tables = {}
tablesSet = {}
with open("fucktheimmigrationpopo.txt") as f:
    content = f.readlines()
    nextTable = -1
    for line in content:
        words = line.split()
        if words[0] == "1" and len(words) > 1:
            nextTable += 1
        if words[0] == "1104":
            break
        tableName = ""
        for i in range(2,len(words)):
            if nextTable == 1:
                tableName = words[2]
                break
            elif '_' in words[i]:
                tableName = words[i]
                break

        if tableName != "" and tableName.replace("_","").lower() not in tablesSet:
            tableName = words[i]
            key = words[1]
            tables[tableName] = key
            tablesSet[tableName.replace("_","").lower()] = True
        else:
            continue



for key, value in tables.items():
    print("Key: "+value+"\nTable: "+key+"\n\n")
