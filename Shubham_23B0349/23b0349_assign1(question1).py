
def input_country():
    country = input("Enter country name: ")
    gold = int(input("Enter gold medals: "))
    silver = int(input("Enter silver medals: "))
    bronze = int(input("Enter bronze medals: "))
    return country, gold, silver, bronze
def sort_countries(countries):
    return sorted(countries, key=lambda x: (-x[1], x[0]))

num_countries = int(input("Enter the number of countries: "))
countries_data = [input_country() for _ in range(num_countries)]

sorted_countries = sort_countries(countries_data)

print("Countries sorted in descending order of gold medals:")
for country_data in sorted_countries:

    print(f"'{country_data[0]}' : [{country_data[1]},  {country_data[2]},  {country_data[3]}]")