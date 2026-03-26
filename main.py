import time
from environment import MiniGameEnv


class Agent:

    def __init__(self):
        # Fixed path to reach goal
        self.actions = [3, 3, 1, 1]
        self.index = 0

    def choose_action(self):

        action = self.actions[self.index]
        self.index += 1

        return action


def grade(path, goal):

    if path[-1] == goal:
        return "PASS"
    else:
        return "FAIL"


def run_game():

    env = MiniGameEnv()
    agent = Agent()

    state = env.reset()

    done = False
    path = []

    print("\nStarting Game...\n")

    while not done:

        env.render()

        action = agent.choose_action()

        state, reward, done = env.step(action)

        path.append(state)

        print("Action:", action)
        print("Reward:", reward)

        time.sleep(1)

    print("\nFinal Grid:")
    env.render()

    print("Agent Path:", path)

    result = grade(path, env.goal_pos)

    print("Result:", result)


if __name__ == "__main__":
    run_game()