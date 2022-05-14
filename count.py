from email.policy import default


class Counter:
    default = 0
    def per(self, text):
        print(text)
    def plus(self, single_number = 1):
        self.default = self.default + single_number
        print(self.default)
        return self.default
    def reset(self):
        self.default = 0
        print(self.default)


item = Counter()

item.per('Hello!')


num = Counter()
num.plus(3)

num.plus(5)

num.reset()

num.plus(2)



