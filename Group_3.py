from pip._vendor import requests
 
welcome_msg = """Welcome to the Global Pandemic (COVID-19) Tracker!
Your one-stop app for information about COVID-19 around the globe.
To stay up-to-date with relevant information about the pandemic in different countries around the globe,
this app is here to meet your needs."""

class ConsoleColors:
    BOLD = '\033[1m'
    RESET = '\033[0m'
    GREEN = '\033[92m'
    
def display_country_info(country_info):
    continent = ', '.join(country_info[0]['continents'])
    area_value = country_info[0]['area']
    population = country_info[0]['population']
    capital = ', '.join(country_info[0]['capital'])
    timezone = ', '.join(country_info[0]['timezones'])
    languages = ', '.join(f"{k}: {v}" for k, v in country_info[0]['languages'].items())
    currencies = ', '.join(f"{k}: {v['name']} ({v['symbol']})" for k, v in country_info[0]['currencies'].items())
 
def display_covid_info(covid_info):
    cases = covid_info['cases']
    deaths = covid_info['deaths']
    recovered = covid_info['recovered']
    population = covid_info['population']
    tests = covid_info['tests']
 
    tested_positive = cases
    tested_negative = tests - cases
    population_left_after_covid = population - deaths
 
msg = (f"{country} has a total population of {population} people.\n"
           f"Out of the {population} people, {tested_positive} tested positive for COVID-19 and {tested_negative} tested negative.\n"
           f"Fortunately, some people survived COVID-19, but the number of people who couldn't survive was {deaths}.\n"
           f"That's very unfortunate! \nPopulation left after COVID: {population_left_after_covid}")
 
with open("covid_data.txt", "w") as txt_file:
        txt_file.write(msg + '\n') 

def app_exit():
    exit_choice = input("We hope you find the information useful and that it helps in making better decisions regarding your travel plans.\n"
                        "Upon completion, would you like to exit the app? Yes or No?: ").lower()
    return exit_choice == "yes"
