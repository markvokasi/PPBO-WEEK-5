class Driver:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __add__(self, other):
        return Driver(self.name, self.points + other.points)

    def info(self):
        print(f"Driver: {self.name}, Total Points: {self.points}")

# driver points from four race
verstappen_r1 = Driver("Max Verstappen", 25)  # P1 Finish
verstappen_r2 = Driver("Max Verstappen", 18)  # P2 Finish
verstappen_r3 = Driver("Max Verstappen", 25)  # P1 Finish
verstappen_r4 = Driver("Max Verstappen", 12)  # P4 Finish

hamilton_r1 = Driver("Lewis Hamilton", 18)  # P2 Finish
hamilton_r2 = Driver("Lewis Hamilton", 15)  # P3 Finish
hamilton_r3 = Driver("Lewis Hamilton", 10)  # P5 Finish
hamilton_r4 = Driver("Lewis Hamilton", 18)  # P2 Finish

verstappen_total = verstappen_r1 + verstappen_r2 + verstappen_r3 + verstappen_r4
hamilton_total = hamilton_r1 + hamilton_r2 + hamilton_r3 + hamilton_r4

verstappen_total.info()
hamilton_total.info()
