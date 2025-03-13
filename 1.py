class RebBullRacing:
    def team_info(self):
        print("Red Bull Racing: Max Verstappen")

    def max_speed(self):
        print("Max speed: 350 km/h")

class ScuderiaFerrari:
    def team_info(self):
        print("Scuderia Ferrari: Carlos Sainz")

    def max_speed(self):
        print("Max speed: 340 km/h")


verstappen = RebBullRacing()
sainz = ScuderiaFerrari()

for driver in (verstappen, sainz):
    driver.team_info()
    driver.max_speed()
