class MiniGameEnv:

    def __init__(self):
        self.grid_size = 3
        self.agent_pos = [0, 0]
        self.goal_pos = [2, 2]
        self.obstacle = [1, 1]

    def reset(self):
        self.agent_pos = [0, 0]
        return self.agent_pos

    def step(self, action):

        # Move agent
        if action == 0:  # UP
            self.agent_pos[0] -= 1
        elif action == 1:  # DOWN
            self.agent_pos[0] += 1
        elif action == 2:  # LEFT
            self.agent_pos[1] -= 1
        elif action == 3:  # RIGHT
            self.agent_pos[1] += 1

        # Keep agent inside grid
        self.agent_pos[0] = max(0, min(self.grid_size - 1, self.agent_pos[0]))
        self.agent_pos[1] = max(0, min(self.grid_size - 1, self.agent_pos[1]))

        reward = -1
        done = False

        if self.agent_pos == self.goal_pos:
            reward = 10
            done = True

        if self.agent_pos == self.obstacle:
            reward = -10
            done = True

        return self.agent_pos, reward, done

    def render(self):

        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        grid[self.goal_pos[0]][self.goal_pos[1]] = "G"
        grid[self.obstacle[0]][self.obstacle[1]] = "X"
        grid[self.agent_pos[0]][self.agent_pos[1]] = "A"

        print("\nGame Grid")

        for row in grid:
            print(" ".join(row))

        print()