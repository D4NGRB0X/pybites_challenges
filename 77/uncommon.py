def uncommon_cities(my_cities, other_cities):
    return len(set(other_cities).symmetric_difference(my_cities))
