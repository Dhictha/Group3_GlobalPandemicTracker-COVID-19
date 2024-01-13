# Importing the 'requests' library from the '_vendor' module.
from pip._vendor import requests

# A welcome message for the COVID-19 Tracker application.
welcome_msg = """Welcome to the Global Pandemic (COVID-19) Tracker!
Your one-stop app for information about COVID-19 around the globe.
To stay up-to-date with relevant information about the pandemic in different countries around the globe,
this app is here to meet your needs."""

# Class to define console colors for better visual presentation.
class ConsoleColors:
    BOLD = '\033[1m'
    RESET = '\033[0m'
    GREEN = '\033[92m'
    
# Function to display information about a country based on API response.    
def display_country_info(country_info):
    continent = ', '.join(country_info[0]['continents'])
    area_value = country_info[0]['area']
    population = country_info[0]['population']
    capital = ', '.join(country_info[0]['capital'])
    timezone = ', '.join(country_info[0]['timezones'])
    languages = ', '.join(f"{k}: {v}" for k, v in country_info[0]['languages'].items())
    currencies = ', '.join(f"{k}: {v['name']} ({v['symbol']})" for k, v in country_info[0]['currencies'].items())

# Extracting various information from the API
    msg = (f"{country} is located in {continent}. It has an area of {area_value} and {population} number of people.\n"
           f"The capital of {country} is {capital} and their timezone is {timezone}.\n"
           f"They speak these languages: {languages} and their currency is {currencies}.")
# Creating a formatted message with extracted information.
    with open("country_data.txt", "w", encoding='utf-8') as txt_file:
        txt_file.write(msg + '\n')

# Writing the information to a text file named 'country_data.txt'.      
def display_covid_info(covid_info):
    cases = covid_info['cases']
    deaths = covid_info['deaths']
    recovered = covid_info['recovered']
    population = covid_info['population']
    tests = covid_info['tests']

 # Calculating additional statistics based on the extracted information.
    tested_positive = cases
    tested_negative = tests - cases
    population_left_after_covid = population - deaths

# Creating a formatted message with extracted and calculated information. 
    msg = (f"{country} has a total population of {population} people.\n"
           f"Out of the {population} people, {tested_positive} tested positive for COVID-19 and {tested_negative} tested negative.\n"
           f"Fortunately, some people survived COVID-19, but the number of people who couldn't survive was {deaths}.\n"
           f"That's very unfortunate! \nPopulation left after COVID: {population_left_after_covid}")
 
# Writing the information to a text file named 'covid_data.txt'. 
    with open("covid_data.txt", "w") as txt_file:
        txt_file.write(msg + '\n') 

# Function to handle user's choice of exiting the application.
def app_exit():
    exit_choice = input("We hope you find the information useful and that it helps in making better decisions regarding your travel plans.\n"
                        "Upon completion, would you like to exit the app? Yes or No?: ").lower()
    return exit_choice == "yes"

# Function to construct the API endpoint based on user input.
def construct_api_endpoint(info_needed, country):
    if info_needed == "Rest countries":
        return f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    elif info_needed == "COVID":
        return f"https://disease.sh/v3/covid-19/countries/{country}"
    else:
        print(f"Invalid choice. {info_needed}")
        exit() 

# Main program execution starts here.
if __name__ == "__main__":
    while True:
# Prompting the user to select the information type (COVID or Rest countries).    
        info_needed = input(f"{ConsoleColors.BOLD}{ConsoleColors.GREEN}{welcome_msg}.{ConsoleColors.RESET} \n"
                            f"Kindly select (COVID, Rest countries:) ")
        country = input("Enter the country of your choice: ")
 
        endpoint = construct_api_endpoint(info_needed, country) # Constructing the API endpoint based on the user's input.
 
        response = requests.get(endpoint) ## Making an API request to fetch data.
        if response.status_code == 200:  
            data = response.json()
            if info_needed == "Rest countries":   
                display_country_info(data)
            elif info_needed == "COVID": 
                display_covid_info(data)
        else:
            print(f"Failed to fetch data for {info_needed}. Please check the country name or try again later.")

# Asking the user if they want to exit the application.
        if app_exit():
            print("We are sad to see you leave! You can click on this link {https://www.who.int/emergencies/diseases/novel-coronavirus-2019} to get more information about COVID-19.")
            break  # Exiting the loop and terminating the program.
        else:
           continue # Exiting the loop and terminating the program. 