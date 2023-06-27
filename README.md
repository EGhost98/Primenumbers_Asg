# Primenumbers Technologies Django Assignment

This is a Django project that includes fuzzy search functionality for restaurant dishes.

## Dependencies

The project relies on the following dependencies:

- Django: A web framework for building Python-based web applications.
- FuzzyWuzzy: A library for fuzzy string matching.
- Pandas: A library for data manipulation and analysis.

Make sure to install these dependencies before running the project.

## Getting Started

To set up the project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install the project dependencies: `pip install -r requirements.txt`
3. Run database migrations: `python manage.py migrate`
4. (Optional) Populate the database from a CSV file: Uncomment the relevant lines in `views.py` and provide the CSV file path.
5. Start the development server: `python manage.py runserver`

## Usage

- Access the application by visiting `http://localhost:8000` in your web browser.
- Use the search form to enter a query and find matching dishes.
- The fuzzy search algorithm uses the FuzzyWuzzy library with the Partial Token Set Ratio scorer.
- The Partial Token Set Ratio scorer measures the similarity of the query to existing dish names based on partial string matching and tokenization.
- Results will be displayed for dishes with a similarity score greater than or equal to 80 (out of 100).

## Screenshots (With Query and it's Results)
![Django Dish_Search (1)](https://github.com/EGhost98/Primenumbers_Asg/assets/76267623/123aec96-32d4-44ef-b680-2688504163f4)
![Django Dish_Search (2)](https://github.com/EGhost98/Primenumbers_Asg/assets/76267623/b9912d63-650d-4e01-a50e-76b53a651e96)
![Django Dish_Search (3)](https://github.com/EGhost98/Primenumbers_Asg/assets/76267623/e852700c-5eec-4211-9496-a731803e3bb4)
![Django Dish_Search (4)](https://github.com/EGhost98/Primenumbers_Asg/assets/76267623/bd737127-2257-4619-a3ca-ffba365c5fc1)




## Project Structure

The project consists of the following files and directories:

- `views.py`: Contains the views for rendering the index page and performing fuzzy search.
- `models.py`: Defines the Django models for `Restaurant` and `Item` used in the project.
- `forms.py`: Includes the `Query` form used for querying dishes.
- `index.html`: The HTML template rendered by the `index` view.
- Other Django project files and directories.

## Models and Relationships

The project includes the following models:

### Restaurant Model

- The `Restaurant` model represents a restaurant.
- It has the following fields:
  - `name`: A character field representing the name of the restaurant.
  - `location`: A character field representing the location of the restaurant.
  - `latitude`: A float field representing the latitude of the restaurant's location.
  - `longitude`: A float field representing the longitude of the restaurant's location.
- The `__str__` method is overridden to provide a string representation of the restaurant instance.

### Item Model

- The `Item` model represents a dish or item served at a restaurant.
- It has the following fields:
  - `restaurant`: A foreign key to the `Restaurant` model, representing the restaurant that serves the item.
  - `name`: A character field representing the name of the item.
  - `price`: A character field representing the price of the item.
- The `__str__` method is overridden to provide a string representation of the item instance.

The relationship between the `Restaurant` and `Item` models is defined as follows:

- Each `Item` is associated with a specific `Restaurant` through a foreign key relationship.
- A `Restaurant` can have multiple `Item` instances, while each `Item` belongs to only one `Restaurant`.

## Views

### `index` function

The `index` function is the view associated with the index page of the project. It performs the following tasks:

1. Renders the `index.html` template.
2. Initializes an instance of the `Query` form to handle the search query input from the user.
3. Modifies the label attribute of the `query` field in the form to hide it in the HTML template.
4. Checks if the form is valid, i.e., if a query has been submitted.
5. If the form is valid, it retrieves all the items from the `Item` model.
6. Uses the FuzzyWuzzy library to perform a fuzzy search on the items, matching them against the query.
7. The fuzzy search uses the Partial Token Set Ratio scorer, which measures the similarity between the query and the item names based on partial string matching and tokenization.
8. The search results are filtered to only include items with a similarity score greater than or equal to 80 (out of 100).
9. The matched items are stored in the `results` variable.
10. The `results` variable is added to the context dictionary to be passed to the template.
11. The `search_form` is also added to the context dictionary to be used in the template for displaying the search form.

## References

These are some of the resources I used to complete this assignment:

- [Django Documentation](https://docs.djangoproject.com/): The official documentation for Django, which provided guidance on building web applications using Django.
- [FuzzyWuzzy Documentation](https://github.com/seatgeek/fuzzywuzzy): The official documentation for the FuzzyWuzzy library, which helped me implement fuzzy string matching for the search functionality.
- [Pandas Documentation](https://pandas.pydata.org/docs/): The official documentation for the Pandas library, which I used for data manipulation and analysis when populating the database from a CSV file.
- [Medium](https://medium.com/): An online publishing platform that provided tutorials and articles related to Django, FuzzyWuzzy, and other relevant topics.
- [ChatGPT](https://openai.com/): An AI language model developed by OpenAI, which provided guidance and assistance during the development of this project.

Feel free to refer to these resources for more information and detailed explanations about the topics covered in this assignment.
