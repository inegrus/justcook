# from flask import Flask, render_template, request
import urllib
import json
import requests
from pprint import pprint

# app = Flask ("MyApp")
# app.run (debug=True)
# @app.route("/")
# def hello ():
# 	return render_template("hello.html", name = name.title ())

# endpoint = "https://www.edamam.com/recipes"

ingredients = ["flour", "apple"]
url_for_recipes = "https://api.edamam.com/search?app_id=ff6d4efa&app_key=f70aa029996a664dcb7516a504f11d74&q={}".format(" ".join(ingredients))

response = requests.get(url_for_recipes).json()

#print response.url
#print response.status_code
#print response.text.hits.recipe.ingredientLines


for i in range(0, 9):
    print("\n ======= Another recipe ======= \n ")
    pprint(response['hits'][i]['recipe']['label'])
    pprint(response['hits'][i]['recipe']['ingredientLines'])
    pprint(response['hits'][i]['recipe']['image'])

    # pprint(response['hits'][i]['recipe'])

