class Reader:

    def __init__(self, path):
        self.path = path

    def get_file(self):
        # Get string from a text file
        text = ""
        if self.path.endswith(".txt"):
            file = open(self.path, "r")
            if file.mode == "r":
                text = file.read()
            file.close()
        return text

    def split_rows(self):
        # Split text in rows for each account
        data = self.get_file()
        rows = [""]
        for i, line in enumerate(data.splitlines(True)):
            if (i + 1) % 4 == 0:
                rows.append("")
            else:
                rows[-1] += line
        return rows

    def split_row_columns(self, row):
        # Split in columns the row selected in a file
        len_number = 3
        len_row = 27
        rows = self.split_rows()
        empty_row = ["   " for i in range(0, len_row, len_number)]
        header, body, footer = rows[row].splitlines()[0:3] or [empty_row, empty_row, empty_row]
        if isinstance(header, str):
            header = [header[i:i+len_number]
                      if header[i:i+len_number] else "   "
                      for i in range(0, len_row, len_number)]
            body = [body[i:i+len_number]
                    if body[i:i + len_number] else "   "
                    for i in range(0, len_row, len_number)]
            footer = [footer[i:i+len_number]
                      if footer[i:i + len_number] else "   "
                      for i in range(0, len_row, len_number)]
        columns = ["\n".join(list(e)) for e in zip(header, body, footer)]
        return columns
