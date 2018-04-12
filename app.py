from flask import Flask, render_template, request
import urllib
import json
import requests
from pprint import pprint
import os
from secret_key import SECRET_APP_ID, SECRET_APP_KEY


app = Flask("MyApp")

# Home page
@app.route("/")
def show():
    return render_template("index.html")

# Load css
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


# Search page
@app.route("/search_recipe", methods=["POST"])
def sign_up():
    form_data = request.form.get("input_text")
    print(form_data)
    
    ingredients = str(form_data)
    #ingredients = ["lemon", "orange", "flour"]
    url_for_recipes = "https://api.edamam.com/search?app_id={}&app_key={}&q={}".format(SECRET_APP_ID, SECRET_APP_KEY, ingredients)
    
    print("URL:" + url_for_recipes)
    response = requests.get(url_for_recipes).json()


    # for i in range(0, len(response['hits'])):
    #     print("\n ======= Another recipe ======= \n ")
    #     pprint(response['hits'][i]['recipe']['label'])
    #     pprint(response['hits'][i]['recipe']['ingredientLines'])
    #     pprint(response['hits'][i]['recipe']['image'])

    # pprint(response['hits'][0]['recipe'])
    
    print(len(response['hits']))
    return render_template("recipe.html", response = response )

app.run(debug=True)