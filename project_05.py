import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        self.result = ''
        for key in kwargs:
            value = kwargs[key]
            self.result = key
            for i in range(value):
                self.contents.append(self.result)

    def draw(self, numballs):
        picked = []
        if numballs < len(self.contents):
            for i in range(numballs):
                p = random.choice(self.contents)
                picked.append(p)
                self.contents.remove(p)
            # print('randomly picked:', picked)
            return(picked)
        else:
            print('you picked all the balls', self.contents)
            return(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    checklist = []
    for i in range(num_experiments):
        if num_balls_drawn >= len(hat.contents):
            m += 1
            probability = m/num_experiments
        else:
            copyhat = copy.deepcopy(hat)
            x = copyhat.draw(num_balls_drawn)
            for key in expected_balls:
                if expected_balls[key] >= 1:
                    color = key
                    num = expected_balls[key]
                    # print('expected', color, num)
                    counting = 0
                    for n, i in enumerate(x):
                        if color == x[n]:
                            counting += 1
                            # print(color, counting)
                            if counting >= num and color not in checklist:
                                checklist.append(color)
                                # print(checklist)
            # print(colorcount)
            if len(checklist) <= 1:
                checklist = []
                # print(checklist)
            if len(expected_balls) == len(checklist):
                m+=1
                checklist = []
            # print('m', m)
            # print('n', num_experiments)
            probability = m/num_experiments
    print('probability', probability)
    return(probability)

hat1 = Hat(blue=6, red=6)
experiment(hat=hat1, expected_balls = {'blue':2, 'red':2}, num_balls_drawn = 4, num_experiments = 1000)
