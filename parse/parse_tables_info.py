import json
import re


class TableInfoParser:
    TABLE_INFO_FILE = "parse/fucktheimmigrationpopo.txt"
    TABLE_JSON_FILE = "parse/undocumented_tables.json"
    TABLE_NAME_RE = r"[a-zA-Z]+_[a-zA-Z_]+"
    VARTYPE_RE = r"(int|bit|[Dd]atetime|varchar\([0-9]+\)|char\([0-9]+\)|unique ?identifier)"

    def __init__(self):
        self.tables = {}

    def parse_tables_info(self):
        with open(TableInfoParser.TABLE_INFO_FILE, "r") as fh:
            lines = fh.readlines()

        section1 = lines[2:411]
        section2 = lines[412:1523]

        self.parse_section(section1, True)
        self.parse_section(section2, False)

    def parse_section(self, lines, section1):
        tokenized_lines = []
        for line in lines:
            words = line.split()

            try:
                int(words[0])
                tokenized_lines.append(words)
            except ValueError:
                # some table rows got broken over several lines for some reason
                tokenized_lines[-1] += words

        for line in tokenized_lines:
            print(line)
            if len(line) < 2:
                continue
            field_name = line[1]
            table_name = line[2] if (not section1) else None
            vartype = None
            for word in line[2:]:
                if section1 and re.match(TableInfoParser.TABLE_NAME_RE, word):
                    table_name = word
                elif re.match(TableInfoParser.VARTYPE_RE, word):
                    vartype = word

            if table_name is None:
                raise ValueError("Invalid line: " + repr(line))

            if vartype is None:
                vartype = "varchar(256)"

            if table_name in self.tables:
                self.tables[table_name][field_name] = {
                    "vartype": vartype,
                    "primary": False
                }
            else:
                self.tables[table_name] = {
                    field_name: {
                        "vartype": vartype,
                        "primary": True
                    }
                }

    def write_json(self):
        with open(TableInfoParser.TABLE_JSON_FILE, "w") as fh:
            json.dump(self.tables, fh, indent=4)


if __name__ == "__main__":
    tip = TableInfoParser()
    tip.parse_tables_info()
    tip.write_json()