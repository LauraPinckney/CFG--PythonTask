import requests
from dotenv import load_dotenv
import os

load_dotenv()
app_id = os.getenv('APP_ID')
app_key = os.getenv('APP_KEY')


def recipe_search(ingredient):
    app_id = os.getenv('APP_ID')
    app_key = os.getenv('APP_KEY')
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()

    return data['hits']


def run():
    ingredient = input('Enter an ingredient:')

    results = recipe_search(ingredient)
    with open('recipes.txt', 'a') as recipes_file:
        for result in results:
            recipe = result['recipe']

            print(recipe['label'])
            print(recipe['uri'])

            recipe_string = 'Label: {}, \nURI: {}\n\n'.format(recipe['label'], recipe['uri'])
            recipes_file.write(recipe_string)


run()
