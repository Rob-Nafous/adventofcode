class GuardMap:

    def __init__(self, filename):
        self.map = self.load_map(filename)
        self.sum = 0
        self.directions = {'^': [-1,0], '>': [0,1], 'v': [1,0], '<': [0,-1]}

    def load_map(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        # Build matrix
        x = [[*map(str, line.split())] for line in content.split('\n') if line.strip()]
        separated_matrix = [[char for char in row[0]] for row in x]
        return separated_matrix

    def moving_guard(self, i, j):
        self.position = [i,j]
        obstacle = False
        while not obstacle:
            try:
                if self.position[0]<0 or self.position[1]<0:
                    break
                view = self.map[self.position[0]+self.direction[0]][self.position[1]+self.direction[1]]
                if view != "#":
                    if self.map[self.position[0]][self.position[1]] == "X":
                        self.position = [self.position[0]+self.direction[0], self.position[1]+self.direction[1]]
                        # print("moving")
                    else:
                        self.map[self.position[0]][self.position[1]] = 'X'
                        self.sum+=1
                        self.position = [self.position[0]+self.direction[0], self.position[1]+self.direction[1]]
                        # print("moving")
                else:
                    # print("obstacle at :",self.position[0]+self.direction[0],self.position[1]+self.direction[1])
                    # print("actual direction :",self.direction)
                    directions_values = list(self.directions.values())
                    index = directions_values.index(self.direction)
                    self.direction = directions_values[(index + 1) % len(directions_values)]
                    # print("Turning at 90 degree :",self.direction)

            except IndexError:
                # print("Out of map reached")
                self.map[self.position[0]][self.position[1]] = 'X'
                self.sum+=1
                break

    def main(self):
        for row_idx, row in enumerate(self.map):
            for col_idx, value in enumerate(row):
                if value in self.directions:
                    self.direction = self.directions.get(value)
                    self.moving_guard(row_idx, col_idx)
                    break
        print(self.sum)
        # for row in self.map:
        #     print("".join(row))
#GuardMap("day6.txt").main()

#Mathematical solution part 2:

#   *#****
#   *****#
#   ******
#   #*****
#   ****#*
# [i,j] -> [i-1,j'] -> [i', j'-1] -> [i'+1,j-1] -> [i,j] -> etc...
#we can mathematically link the obstacles between them : gotta check if no obstacles in between.
# So, each time an obstacle is touched : get the current direction and calculates the possible outcome if we add another obstacle.