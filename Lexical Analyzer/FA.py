class FA:
    def __init__(self, input_file):
        self.__alphabet = []
        self.__states = []
        self.__transitions = {}
        self.__final_states = []
        self.__initial_state = None

        self.load(input_file)
        self.findFinalStates()
        self.findInitialState()

    def findInitialState(self):
        dict_transition_list = self.__transitions.values()
        state = 0
        # posibil să fie o problemă aici
        state_freq_list = [0] * len(self.__states)
        for transition_list in dict_transition_list:
            for transition in transition_list:
                transition = transition.strip("()")
                transition = transition.split(",")
                for q in transition:
                    if q != self.__states[state] and q != "NULL":
                        state_freq_list[list(self.__states).index(q)] += 1
            state += 1
        for s in range(0, len(state_freq_list)):
            if state_freq_list[s] == 0:
                self.__initial_state = self.__states[s]

    def findFinalStates(self):
        dict_transition_list = self.__transitions.values()
        for transition_list in dict_transition_list:
            final = True
            for transition in transition_list:
                if transition != 'NULL':
                    final = False
            if final:
                self.__final_states.append(
                    list(self.__transitions.keys())[list(dict_transition_list).index(transition_list)])

    def load(self, input_file):
        fa_file = open(input_file, "r")
        fa_lines = fa_file.readlines()
        self.__alphabet = fa_lines[0]
        self.__alphabet = self.__alphabet.split()
        self.__states = fa_lines[1]
        self.__states = self.__states.split()

        for line in range(2, len(fa_lines)):
            transition_list = fa_lines[line]
            transition_list = transition_list.split()

            self.__transitions.update({self.__states[line - 2]: transition_list})

    @staticmethod
    def menu():
        print("1. States")
        print("2. Alphabet")
        print("3. Transitions")
        print("4. Initial state")
        print("5. Set of final states")
        print("6. Exit")

    def run(self):
        while True:
            self.menu()
            choice = int(input("Option: "))
            if choice == 1:
                print(self.__states)
            elif choice == 2:
                print(self.__alphabet)
            elif choice == 3:
                print(self.__transitions)
            elif choice == 4:
                print(self.__initial_state)
            elif choice == 5:
                print(self.__final_states)
            elif choice == 6:
                return
