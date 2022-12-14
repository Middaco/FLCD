class RecursiveDescendant:
    def __init__(self, sequence, final_config):
        self.__work_stack = []
        self.__input_stack = list(sequence)
        self.__state = 'q'
        self.__index = 1
        self.__final_config = final_config

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
            self.__work_stack[-1][1] += 1
            self.__input_stack[0] = self.__work_stack[-1][0].production(self.__work_stack[-1][1])
        elif # conditie:
            # ce fac aici?
        else:
            self.__state = 'e'

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

