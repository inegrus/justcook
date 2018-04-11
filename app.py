# from flask import Flask, render_template, request
import urllib

import requests

# @app.route("/")
# def hello ():
# 	return render_template("hello.html", name = name.title ())


endpoint = "https://www.edamam.com/recipes"

ingredients = ["flour", "apple"] 

print ingredients

# if ingredients:
# 	ingredients = urllib.urlencode(ingredients)

print ingredients

url_for_recipes = "https://api.edamam.com/search?app_id=ff6d4efa&app_key=f70aa029996a664dcb7516a504f11d74&q={}".format(" ".join(ingredients))

response = requests.get(url_for_recipes)

print response.url
print response.status_code
print response.text

# app = Flask ("MyApp")
# app.run (debug=True)
