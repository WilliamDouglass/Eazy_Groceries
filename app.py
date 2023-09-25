# from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
from functions import *


class recipie:
    def __init__(self, image, name, ingredients, description):
        self.image = image
        self.name = name
        self.ingredients = ingredients
        self.description = description


temp_recipies = []
fav_recipies = []

# ---------------------------------------------------------------------------- #
#                                      URL                                     #
# ---------------------------------------------------------------------------- #


meal_time = "dinner"  # Can me dinner breckfast or lunch
url = f"https://www.bonappetit.com/meal-time/{meal_time}"
# main side or starter
meal_cuisine = "asian"
meal_portion = "main"

url += f"?filter={meal_portion}"
if meal_cuisine:
    url += f"%2C{meal_cuisine}"
# url += "&sort=highest-rating"


url = "https://www.bonappetit.com/meal-time/dinner?sort=most-recent"

source = requests.get(url)
if source.status_code == 200:
    soup = BeautifulSoup(source.text, "html.parser")
    elements = soup.find_all(
        class_="StackedRatingsCardWrapper-fRZEyp brTrfS SummaryCollectionGridSummaryItem-WColm ccdIoi"
    )
else:
    print(f"Failed to get source Html Error:{source.status_code}")

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto(url)
#     soup = BeautifulSoup(page.content(), "html.parser")
#     elements = soup.find_all(
#         class_="StackedRatingsCardWrapper-fRZEyp brTrfS SummaryCollectionGridSummaryItem-WColm ccdIoi"
#     )


i = 1
for element in elements:
    if is_recipe(element):
        name = get_name(element)
        img_src = get_image_src(element)
        ingredients = get_Ingredients(element)

        print(f"\n\n###################### {i} ######################")
        print("Name: " + name)
        print("Img " + img_src)
        print("ingredients " + ingredients)
    else:
        print(f"\n\n###################### {i} ######################")
        print("NOT A RECIPE!!!")
        print("NOT A RECIPE!!!")

    i += 1
    # find image
    # find ingrediants
    # append to temp_recipies
