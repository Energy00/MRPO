from flask import Flask, request, redirect, render_template, jsonify
from view import *
from services import *


app = Flask(__name__)


@app.route('/create_category', methods=['GET', 'POST'])
def cr_category():
    if request.method == 'POST':
        name = request.form['name']
        uow = SqlAlchemyUnitOfWork()
        category_id = create_category(uow, name)

        return redirect('/create_recipe', code=301, Response=None)
    else:
        return render_template('create_category.html')


@app.route('/create_ingridient', methods=['GET', 'POST'])
def cr_ingridient():
    if request.method == 'POST':
        name = request.form['name']

        uow = SqlAlchemyUnitOfWork()
        ingridient_id = create_ingridients(uow, name)

        return redirect('/create_recipe', code=301, Response=None)
    else:
        return render_template('create_ingridient.html')


@app.route('/create_recipe', methods=['GET', 'POST'])
def cr_recipe():
    if request.method == 'POST':
        name = request.form['name']
        numbers_of_servings = request.form['numbers_of_servings']
        cooking_time = request.form['cooking_time']
        description = request.form['description']

        uow = SqlAlchemyUnitOfWork()
        ingridients = uow.ingridient_repository.get_all()
        recipe_id = create_recipe(uow, name, numbers_of_servings, cooking_time, description, ingridients)

        return redirect('/create_post', code=301, Response=None)
    else:
        return render_template('create_recipe.html')

@app.route('/create_post', methods=['GET', 'POST'])
def cr_post():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        description = request.form['description']

        uow = SqlAlchemyUnitOfWork()
        category = uow.category_repository.get_by_id(1)
        recipe = uow.recipe_repository.get_by_id(1)
        post_id = create_post(uow, name, author, description, category, recipe)

        return redirect(f'/posts/{post_id}', code=301, Response=None)
    else:
        return render_template('create_post.html')


@app.route('/posts/<post_id>', methods=['GET'])
def post_by_id(post_id):
    uow = SqlAlchemyUnitOfWork()
    post = get_post_by_id(post_id, uow)
    if post is None:
        return 'Not found', 404
    return render_template('post.html', post=post)
    

@app.route('/posts', methods=['GET'])
def posts():
    uow = SqlAlchemyUnitOfWork()
    posts = get_all_posts(uow)
    if not posts:
        return 'Not found', 404
    return render_template('posts.html', posts = posts)