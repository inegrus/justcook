# from flask import Flask, render_template, request
import urllib
import json
import requests
from pprint import pprint
import os
from secret_key import SECRET_APP_ID, SECRET_APP_KEY


# app = Flask ("MyApp")
# app.run (debug=True)
# @app.route("/")
# def hello ():
# 	return render_template("hello.html", name = name.title ())

# endpoint = "https://www.edamam.com/recipes"


ingredients = ["flour", "apple"]
part_of_url = "https://api.edamam.com/search?app_id={}&app_key={}&q=".format(SECRET_APP_ID, SECRET_APP_KEY)
url_for_recipes = part_of_url + "{}".format(" ".join(ingredients))

response = requests.get(url_for_recipes).json()

for i in range(0, 9):
    print("\n ======= Another recipe ======= \n ")
    pprint(response['hits'][i]['recipe']['label'])
    pprint(response['hits'][i]['recipe']['ingredientLines'])
    pprint(response['hits'][i]['recipe']['image'])

    # pprint(response['hits'][i]['recipe'])

