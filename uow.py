from repositories import *
from engine import *


class AbstractUnitOfWork(ABC):
    category_repository: abstract_repository
    ingridient_repository: abstract_repository
    recipe_repository: abstract_repository
    post_repository: abstract_repository
    comment_repository: abstract_repository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

session = mapping()

class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __enter__(self):
        self.category_repository = CategoryRepository(self.session)
        self.ingridient_repository = IngridientRepository(self.session)
        self.recipe_repository = RecipeRepository(self.session)
        self.post_repository = PostRepository(self.session)
        self.comment_repository = CommentRepository(self.session)
        return super().__enter__()
    
    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
    

class XMLUnitOfWork(AbstractUnitOfWork):
    def __init__(self, xml_file = 'mrpo.xml'):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file, ET.XMLParser(encoding='UTF-8'))

    def __enter__(self):
        self.category_repository = CategoryXMLRepository(self.tree)
        self.ingridient_repository = IngridientXMLRepository(self.tree)
        self.recipe_repository = RecipeXMLRepository(self.tree, self.ingridients)
        self.post_repository = PostXMLRepository(self.tree, self.recipes, self.categories)
        self.comment_repository = CommentXMLRepository(self.tree, self.posts)
        return super().__enter__()
    
    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        self.tree.write(self.xml_file, encoding='UTF-8')

    def rollback(self):
        pass


class JSONUnitOfWork(AbstractUnitOfWork):
    def __init__(self, json_file = 'mrpo.json'):
        self.json_file = json_file
        if os.stat(self.json_file).st_size == 0:
            self.data = {"categories":[],
                        "ingridients":[],
                        "recipes":[],
                        "posts":[],
                        "comments":[]}
        else:
            with open(self.json_file, "r", encoding='utf-8') as file:
                self.data = json.load(file)

    def __enter__(self):
        self.category_repository = CategoryJSONRepository(self.data, self.json_file)
        self.ingridient_repository = IngridientJSONRepository(self.data, self.json_file)
        self.recipe_repository = RecipeJSONRepository(self.data, self.json_file)
        self.post_repository = PostJSONRepository(self.data, self.json_file)
        self.comment_repository = CommentJSONRepository(self.data, self.json_file)
        return super().__enter__()
    
    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        with open(self.json_file, "w", encoding='UTF-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)            

    def rollback(self):
        pass