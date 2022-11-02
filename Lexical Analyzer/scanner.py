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

    def token(self, token_file):
        token = open(token_file, "r")
        token_lines = token.readlines()
        empty_lines = 0
        for line in token_lines:
            if line == '':
                empty_lines += 1
            self.__token[empty_lines].append(line.strip())

    def scan(self):
        program = open(self.__program_file, "r")
        lines = program.readlines()

        for line in lines:
            pass_next_char = False
            pass_line = False

            for word in line:
                new_word = ""
                if pass_line:  # skips the current line, used in case of comment line
                    pass_line = False
                    continue

                for character in word:
                    if pass_next_char:
                        pass_next_char = False
                        continue
                    if character not in self.__operators or character not in self.__separators:
                        new_word += character
                    elif new_word == "":  # operator or separator found on the first attempt to make a word
                        if character in self.__operators:  # character is an operator that might be a separator
                            # performs a look ahead to see if the operator is actually a separator
                            if character+word[word.index(character)] == "--":
                                pass_line = True
                                pass_next_char = True
                                self.__PIF.append(("--", -1))
                                continue
                            elif character+word[word.index(character)] == "//":
                                pass_next_char = True
                                self.__PIF.append(("//", -1))
                                continue
                        self.__PIF.append((character, -1))  # character is a separator
                    else:  # operator or separator found after a word was made
                        if new_word in self.__reservedWords:  # found word is a reserved word
                            self.__PIF.append((new_word, -1))
                        else:  # found word is an identifier
                            index = self.__symTable.add(word)
                            self.__PIF.append((word, index))
