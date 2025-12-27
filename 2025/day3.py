class Joltage:
    def __init__(self, file):
        self.ranges = []
        self.input = self.read_file(file)
        self.sum = 0

    def read_file(self, file):
        with open(file, "r", encoding="utf-8") as f:
            return f.read().splitlines()

    def max_jolt(self, bank):
        list = []
        max2 = 0
        for i in bank:
            list.append(int(i))
        max1= list[0]
        while True:
            for j in range(len(list)-1):
                if list[j] < list[j+1]:
                    list[j] = 0
                else:
                    max1 = list[j]
            print(max1, max2)

    def main(self):
        for i in self.input:
            self.max_jolt(i)
Joltage("day3.txt").main()