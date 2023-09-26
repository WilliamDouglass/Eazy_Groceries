from bs4 import BeautifulSoup
import requests
import time


def get_name(html):
    return html.find(
        class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ Hed-kAccSO iUEiRd cSyirH kwWXVy"
    ).get_text()


def is_recipe(html):
    if "/gallery/" in get_link(html):
        return False
    else:
        return True


def get_link(html):
    return html.find(class_="ClampContent-hilPkr jEyoCN").find("a").get("href")


def get_image_src(html):
    img_element = html.find(
        class_="ResponsiveImagePicture-cWuUZO dUOtEa Image-bjZVCr czXXWW responsive-image"
    ).find("img")
    return img_element["src"]


def get_Ingredients(html):  # returns a list of ingedents seperated by a "|"
    # new_Html = page.goto("https://www.bonappetit.com" + get_link(html)).content()
    url = "https://www.bonappetit.com" + get_link(html)
    source = requests.get(url)
    if source.status_code == 200:
        ingredient_List_Html = BeautifulSoup(source.text, "html.parser").find(
            class_="List-iSNGTT guHkXK"
        )
    else:
        print(f"Failed to get source from {url} Error:{source.status_code}")

    ammounts = ingredient_List_Html.find_all(
        class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ Amount-hYcAMN iUEiRd eCLzqJ hoAJEl"
    )
    descrs = ingredient_List_Html.find_all(
        class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ Description-cSrMCf iUEiRd eCLzqJ fsKnGI"
    )

    if len(ammounts) == len(descrs):
        n = len(ammounts)
    else:
        print(f"Error on {url} gettiing ingredeants")

    ingredients = ""
    for i in range(n):
        # Removes the newline char from str
        clean_Amm = ammounts[i].get_text().replace("\n", "")
        clean_Descr = descrs[i].get_text().replace("\n", "")
        ingredients += "[" + clean_Amm + "] = " + clean_Descr + "|\n"

    return ingredients
