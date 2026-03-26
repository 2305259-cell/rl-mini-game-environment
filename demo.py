from environment import MiniGameEnv
import time

actions = [3,3,1,1]

env = MiniGameEnv()
state = env.reset()

done = False
step = 0

print("Demo Starting...\n")

while not done:

    env.render()

    action = actions[step]

    state, reward, done = env.step(action)

    step += 1

    time.sleep(1)

print("Goal Reached!")