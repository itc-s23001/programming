class Nigiri:
    def __init__(self, topping):
        self.topping = topping
        self.ingredients = ["しょうが", "ねぎ"]

    def add_topping(self, extra_topping):
        self.ingredients.append(extra_topping)

    def show_attributes(self):
        print(f"{self.topping}握り寿司:")
        print("  ねた: 赤身")
        print("  トッピング:", ', '.join(self.ingredients))

class Katsuo(Nigiri):
    def __init__(self):
        super().__init__("かつお")

katsuo_nigiri = Katsuo()
katsuo_nigiri.show_attributes()

