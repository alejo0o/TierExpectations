if __name__ == "__main__":
    world_cup_countries = ["Brazil", "Ecuador", "Canada", "Argentina", "Germany", "USA"]
    # print first 3 countries
    for i in range(3):
        print(f"{i+1}:", world_cup_countries[i])

    for country in world_cup_countries:
        print(country)
    
    print("---Iterable---")
    iterable = iter(world_cup_countries)
    print(next(iterable))  # Brazil
    print(next(iterable))  # Ecuador
    print(next(iterable))  # Canada
    
    print("---Enumerate---")
    for count, country in enumerate(world_cup_countries, start=1):
        print(f"{count}:", country)
    
    
