class FileSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_handler = None
        self.open()

    def open(self):
        pass

    def close(self):
        self.file_handler.close()

    def __del__(self):
        self.close()


class Reader(FileSystem):

    def open(self):
        self.file_handler = open(self.file_path, 'r')

    def get_nex_line(self):
        return self.file_handler.readline()


class Writer(FileSystem):

    def open(self):
        self.file_handler = open(self.file_path, 'w')

    def write(self, line: str):
        self.file_handler.write(line)


class Splitter:
    def __init__(self, input_file_path: str, pass_file_path: str, fail_file_path: str):
        self.reader = Reader(input_file_path)
        self.pass_writer = Writer(pass_file_path)
        self.fail_writer = Writer(fail_file_path)

    @staticmethod
    def check_is_pass_line(line: str):
        return line.split(' ')[2].strip() == 'P'

    def split(self):
        while True:
            line = self.reader.get_nex_line()
            if not line:
                break
            writer = self.pass_writer if self.check_is_pass_line(line) else self.fail_writer
            writer.write(line)


if __name__ == "__main__":
    spliter = Splitter("inputFile.txt", "PassFile.txt", "FailFile.txt")
    spliter.split()
    del spliter