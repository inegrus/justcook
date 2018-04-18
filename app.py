from flask import Flask, render_template, request
import urllib, json, os
import requests
from pprint import pprint
from os.path import join, dirname
from dotenv import load_dotenv

# Load env var
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

#Accessing variables
SECRET_APP_ID = os.getenv('SECRET_APP_ID')
SECRET_APP_KEY = os.getenv('SECRET_APP_KEY')

app = Flask("MyApp")

# Home page
@app.route("/")
def show():
    return render_template("index.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Load css
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

# Search page
@app.route("/search_recipe", methods=["POST"])
def search():
    form_data = request.form.get("input_text")
    print(form_data)
    
    ingredients = str(form_data)
    
    #ingredients = ["lemon", "orange", "flour"]
    url_for_recipes = "https://api.edamam.com/search?app_id={}&app_key={}&q={}".format(SECRET_APP_ID, SECRET_APP_KEY, ingredients)

    response = requests.get(url_for_recipes).json()
    # print("heei\n\n\n")
    # print(len(response['hits']))

    return render_template("recipe.html", 
        response = response, 
        objects_no = min(9, len(response['hits'])))
    
    # if response.status_code != 200:
    #     print(response.text)
    # else:
    #     response = response.json()

    # for i in range(0, len(response['hits'])):
    #     print("\n ======= Another recipe ======= \n ")
    #     pprint(response['hits'][i]['recipe']['label'])
    #     pprint(response['hits'][i]['recipe']['ingredientLines'])
    #     pprint(response['hits'][i]['recipe']['image'])

    # pprint(response['hits'][0]['recipe'])
    
    # print(len(response['hits']))
    # print(type(response['hits'][0]['recipe']['ingredientLines']))
    # print(response['hits'][0]['recipe']['ingredientLines'][0])
    


@app.route("/suggestions")
def suggest():
    return render_template("suggestions.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, port=port)
    app.run(host='0.0.0.0', debug=True, port=port)
    
