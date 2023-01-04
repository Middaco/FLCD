import re


class Grammar:
    def __init__(self, file_name):
        self.__terms = []
        self.__non_terms = []
        self.__productions = {}
        self.read_grammar(file_name)

    def read_grammar(self, file_name):
        grammar = open(file_name, 'r')
        lines_grammar = grammar.readlines()
        term_regex = re.compile("[a-z]")
        non_term_regex = re.compile("[A-Z]")
        for line in lines_grammar:
            production = line.split("->")
            self.__productions.update({production[0].strip(): production[1].strip()})
            line = line.split()
            for symb in line:
                if term_regex.fullmatch(symb) and symb not in self.__terms:
                    self.__terms.append(symb)
                elif non_term_regex.fullmatch(symb) and symb not in self.__non_terms:
                    self.__non_terms.append(symb)

    def print_nonTerms(self):
        print(self.__non_terms)

    def print_terms(self):
        print(self.__terms)

    def print_productions(self):
        print(self.__productions)

    def print_productions_nonTerms(self, non_terminal):
        print(self.__productions.get(non_terminal))

    def CFG_check(self):
        pass


gr = Grammar("g2.txt")
gr.print_terms()
gr.print_nonTerms()
gr.print_productions()
gr.print_productions_nonTerms("D")
