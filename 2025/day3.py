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
        for i in bank:
            list.append(i)
        index1, value1 = max(enumerate(list), key=lambda x: x[1]) #key=lambda x:x[1] compare the max value, not the index
        list[index1] = "0"
        index2, value2 = max(enumerate(list), key=lambda x: x[1]) #key=lambda x:x[1] compare the max value, not the index
        if index1 < index2:
            return int(str(value1) + str(value2))
        else:
            return int(str(value2) + str(value1))

    def main(self):
        for i in self.input:
            self.sum += self.max_jolt(i)
        print(self.sum)

Joltage("day3.txt").main()