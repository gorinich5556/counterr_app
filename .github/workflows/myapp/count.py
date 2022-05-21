from email.policy import default


class Counter:
    default = 0
    def per(self, text):
        print(text)
    
    def plus(self, single_number = 1):
        self.default = self.default + single_number
        return self.default
    
    def reset(self):
        self.default = 0
        return self.default

    def minus(self, single_number=1):
        self.default = self.default - single_number
        return self.default






