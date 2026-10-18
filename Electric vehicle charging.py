battery = 25
target = 80

while battery < target:
    battery += 5
    print("Battery:", min(battery, target), "%")

print("Charging target reached")
