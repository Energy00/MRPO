from uow import *

def get_post_by_id(id: int, uow:SqlAlchemyUnitOfWork):
    with uow:
        post = uow.post_repository.get_by_id(id)
        return post.to_dict()

def get_post_comments_by_post_id(id:int, uow:SqlAlchemyUnitOfWork):
    with uow:
        post = uow.post_repository.get_by_id(id)
        comments = uow.comment_repository.get_all()
        comments = [comment for comment in comments if comment.post == post]
        return [comment.to_dict() for comment in comments]
    
def get_all_posts(uow: SqlAlchemyUnitOfWork):
    with uow:
        posts = uow.post_repository.get_all()
        print(posts)
        return [post.to_dict() for post in posts]