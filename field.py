class Field(list):
    def __init__(self, width, height):
        if width < 1 or height < 1:
            raise ValueError
        self.width, self.height = width, height
        self.length = self.width * self.height
        self.cells_size = len(str(self.length))
        self.empty_cell = "_" * self.cells_size
        super().__init__(self.empty_cell for _ in range(self.length))

    def __str__(self):
        row_indent = (len(str(self.height)))
        border = " " * row_indent + "-" * (self.width * (self.cells_size + 1) + 3)
        result = border
        for y in reversed(range(0, self.length, self.width)):
            n = str(y // self.width + 1)
            result += "\n" + " " * (row_indent - len(n)) + n + "| " + " ".join(self[y:y + self.width]) + " |"
        result += "\n" + border + "\n " + " " * row_indent
        for n in range(1, self.width + 1):
            result += " " * (self.cells_size + 1 - (len(str(n)))) + str(n)
        return result + "\n"

    def __getitem__(self, key):
        if isinstance(key, slice):
            return super().__getitem__(key)
        else:
            return super().__getitem__(self.convert(key)).replace("_", "")

    def __setitem__(self, key, val):
        val = " " * (self.cells_size - len(str(val))) + str(val)
        return super().__setitem__(self.convert(key), val)

    def __delitem__(self, key):
        return super().__setitem__(self.convert(key), self.empty_cell)

    def convert(self, key):
        x, y = key
        if 0 <= x <= self.width and 0 <= y <= self.height:
            return x - 1 + (y - 1) * self.width
        raise IndexError
