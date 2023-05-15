import sqlalchemy as sa

engine = sa.create_engine("postgresql+psycopg2://postgres:Bogoslov8769@localhost:5432/Food_blog", echo=True)
meta = sa.MetaData()
recipe_table = sa.Table('Recipes', meta,
            sa.Column('id_recipe', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(100)),
            sa.Column('numbers_of_servings', sa.Integer),
            sa.Column('cooking_time', sa.Integer),
            sa.Column('description', sa.String())
            )

ingridients_table = sa.Table('Ingridients', meta,
            sa.Column('id_ingridients', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(100))
            )

ingridients_in_recipes_table = sa.Table('Ingridients_in_recipes', meta,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('ingridients_id', sa.Integer, sa.ForeignKey('Ingridients.id_ingridients')),
            sa.Column('recipe_id', sa.Integer, sa.ForeignKey('Recipes.id_recipe'))
            )

category_table = sa.Table('Categories', meta,
            sa.Column('id_category', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(100))
            )

post_table = sa.Table('Posts', meta,
            sa.Column('id_post', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(250)),
            sa.Column('author', sa.String(125)),
            sa.Column('description', sa.String()),
            sa.Column('recipe_id', sa.Integer, sa.ForeignKey('Recipes.id_recipe')),
            sa.Column('category_id', sa.Integer, sa.ForeignKey('Categories.id_category'))
            )

comment_table = sa.Table('Comments', meta,
            sa.Column('id_comment', sa.Integer, primary_key=True),
            sa.Column('username', sa.String(100)),
            sa.Column('message', sa.String()),
            sa.Column('data_creating', sa.DateTime),
            sa.Column('post_id', sa.Integer, sa.ForeignKey('Posts.id_post')),
            )
        
meta.create_all(engine)