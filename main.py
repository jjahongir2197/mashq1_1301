class Talaba:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.baholar = []

    def baho_qoshish(self, baho):
        if 0 <= baho <= 100:
            self.baholar.append(baho)
        else:
            print("Noto‘g‘ri baho kiritildi!")

    def ortacha_baho(self):
        if len(self.baholar) == 0:
            return 0
        return sum(self.baholar) / len(self.baholar)

    def malumot_chiqarish(self):
        print("Ism:", self.ism)
        print("Familiya:", self.familiya)
        print("Yosh:", self.yosh)
        print("Baholar:", self.baholar)
        print("O‘rtacha baho:", self.ortacha_baho())


talaba1 = Talaba
