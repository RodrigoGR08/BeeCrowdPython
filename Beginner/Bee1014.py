#Calculate a car's average consumption being provided the total distance traveled (in Km) and the spent fuel total (in liters).
distance = int(input())
fuelSpent = float(input())
consumption = distance/fuelSpent
print(f'{consumption:.3f} km/l')