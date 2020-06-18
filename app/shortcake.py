import os
import random


class FoodName:
    def __init__(self, *args, **kwargs):
        self.adjectives = ["Magic", "Smelly", "Parboiled", "Baked"]
        self.ingredient = ["Shrimp", "Cheese", "Rice", "Noodle", "Burger"]
        self.dish = ["Soup", "Pasta", "Casserole", "Roast", "Skewer"]

    def generate(self):
        return (
            random.choice(self.adjectives)
            + random.choice(self.ingredient)
            + random.choice(self.dish)
        )


food_name = FoodName()


def get_domain():
    return "http://shortcake.xyz/"


def get_stored(url):
    return None


def get_short(url):
    if shortened := get_stored(url):
        return shortened
    return get_domain() + food_name.generate()
