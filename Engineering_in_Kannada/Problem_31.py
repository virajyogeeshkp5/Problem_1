"""Dictionary Comprehension:

Create a dictionary where the keys are Kannada cities, and the values are their populations. 
Use dictionary comprehension to filter out cities with populations below 10 lakhs."""

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)







