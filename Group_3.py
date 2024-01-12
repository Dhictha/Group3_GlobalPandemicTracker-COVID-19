from pip._vendor import requests
 
welcome_msg = """Welcome to the Global Pandemic (COVID-19) Tracker!
Your one-stop app for information about COVID-19 around the globe.
To stay up-to-date with relevant information about the pandemic in different countries around the globe,
this app is here to meet your needs."""

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
 