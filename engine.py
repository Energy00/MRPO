import sqlalchemy as sa
from sqlalchemy.orm import registry, relationship, sessionmaker
from models import *
from SqlAlchemyTables import *

def mapping():
    mapper_registry = registry()
    mapper_registry.map_imperatively(Ingridient, ingridients_table, properties={
        'recipes':relationship(Recipe, secondary=ingridients_in_recipes_table, back_populates='ingridients')
    })
    mapper_registry.map_imperatively(Recipe, recipe_table, properties={
        'ingridients': relationship(Ingridient, secondary=ingridients_in_recipes_table, back_populates='recipes')})
    mapper_registry.map_imperatively(Category, category_table, properties={
    'posts': relationship(Post, backref='category')})
    mapper_registry.map_imperatively(Post, post_table, properties={
    'recipe': relationship(Recipe, backref='posts'),
    'comments': relationship(Comment, backref='posts')})
    mapper_registry.map_imperatively(Comment, comment_table)

    engine = sa.create_engine("postgresql+psycopg2://postgres:Bogoslov8769@localhost:5432/Food_blog", echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session