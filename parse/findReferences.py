


i = 0
tablesFo = {}
tables = {}
tablesSet = {}
with open("fucktheimmigrationpopo.txt") as f:
    content = f.readlines()
    nextTable = -1
    for line in content:
        words = line.split()
        try:
            val = int(words[0])
        except ValueError:
            continue
        if words[0] == "1" and len(words) > 1:
            nextTable += 1
        if words[0] == "1104":
            break
        tableName = ""

        for i in range(2,len(words)):
            if tableName == "":
                if nextTable == 1:
                    tableName = words[2]
                elif '_' in words[i]:
                    tableName = words[i]


                if tableName != "" and tableName.replace("_","").lower() not in tablesSet:
                    tableName = words[i]
                    key = words[1]
                    tables[tableName] = key
                    tablesFo[tableName] = ""
                    tablesSet[tableName.replace("_","").lower()] = tableName
            else:
                if words[i].lower().replace(" ","") == "key" and words[i+1].lower().replace(" ","") == "for":
                    #Find the table name
                    newi = i+2
                    for j in range(1,10):
                        if "".join(words[newi:newi+j]).replace("_","").lower() in tablesSet:
                            #We want to match on the longest subset. Some of tables are subsets of each other (>_<)
                            if newi + j + 1 < len(words) and "".join(words[newi:newi+j+1]).replace("_","").lower() in tablesSet:
                                continue
                            primaryTable = tablesSet["".join(words[newi:newi+j]).replace("_","").lower()]
                            if tableName not in tablesFo[primaryTable] and tableName != primaryTable:
                                tablesFo[primaryTable] += tableName +","
                            break
                    break





for key, value in tablesFo.items():
    print("Table: "+key+"\nOther Tables Refrencing: "+str(value[0:len(value)-1])+"\n\n")
