class GiftShop:
    def __init__(self, filename):
        self.ranges = []
        self.load_content(filename)
        self.sum = 0

    def load_content(self, file):
        with open(file, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        for line in lines:
            parts = line.split(",")
            for part in parts:
                a, b = part.split("-")
                a, b = int(a), int(b)
                self.ranges.append(range(a, b + 1))

    def main(self):
        for r in self.ranges:
            for i in r:
                s = str(i)
                mid = len(s) // 2
                if len(s) % 2 == 0 and s[:mid] == s[mid:]:
                    self.sum += i

        print(self.sum)


GiftShop("day2.txt").main()
