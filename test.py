import unittest
from datetime import date
import appsql

class testclass(unittest.TestCase):
    def test_recipe_model(self):
    # Given a Recipe model
    # When a new recipe is created
    # Then check the title,is_vegetarian and suitable_for fields are defined correctly
        recipe=Recipe("Red sauce pasta",'Yes',3)
        assert recipe.title == 'TestDish'
        assert recipe.is_vegetarian == 'Yes'
        assert recipe.suitable_for == 3
    def test_dish_name(self):
        self.assertTrue("title",'Red sauce pasta')
    def test_suitable_for(self):
        self.assertTrue("suitable_for",3)
    def test_is_vegeterian_check(self):
        self.assertTrue("is_vegetarian",'Yes')
    def test_ingredient(self):
        self.assertTrue("ingredients",'basil,onion,garlic,tomato')
    def test_cooking_instructions(self):
        self.assertTrue("cooking_instructions",'A great introduction to pasta for kids – loads of fun to eat, and a brilliant base for adding all kinds of other fresh ingredients')

if __name__ == '__main__':
    unittest.main()
