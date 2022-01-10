from flask import Flask, redirect, render_template

import pandas as pd
import numpy as np
from plots import *

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/refresh_plots', methods=['POST'])
def refresh_plots():

    
    #get and mutate dataframe
    african_countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina", "Burundi", "Cameroon", "Cape Verde",
                         "Central African Republic", "Chad", "Comoros", "Congo", "Congo, Democratic Republic of",
                         "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana",
                         "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar",
                         "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger",
                         "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone",
                         "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia",
                         "Uganda", "Zambia", "Zimbabwe"]
    df = pd.read_csv('cleaned_data.csv')
    df = df[['SpatialDim', 'TimeDim', 'NumericValue', 'Country']]
    
    #generate plots
    bar_plots(df)
    dispersion_plots(df)
    box_plots(df)

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)