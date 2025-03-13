class NCT:
    def intro(self):
        print("\nNCT has diverse music styles")

    def concept(self):
        print("NCT has many sub-units")

class NCT127(NCT):
    def concept(self):
        print("NCT 127: focuses on powerful and experimental music.")

class NCTDream(NCT):
    def concept(self):
        print("NCT Dream: focuses on fresh and youthful music.")


groups = [NCT(), NCT127(), NCTDream()]

for group in groups:
    group.intro()
    group.concept()
