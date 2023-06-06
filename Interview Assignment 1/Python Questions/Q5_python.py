# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:29:38 2023

@author: sriharsha
"""

import requests

# API link
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to the API and fetch the data
response = requests.get(api_link)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    data = response.json()

    # Extract show name
    show_name = data["name"]

    # Extract show status
    show_status = data["status"]

    # Extract episodes data
    episodes = data["_embedded"]["episodes"]

    # Print the extracted data with proper formatting
    print("Show Name: ", show_name)
    print("Status: ", show_status)
    print("Episodes: ")
    for episode in episodes:
        episode_name = episode["name"]
        episode_season = episode["season"]
        episode_number = episode["number"]
        print(f"Season {episode_season}, Episode {episode_number}: {episode_name}")
else:
    print("Error occurred while fetching data from the API")
