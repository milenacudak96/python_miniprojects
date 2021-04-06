'''
Create a python script that asks a user questions in the command line. The script should follow the outlined specs.
Receive the following arguments from the user:

kilometers to drive
liters-per-kilometer usage of the car
price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.
'''

km_to_drive = int(input('Please tell me how many kms you want to drive: '))
litters_per_km = int(input('Please tell me how much liters-per-kilometer usage of the car: '))
price_per_km = int(input('Please tell me the price per km: '))
km_per_liters = km_to_drive/litters_per_km
total_fuel_cost = km_per_liters*price_per_km
print(int(total_fuel_cost))