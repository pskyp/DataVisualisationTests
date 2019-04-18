from random import choice

class RandomWalk():
    """a class to define a random walk"""

    def __init__(self,num_points=5000):
        """initialise attributes"""
        self.num_points = num_points

        #all wals start at 0,0
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """calculates a  step in random choice of two directions and 5 lengths"""
        # decide which direction and how far
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):

        """calculate all the points on the walk"""

        # keep walking until walk reaches desired length
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            #rejects streps that do nowhere
            if y_step == 0 and x_step ==0:
                continue

            #calculate the next x and y values for the list and add it [-1] gets the last item in a list
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



