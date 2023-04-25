import datetime
from models import *

def test_post_creation():
    recipe = Recipe(name="Spaghetti Carbonara", numbers_of_servings=4, cooking_time=30, ingridients=["pasta", "eggs", "guanciale", "pecorino romano cheese", "black pepper"], description="A classic Italian pasta dish.")
    category = Category(name="Pasta")
    post = Post(name="My favorite recipe", author="John Doe", description="This is my go-to recipe whenever I have guests over.", recipe=recipe, category=category)
    assert post.name == "My favorite recipe"
    assert post.author == "John Doe"
    assert post.description == "This is my go-to recipe whenever I have guests over."
    assert post.recipe == recipe
    assert post.category == category
    assert post.comments == []

def test_comment_creation():
    recipe = Recipe(name="Spaghetti Carbonara", numbers_of_servings=4, cooking_time=30, ingridients=["pasta", "eggs", "guanciale", "pecorino romano cheese", "black pepper"], description="A classic Italian pasta dish.")
    category = Category(name="Pasta")
    post = Post(name="My favorite recipe", author="John Doe", description="This is my go-to recipe whenever I have guests over.", recipe=recipe, category=category)
    comment = Comment(user_name="Jane Doe", message="Thanks for sharing this recipe!", data_creating=datetime.date(2023, 4, 24), post=post)
    assert comment.user_name == "Jane Doe"
    assert comment.message == "Thanks for sharing this recipe!"
    assert comment.data_creating == datetime.date(2023, 4, 24)
    assert comment.post == post
    assert post.comments == [comment]

def test_len_description_post():
    recipe = Recipe(name="Spaghetti Carbonara", numbers_of_servings=4, cooking_time=30, ingridients=["pasta", "eggs", "guanciale", "pecorino romano cheese", "black pepper"], description="A classic Italian pasta dish.")
    category = Category(name="Pasta")
    post = Post(name="My favorite recipe", author="John Doe", description="This is my go-to recipe whenever I have guests over.", recipe=recipe, category=category)
    assert len_description_post(post) == 52

def test_count_ingridients_recipe():
    recipe = Recipe(name="Spaghetti Carbonara", numbers_of_servings=4, cooking_time=30, ingridients=["pasta", "eggs", "guanciale", "pecorino romano cheese", "black pepper"], description="A classic Italian pasta dish.")
    assert count_ingridients_recipe(recipe) == 5

def test_count_comment_post():
    recipe = Recipe(name='Pancakes', numbers_of_servings=4, cooking_time=20, ingridients=['flour', 'sugar', 'eggs', 'milk'], description='Delicious pancakes recipe')
    category = Category(name='Breakfast')
    post = Post(name='Best Pancakes Recipe', author='John Doe', description='Check out this amazing recipe!', recipe=recipe, category=category)
    comment1 = Comment(user_name='Alice', message='Looks great!', data_creating=datetime.date.today(), post=post)
    comment2 = Comment(user_name='Bob', message='Can\'t wait to try it!', data_creating=datetime.date.today(), post=post)
    comment3 = Comment(user_name='Charlie', message='Thanks for sharing!', data_creating=datetime.date.today(), post=post)
    assert count_comment_post(post) == 3
    comment4 = Comment(user_name='Eve', message='This recipe changed my life!', data_creating=datetime.date.today(), post=post)
    assert count_comment_post(post) == 4


def test_sort_comment_on_date():
    recipe = Recipe(name='Pancakes', numbers_of_servings=4, cooking_time=20, ingridients=['flour', 'sugar', 'eggs', 'milk'], description='Delicious pancakes recipe')
    category = Category(name='Breakfast')
    post = Post(name='Best Pancakes Recipe', author='John Doe', description='Check out this amazing recipe!', recipe=recipe, category=category)
    comment1 = Comment(user_name='Alice', message='Looks great!', data_creating=datetime.date(2023, 4, 23), post=post)
    comment2 = Comment(user_name='Bob', message='Can\'t wait to try it!', data_creating=datetime.date(2023, 4, 24), post=post)
    comment3 = Comment(user_name='Charlie', message='Thanks for sharing!', data_creating=datetime.date(2023, 4, 22), post=post)
    sorted_comments = sort_comment_on_date(post, datetime.date(2023, 4, 22), '>')
    assert sorted_comments == [comment1, comment2]
    sorted_comments = sort_comment_on_date(post, datetime.date(2023, 4, 22), '<')
    assert sorted_comments == []
    sorted_comments = sort_comment_on_date(post, datetime.date.today(), '')
    assert sorted_comments == [comment1, comment2, comment3]