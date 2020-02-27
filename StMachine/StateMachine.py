import sys

class StateMachine:
    state = 1
    result = []
    states = []

    def changeState(income, self):
        pass


    def stateOne(self, letter):
        if letter == '0':
            self.result.append('O')
            self.state = 3

        elif letter == '1':
            self.result.append('U')
            self.state = 2

        elif letter == '2':
            self.result.append('w')
            self.state = 1

        self.states.append(1)


    def stateTwo(self, letter):
        if letter == '0':
            self.result.append('w')
            self.state = 3

        elif letter == '1':
            self.result.append('U')
            self.state = 1

        elif letter == '2':
            self.result.append('U')
            self.state = 2

        self.states.append(2)


    def stateThree(self, letter):
        if letter == '0':
            self.result.append('O')
            self.state = 2

        elif letter == '1':
            self.result.append('w')
            self.state = 3

        elif letter == '2':
            self.result.append('U')
            self.state = 1

        self.states.append(3)

    def translate(self, income):
        for i in range(0, len(income)):
            if self.state == 1:
                self.stateOne(income[i])
            elif self.state == 2:
                self.stateTwo(income[i])
            elif self.state == 3:
                self.stateThree(income[i])

    def print(self):
        print("result dictionary: ", ''.join(self.result))

        print("states: ", ''.join(str(self.states)))

