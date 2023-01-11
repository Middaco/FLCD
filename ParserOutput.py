# parsing tree representation : table (using father and sibling relation)

class ParserOutput:
    def __init__(self, tree):
        self.__tree = tree

    def printToScreen(self):
        print("Info | Parent | Right Sibling")
        for i in range(0, len(self.__tree[0])):
            print(str(self.__tree[0][i]) + ' | ' + self.__tree[1][i] + ' | ' + self.__tree[2][i])

    def printToFile(self, file_name):
        output_file = open(file_name, "a")
        output_file.write("Info | Parent | Right Sibling")
        for i in range(0, len(self.__tree[0])):
            output_file.write(str(self.__tree[0][i]) + ' | ' + self.__tree[1][i] + ' | ' + self.__tree[2][i])
        output_file.close()
