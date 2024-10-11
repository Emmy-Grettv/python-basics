#1. The solutions is using flat list format
cars = [
    {'location': 'Gasabo', 'car_name': 'Ford', 'year': 2005, 'car_price': 5000, 'car_owner': 'Alice'},
    {'location': 'Gasabo', 'car_name': 'Mitsubishi', 'year': 2000, 'car_price': 3000, 'car_owner': 'Bob'},
    {'location': 'Gasabo', 'car_name': 'BMW', 'year': 2019, 'car_price': 25000, 'car_owner': 'Charlie'},
    {'location': 'Gasabo', 'car_name': 'VW', 'year': 2011, 'car_price': 12000, 'car_owner': 'David'},
    {'location': 'Kicukiro', 'car_name': 'Toyota', 'year': 2018, 'car_price': 22000, 'car_owner': 'Eve'},
    {'location': 'Kicukiro', 'car_name': 'Honda', 'year': 2015, 'car_price': 18000, 'car_owner': 'Frank'},
    {'location': 'Kicukiro', 'car_name': 'Subaru', 'year': 2020, 'car_price': 27000, 'car_owner': 'Grace'},
    {'location': 'Kicukiro', 'car_name': 'Nissan', 'year': 2017, 'car_price': 20000, 'car_owner': 'Heidi'},
    {'location': 'Nyarugenge', 'car_name': 'Chevrolet', 'year': 2016, 'car_price': 15000, 'car_owner': 'Ivan'},
    {'location': 'Nyarugenge', 'car_name': 'Hyundai', 'year': 2019, 'car_price': 21000, 'car_owner': 'Judy'},
    {'location': 'Nyarugenge', 'car_name': 'Kia', 'year': 2021, 'car_price': 23000, 'car_owner': 'Kevin'},
    {'location': 'Nyarugenge', 'car_name': 'Mazda', 'year': 2014, 'car_price': 16000, 'car_owner': 'Laura'}
]

#2. sortimg according to car price
# def sort_by_car_price(cars):
#     n = len(cars);
#     for i in range(n):
#         for j in range(n-i-1):
#             if cars[j]['car_price'] > cars[j+1]['car_price']:
#                 cars[j], cars[j+1] = cars[j+1], cars[j]

# sort_by_car_price(cars);
# for car in cars:
#     print(car)
sorted_car=sorted(cars,key=lambda x:x['car_price'])
print(sorted_car)

#3.  Return total price of all
def total_price(cars):
    total_price = 0;
    for car in cars:
        total_price += car['car_price']
    return total_price

print(f'The total price is: {total_price(cars)}')

# #4. Total price of cars in Nyarugenge
# def total_price_Nyarugenge(cars):
#     total_price = 0
#     for car in cars:
#         if car['location'] == 'Nyarugenge':
#          total_price += car['car_price']
#     return total_price

def total_price_Nyarugenge(cars):   
    return sum(map(lambda car: car['car_price'], filter(lambda car: car['location'] == 'Nyarugenge', cars)))


print(f'The tal priceof cars in Nyarugenge: {total_price_Nyarugenge(cars)}')

#5. Location of the cheapest car
def cheapest_car_location(cars):
    cheapest_car = cars[0]
    for car in cars:
        if car['car_price'] < cheapest_car['car_price']:
            cheapest_car = car
    return cheapest_car['location']

print(f'The location of the cheapest car: {cheapest_car_location(cars)}')

#6. returning car names
def available_car_names(cars):
    car_names = []
    for car in cars:
        car_names.append(car['car_name'])
    return car_names
    
print(f'Available car names: {available_car_names(cars)}')
    
 #7. Adding two new brands
def adding_brands(cars):
   car_namess = available_car_names(cars)
   car_namess.sort()
   new_brands = ['Audi', 'Tesla']
   car_namess.extend(new_brands)
   return car_namess

print(f'Adding two new brands: {adding_brands(cars)}')
    
#8. All elements except the first one
car_names = adding_brands(cars)
elements_1 = car_names[1:] 
print(f'All cars except the first one: {elements_1}')

#9. Two cars and ignore the rest
first_car, second_car, *rest = car_names 
print(f'First car: {first_car} and second car: {second_car}')

#10. First two and print the rest
first_two_ones, *remaining = car_names[:2], car_names[2:]
print(f'The remaining: {remaining}')

#11. Replacing
new_cars = ['Tesla', 'Volvo']
car_names[1:4] = new_cars
print(f'Updated car names: {car_names}')

#12.Replace second position
new_car = ['Tesla', 'Volvo']
car_names[1:2] = new_car
print(f'Replacing second element: {car_names}')

#13. 3rd position with hybrid car
new_name = 'Hybrid_car'
car_names[2] = new_name
print(f'Updated list: {car_names}')

#14. Replacing with eCar
eCar = 'Electric car'
car_names[1:4] = [eCar]*3
print(f'With ecar value: {car_names}')