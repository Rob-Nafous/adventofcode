class Password:

    def __init__(self, filename):
        self.list = self.load_content(filename)
        self.current = 50
        self.sum = 0

    def load_content(self, file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read().splitlines()
        return content

    def direction(self, value):
        if value[0] == 'L':
            return -1
        if value[0] == 'R':
            return 1

    def main(self):
        for i in self.list:
            distance = int(i[1:])

            for tick in range(distance):
                self.current = (self.current + self.direction(i))%100
                if self.current == 0:
                    self.sum += 1
        print(self.sum)
Password("day1.txt").main()
# 5202 is too low