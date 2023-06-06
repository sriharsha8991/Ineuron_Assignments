import requests
import json
import pandas as pd
def read_data_from_web_to_csv(link,path_):
    #Get the data from web
    response = requests.get(link)
    #make it into huma readable format
    data = response.text

    #Jsonify the data
    json_data = json.loads(data)

    # Make it into a dataframe using pandas
    df = pd.DataFrame(json_data)
    file_op = df.to_csv(path_)

    return "Process_done"

link = "https://data.nasa.gov/resource/y77d-th95.json"
path = r"C:\Users\sriharsha\Desktop\INueron\Interview Assignment 1\Python Questions\Q4_python\nasa_data.csv"

read_data_from_web_to_csv(link,path)