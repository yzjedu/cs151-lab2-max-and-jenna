birth_rate = float(input("Enter the time between births (in seconds):"))
death_rate = float(input("Enter the time between deaths (in seconds):"))
immigrant_rate = float(input("Enter the time between immigrants (in seconds):"))
current_population = float(input("Enter the current population (in population):"))
years_into_future = float(input("Enter the number of years into the future:"))
SECONDS_PER_YEAR = 365 * 24 * 60 * 60
births_per_year = SECONDS_PER_YEAR / birth_rate
deaths_per_year = SECONDS_PER_YEAR / death_rate
immigrants_per_year = SECONDS_PER_YEAR / immigrant_rate
population_change_per_year = births_per_year + immigrants_per_year - deaths_per_year
future_population = current_population + (population_change_per_year * years_into_future)
if future_population > current_population:
    change = "increased"
elif future_population < current_population:
    change = "decreased"
else:
    change = "remained the same"
print(f"In {years_into_future} years, the population will be {future_population}.")
print(f"The population has {change}.")
