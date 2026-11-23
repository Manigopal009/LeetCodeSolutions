class ProductOfNumbers:

    def __init__(self):
        # Stores prefix products since the last zero; sentinel 1 simplifies division
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix)
        # If k >= n, the last k elements include a zero that reset the stream
        if k >= n:
            return 0
        return self.prefix[-1] // self.prefix[n - 1 - k]