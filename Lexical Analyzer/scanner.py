import re


class Scanner:
    def __init__(self, token_file, program_file, sym_table):
        self.__program_file = program_file
        self.__symTable = sym_table
        self.__PIF = []
        self.__reservedWords = []
        self.__separators = []
        self.__operators = []
        self.__token = [self.__operators, self.__separators, self.__reservedWords]
        self.token(token_file)

    def get_sym_table(self):
        return self.__symTable.get()

    def get_PIF(self):
        return self.__PIF

    def token(self, token_file):
        token = open(token_file, "r")
        token_lines = token.readlines()
        empty_lines = 0
        for line in token_lines:
            if line == '\n':
                empty_lines += 1
                continue
            elif line == 'space\n':
                self.__token[empty_lines].append(' ')
                continue
            self.__token[empty_lines].append(line.strip())

    def scan(self):
        program = open(self.__program_file, "r")
        lines = program.readlines()
        identifier = re.compile("^([a-zA-Z]+[0-9]*)+$")
        integer_constant = re.compile("^\+[1-9][0-9]*$|^-[1-9][0-9]*$|^[1-9][0-9]*$|^0$")
        char_constant = re.compile("^\'[a-zA-Z]\'$")
        string_constant = re.compile("^\"\"$|^\"([a-zA-Z][a-zA-Z]+\s*)+\"$")
        boolean_constant = re.compile("[01]")
        double_constant = re.compile("^0\.[0-9]+$|^\+[1-9][0-9]*\.[0-9]+$|^-[1-9][0-9]*\.[0-9]+$")

        for line in lines:
            pass_next_char = False
            pass_line = False
            word = ""

            for character in line:

                if line == "\n":
                    pass_line = True

                if pass_line:  # skips the current line, used in case of comment line
                    pass_line = False
                    break

                if pass_next_char:
                    pass_next_char = False
                    continue

                if character not in self.__operators and character not in self.__separators and character != '\n':
                    word += character
                elif word == "":  # operator or separator found on the first attempt to make a word
                    if character in self.__operators:  # character is an operator that might be a separator
                        # performs a look ahead to see if the operator is actually a separator
                        if character + line[line.index(character)] == "--":
                            pass_line = True
                            self.__PIF.append(("--", -1))
                            continue
                        elif character + line[line.index(character)] == "//":
                            pass_next_char = True
                            self.__PIF.append(("//", -1))
                            continue
                    self.__PIF.append((character, -1))  # character is a separator
                else:  # operator or separator found after a word was made
                    if word in self.__reservedWords:  # found word is a reserved word
                        self.__PIF.append((word, -1))
                    else:  # found word is an identifier or a constant
                        if self.__symTable.search(word) != -1:  # verify if the word is already in the Symbol Table
                            if integer_constant.fullmatch(word) or string_constant.fullmatch(
                                    word) or char_constant.fullmatch(word) or boolean_constant.fullmatch(
                                    word) or double_constant.fullmatch(
                                    word):  # see if it is an identifier or a constant
                                self.__PIF.append(("const", self.__symTable.search(word)))
                            elif identifier.fullmatch(word):
                                self.__PIF.append(("id", self.__symTable.search(word)))
                        else:
                            index = self.__symTable.add(word)
                            self.__PIF.append((word, index))
                    word = ""
