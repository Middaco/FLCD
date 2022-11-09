class FA:
    def __init__(self, input_file):
        self.__file = input_file
        self.__transitions = []
        self.__states = []
        self.__future_states = []
        self.load(input_file)

    def load(self, input_file):
        fa_file = open(input_file, "r")
        transitions = fa_file.readline()
        states = fa_file.readline()

        eof = False
        count_line = 0
        while not eof:
            line = fa_file.readline()
            line.insert(0, states[count_line])
            self.__future_states.append(fa_file.readline())
            count_line += 1



    @staticmethod
    def menu():
        print("1. States")
        print("2. Alphabet")
        print("3. Transitions")
        print("4. Initial state")
        print("5. Set of final states")

    def run(self):
        self.menu()
        choice = input("Option: ")
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass