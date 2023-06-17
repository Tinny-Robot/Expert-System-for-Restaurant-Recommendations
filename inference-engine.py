import clips
import csv

def load_restaurant_data(filename):
  """
  Loads restaurant data from a CSV file.

  Args:
    filename: The path to the CSV file.

  Returns:
    A list of dictionaries, where each dictionary represents a restaurant.
  """

  restaurants = []

  with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      restaurant = {}
      for i, column in enumerate(reader.fieldnames):
        restaurant[column] = row[i]
      restaurants.append(restaurant)

  return restaurants

def recommend_restaurant(engine, cuisine, price_range, location):
  """
  Recommends a restaurant based on the user input.

  Args:
    engine: A CLIPS engine.
    cuisine: The user's preferred cuisine.
    price_range: The user's preferred price range.
    location: The user's location.

  Returns:
    A list of restaurants that match the user input.
  """

  # Get the restaurants that match the user input.
  restaurants = engine.findFacts('(restaurant cuisine {} price-range {} location {})'.format(cuisine, price_range, location))

  # Sort the restaurants by rating.
  restaurants.sort(key=lambda restaurant: restaurant['rating'], reverse=True)

  # Return the top 5 restaurants.
  return restaurants[:5]

if __name__ == '__main__':
  # Create a CLIPS engine.
  engine = clips.Engine()

  # Load the knowledge base.
  engine.load('knowledge-base.clp')

  # Load the data into the restaurant recommendation system.
  restaurants = load_restaurant_data('data.csv')

  # Get the user input.
  cuisine = input('What cuisine are you looking for? ')
  price_range = input('What price range are you looking for? ')
  location = input('Where are you located? ')

  # Make a recommendation.
  recommendations = recommend_restaurant(engine, cuisine, price_range, location)

  # Print the recommendations.
  for restaurant in recommendations:
    print(restaurant['name'])
