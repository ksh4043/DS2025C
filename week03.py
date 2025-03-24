def duplicate_city(cities):
    result_cities = []
    city_set = set()

    for city in cities:
        l1 = len(city_set)
        city_set.add(city)
        l2 = len(city_set)

        if l1 == l2:
            result_cities.append(city)

    return result_cities

cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Seoul']
cities.append('Anyang')
cities.append('Seoul')
print(cities)


print(set(duplicate_city(cities)))