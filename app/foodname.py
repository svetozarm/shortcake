import hashlib
from functools import reduce


class FoodName:
    def __init__(self, *args, **kwargs):
        self.adjectives = [
            "Spicy",
            "Mild",
            "Magical",
            "Smelly",
            "Delicious",
            "Sour",
            "Sweet",
            "Mushy",
            "Soggy",
            "Winter",
            "Summer",
            "Chewy",
            "Crunchy",
            "Savory",
            "Bitter",
            "Salty",
        ]
        self.methods = [
            "Parboiled",
            "Baked",
            "Fermented",
            "Boiled",
            "Sauteed",
            "SousVide",
            "Poached",
            "Emulsified",
            "Broiled",
            "Burnt",
            "Hardboiled",
            "Fried",
            "Simmered",
            "Iced",
            "Grilled",
            "Barbecued",
        ]
        self.ingredients = [
            "Shrimp",
            "Cheese",
            "Rice",
            "Noodle",
            "Burger",
            "Tofu",
            "Broccolini",
            "Broccoli",
            "Tomato",
            "Potato",
            "Strawberry",
            "Bean",
            "Egg",
            "Eggplant",
            "Mango",
            "Sage",
            "Edamame",
            "Chicken",
            "Beef",
            "Pork",
            "PorkBelly",
            "HotDog",
            "Sausage",
            "Meatball",
            "Liver",
            "Hock",
            "Duck",
        ]
        self.dishes = [
            "Soup",
            "Pasta",
            "Casserole",
            "Roast",
            "Skewer",
            "Feast",
            "Meze",
            "Tapas",
            "Taco",
            "Burrito",
            "Sushi",
            "Ramen",
            "Sandwich",
            "Bun",
            "DimSum",
            "Loaf",
        ]

        self.lists = [self.adjectives, self.methods, self.ingredients, self.dishes]

        lengths = [len(l) for l in self.lists]
        total_combinations = reduce(lambda x, y: x * y, lengths)
        print(f"Total combinations: {total_combinations}")

    def split_digest(self, digest, num_categories):
        total_len = len(digest)
        cat_size = int(total_len / num_categories)
        return [digest[i : i + cat_size] for i in range(0, len(digest), cat_size)]

    def generate(self, input=""):
        num_lists = len(self.lists)
        input_hash = hashlib.sha1(input.encode())
        splits = self.split_digest(input_hash.digest(), num_lists)

        components = list()
        for i in range(num_lists):
            l = self.lists[i]
            hsh = int.from_bytes(splits[i], byteorder="little")
            components.append(l[hsh % len(l)])

        return "".join(components)

