class Words:
    def __init__(self, text):
        self.text = text

    def print_words(self):
        exampl = self.split()
        exampl.sort()
        max_len = len(max(exampl, key=len))
        for item, value in enumerate(exampl, 1):
            print(f'{item} {value:>{max_len}}')


Words.print_words('А лето цвета неба')