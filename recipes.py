import requests


def get_meals(pantry_items):
   item_array = {item.strip().lower() for item in pantry_items.split(',')}
   try:
       response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
       data = response.json()


       meals = data.get("meals", [])
       filtered_meals = []


       for meal in meals:
           ingredients = {meal[f"strIngredient{i}"].strip().lower()
                          for i in range(1, 31) if meal.get(f"strIngredient{i}")}
          
           if item_array.intersection(ingredients):
               filtered_meals.append(meal)


       return filtered_meals


   except Exception as error:
       print('Fetch error:', error)
       return []


def main():
   pantry_items = input("Enter pantry items (separated by commas): ")
   meals = get_meals(pantry_items)


   if meals:
       for meal in meals:
           print(f"Meal: {meal['strMeal']}\nInstructions: {meal['strInstructions']}\n")
   else:
       print("No meals found with the provided ingredients.")


if __name__ == "__main__":
   main()
