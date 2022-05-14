class Counter:
    def per(self, text):
        print(text)
    def plus(self, default = 0, single_number = 1):
        self.default = default + single_number
        print(self.default)
        return self.default


item = Counter()

item.per('Hello!')


num = Counter()
a = num.plus(0, 3)

num.plus(a, 3)



