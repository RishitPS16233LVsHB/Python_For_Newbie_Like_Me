country_capital_dict = {
    "USA": "Washington D.C.",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

sorted_dict = sorted(country_capital_dict.items())
print("Sorted Country-Capital Dictionary:")
for country, capital in sorted_dict:
    print(country, "-", capital)
