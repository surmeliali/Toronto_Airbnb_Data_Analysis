# Toronto Airbnb Data Analysis

This repository contains a data analysis project on Airbnb data from Toronto city. This project was done as part of my Udacity Data Science Nanodegree. It primarily explores the data to answer key questions about prices, popular districts, popular months, preferable places by districts, and types of rooms, which is essential for anyone planning to travel or settle in Toronto.

# The blog page of the Toronto Airbnb Analysis

Descriptive analysis and diagnostic analysis of the project are published on [my Medium blog post](https://medium.com/@surmeliali/the-rising-star-of-20th-century-toronto-city-33c881252260). 

## Project Description
The data for this project was sourced from the [Inside Airbnb](http://insideairbnb.com/get-the-data.html) website, which contained detailed information about Airbnb listings in Toronto. Additionally, neighbourhood data was manually added from [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_neighbourhoods_in_Toronto) as it wasn't available in the original dataset.

## Files in this Repository

- `1_toronto_airbnb_etl_process.ipynb` : The main Jupyter Notebook for the ETL process of AirBnb datasets.
- `2_toronto_airbnb_visual_analysis.ipynb` : This file should be run after the ETL process to visualize the clean datasets.
- `toronto_airbnb_analysis.py` : Python file converted from the Jupyter Notebook for those who want to analyze using their IDE.

## Data

This project makes use of the following data files:

- `listings.csv` : Dataset of information about each listing in Toronto.

- `neighbourhoods.csv` : Dataset of information about neighbourhoods in Toronto. 

You can clone and download the files using: 

$ git clone https://github.com/surmeliali/Toronto_AirBnb_Data_Analysis.git


## Libraries Used

- numpy
- pandas
- seaborn
- matplotlib.pyplot

