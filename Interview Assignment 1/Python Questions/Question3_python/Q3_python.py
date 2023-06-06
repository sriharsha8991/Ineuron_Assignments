import requests
import json
import pandas as pd
# Write a program, which would download the data from the provided link, and then read the data and convert
# that into properly structured data and return it in Excel format.
# Note - Write comments wherever necessary explaining the code written.
def read_data_from_web(link,path_to_data):
    #Get the data from web
    response = requests.get(link)
    #make it into huma readable format
    data = response.text

    #Jsonify the data
    json_data = json.loads(data)

    #Take only the data of attributes by removing title
    poke_data = json_data['pokemon']

    # Make it into a dataframe using pandas
    df = pd.DataFrame(poke_data)

    #Convert the data frame into excel file
    file = df.to_excel(path_to_data)

    return "Progress done"

    
link = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
path = r"C:\Users\sriharsha\Desktop\INueron\Interview Assignment 1\Python Questions\pokemon_data.xlsx"

read_data_from_web(link,path)
