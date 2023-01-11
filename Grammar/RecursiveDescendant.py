from Grammar import Grammar


class RecursiveDescendant:
    def __init__(self, grm, final_config):
        self.__work_stack = []
        self.__grm = grm
        self.__input_stack = list(grm.get_start_symbol())
        self.__productions = grm.get_productions()
        self.__state = 'q'
        self.__index = 1
        self.__final_config = final_config
        # 0 - info 1 - parent 2 - right sibling
        self.__parsing_tree = [[grm.get_start_symbol()], [0], [0]]

    def __expand(self):
        self.__work_stack.append([self.__input_stack.pop(0), 1])
        prods = self.__grm.get_productions_nonTerms(self.__work_stack[-1][0])[self.__work_stack[-1][1]-1].split()
        prods.reverse()
        for prod in prods:
            self.__input_stack.insert(0, prod)

    def __advance(self):
        self.__index += 1
        self.__work_stack.append(self.__input_stack.pop(0))

    def __momentary_insuccess(self):
        self.__state = 'b'

    def __back(self):
        self.__index -= 1
        self.__input_stack.insert(0, self.__work_stack.pop(-1))

    def __another_try(self):
        if len(self.__grm.get_productions_nonTerms(self.__work_stack[-1][0])) >= self.__work_stack[-1][1]+1:
            self.__state = 'q'
            prod_tobe_popped = self.__grm.get_productions_nonTerms(self.__work_stack[-1][0])[self.__work_stack[-1][1]-1].split()
            for i in prod_tobe_popped:
                self.__input_stack.pop(0)
            self.__work_stack[-1][1] += 1
            prods = self.__grm.get_productions_nonTerms(self.__work_stack[-1][0])[self.__work_stack[-1][1]-1].split()
            prods.reverse()
            for prod in prods:
                self.__input_stack.insert(0, prod)
        elif self.__index == 1 and self.__work_stack[-1] == self.__grm.get_start_symbol():
            self.__state = 'e'
        else:
            self.__input_stack.pop(0)
            self.__input_stack.insert(0, self.__work_stack[-1][0])
            self.__work_stack.pop(-1)

    def __success(self):
        self.__state = 'f'

    def run(self):
        while self.__state != 'f' and self.__state != 'e':
            if self.__state == 'q':
                if self.__index == len(self.__final_config)+1 and len(self.__input_stack) == 0:
                    self.__success()
                else:
                    if self.__grm.is_nonterm(self.__input_stack[0]):
                        self.__expand()
                    elif self.__index <= len(self.__final_config) and self.__input_stack[0] == self.__final_config[self.__index-1] :
                        self.__advance()
                    else:
                        self.__momentary_insuccess()
            elif self.__state == 'b':
                if self.__grm.is_term(self.__work_stack[-1]):
                    self.__back()
                else:
                    self.__another_try()
        if self.__state == 'e':
            print("Error")
        else:
            print("Sequence accepted")


grammar = Grammar("seminar_grammar.txt")
rec = RecursiveDescendant(grammar, "aacbc")
rec.run()
