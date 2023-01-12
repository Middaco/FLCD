# parsing tree representation : table (using father and sibling relation)

class ParserOutput:
    def __init__(self, prod_string, file_name):
        self.__prod_string = prod_string
        self.__file_name = file_name

    def printToScreen(self):
        for i in self.__prod_string:
            print(i)

    def printToFile(self):
        output_file = open(self.__file_name, "a")
        for i in self.__prod_string:
            output_file.write(str(i))
        output_file.close()
