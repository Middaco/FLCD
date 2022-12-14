class Grammar:
    def __init__(self, file_name):
        self.read_grammar(file_name)
        terms = []
        non_terms = []
        productions = []

    def read_grammar(self, file_name):
        grammar = open(file_name, 'r')
        lines_grammar = grammar.readlines()
        for line in lines_grammar:
            pass

    def print_nonTerms(self):
        pass

    def print_terms(self):
        pass

    def print_productions(self):
        pass

    def print_productions_nonTerms(self, nonTerminal):
        pass

    def CFG_check(self):
        pass