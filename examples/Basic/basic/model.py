import random

from mesa import Model, Agent
from mesa.space import SingleGrid
from mesa.time import RandomActivation


class Walker(Agent):
    def __init__(self, unique_id, pos, heading=(1, 0)):
        self.unique_id = unique_id
        self.pos = pos
        self.heading = heading
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}


class ShapesModel(Model):
    def __init__(self, N, width=20, height=10):
        self.running = True
        self.N = N    # num of agents
        self.headings = ((1, 0), (0, 1), (-1, 0), (0, -1))  # tuples are fast
        self.grid = SingleGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.make_walker_agents()

    def make_walker_agents(self):
        unique_id = 0
        while True:
            if unique_id == self.N:
                break
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pos = (x, y)
            heading = random.choice(self.headings)
            # heading = (1, 0)
            if self.grid.is_cell_empty(pos):
                print("Creating agent {2} at ({0}, {1})"
                      .format(x, y, unique_id))
                a = Walker(unique_id, pos, heading)
                self.schedule.add(a)
                self.grid.place_agent(a, pos)
                unique_id += 1

    def step(self):
        self.schedule.step()
