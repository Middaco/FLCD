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
        self.__work_stack.append([self.__input_stack.pop(), 1])
        self.__input_stack.insert(0, self.__work_stack[-1][0].production(self.__work_stack[-1][1]))

    def __advance(self):
        self.__index += 1
        self.__work_stack.append(self.__input_stack.pop())

    def __momentary_insuccess(self):
        self.__state = 'b'

    def __back(self):
        self.__index -= 1
        self.__input_stack.insert(0, self.__work_stack.pop(-1))

    def __another_try(self):
        self.__state = 'q'
        if self.__work_stack[-1][0].next():
            self.__state = 'q'
            self.__work_stack[-1][1] += 1
            self.__input_stack[0] = self.__work_stack[-1][0].production(self.__work_stack[-1][1])
        elif self.__index == 1 and self.__work_stack[-1] == 'S':
            self.__state = 'e'
        else:
            pass

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
                    elif self.__grm.is_term(self.__input_stack[0]):
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
rec = RecursiveDescendant(grammar, "a a c b c")
rec.run()
