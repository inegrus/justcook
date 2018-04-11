from flask import Flask, render_template, request

import requests

endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"

def recipe_food (ingredientone, ingredienttwo)

response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients=false&ingredients=apples%2Cflour%2Csugar&limitLicense=false&number=5&ranking=1",
  headers={
    "X-Mashape-Key": "iKBcUotH8nmshvpG46gPjRsSMSQop1Yumztjsnj3MXfTUkkFt0",
    "Accept": "application/json"
  }
)

print response.url
print response.status_code
print response 

# app = Flask ("MyApp")
# app.run (debug=True)