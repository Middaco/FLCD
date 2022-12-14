class RecursiveDescendant:
    def __init__(self, start_symbol, productions, final_config):
        self.__work_stack = []
        self.__input_stack = list(start_symbol)
        self.__productions = productions
        self.__state = 'q'
        self.__index = 1
        self.__final_config = final_config
        # 0 - info 1 - parent 2 - right sibling
        self.__parsing_tree = [[start_symbol], [0], [0]]

    def expand(self):
        self.__work_stack.append([self.__input_stack.pop(), 1])
        self.__input_stack.insert(0, self.__work_stack[-1][0].production(self.__work_stack[-1][1]))

    def advance(self):
        self.__index += 1
        self.__work_stack.append(self.__input_stack.pop())

    def momentary_insuccess(self):
        self.__state = 'b'

    def back(self):
        self.__index -= 1
        self.__input_stack.insert(0, self.__work_stack.pop(-1))

    def another_try(self):
        self.__state = 'q'
        if self.__work_stack[-1][0].next():
            self.__state = 'q'
            self.__work_stack[-1][1] += 1
            self.__input_stack[0] = self.__work_stack[-1][0].production(self.__work_stack[-1][1])
        elif self.__index == 1 and self.__work_stack[-1] == 'S':
            self.__state = 'e'
        else:
            pass

    def success(self):
        self.__state = 'f'

    def run(self):
        while self.__state != 'f' and self.__state != 'e':
            if self.__state == 'q':
                if self.__index == len(self.__final_config)+1 and len(self.__input_stack) == 0:
                    self.success()
                else:
                    if self.__input_stack[0].is_nonterm():
                        self.expand()
                    elif self.__input_stack[0].is_term():
                        self.advance()
                    else:
                        self.momentary_insuccess()
            elif self.__state == 'b':
                if self.__work_stack[-1].is_term():
                    self.back()
                else:
                    self.another_try()
        if self.__state == 'e':
            print("Error")
        else:
            print("Sequence accepted")
