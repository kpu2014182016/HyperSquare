class GameState:
    def __init__(self, state):
        self.handle_events = state.handle_events


class TestGameState:

    def __init__(self, name):
        self.name = name

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def main(self):
        print("State [%s] update" % self.name)



running = None
stack = None


def change_state(state):
    global stack
    pop_state()
    stack.append(state)



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    while (running):
        stack[-1].handle_events()
        stack[-1].main()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)



if __name__ == '__main__':
    test_game_framework()
