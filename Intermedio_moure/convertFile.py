import codecs

class ConvertFile:
    def __init__(self, input_file):
        self.row = str()
        self.total_columns = int()
        self.delimiter = str()
        self.lines_to_write = list()

    def count_columns(self,file):


    def write_in_csv(self,line,file):
        self.lines_to_write.append(line)
        if len(self.lines_to_write) == 200:
            with open (file,'a'):

    def add_lines_to_write(self,line):
